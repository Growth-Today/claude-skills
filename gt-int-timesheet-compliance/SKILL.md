---
name: gt-int-timesheet-compliance
description: "Internal Growth Today workflow for running the Asana timesheet compliance loop: the weekday nudge to people whose hours are missing, the Friday review, and the biweekly accuracy gate that decides when timesheets are trustworthy enough for payroll and client billing. Use when the user says run the timesheet nudge, who has not logged their hours, chase timesheets, timesheet review, Friday timesheet check, score the timesheets, timesheet accuracy, run the gate, pay period report, is the gate passing, timesheet backfilling, attribution score, daily hygiene score, or asks to set up or change the timesheet automation. Also use when a scheduled Routine fires with a nudge, review, or gate prompt. All arithmetic runs in the bundled Python scripts, never in the model. Do NOT use for GTM engineer performance scoring from meeting summaries (use gt-gtm-scoring-system) or for Asana project setup unrelated to time tracking."
license: MIT
metadata:
  author: growthtoday
  version: "1.6.0"
  category: internal-ops
---

# Timesheet compliance loop

Three jobs run off one data source. Asana time entries are the only truth: who logged what, against which project, and when they actually typed it in.

## Critical concept: the model never does the arithmetic

Every hour count, percentage and score comes from `scripts/`. Claude reads the JSON those scripts print and writes the judgement and the messages. If you ever find yourself adding up minutes in your head, stop and run the script. A hallucinated hour total in a payroll conversation is the one failure this skill exists to prevent.

Second rule: **only contact people who are actually behind.** Nudging someone who logged their hours is how the whole thing gets muted inside two weeks.

## Route by what was asked

| Request | Playbook |
|---|---|
| Weekday nudge, "who has not logged", chase people | `playbooks/daily-nudge.md` |
| Friday review, score the week, approval handoff | `playbooks/friday-review.md` |
| Pay period report, "is the gate passing", biweekly read | `playbooks/biweekly-gate.md` |
| "Who keeps missing this", draft for the leads | `playbooks/friday-review.md`, the persistence section |
| First-time setup, token, Routines, roster | `references/setup.md` |
| "how do I run this on my laptop", no Owner role | `references/run-locally.md` |
| Run it unattended without an Owner role, GitHub Actions | `references/github-actions.md` |
| How a score is built, weights, worked examples | `references/scoring-model.md` |
| Move the heartbeat to Make instead | `references/make-scenarios.md` |

## Before any run

1. Confirm `ASANA_WORKSPACE_GID` is set. Authentication works two ways: `ASANA_ACCESS_TOKEN` in the environment, or an API credential on the cloud environment that the agent proxy attaches outside the sandbox. Either is fine and the scripts detect which. If a run returns 401 or a proxy 403, stop and send the user to `references/setup.md`. Never guess a workspace.
2. Confirm `config/roster.json` exists. The repo ships `config/roster.example.json` only, because a real roster holds names, emails and Slack IDs.
3. Install once: `pip install -r requirements.txt`.

## The scripts

```bash
# always first on a new environment: is the setup trustworthy
python scripts/verify_setup.py

# raw entries for a date range, paginated
python scripts/fetch_entries.py --start 2026-08-24 --end 2026-09-04 --out /tmp/entries.json

# who to nudge right now, timezone aware, with escalation level
python scripts/who_is_behind.py --entries /tmp/entries.json

# full scorecard for a period
python scripts/score.py --entries /tmp/entries.json --start 2026-08-24 --end 2026-09-04

# trailing weeks plus the persistence check that feeds the weekly draft
python scripts/score.py --weeks 3

# Monday to Friday of the current week, no shell date arithmetic
python scripts/score.py --this-week

# unattended senders, both dry run unless you pass --send
python scripts/send_nudges.py --targets targets.json
python scripts/weekly_report.py --scores week.json
```

Every script prints JSON to stdout and human-readable warnings to stderr. Read both. A warning that the approval endpoint returned nothing changes how you report the on-time score, so never drop stderr.

## State: there isn't any

Nothing persists between runs and nothing needs to. Escalation level is derived from how many weekdays in a row a person has been behind, which the entries already tell you. Past pay periods recompute from Asana on demand. So a fresh container, a re-run, or a missed day costs you nothing, and there is no log file to keep in sync or leak.

## What this skill will not do

- It will not mark a timesheet submitted or approved on someone's behalf. Approval is a human decision that carries payroll weight.
- It will not write per-person hours or scores into this repo. Reporting goes to Slack, Notion, or the terminal.
- It will not copy a manager on a daily nudge. Every level of the ladder reaches the person alone. Repeated patterns become a weekly draft that a human sends.
- It will not send a fifth nudge to the same person in one week, or email anyone unless `nudge.email_enabled` is on. Slack, short, four a week maximum.
- It will not nudge outside the window in `config/roster.json`. Someone in Manila does not get a Slack DM at 22:30 because the scheduler runs on Central European Time.

---

Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
