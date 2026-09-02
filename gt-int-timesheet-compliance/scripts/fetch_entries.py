"""Dump Asana time tracking entries for a date range.

  python scripts/fetch_entries.py --start 2026-08-31 --end 2026-09-04 --out /tmp/entries.json

Useful on its own when you want to look at the raw data, and useful to avoid
hitting the API twice when you run who_is_behind.py and score.py back to back.
Without --out it prints to stdout.
"""

import argparse
import json

import _lib as lib


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", required=True, help="YYYY-MM-DD, inclusive")
    parser.add_argument("--end", required=True, help="YYYY-MM-DD, inclusive")
    parser.add_argument("--out", help="write here instead of stdout")
    args = parser.parse_args()

    start = lib.parse_date(args.start)
    end = lib.parse_date(args.end)
    if end < start:
        lib.die("--end is before --start")

    entries = lib.fetch_entries(start, end)
    lib.warn("fetched {} entries between {} and {}".format(len(entries), start, end))

    payload = json.dumps(entries, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(payload)
        lib.warn("wrote {}".format(args.out))
    else:
        print(payload)


if __name__ == "__main__":
    main()
