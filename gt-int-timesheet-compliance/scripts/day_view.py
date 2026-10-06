"""Print one line per person per weekday, so a run log can be read against Asana.

  python scripts/day_view.py --days 10
  python scripts/day_view.py --entries /tmp/entries.json --days 5

Exists because every number this skill reports is an aggregate, and an
aggregate cannot be checked. When somebody says "that is not what my timesheet
says", the only useful answer is a list of days with hours against them, next
to the same list in Asana, so the missing row can be pointed at.

Output is pipe-delimited with no braces in it, for the same reason summarise.py
is: a pretty-printed ROSTER_JSON secret makes GitHub mask every lone brace in
the log, and JSON would come back full of asterisks.

Columns, after DAY:
  name | date | weekday | hours | when it was entered | state

state is one of:
  on time    an entry created within grace_days of the day it covers
  late       the hours are there, entered more than grace_days afterwards
  empty      a working day with nothing on it
  leave      a day off for this person, or a company holiday
  weekend    not shown, weekends are skipped entirely
"""

import argparse
import datetime as dt
import json

import _lib as lib


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=10, help="how many days back to show")
    parser.add_argument("--entries", help="reuse a fetch_entries.py dump instead of the API")
    args = parser.parse_args()

    scoring = lib.load_scoring()
    people = lib.load_roster()
    grace = scoring["hygiene"]["grace_days"]

    end = dt.datetime.now(dt.timezone.utc).date()
    start = end - dt.timedelta(days=args.days)

    if args.entries:
        with open(args.entries, "r", encoding="utf-8") as handle:
            raw = json.load(handle)
    else:
        raw = lib.fetch_entries(start, end)

    by_person = lib.index_entries(raw, people)
    holidays = {lib.parse_date(h) for h in (scoring.get("holidays") or [])}
    floor = lib.program_start(scoring)

    for person in people:
        entries = by_person.get(person["asana_gid"], [])
        off = holidays | lib.leave_days(person)

        cursor = start
        while cursor <= end:
            if cursor.weekday() >= 5 or (floor and cursor < floor):
                cursor += dt.timedelta(days=1)
                continue

            same_day = [
                e
                for e in entries
                if e.get("entered_on") and lib.parse_date(e["entered_on"]) == cursor
            ]
            minutes = sum(e.get("duration_minutes") or 0 for e in same_day)
            created = sorted(
                {
                    lib.iso(c)
                    for c in (lib.parse_created_at(e.get("created_at")) for e in same_day)
                    if c is not None
                }
            )

            if cursor in off:
                state = "leave"
            elif not same_day:
                state = "empty"
            elif lib.logged_on_day(entries, cursor, grace):
                state = "on time"
            else:
                state = "late"

            print(
                "DAY | {} | {} | {} | {} | {} | {}".format(
                    person["name"],
                    lib.iso(cursor),
                    cursor.strftime("%a"),
                    "{:g}h".format(round(minutes / 60.0, 2)) if minutes else "none",
                    ", ".join(created) if created else "not entered",
                    state,
                )
            )
            cursor += dt.timedelta(days=1)


if __name__ == "__main__":
    main()
