# Changelog

All notable changes to the timesheet compliance skill.

## 1.2.1

**Fixed**

- Corrected the developer console location. Personal access tokens are at `app.asana.com/0/developer-console`, reached through My Settings, Apps, Manage Developer Apps. The path previously documented here did not resolve, and looking under the Apps settings list alone turns up nothing because the tokens live in the console rather than that list.

**Changed**

- Setup now recommends a **service account** over a personal token where the plan allows one. It reads org-wide, so a team score cannot be quietly incomplete; it is not tied to a person, so it survives a deactivation that would otherwise stop a scheduled job reading half the team; and a super admin can revoke it centrally. The trade-off, that a full-permission service account can read everything in the organization, is stated alongside it.
- Noted that an organization can forbid personal access tokens outright, which presents as a message on the console page rather than a missing menu item.

## 1.2.0

Credential handling, and a setup check that tells you whether to trust a score.

**Added**

- `scripts/verify_setup.py`. Checks the credential, reachability, who it authenticates as, whether entries come back, **whether it sees every submitter or only its owner**, and whether `created_at` and `attributable_to` are populated. Exits non-zero when something would make a score misleading, and prints where time is currently attributed so the attribution allowlist can be filled from real data.
- `target_confirmed` on a roster entry. Set it false for anyone whose contracted hours are not confirmed, typically part time, and every run warns that their coverage sub-metric is provisional rather than presenting a guess as a number.

**Changed**

- Authentication now works two ways with no configuration. `ASANA_ACCESS_TOKEN` in the environment means the script sends the header; without it the script sends no Authorization header and lets Anthropic's agent proxy attach an API credential stored on the cloud environment. The second path keeps the token outside the sandbox entirely, where nothing in a session can print, log or commit it, and it opens network egress to `app.asana.com` at the same time.
- Setup reference rewritten around those two paths, with the exact UI steps for each and the note that adding an API credential needs an organization Owner role.

**Fixed**

- A network or proxy failure used to surface as a raw `requests` traceback. It now retries, then explains the likely cause: a proxy 403 means the environment is not permitted to reach `app.asana.com`, and an API credential for that host fixes both the key and the egress.
- 401 and 403 now get separate hints. 403 points at the missing `time_tracking_entries:read` scope or a token whose owner cannot see other people's time, which is the failure that produces plausible but wrong team scores.

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
