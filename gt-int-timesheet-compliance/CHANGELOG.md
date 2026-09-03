# Changelog

All notable changes to the timesheet compliance skill.

## 1.6.0

A start date, so the process is measured from the day it is announced rather than from whatever is already in Asana.

**Added**

- `program_start_date` in `config/scoring.json`. Nothing before it is scored or nudged. Applied inside `workdays()`, which every window, streak and nudge is built from, so one setting covers the whole system rather than whichever caller remembered it. Set to the first live day.
- `holidays` is now used for the launch week's non-working days, so a team that is out on the Monday is scored out of four days rather than marked twenty percent behind.
- `not_counted_yet` in the nudge output, and a line in the dry run naming how many people are in it, so a quiet run before go-live reads as working rather than broken.
- `verify_setup.py` prints the start date and how many days remain until it.

**Changed**

- `workdays()` takes the scoring config rather than a bare holiday list. One argument, both rules, no call site that can silently skip one.
- The firm closing lines dropped the billing framing. "We can't bill the client for them" asks the reader to accept a claim they cannot check, which invites an argument about the claim instead of getting the hours logged. They now give a reason the person can act on: the week closes on Friday, and filling a week in later is guesswork.

**Fixed**

- **A window with no countable days nudged everyone.** Expected hours came to zero, zero is not above the behind threshold, so every person fell through to being nudged. Guarded explicitly, and entries from outside the countable days are dropped before scoring so attribution cannot score work from before the process existed.

**Verified**

- The launch week resolves to Tuesday through Friday with the Monday held out, a week entirely before the start date resolves to no days at all and scores `None` rather than zero, and later weeks are unaffected at five days.
- Dry runs on the pre-launch Friday and the OOO Monday nudge nobody and report all six people as not counted yet. The first live Tuesday nudges against one day of expected hours, at the lightest escalation level.

## 1.5.1

Nudge copy rewritten in plain English after reading the first real dry run.

**Changed**

- **The copy no longer sounds written by a machine.** The problem sentence and the closing ask are now chosen together from what is actually wrong, so someone whose hours are complete but logged two days late is asked to change a habit rather than told to "spend two minutes catching up". Hours print as `17.5` and `13` rather than `17.50` and `13.0`, missing days print as `Mon, Tue and Thu` rather than a list of ISO dates, and singular and plural agree per person.
- Streaks read as language rather than a counter. Past five weekdays the firm template says "you've been behind every day for over a week now" instead of "this is day 11", which is meaningless to someone who only sees this week.

**Fixed**

- **Capitalisation disagreed between the two templates.** The same clause opens a sentence in the firm template and follows a comma in the light one, which produced "Hi Gaze, Your hours add up". Clauses are now stored as fragments and `fit_case()` matches the first letter to its position, so both templates read correctly from one string.

**Verified**

- All six copy paths rendered against the four people flagged in the live dry run plus a part-time and a mixed case: firm with missing days, firm short on hours only, light backfill-only, light short on hours only, and a short streak under the five-day threshold. Every message reads as a sentence and every ask matches its problem.

## 1.5.0

An unattended path that needs no organization Owner: GitHub Actions running the same scripts.

**Added**

- `scripts/send_nudges.py`. Reads `who_is_behind.py` output and sends the Slack DMs, using templates from the new `config/messages.json`. **Dry run is the default**, because these messages go to real colleagues and sending should be opt-in. Slack errors get specific hints rather than a raw API response.
- `scripts/weekly_report.py`. Posts the weekly digest to a channel, also dry run by default, and surfaces the partial, loose-attribution and degraded-hygiene caveats in the message rather than burying them in a log.
- `config/messages.json`. Nudge and digest copy, editable without touching code. The firm template renders the script's own reason list, so it stays accurate whether the problem is missing hours, late-logged days or both.
- `github-actions/timesheet-nudge.yml` and `github-actions/timesheet-weekly.yml`. Ship as templates inside the skill rather than in `.github/workflows/`, so nothing starts firing from the public monorepo by accident. Both gate real sending behind a repository variable, so a scheduled dry-run week costs nothing to arrange.
- `references/github-actions.md`. The full setup, including the Slack scopes, the secrets, the dry-run week, and the failure modes worth knowing before they happen.
- `score.py --this-week` and `ROSTER_JSON` support in `_lib.py`, so a runner can score the current week without shell date arithmetic and can read the roster from a secret when it cannot be committed.

**Fixed**

- **Nudge copy could contradict itself.** For someone who logged hours late, the firm template rendered "24.0h of 24.0h logged, nothing for [dates]", which is nonsense to receive. The template now renders the script's reason list, and `logged` is computed as-of today so the total can no longer disagree with the missing-days list.
- **A person with no entries falsely reported that backfill detection was off.** `hygiene_degraded_no_created_at` fired whenever no entry carried `created_at`, which is trivially true when there are no entries at all, so a single non-logger made the whole digest claim the workspace was missing the field. It now requires entries to exist before claiming the field is absent.
- **Off-by-a-week in the weekly workflow.** `date -d "last monday"` resolved to the run date itself when the runner was already on a Friday, so the digest would have scored the wrong window. Replaced with the tested `--this-week` flag.

**Verified**

- Both senders dry-run end to end against synthetic entries, printing per-person level, weekly nudge count, channel list and exact message text, with on-track people counted and capped people named.
- `--this-week` resolves to Monday through Friday of the current week regardless of which weekday it runs on.
- Both workflow files parse as valid YAML with the expected triggers and steps.

## 1.4.0

Nudge volume capped, and Slack made the only default channel.

**Changed**

- **Slack only by default.** `nudge.email_enabled` is off, because the team lives in Slack and a second channel for the same message is noise. Each target carries a `channels` list, so turning email back on for one person who genuinely does not read Slack is a config change rather than a code change.
- **Nudge copy is now explicitly one or two sentences.** A nudge is not a briefing, and a skimmed nudge is a wasted one.

**Added**

- **A hard cap of four nudges per person per calendar week** (`nudge.max_per_week`). Tone already stopped escalating after day three; nothing stopped the volume, so someone behind all week was in line for five DMs and five emails. By the fifth day the daily nudge has demonstrably failed on that person that week, and a fifth identical message only trains them to filter it, which then costs you the weeks it would have worked. That case belongs to the weekly persistence draft instead, so the cap and the escalation to a human are complements rather than a softening.
- `suppressed_by_weekly_cap` in the nudge output, so a deliberate silence is visible in the run rather than looking like a missed person.
- `was_nudge_target_on` and `nudges_this_week` in `_lib.py`. The weekly count is recomputed from the entries, using the same as-of reconstruction as the persistence rule, so the cap needs no stored counter and survives a missed run or a recycled container.

**Verified**

- A person logging nothing all week is nudged Monday through Thursday and suppressed on Friday at count 5, with everyone on track left uncontacted throughout.
- The ladder still opens at `light` for a fresh case: light, light, firm across days one to three for someone clean the previous week.

## 1.3.0

**Added**

- `references/run-locally.md`. A step by step for running the scripts on your own machine with a personal access token in `.env`, for anyone without the organization Owner role that storing a cloud credential requires. Covers the Python 3.9 floor that the timezone handling needs, getting the token into `.env` without it landing in shell history, what each `verify_setup.py` failure actually means, and the honest split: local runs give you every number, and the Slack and email half still needs either the cloud credential or a person pasting output into a session.

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
