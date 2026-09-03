"""Score timesheet accuracy for a window, or evaluate the biweekly gate.

Two modes:

  # one window (a week for the Friday review, a fortnight for a period read)
  python scripts/score.py --start 2026-08-31 --end 2026-09-04

  # the gate: N consecutive pay periods, most recent first
  python scripts/score.py --gate-anchor 2026-08-24 --periods 2

  # the weekly persistence check that feeds the draft to the leads
  python scripts/score.py --weeks 3

  # Monday to Friday of the current week, for an unattended Friday run
  python scripts/score.py --this-week

Prints JSON on stdout. Read stderr too: a warning there changes what the numbers
mean. Weights and thresholds come from config/scoring.json, never from here.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone

import _lib as lib


def clamp(value, low=0.0, high=1.0):
    return max(low, min(high, value))


def score_coverage(logged_minutes, expected_minutes, tolerance_ratio):
    if expected_minutes <= 0:
        return None
    ratio = logged_minutes / expected_minutes
    if abs(1.0 - ratio) <= tolerance_ratio:
        return 1.0
    return clamp(1.0 - abs(logged_minutes - expected_minutes) / expected_minutes)


def score_hygiene(entries, days, grace_days):
    """Share of workdays that hold an entry logged at or near the time.

    An entry counts for its day only if it was created within grace_days of that
    day. That is the whole anti-backfill mechanism: ten days reconstructed on day
    ten score one day, not ten.
    """
    if not days:
        return None, False, 0.0

    any_created_at = any(e.get("created_at") for e in entries)
    on_day = set()
    backfilled_minutes = 0
    total_minutes = 0

    for entry in entries:
        entered = lib.parse_date(entry["entered_on"])
        minutes = entry.get("duration_minutes") or 0
        total_minutes += minutes
        created = lib.parse_created_at(entry.get("created_at"))

        if created is None:
            # No timestamp available, so we cannot tell prompt from reconstructed.
            on_day.add(entered)
            continue

        lag = (created - entered).days
        if lag <= grace_days:
            on_day.add(entered)
        else:
            backfilled_minutes += minutes

    qualifying = len([d for d in days if d in on_day])
    backfill_share = (backfilled_minutes / total_minutes) if total_minutes else 0.0
    # Only a real degradation when entries exist but none carry created_at.
    # Someone with no entries at all says nothing about the workspace's fields.
    degraded = bool(entries) and not any_created_at
    return qualifying / len(days), degraded, backfill_share


def score_attribution(entries, allowlist, excluded):
    total = 0
    attributed = 0
    for entry in entries:
        minutes = entry.get("duration_minutes") or 0
        total += minutes
        gid = (entry.get("attributable_to") or {}).get("gid")
        if not gid or gid in excluded:
            continue
        if allowlist and gid not in allowlist:
            continue
        attributed += minutes
    if total == 0:
        return None
    return attributed / total


def score_on_time(approvals, person_gid, week_starts):
    """Weeks submitted on time, out of the weeks in the window.

    Returns None when the approval endpoint is not configured, so the caller can
    renormalize instead of pretending the score exists.
    """
    if approvals is None:
        return None
    person = approvals.get(person_gid, {})
    if not person:
        return None

    on_time = 0
    for week in week_starts:
        rows = person.get(lib.iso(week)) or []
        states = {str(r.get("approval_status") or r.get("status") or "").upper() for r in rows}
        if states & {"SUBMITTED", "APPROVED"}:
            on_time += 1
    return on_time / len(week_starts) if week_starts else None


def composite(parts, weights):
    """Weighted mean over the metrics that exist, renormalized.

    Returns (score, renormalized_flag, missing_metric_names).
    """
    available = {k: v for k, v in parts.items() if v is not None}
    missing = sorted(k for k, v in parts.items() if v is None)
    if not available:
        return None, False, missing
    live_weight = sum(weights[k] for k in available)
    total = sum(weights[k] * available[k] for k in available)
    return total / live_weight, bool(missing), missing


def score_window(entries_by_person, people, start, end, scoring, approvals):
    days = lib.workdays(start, end, scoring)
    weeks = sorted({lib.week_start(d) for d in days})
    weights = scoring["weights"]
    allowlist = set(scoring["attribution"].get("attributable_project_gids") or [])
    excluded = set(scoring["attribution"].get("excluded_project_gids") or [])
    grace = scoring["hygiene"]["grace_days"]
    tolerance = scoring["coverage"]["tolerance_ratio"]

    # Days before the program start date are not in `days`, so entries logged on
    # them must not be in `entries` either. Otherwise attribution and coverage
    # would quietly score work from before the process existed.
    first = days[0] if days else None
    last = days[-1] if days else None

    rows = []
    for person in people:
        entries = entries_by_person.get(person["asana_gid"], [])
        if first is None:
            entries = []
        else:
            entries = [
                e for e in entries if first <= lib.parse_date(e["entered_on"]) <= last
            ]
        logged = sum(e.get("duration_minutes") or 0 for e in entries)
        expected = len(days) * float(person["daily_target_hours"]) * 60

        hygiene, hygiene_degraded, backfill_share = score_hygiene(entries, days, grace)
        parts = {
            "hours_coverage": score_coverage(logged, expected, tolerance),
            "daily_hygiene": hygiene,
            "attribution": score_attribution(entries, allowlist, excluded),
            "on_time_submission": score_on_time(approvals, person["asana_gid"], weeks),
        }
        total, renormalized, missing = composite(parts, weights)

        rows.append(
            {
                "name": person["name"],
                "asana_gid": person["asana_gid"],
                "logged_hours": round(logged / 60, 2),
                "expected_hours": round(expected / 60, 2),
                "workdays": len(days),
                "days_logged_on_time": (
                    None if hygiene is None else int(round(hygiene * len(days)))
                ),
                "backfilled_share_of_hours": round(backfill_share, 3),
                "metrics": {k: (None if v is None else round(v, 3)) for k, v in parts.items()},
                "score": None if total is None else round(total, 3),
                "flags": {
                    "weights_renormalized": renormalized,
                    "missing_metrics": missing,
                    "hygiene_degraded_no_created_at": hygiene_degraded,
                    "attribution_loose_no_allowlist": not allowlist,
                    "no_entries_at_all": len(entries) == 0,
                },
            }
        )

    scored = [r["score"] for r in rows if r["score"] is not None]
    return {
        "window": {"start": lib.iso(start), "end": lib.iso(end), "workdays": len(days)},
        "people": sorted(rows, key=lambda r: (r["score"] is not None, r["score"] or 0)),
        "team": {
            "mean_score": round(sum(scored) / len(scored), 3) if scored else None,
            "min_score": round(min(scored), 3) if scored else None,
            "people_scored": len(scored),
            "people_below_floor": len(
                [s for s in scored if s < scoring["gate"]["individual_floor"]]
            ),
        },
    }


def evaluate_gate(periods, scoring):
    gate = scoring["gate"]
    needed = gate["consecutive_periods_required"]
    if len(periods) < needed:
        lib.warn(
            "the gate needs {} consecutive periods but only {} were scored, so it "
            "cannot pass. Re-run with --periods {}.".format(needed, len(periods), needed)
        )
    recent = periods[:needed]

    checks = []
    for period in recent:
        team = period["team"]
        checks.append(
            {
                "window": period["window"],
                "mean_score": team["mean_score"],
                "min_score": team["min_score"],
                "mean_ok": team["mean_score"] is not None
                and team["mean_score"] >= gate["team_mean_threshold"],
                "floor_ok": team["min_score"] is not None
                and team["min_score"] >= gate["individual_floor"],
            }
        )

    partial = any(
        person["flags"]["weights_renormalized"] for p in recent for person in p["people"]
    )
    passing = len(checks) == needed and all(c["mean_ok"] and c["floor_ok"] for c in checks)

    return {
        "thresholds": {
            "team_mean": gate["team_mean_threshold"],
            "individual_floor": gate["individual_floor"],
            "consecutive_periods": needed,
        },
        "periods_checked": checks,
        "passing": passing,
        "trustworthy": passing and not partial,
        "note": (
            "Gate arithmetic passes but at least one metric was unavailable, so this is "
            "not yet a payroll-grade result. Fix the missing metric first."
            if passing and partial
            else None
        ),
    }


def evaluate_persistence(weekly, entries_by_person, people, scoring):
    """Who is not following the process as a pattern rather than a bad week.

    Feeds the weekly draft in playbooks/friday-review.md. It never sends
    anything: it names who meets the rule and why, and a person decides.
    """
    rule = scoring["persistence"]
    floor = scoring["gate"]["individual_floor"]
    flagged = []
    clear = []

    for person in people:
        gid = person["asana_gid"]
        entries = entries_by_person.get(gid, [])
        below = []
        streaks = []

        for week in weekly:
            monday = lib.parse_date(week["window"]["start"])
            row = next((r for r in week["people"] if r["asana_gid"] == gid), None)
            if row and row["score"] is not None and row["score"] < floor:
                below.append({"week_of": week["window"]["start"], "score": row["score"]})
            streaks.append(
                {
                    "week_of": week["window"]["start"],
                    "longest_streak": lib.longest_streak_in_week(
                        entries, person, monday, scoring
                    ),
                }
            )

        worst_streak = max((s["longest_streak"] for s in streaks), default=0)
        reasons = []
        if len(below) >= rule["weeks_below_floor_to_flag"]:
            reasons.append(
                "scored below {} in {} of the last {} weeks ({})".format(
                    floor,
                    len(below),
                    len(weekly),
                    ", ".join("{} at {}".format(b["week_of"], b["score"]) for b in below),
                )
            )
        if worst_streak >= rule["nudge_streak_to_flag"]:
            worst = max(streaks, key=lambda s: s["longest_streak"])
            reasons.append(
                "ran {} straight weekdays behind in the week of {}".format(
                    worst_streak, worst["week_of"]
                )
            )

        record = {
            "name": person["name"],
            "asana_gid": gid,
            "weeks_below_floor": below,
            "streaks_by_week": streaks,
            "worst_streak": worst_streak,
        }
        if reasons:
            record["reasons"] = reasons
            flagged.append(record)
        else:
            clear.append({"name": person["name"], "worst_streak": worst_streak})

    return {
        "rule": rule,
        "individual_floor": floor,
        "weeks_examined": [w["window"]["start"] for w in weekly],
        "flagged": flagged,
        "clear": clear,
        "draft_required": bool(flagged),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", help="window start, YYYY-MM-DD")
    parser.add_argument("--end", help="window end, YYYY-MM-DD")
    parser.add_argument("--gate-anchor", help="Monday starting the most recent pay period")
    parser.add_argument("--periods", type=int, default=1, help="how many pay periods back")
    parser.add_argument("--weeks", type=int, help="score this many trailing weeks and run the persistence check")
    parser.add_argument("--end-week", help="Monday of the last week to include, defaults to this week")
    parser.add_argument(
        "--this-week",
        action="store_true",
        help="score Monday to Friday of the current week. Avoids shell date arithmetic "
        "in a scheduler, which is a classic source of off-by-a-week bugs.",
    )
    parser.add_argument("--entries", help="reuse a fetch_entries.py dump instead of calling the API")
    args = parser.parse_args()

    scoring = lib.load_scoring()
    people = lib.load_roster()
    weeks_per_period = scoring["gate"]["pay_period_weeks"]

    if args.this_week:
        monday = lib.week_start(datetime.now(timezone.utc).date())
        windows = [(monday, monday + timedelta(days=4))]
    elif args.weeks:
        if args.end_week:
            last_monday = lib.parse_date(args.end_week)
            if last_monday.weekday() != 0:
                lib.die("--end-week must be a Monday, got a {}".format(last_monday.strftime("%A")))
        else:
            last_monday = lib.week_start(datetime.now(timezone.utc).date())
        windows = [
            (last_monday - timedelta(weeks=i), last_monday - timedelta(weeks=i) + timedelta(days=4))
            for i in range(max(1, args.weeks))
        ]
    elif args.gate_anchor:
        anchor = lib.parse_date(args.gate_anchor)
        if anchor.weekday() != 0:
            lib.die("--gate-anchor must be a Monday, got a {}".format(anchor.strftime("%A")))
        windows = [
            lib.pay_period_bounds(anchor, weeks_per_period, index)
            for index in range(max(1, args.periods))
        ]
    elif args.start and args.end:
        windows = [(lib.parse_date(args.start), lib.parse_date(args.end))]
    else:
        lib.die("give one of: --this-week, --start with --end, --gate-anchor, or --weeks")

    overall_start = min(w[0] for w in windows)
    overall_end = max(w[1] for w in windows)

    if args.entries:
        with open(args.entries, "r", encoding="utf-8") as handle:
            raw = json.load(handle)
    else:
        raw = lib.fetch_entries(overall_start, overall_end)

    approvals = None
    all_weeks = sorted(
        {
            lib.week_start(d)
            for start, end in windows
            for d in lib.workdays(start, end, scoring)
        }
    )
    fetched, available = lib.fetch_approvals(scoring, people, all_weeks)
    if available:
        approvals = fetched

    results = []
    for start, end in windows:
        window_entries = [
            e
            for e in raw
            if e.get("entered_on") and start <= lib.parse_date(e["entered_on"]) <= end
        ]
        results.append(
            score_window(lib.index_entries(window_entries, people), people, start, end, scoring, approvals)
        )

    output = {"weights": scoring["weights"], "periods": results}
    if args.gate_anchor:
        output["gate"] = evaluate_gate(results, scoring)
    if args.this_week:
        monday = lib.week_start(datetime.now(timezone.utc).date())
        windows = [(monday, monday + timedelta(days=4))]
    elif args.weeks:
        output["persistence"] = evaluate_persistence(
            results, lib.index_entries(raw, people), people, scoring
        )
        output["escalation_contacts"] = lib.load_escalation_contacts()

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
