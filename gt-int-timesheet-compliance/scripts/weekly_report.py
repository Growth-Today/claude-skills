"""Post the weekly timesheet digest to a Slack channel, for the unattended runner.

  python scripts/weekly_report.py --scores /tmp/scores.json
  python scripts/weekly_report.py --scores /tmp/scores.json --send

Reads score.py output and posts one message: team mean, then a line per person.
Dry run by default.

This is the table, not the review. It cannot tell you that eighty logged hours
were reconstructed on Friday night, which is the sentence the Friday review
exists to produce. Attach the JSON to the run and read it properly once a week.

Needs SLACK_BOT_TOKEN with chat:write, and SLACK_REPORT_CHANNEL.
"""

import argparse
import json
import os

import _lib as lib
from send_nudges import slack_post


def fmt(value, digits=2):
    return "n/a" if value is None else "{:.{d}f}".format(value, d=digits)


def build(period, messages):
    team = period["team"]
    people = period["people"]
    header = messages["weekly_digest_header"].format(
        week_of=period["window"]["start"],
        scored=team["people_scored"],
        total=len(people),
        mean=fmt(team["mean_score"]),
    )

    rows = []
    for person in sorted(people, key=lambda p: (p["score"] is None, p["score"] or 0)):
        rows.append(
            messages["weekly_digest_row"].format(
                name=person["name"],
                logged=fmt(person["logged_hours"], 1),
                expected=fmt(person["expected_hours"], 1),
                days_on_time=person["days_logged_on_time"]
                if person["days_logged_on_time"] is not None
                else "?",
                workdays=person["workdays"],
                score=fmt(person["score"]),
            )
        )

    notes = []
    if any(p["flags"]["weights_renormalized"] for p in people):
        notes.append(
            "_Partial scores: at least one metric was unavailable, so these are not "
            "final and are not comparable to a four-metric week._"
        )
    if any(p["flags"]["attribution_loose_no_allowlist"] for p in people):
        notes.append(
            "_Attribution is running loose: no project allowlist is set, so any "
            "attributed time counts._"
        )
    if any(p["flags"]["hygiene_degraded_no_created_at"] for p in people):
        notes.append(
            "_Backfill detection is off for this window, so daily hygiene is weaker "
            "than it looks._"
        )

    parts = [header, ""] + rows
    if notes:
        parts += [""] + notes
    parts += ["", messages["weekly_digest_footer"]]
    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scores", required=True, help="score.py output")
    parser.add_argument("--send", action="store_true", help="actually post. Without this, dry run")
    args = parser.parse_args()

    with open(args.scores, "r", encoding="utf-8") as handle:
        payload = json.load(handle)

    periods = payload.get("periods") or []
    if not periods:
        lib.die("No periods in the score output.")

    text = build(periods[0], lib.load_messages())
    print(text)

    if not args.send:
        print("\nDRY RUN. Add --send to post it.")
        return

    token = os.environ.get("SLACK_BOT_TOKEN")
    channel = os.environ.get("SLACK_REPORT_CHANNEL")
    if not token or not channel:
        lib.die("--send needs both SLACK_BOT_TOKEN and SLACK_REPORT_CHANNEL.")

    slack_post("chat.postMessage", token, {"channel": channel, "text": text})
    print("\nPosted to {}.".format(channel))


if __name__ == "__main__":
    main()
