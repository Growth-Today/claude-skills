---
name: biweekly-gate
description: "The biweekly accuracy gate: score two consecutive pay periods and decide whether timesheets are trustworthy enough to drive payroll and client billing."
license: MIT
metadata:
  author: growthtoday
  version: "1.0.0"
  category: internal-ops
---

# Biweekly gate

## Why this matters

Most of the team is paid every two weeks, so a two-week window is the only unit that matters for this decision. The gate exists to stop one good fortnight from being mistaken for a working process. Until it passes, timesheets are measured and nagged but they do not drive money. That is shadow mode, and staying in it is a normal outcome, not a failure.

## Prerequisites

- Two full pay periods of data behind the anchor date.
- The anchor must be the Monday that starts the most recent finished period. The script rejects any other weekday, on purpose.

## Plan

1. Score both periods and read the gate verdict.
2. Report the verdict either way, with the reason.
3. If it fails, name the specific blocker and the one action that moves it.

## Before state

```bash
cd <skill>/scripts
python score.py --gate-anchor <monday> --periods 2
```

The `gate` block gives you two fields that are not the same thing:

- `passing`: the arithmetic cleared both thresholds.
- `trustworthy`: it cleared them *and* no metric was missing. This is the one that licenses a payroll decision.

`passing: true` with `trustworthy: false` means the gate technically cleared while one of the four metrics was unavailable. Report it as not passed. Fix the missing metric first.

## Execute

Report in this order, whatever the verdict:

1. **The verdict**, in one sentence, with both period means.
2. **The blocker**, if any. There are only three: the team mean is short, one person is below the floor, or a metric was missing. Name which.
3. **The trend.** Period over period, is the mean moving up, flat, or down? Two periods is enough for a direction and not enough for a trend line. Say which you have.
4. **One action per amber or red person.** Named, specific, and pointed at the sub-metric that is actually low. "Log at the end of each day" for hygiene. "We need a task for this work" for attribution. "Let us talk about the target" for coverage.

If the gate passes and is trustworthy, say plainly that timesheets are now payroll-grade, and hand the switchover decision to a person. Do not change anything in payroll yourself.

If the gate has now failed four periods in a row, stop treating it as a reminder problem. Eight weeks of nudging that has not moved the number means the target, the task structure, or the expectation is wrong. Say that instead of proposing more nudges.

## After state

- Verdict posted with both period means and the named blocker.
- Every amber or red person has one action tied to one sub-metric.
- Shadow mode confirmed as still on, or the switchover explicitly handed to a person.

## Key technical learnings

- Any past period recomputes on demand, because Asana holds the entries and nothing here caches. So a gate report is never blocked by a missed run, and you can re-derive the whole history after changing a weight. Changing a weight rewrites history, though, so note the config change next to any number you compare across time.
- Attribution at 30% cannot pass while `attributable_project_gids` is empty and people log to catch-all tasks. Run one baseline period, look at what `attributable_to` actually contains, then fill the allowlist. Setting a 30% weight on a metric nobody can satisfy is how a gate becomes theatre.
- `people_below_floor` matters more than the mean. A team mean of 0.82 carrying one person at 0.31 is not a passing team, and the floor check is what catches it.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
