# Changelog

All notable changes to the timesheet compliance skill.

## 1.1.0

Escalation reworked after review, plus the weekly pattern check.

**Changed**

- The daily nudge now contacts the person and nobody else, at every level of the ladder. The old top rung that copied a squad lead is gone, and the copy rules forbid mentioning that a manager will be told.
- The nudge window opens on the hour and runs for an hour, so a single cron minute can land inside it for a timezone with a half-hour offset.
- `escalation_contacts` moved to `roster.json`, so no real person's name or Slack ID sits in a committed config file.

**Added**

- `score.py --weeks N` scores trailing weeks individually and runs a persistence check. Someone is flagged when their weekly score fell below the individual floor in at least 2 of the last 3 weeks, or when they ran 4 or more consecutive weekdays behind inside any one week.
- A weekly persistent-pattern step in the Friday review that writes one draft addressed to the escalation contacts. It is a draft only. Nothing is sent, and it never goes to the flagged person.
- Shared behind and streak helpers in `_lib.py`, so the daily nudge and the weekly rule use one definition of "behind" rather than two copies.

**Fixed**

- The retrospective streak now reconstructs what had actually been entered as of each day, via a new `as_of` filter on `logged_minutes`. Before this, someone who reconstructed a whole week on Friday looked like they were never behind, because in hindsight their entries carry the correct earlier dates. Verified: a person with the right weekly total, all of it backfilled, now trips the streak condition at 4 days while their score stays above the floor.

## 1.0.0

First working version. Covers the three jobs end to end: weekday nudge, Friday review, biweekly gate.

**Added**

- `SKILL.md` router with the rule that all arithmetic runs in the scripts, never in the model.
- `scripts/fetch_entries.py`, `scripts/who_is_behind.py`, `scripts/score.py` and the shared `scripts/_lib.py`. Asana pagination, rate-limit retry, and a clear 403 message pointing at the missing `time_tracking_entries:read` scope.
- Four sub-metric scoring model weighted 30% daily hygiene, 30% attribution, 25% hours coverage, 15% on-time submission. Gate at a team mean of 0.80 across two consecutive pay periods with an individual floor of 0.60.
- Backfill detection: an entry only counts toward daily hygiene if it was created within a day of the date it covers, so a reconstructed fortnight scores one or two days rather than ten.
- Timezone-aware nudging. One scheduler covers a roster spanning Europe, Asia and Africa without waking anyone in the middle of the night.
- Stateless escalation. The ladder is derived from consecutive weekdays behind, recomputed from the entries each run, so a missed run or a recycled container changes nothing.
- Honest degradation. A missing metric reports as unavailable, the remaining weights renormalize, and the output is flagged partial rather than presenting a confident number built on a gap.
- Three playbooks, plus setup, scoring model and Make build spec references.

**Notes**

- The on-time metric is inert until `approval_endpoint.path` is verified against the workspace and filled in. No endpoint path is guessed in shipped code.
- `config/roster.json` is gitignored. Only the example ships, because a real roster holds names, work emails and Slack member IDs.
- Verified against synthetic entries covering four archetypes: clean, backfilled, diligent but short, and barely logging. Sub-metric outputs and the composite arithmetic match the worked examples in `references/scoring-model.md`.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
