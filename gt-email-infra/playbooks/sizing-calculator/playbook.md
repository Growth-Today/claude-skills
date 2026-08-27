---
name: sizing-calculator
description: "Size cold-email infrastructure from a monthly goal or a deadline-driven campaign: daily volume, mailboxes needed, mailboxes to buy, Google/Microsoft split, and domain count. Reads the per-provider send limits live from reference.md so the numbers cannot drift from the standard."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: planning
---

# Infrastructure Sizing Calculator

Work backwards from what the client wants to send to what we have to buy. Replaces the Notion bandwidth SOP, its Google Sheet, and the Row Zero inbox-count lookup.

## Why This Matters

This is not here to save arithmetic. It is here because **the arithmetic was wrong for a long time and nobody noticed.**

The Notion SOP told you to divide daily volume by "20–25 emails per mailbox." Two figures got
collapsed into a range there: **20 is Growth Today's own per-mailbox number for a Google inbox,
25 is ScaledMail's.** We run the lower one.

But the deeper problem isn't which of the two you pick — it's that **both describe a Google
mailbox, and a Microsoft mailbox sends 5.** Applying either to a mixed fleet assumes every
inbox is Google-like. On a 50/50 fleet the real blended figure is 12.5 — and our own Instantly
workspace went the other way, 25 Google / 0 Microsoft on the 21 Aug audit. Neither is a default;
both are answers to the question you have to ask.

**How much it matters:** at 15,000/month, an all-Google client needs **57** mailboxes and a
25/75 client needs **129**. Same goal, same formula, 2.3× the inventory. Size a Microsoft-heavy
client on the Google number and you plan infrastructure that cannot carry the campaign — which
shows up later as inboxes pushed past their limits, the exact thing that burns them.

So the script does not contain the limits or a fixed split. It **parses the limits out of
`resources/reference.md` §1 at run time** and **takes the split as a required judgement call**
via `--split-google`. A hardcoded number drifts from the standard; a parsed one cannot, and a
split you have to state is a split you have to think about.

## Prerequisites

- Nothing. No API key, no network, standard library only.
- Must run from inside the skill directory so it can find `resources/reference.md`. It refuses to run otherwise, on purpose.

## Interview: Gather Requirements

**Q1: Do you have a monthly email goal, or a list and a deadline?**
- *Monthly goal* — use `--monthly-goal`. Divides by 20 working days.
- *List and deadline* — use `--contacts`, `--steps` and `--days-to-clear`. This is the honest one for a real campaign, because sequence steps multiply the send volume and most people forget that.

**Q2: How fast must the campaign clear?**
Named presets are built in, from `reference.md` §4:

| Preset | Days | When |
|---|---|---|
| `website-visitor`, `app-install`, `churn` | 1 | Act the same day or the signal is dead |
| `hiring` | 5 | Roles close inside a week |
| `one-off` | 20 | Standard month, initial tests |
| `evergreen` | 45 | Long-running, balanced against other campaigns |

The same list run in 5 days instead of 20 needs **4× the daily capacity**. This is the single biggest driver of a sizing surprise.

**Q3: What already exists?**
Pass `--have-google` and `--have-outlook` to get a gap read against current capacity instead of a greenfield number.

**Q4: What is this client's Google / Microsoft mix?**
`--split-google` is required — there is no default, because there is no house mix. Ask the client. Note that domain count is driven almost entirely by the Google side — Google holds 2–3 mailboxes per domain, Microsoft up to ~25 — so shifting the split moves the domain bill far more than the mailbox bill.

## Plan

1. Establish the goal (monthly target, or contacts × steps ÷ days to clear).
2. Run `execute.py`.
3. Sanity-check the run header — it prints which limits it read from §1. If those aren't the current standard, stop and fix `reference.md`, not the output.
4. Hand the mailbox and domain counts to ScaledMail, together with the spread rule.

## Execute

```bash
cd playbooks/sizing-calculator/scripts

# Monthly goal
uv run execute.py --monthly-goal 15000

# Deadline-driven, against existing capacity
uv run execute.py --contacts 9000 --steps 4 --days-to-clear hiring \
                  --have-google 12 --have-outlook 8

# Prove the calculator still agrees with the published table
uv run execute.py --validate
```

Every run prints its source limits in the header:

```
Limits read live from reference.md §1: Google cold 20 · Outlook cold 5
```

If that line is ever wrong, every number below it is wrong. Read it.

## After State

`--validate` is the regression test. It reads **both** §4 tables out of `reference.md` — the provider-mix grid and the 60/40 worked example — and recomputes every row. Nothing is hardcoded in the script, so editing a number in the doc without editing the model makes this fail.

```
  Provider-mix grid (5 rows, 15,000/mo):
  Worked example at 60/40 (4 rows):
     3,000 /mo  expected (150, 11, 17, 10, 7, 5)  got (150, 11, 17, 10, 7, 5)  MATCH
     7,500 /mo  expected (375, 27, 41, 25, 16, 11)  got (375, 27, 41, 25, 16, 11)  MATCH
    15,000 /mo  expected (750, 54, 81, 49, 32, 22)  got (750, 54, 81, 49, 32, 22)  MATCH
    30,000 /mo  expected (1500, 108, 162, 97, 65, 42)  got (1500, 108, 162, 97, 65, 42)  MATCH
```

**Run this after any edit to `reference.md` §1 or §4.** A MISMATCH means the doc and the model disagree. Work out which one is wrong before you touch either.

**Verification checklist:**

1. `--validate` reports MATCH on all nine rows (5 mix + 4 worked example).
2. The header shows the current §1 cold limits.
3. The blended capacity line reads 14.0/day at a 60/40 mix. If it says 22, someone has put the deprecated Google 30 / Microsoft 10 limits back into §1.

## Key Technical Learnings

- **A number typed into a script is a number that will go stale.** This one is parsed from the source of truth, and the header makes the dependency visible on every run. Copy that pattern into the other playbooks.
- **The buffer applies to every tier.** An earlier version of the table applied ×1.5 to the smallest row only, which made the larger tiers look cheap. Round whole mailboxes first, then buffer, then round again — and take the Google/Microsoft split out of that total, so the two provider counts always add back up to it. Rounding each provider separately quietly inflates the buy.
- **Days-to-clear is where sizing surprises live.** Multiplying by sequence steps and dividing by a real deadline can produce several times the greenfield "monthly goal" answer — how much depends entirely on the deadline. Ask for the deadline.
- **This sizes the buy, it does not make it.** Purchasing, registrar spread and timing sit with ScaledMail. Hand over the counts plus the rule: multiple registrars, multiple days, max 4 per registrar per day. GT verifies on delivery.

---

*Part of [gt-email-infra](https://www.growthtoday.co/claude-skills) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
