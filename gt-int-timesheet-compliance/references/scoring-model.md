---
name: scoring-model
description: "How a timesheet accuracy score is built: the four sub-metrics, the weights and why they are set where they are, the gate thresholds, and worked examples including the case that fools a simpler metric."
license: MIT
metadata:
  author: growthtoday
  version: "1.0.0"
  category: internal-ops
---

# The scoring model

Four sub-metrics per person per window, combined into one score between 0 and 1. Every number here is computed by `scripts/score.py`. The weights live in `config/scoring.json` and nowhere else, so changing them is a config edit, not a code edit.

## The weights

| Sub-metric | Weight | What it answers |
|---|---|---|
| Daily hygiene | **30%** | Were these hours remembered, or reconstructed? |
| Attribution | **30%** | Do we know whose budget they came out of? |
| Hours coverage | 25% | Is the total right? |
| On-time submission | 15% | Did it arrive before cutoff? |

Hygiene and attribution carry the most because they are what make hours *usable*. A total can be right and worthless: if the hours were invented on Friday night and pointed at a catch-all task, we cannot bill them, cannot defend them to a client, and cannot plan capacity from them. Coverage and submission are hygiene checks on the process. The other two are checks on whether the data means anything.

Submission sits lowest on purpose. It is the easiest thing to comply with and the easiest to game: someone can submit a blank timesheet on time. Weighting it heavily would reward the exact behaviour we are trying to catch.

## Hours coverage, 25%

```
ratio    = logged / expected
coverage = 1.0                                  if |1 - ratio| <= tolerance_ratio
         = clamp(1 - |logged - expected| / expected, 0, 1)   otherwise
```

`expected` is workdays in the window times that person's `daily_target_hours`. Weekends and configured holidays are excluded.

Over-logging costs the same as under-logging. Someone at 95 hours against 80 expected is not doing better than someone at 80, they are either miscounting or working in a way we need to know about. The default `tolerance_ratio` of 0.05 means anything inside 5% scores a clean 1.0, so nobody loses points for a 15-minute rounding difference.

## Daily hygiene, 30%

```
hygiene = workdays holding an entry created within grace_days of that day
          / workdays in the window
```

This is the anti-backfill mechanism, and it is the reason the model is worth having. An entry only counts for its day if the `created_at` timestamp is within `grace_days` (default 1) of the `entered_on` date. So logging yesterday's work this morning counts. Reconstructing a fortnight on the last Friday does not: those ten days score as one or two.

The script also reports `backfilled_share_of_hours`, the share of minutes that failed this check. That is the number to quote in a coaching conversation, because it is concrete and hard to argue with.

If `created_at` is unavailable on the workspace, hygiene silently becomes "a day with any entry counts", which is much weaker. The script detects that and sets `hygiene_degraded_no_created_at`. Never report a hygiene number with that flag set without saying so.

## Attribution, 30%

```
attribution = minutes attributed to an allowed project / total minutes
```

An entry counts when its `attributable_to` is present, is not in `excluded_project_gids`, and (once the allowlist is non-empty) is in `attributable_project_gids`.

The order of operations matters more here than anywhere else in the model. **Run a baseline period with an empty allowlist first.** While it is empty, any non-null attribution counts and the score carries `attribution_loose_no_allowlist: true`. That gives you a picture of what people actually attribute to, which is what you need to build a sensible allowlist. Setting a 30% weight on a metric nobody can satisfy, because the tasks to attribute to do not exist yet, turns the gate into theatre.

If nothing carries `attributable_to` at all, the metric is `null` and the whole composite is flagged partial. That is a task structure problem and no scoring change fixes it.

## On-time submission, 15%

```
on_time = weeks submitted or approved before cutoff / weeks in the window
```

Read from Asana's approval state, not from anyone saying they submitted. A Slack confirmation is a useful signal for the nudge loop and is not evidence here. Where the two disagree, that gap is itself worth a conversation.

Until `approval_endpoint.path` is verified and configured, this metric is `null`, the other three weights are renormalized over what is available, and every affected score carries `weights_renormalized: true`.

## Combining them

```
score = sum(weight * metric) over metrics that exist
        / sum(weight) over metrics that exist
```

Renormalizing rather than treating a missing metric as zero is deliberate: a metric we cannot measure is not the same as a person scoring nothing on it. The cost is that a three-metric score and a four-metric score are not directly comparable. Do not chart them together without labelling which is which.

## The gate

```
passing      = mean(score) >= 0.80 for 2 consecutive pay periods
               AND min(score) >= 0.60
trustworthy  = passing AND no metric was missing in either period
```

`trustworthy` is the field that licenses a payroll decision. `passing` on its own can be true while a metric was unavailable, and the script reports that combination as not passed.

The individual floor is what stops a good average from hiding someone. A team mean of 0.82 carrying one person at 0.31 is not a passing team.

## Worked examples

Four people, one two-week period, ten workdays, eight hours a day expected. Illustrative figures, not a read on anyone real. Scores here are computed over all four metrics.

| | Logged | Days on time | Backfilled | Coverage | Hygiene | Attribution | On-time | **Score** |
|---|---|---|---|---|---|---|---|---|
| Working as intended | 80h | 10 / 10 | 0% | 1.00 | 1.00 | 1.00 | 1.00 | **1.00** |
| Hours fine, habit broken | 80h | 4 / 10 | 60% | 1.00 | 0.40 | 1.00 | 1.00 | **0.82** |
| Diligent, slightly short, half on a catch-all | 55h | 10 / 10 | 0% | 0.92 | 1.00 | 0.73 | 1.00 | **0.90** |
| Barely logging | 4h | 2 / 10 | 0% | 0.05 | 0.20 | 0.00 | 0.00 | **0.07** |

The second row is the one that matters. Eighty hours out of eighty expected, submitted on time, every hour pointed at a client project. A submission-rate metric calls that person fully compliant. The hygiene weight is what surfaces that 60% of those hours were typed in from memory at the end of each week, which means the client attribution underneath them is a best guess. At 0.82 they still pass the team threshold, and that is the right outcome: the total is genuinely fine and the habit needs work, so the score should be a nudge rather than an alarm.

Row three shows why coverage is not the top weight. Someone logging religiously every day and landing at 55 of 60 hours is not a compliance problem, and the model should not scream about them. Their real issue is the catch-all task taking half their time, which is exactly where the attribution weight points you.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
