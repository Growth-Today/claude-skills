# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "dnspython>=2.6",
# ]
# ///
"""
DNS / auth audit — after step.

Re-runs the audit and diffs it against the CSV written by execute.py, so a
DNS fix is proven to have landed rather than assumed. This is the step the
manual MXToolBox workflow never had, and it is why silent drift went unnoticed.

Usage:
    uv run after.py --csv dns_audit.csv

Exit code: 0 = every previous FAIL is resolved and nothing regressed,
           2 = FAILs remain or something regressed.
"""

import argparse
import csv
import sys
from collections import defaultdict

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from execute import audit  # noqa: E402  (same directory)


RANK = {"PASS": 0, "WARN": 1, "FAIL": 2}   # severity, for spotting a downgrade


def load_before(path):
    before = defaultdict(dict)
    with open(path) as fh:
        for r in csv.DictReader(fh):
            before[r["domain"]][r["dimension"]] = r["verdict"]
    return before


def main():
    ap = argparse.ArgumentParser(description="Re-audit and diff against the before state.")
    ap.add_argument("--csv", default="dns_audit.csv", help="CSV written by execute.py")
    args = ap.parse_args()

    before = load_before(args.csv)
    if not before:
        sys.exit(f"No rows in {args.csv} — run execute.py first.")

    print("=" * 68)
    print("AFTER STATE: re-audit vs before")
    print("=" * 68)

    fixed = regressed = still_failing = 0

    for domain, dims in before.items():
        _, rows = audit(domain)
        now = {dim: v for dim, v, _ in rows}
        lines = []
        for dim, was in dims.items():
            is_ = now.get(dim, "?")
            if was == is_:
                if is_ == "FAIL":
                    still_failing += 1
                    lines.append(f"  [STILL FAIL] {dim:12} unchanged")
                continue
            # A downgrade is a regression, not a change. PASS -> WARN is how a
            # DMARC drops from p=reject to p=none and how a DKIM key disappears;
            # both used to print [CHANGED] and exit 0, which is the exact drift
            # this script exists to catch.
            if RANK.get(is_, 0) < RANK.get(was, 0):
                fixed += 1
                lines.append(f"  [FIXED]      {dim:12} {was} -> {is_}")
            elif RANK.get(is_, 0) > RANK.get(was, 0):
                regressed += 1
                lines.append(f"  [REGRESSED]  {dim:12} {was} -> {is_}")
            else:
                lines.append(f"  [CHANGED]    {dim:12} {was} -> {is_}")
        if lines:
            print(f"\n{domain}")
            print("\n".join(lines))

    print("\n" + "=" * 68)
    print(f"{fixed} fixed · {still_failing} still failing · {regressed} regressed")
    if regressed:
        print("REGRESSION: a record got worse since the baseline — including PASS -> WARN,\nwhich is how p=reject quietly becomes p=none. Treat as P0.")
    elif still_failing:
        print("Not clear to launch — FAILs remain.")
    else:
        print("All previous FAILs resolved, nothing regressed.")
    print("=" * 68)

    sys.exit(2 if (regressed or still_failing) else 0)


if __name__ == "__main__":
    main()
