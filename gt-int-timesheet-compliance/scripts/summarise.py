"""Flatten the scoring and nudge JSON into lines a log can carry intact.

  python scripts/summarise.py --scores week.json --targets targets.json

Why this exists. GitHub masks secrets in run logs line by line, and the roster
travels as the ROSTER_JSON secret. That secret is pretty-printed JSON, so lines
consisting of a single brace are themselves secret values, and every brace in
every other line of the log gets replaced by three asterisks. The JSON printed
into the log is then no longer JSON, which matters because artifact bytes are
served from storage an agent session usually cannot reach, so the log is the
only place a session can read these numbers from.

This output has no braces in it at all, so nothing can be mangled. Pipes and
plain words survive masking, whatever the roster secret happens to look like.
"""

import argparse
import json


def num(value, digits=1):
    if value is None:
        return "n/a"
    return "{:.{}f}".format(value, digits)


def scores_block(doc):
    lines = []
    for period in doc.get("periods", []):
        window = period.get("window", {})
        team = period.get("team", {})
        people = period.get("people", [])
        lines.append(
            "WEEK | {} to {} | workdays {} | team mean {} | below floor {} of {}".format(
                window.get("start"),
                window.get("end"),
                window.get("workdays"),
                num(team.get("mean_score"), 3),
                team.get("people_below_floor"),
                team.get("people_scored"),
            )
        )
        for row in people:
            metrics = row.get("metrics", {})
            flags = row.get("flags", {})
            notes = [k for k, v in flags.items() if v is True]
            missing = flags.get("missing_metrics") or []
            lines.append(
                "SCORE | {} | {}h of {}h | on time {} of {} | hygiene {} | "
                "attribution {} | score {} | notes {}".format(
                    row.get("name"),
                    num(row.get("logged_hours")),
                    num(row.get("expected_hours")),
                    row.get("days_logged_on_time"),
                    row.get("workdays"),
                    num(metrics.get("daily_hygiene"), 2),
                    num(metrics.get("attribution"), 2),
                    num(row.get("score"), 2),
                    ", ".join(notes + ["missing " + m for m in missing]) or "none",
                )
            )
    return lines


def targets_block(doc):
    lines = []
    for row in doc.get("nudge_now", []):
        lines.append(
            "BEHIND | {} | {} | {}h of {}h week to date | not logged on the day {} | "
            "weekdays behind in a row {} | nudge {} this week".format(
                row.get("name"),
                row.get("escalation"),
                num(row.get("logged_hours")),
                num(row.get("expected_hours")),
                ", ".join(row.get("missing_days_human") or []) or "none",
                row.get("weekdays_behind_in_a_row"),
                row.get("nudges_this_week_including_this_one"),
            )
        )
    for row in doc.get("on_track_do_not_contact", []):
        lines.append(
            "ON TRACK | {} | {}h of {}h week to date".format(
                row.get("name"),
                num(row.get("logged_hours")),
                num(row.get("expected_hours")),
            )
        )
    for key, label in (
        ("suppressed_by_weekly_cap", "AT WEEKLY CAP"),
        ("not_counted_yet", "NOT COUNTED YET"),
        ("outside_window", "OUTSIDE WINDOW"),
        ("another_fire_owns_this_timezone", "ANOTHER FIRE OWNS THIS TIMEZONE"),
    ):
        for row in doc.get(key) or []:
            lines.append("{} | {} | {}".format(label, row.get("name"), row.get("why", "")))
    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scores", help="score.py output")
    parser.add_argument("--targets", help="who_is_behind.py output")
    args = parser.parse_args()

    lines = []
    if args.scores:
        with open(args.scores, "r", encoding="utf-8") as handle:
            lines += scores_block(json.load(handle))
    if args.targets:
        with open(args.targets, "r", encoding="utf-8") as handle:
            lines += targets_block(json.load(handle))

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
