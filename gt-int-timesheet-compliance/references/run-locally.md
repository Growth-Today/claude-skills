---
name: run-locally
description: "Step by step for running the timesheet scripts on your own machine, for anyone without the organization Owner role needed to store a credential on the cloud environment."
license: MIT
metadata:
  author: growthtoday
  version: "1.0.0"
  category: internal-ops
---

# Running it on your own machine

Use this when you cannot store an API credential on the cloud environment, which needs an organization Owner role. Everything works locally with a personal access token in a `.env` file. Your laptop has no egress restriction, so the calls that a cloud session cannot make will go through fine from here.

## What this gets you, and what it does not

Local runs give you the **numbers**: who is behind, the weekly scores, the pay period gate, where time is attributed. That is the whole measurement half of the system and it is the half you need first.

It does not give you the **automation**. The daily Slack DMs and the Friday digest are written by Claude reading the script output, so a local cron job on its own would compute numbers and message nobody. Scheduling the full loop needs the credential on the cloud environment, which needs an Owner. Until then the pattern is: you run a script, paste the output into a session, Claude does the judgement and drafts the messages.

That is a perfectly good place to sit for the shadow-mode period. You are measuring, which is what the gate needs, and nobody is being nagged by a robot yet.

## Prerequisites

Python 3.9 or newer, because the timezone handling needs `zoneinfo`. Check first:

```bash
python3 --version
```

If that shows 3.8 or older, install a newer Python before going on. On macOS the system Python is often behind; `brew install python@3.12` is the usual fix.

## 1. Get the code

```bash
git clone https://github.com/Growth-Today/claude-skills.git
cd claude-skills
git checkout claude/session-dcwzo3
cd gt-int-timesheet-compliance
```

If you already have the repo cloned, `git fetch origin && git checkout claude/session-dcwzo3` instead.

## 2. Install the two dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The virtual environment keeps these two packages out of your system Python. Skip it if you would rather not, and just run the `pip install` line, but then remember `python3` rather than `python` below.

Every later session in a new terminal needs `source .venv/bin/activate` again before running anything.

## 3. Add the roster

`config/roster.json` is deliberately not in the repo, because it holds names, work emails and Slack member IDs. Save the file you were sent to exactly that path:

```bash
ls config/roster.json    # should print the path, not an error
```

## 4. Add the token

Do not paste the token into a terminal command. Anything you type at a shell prompt lands in your shell history file, and that is a second copy of a live credential sitting in plain text on disk.

Copy the template, then open it in an editor and paste the value there:

```bash
cp .env.example .env
open -e .env          # macOS. Or: nano .env
```

Fill in both lines:

```
ASANA_ACCESS_TOKEN=<paste the new token here>
ASANA_WORKSPACE_GID=1206071818707158
```

Save and close. `.env` is gitignored, so it cannot be committed by accident.

If you would rather stay on the command line, this reads the token without echoing it and without writing it to history:

```bash
printf 'ASANA_WORKSPACE_GID=1206071818707158\n' > .env
read -rsp 'Paste token, then press enter: ' T && printf 'ASANA_ACCESS_TOKEN=%s\n' "$T" >> .env && unset T
```

## 5. Check it works

```bash
cd scripts
python verify_setup.py
```

A healthy run prints a PASS line for each check and finishes with "Setup looks good". Read the FAIL lines rather than the summary, and read stderr too.

What the failures mean:

| What you see | What to do |
|---|---|
| `401` | The token is wrong, expired, or was revoked. Reissue and re-paste. |
| `403` on a time tracking endpoint | The credential cannot read time entries. Usually its owner is not a time reviewer. |
| `team-wide visibility  FAIL` | It sees only your own time, so any team score would be quietly wrong. This is the one failure that produces plausible but false numbers, so do not skip past it. |
| `created_at populated  FAIL` | Backfill detection is off and daily hygiene, 30% of the score, degrades badly. |
| `attributable_to populated  FAIL` | Attribution, another 30%, cannot be scored at all. That is a task structure problem. |
| `no entries came back` | Either nobody logged time in the window, or the credential cannot see time entries. Check one person's timesheet by hand to tell which. |

The script also prints where the logged time is currently attributed, most hours first. That list is what fills `attribution.attributable_project_gids` in `config/scoring.json`.

## 6. Run the real thing

```bash
# who is behind right now, ignoring the local time window so you see everyone
python who_is_behind.py --force

# last full week, Monday to Friday dates
python score.py --start <monday> --end <friday>

# three trailing weeks plus the persistence check
python score.py --weeks 3

# the pay period gate, anchored on a Monday
python score.py --gate-anchor <monday> --periods 2
```

Every one of these prints JSON on stdout and warnings on stderr. To capture both:

```bash
python score.py --weeks 3 > /tmp/scores.json 2> /tmp/warnings.txt
```

## 7. Hand the output over for the judgement half

Paste the JSON into a session and ask for the Friday review, or the nudge drafts, or the gate read. The numbers are already computed, so Claude is only doing what it is good at: reading the pattern behind the numbers and writing the messages.

Safe to paste. The output holds names, hours and project names, which is internal but not secret. It never contains the token.

## Keeping the token healthy

- Rotate it if it is ever pasted into a chat, a ticket, a shared doc, or anywhere with more readers than your own machine.
- Revoke it at `app.asana.com/0/developer-console` the moment it is not needed.
- It carries your full Asana permissions, so treat it like your password rather than like a config value.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
