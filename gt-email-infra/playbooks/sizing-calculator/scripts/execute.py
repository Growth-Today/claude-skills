# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Infrastructure sizing — execute step.

Monthly goal (or contacts x steps / days-to-clear) -> daily volume -> mailboxes
-> mailboxes to buy -> Google/Microsoft split -> domains.

The point of this script is NOT the arithmetic. It is that the per-provider cold
limits are PARSED OUT OF resources/reference.md §1 at run time instead of being
typed in. The Notion version of this SOP carried a hardcoded "Google 30 /
Microsoft 10", which produced a blended 22/mailbox/day and under-bought
inventory by ~43%. A number that is read from the source of truth cannot drift
from it. If §1 changes, this script changes with it.

Read-only. No network. Standard library only.

Usage:
    uv run execute.py --monthly-goal 15000
    uv run execute.py --contacts 9000 --steps 4 --days-to-clear 5
    uv run execute.py --monthly-goal 15000 --have-google 12 --have-outlook 8
    uv run execute.py --validate        # reproduce the §4 table exactly
"""

import argparse
import math
import re
import sys
from pathlib import Path

# ── Locate the source of truth ───────────────────────────────────

REFERENCE = Path(__file__).resolve().parents[3] / "resources" / "reference.md"

WORKING_DAYS = 20      # reference.md §4 step 1
BUFFER = 1.5           # reference.md §4 step 3
SPLIT_GOOGLE = 0.60    # reference.md §4 step 5
MB_PER_DOMAIN_GOOGLE = 2.5   # §4: Google 2-3
MB_PER_DOMAIN_MS = 25        # §4: Microsoft up to ~25

DAYS_TO_CLEAR = {
    "website-visitor": 1, "app-install": 1, "churn": 1,
    "hiring": 5,
    "one-off": 20,
    "evergreen": 45,
}


def load_cold_limits(path=REFERENCE):
    """Parse the 'After warmup (sending)' row out of reference.md §1.

    Expected row shape:
      | After warmup (sending) | 20 | 30 | 5 | 15 |
        state                    G-cold G-warm O-cold O-warm
    """
    if not path.exists():
        sys.exit(
            f"Cannot find {path}\n"
            "This script must run from inside the skill so it can read §1. "
            "Sizing from a typed-in limit is exactly the bug this replaces."
        )
    for line in path.read_text().splitlines():
        if "After warmup (sending)" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        nums = [int(m.group()) for c in cells[1:] if (m := re.search(r"\d+", c))]
        if len(nums) >= 4:
            return {"google_cold": nums[0], "google_warmup": nums[1],
                    "outlook_cold": nums[2], "outlook_warmup": nums[3]}
    sys.exit("Could not parse the 'After warmup (sending)' row from reference.md §1.")


# ── Sizing ───────────────────────────────────────────────────────

def size(limits, monthly_goal=None, contacts=None, steps=None, days_to_clear=20,
         split_google=SPLIT_GOOGLE, have_google=0, have_outlook=0):
    g_cold, o_cold = limits["google_cold"], limits["outlook_cold"]

    if monthly_goal:
        daily = monthly_goal / WORKING_DAYS
        basis = f"{monthly_goal:,} / month over {WORKING_DAYS} working days"
    else:
        daily = contacts * steps / days_to_clear
        basis = f"{contacts:,} contacts x {steps} steps / {days_to_clear} days to clear"

    per_mb = split_google * g_cold + (1 - split_google) * o_cold
    needed = daily / per_mb
    to_buy = needed * BUFFER

    g = math.ceil(to_buy * split_google)
    m = math.ceil(to_buy * (1 - split_google))
    domains = math.ceil(g / MB_PER_DOMAIN_GOOGLE) + math.ceil(m / MB_PER_DOMAIN_MS)

    have_cap = have_google * g_cold + have_outlook * o_cold

    return {
        "basis": basis, "daily": daily, "per_mb": per_mb,
        "needed": math.ceil(needed), "buy_total": g + m,
        "google": g, "microsoft": m, "domains": domains,
        "have_cap": have_cap, "gap": have_cap - daily,
    }


def report(r, limits, split_google, show_have):
    print(f"  Basis                        : {r['basis']}")
    print(f"  Daily requirement            : {r['daily']:,.0f} emails/day")
    print(f"  Blended capacity per mailbox : {r['per_mb']:.1f}/day  "
          f"({split_google:.0%} Google @ {limits['google_cold']} + "
          f"{1-split_google:.0%} Outlook @ {limits['outlook_cold']})")
    print(f"  Mailboxes needed             : {r['needed']}")
    print(f"  Mailboxes to BUY (x{BUFFER})     : {r['buy_total']}")
    print(f"  Split                        : {r['google']} Google + {r['microsoft']} Microsoft")
    print(f"  Domains                      : {r['domains']}  "
          f"(Google /{MB_PER_DOMAIN_GOOGLE}, Microsoft /{MB_PER_DOMAIN_MS})")
    if show_have:
        verdict = "ENOUGH" if r["gap"] >= 0 else "SHORT"
        print(f"  Current capacity             : {r['have_cap']:,.0f}/day -> "
              f"{verdict} ({r['gap']:+,.0f}/day)")


# ── Validation against the published table ───────────────────────

EXPECTED = {   # reference.md §4 table
    3000:  (150,   11, 17,  10, 7,  5),
    7500:  (375,   27, 42,  25, 17, 11),
    15000: (750,   54, 82,  49, 33, 22),
    30000: (1500, 108, 162, 97, 65, 42),
}


def validate(limits):
    print("=" * 68)
    print("VALIDATION — reproduce the reference.md §4 table")
    print("=" * 68)
    ok = True
    for goal, exp in EXPECTED.items():
        r = size(limits, monthly_goal=goal)
        got = (round(r["daily"]), r["needed"], r["buy_total"],
               r["google"], r["microsoft"], r["domains"])
        match = got == exp
        ok &= match
        print(f"  {goal:>6,} /mo  expected {exp}  got {got}  "
              f"{'MATCH' if match else 'MISMATCH'}")
    print("=" * 68)
    if ok:
        print("Calculator and published table agree exactly.")
    else:
        print("MISMATCH — the table in reference.md §4 and this script disagree. "
              "Fix the table, not the script.")
    return 0 if ok else 2


# ── Main ─────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Size cold-email infrastructure from reference.md §1.")
    ap.add_argument("--monthly-goal", type=int, help="Emails per month")
    ap.add_argument("--contacts", type=int, help="Contacts in the list")
    ap.add_argument("--steps", type=int, help="Steps in the sequence")
    ap.add_argument("--days-to-clear", default="20",
                    help=f"Days, or one of: {', '.join(DAYS_TO_CLEAR)}")
    ap.add_argument("--split-google", type=float, default=SPLIT_GOOGLE)
    ap.add_argument("--have-google", type=int, default=0)
    ap.add_argument("--have-outlook", type=int, default=0)
    ap.add_argument("--validate", action="store_true", help="Reproduce the §4 table and exit")
    args = ap.parse_args()

    limits = load_cold_limits()
    print("=" * 68)
    print("INFRASTRUCTURE SIZING")
    print(f"Limits read live from {REFERENCE.name} §1: "
          f"Google cold {limits['google_cold']} · Outlook cold {limits['outlook_cold']}")
    print("=" * 68)

    if args.validate:
        sys.exit(validate(limits))

    dtc = DAYS_TO_CLEAR.get(args.days_to_clear, None)
    if dtc is None:
        try:
            dtc = int(args.days_to_clear)
        except ValueError:
            ap.error(f"--days-to-clear must be a number or one of {list(DAYS_TO_CLEAR)}")

    if not args.monthly_goal and not (args.contacts and args.steps):
        ap.error("give either --monthly-goal, or --contacts with --steps")

    r = size(limits, monthly_goal=args.monthly_goal, contacts=args.contacts,
             steps=args.steps, days_to_clear=dtc, split_google=args.split_google,
             have_google=args.have_google, have_outlook=args.have_outlook)
    report(r, limits, args.split_google, bool(args.have_google or args.have_outlook))
    print("=" * 68)
    print("Buying is ScaledMail's job. Hand them the numbers above plus the "
          "spread rule (multi-day, max 4 per registrar per day).")
    print("=" * 68)


if __name__ == "__main__":
    main()
