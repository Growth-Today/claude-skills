"""Work out who to nudge right now, in their own timezone, and how hard.

  python scripts/who_is_behind.py
  python scripts/who_is_behind.py --entries /tmp/entries.json
  python scripts/who_is_behind.py --force --now 2026-09-03T16:45   # testing

Run it on the few UTC times that are late afternoon somewhere in the roster,
not hourly. Each pass only handles people for whom it is now late afternoon locally,
so one scheduler covers Central European Time, India, Manila and Johannesburg
without waking anyone at 22:30.

Escalation level is derived from the data, not from a stored counter: it is the
number of consecutive weekdays this person has ended behind. Nothing to persist,
nothing to lose when a container is recycled.

Every level of the ladder contacts the person and nobody else. Persistent
patterns are handled once a week by the draft in playbooks/friday-review.md,
which a human reads and sends.

Two limits keep the volume honest. Slack only unless email_enabled is turned on,
and a hard cap of max_per_week nudges per person per calendar week. The count is
recomputed from the entries rather than stored, so it survives a missed run.
"""

import argparse
import json
from datetime import datetime, timedelta, timezone

import _lib as lib


def in_nudge_window(now_local, hour, minute):
    """True when local time sits in the one-hour slot opening at hour:minute."""
    opens = now_local.replace(hour=hour, minute=minute, second=0, microsecond=0)
    return opens <= now_local < opens + timedelta(hours=1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entries", help="reuse a fetch_entries.py dump")
    parser.add_argument("--force", action="store_true", help="ignore the local time window")
    parser.add_argument("--now", help="override current time, ISO local, for testing")
    args = parser.parse_args()

    scoring = lib.load_scoring()
    people = lib.load_roster()
    nudge = scoring["nudge"]
    grace = scoring["hygiene"]["grace_days"]
    ladder = nudge["escalation_ladder"]

    # Two weeks back covers the streak lookback and any Monday edge case.
    today_utc = datetime.now(timezone.utc).date()
    window_start = lib.week_start(today_utc) - timedelta(days=14)

    if args.entries:
        with open(args.entries, "r", encoding="utf-8") as handle:
            raw = json.load(handle)
    else:
        raw = lib.fetch_entries(window_start, today_utc)

    by_person = lib.index_entries(raw, people)

    targets = []
    on_track = []
    asleep = []
    capped = []

    for person in people:
        if args.now:
            now_local = datetime.fromisoformat(args.now)
        else:
            now_local = lib.local_now(person["timezone"])
        today = now_local.date()

        if today.weekday() >= 5:
            asleep.append({"name": person["name"], "why": "weekend locally"})
            continue
        if not args.force and not in_nudge_window(
            now_local, nudge["window_local_hour"], nudge["window_minutes"]
        ):
            asleep.append(
                {
                    "name": person["name"],
                    "why": "local time {} is outside the nudge window".format(
                        now_local.strftime("%H:%M %Z")
                    ),
                }
            )
            continue

        entries = by_person.get(person["asana_gid"], [])
        days = lib.workdays(lib.week_start(today), today, scoring.get("holidays"))
        expected = len(days) * float(person["daily_target_hours"]) * 60
        logged = lib.logged_minutes(entries, days[0], today, as_of=today) if days else 0
        covered = lib.days_with_entries(entries, grace)
        missing_dates = [d for d in days if d not in covered]
        missing = [lib.iso(d) for d in missing_dates]
        missing_human = [d.strftime("%a") for d in missing_dates]

        if expected > 0 and logged >= nudge["behind_ratio"] * expected and not missing:
            on_track.append(
                {
                    "name": person["name"],
                    "logged_hours": round(logged / 60, 2),
                    "expected_hours": round(expected / 60, 2),
                }
            )
            continue

        sent_this_week = lib.nudges_this_week(entries, person, today, scoring)
        limit = nudge.get("max_per_week")
        if limit and sent_this_week > limit:
            capped.append(
                {
                    "name": person["name"],
                    "nudges_this_week": sent_this_week,
                    "limit": limit,
                    "why": (
                        "already nudged {} times this week, the cap is {}. Daily nudging "
                        "has not worked on this person this week, so it stops here and "
                        "the weekly persistence draft picks it up instead.".format(
                            sent_this_week - 1, limit
                        )
                    ),
                }
            )
            continue

        streak = max(1, lib.streak_behind(entries, person, today, scoring))
        level = ladder[min(streak, len(ladder)) - 1]

        reasons = []
        if expected > 0 and logged < nudge["behind_ratio"] * expected:
            reasons.append(
                "logged {:.1f}h of {:.1f}h expected week to date".format(
                    logged / 60, expected / 60
                )
            )
        if missing:
            reasons.append(
                "no same-day entry for {}".format(", ".join(missing))
            )

        targets.append(
            {
                "name": person["name"],
                "email": person.get("email"),
                "slack_member_id": person.get("slack_member_id"),
                "timezone": person["timezone"],
                "local_time": now_local.strftime("%Y-%m-%d %H:%M"),
                "logged_hours": round(logged / 60, 2),
                "expected_hours": round(expected / 60, 2),
                "deficit_hours": round(max(0.0, expected - logged) / 60, 2),
                "missing_days": missing,
                "missing_days_human": missing_human,
                "weekdays_behind_in_a_row": streak,
                "nudges_this_week_including_this_one": sent_this_week,
                "escalation": level,
                "channels": ["slack"] + (["email"] if nudge.get("email_enabled") else []),
                "reasons": reasons,
            }
        )

    print(
        json.dumps(
            {
                "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "nudge_now": targets,
                "on_track_do_not_contact": on_track,
                "suppressed_by_weekly_cap": capped,
                "outside_window": asleep,
                "email_enabled": bool(nudge.get("email_enabled")),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
