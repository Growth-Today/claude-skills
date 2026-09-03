---
name: setup
description: "One-time setup for the timesheet compliance loop: Asana add-on and roles, the access token, environment variables, the roster, the scheduled Routines, and what does not need connecting."
license: MIT
metadata:
  author: growthtoday
  version: "1.0.0"
  category: internal-ops
---

# Setup

Work through this in order. Steps 1 to 4 are required before any script runs, and step 3b tells you whether they worked. Steps 5 to 8 turn it into an automation.

## What does not need connecting

Worth clearing up first, because it saves a week of waiting on access requests.

- **The Asana MCP does not help here.** Neither connected Asana server exposes a time tracking tool, so no amount of MCP connecting gets you time entries. That is what the token and the scripts are for. The Asana MCP is still useful for the task and approval side, and for looking up user GIDs.
- **A Google Calendar connector is not needed.** The submission invite is one recurring event. Create it by hand once (step 8). Waiting on a connector to automate a single click is not worth it.
- **A Make connection is not needed** unless you decide to move the heartbeat there later. See `references/make-scenarios.md`.

## 1. Asana add-on and roles

The Timesheets and Budgets add-on has to be active on the workspace, and it is priced per seat, so decide who is a time submitter before buying rather than after.

- Every person who logs hours: **time submitter**.
- Whoever reviews and approves: **time reviewer**.
- Choose the full flow (draft, submit, approve or reject), not the simple one. Without the approve step there is nothing for the Friday review to hand off to.

Confirm people can actually log time against the tasks they work on. If the work has no task, the hours land on a catch-all and attribution can never score. Fixing that is task hygiene, and it comes before the automation, not after.

## 2. Create the Asana token

Go to **app.asana.com/0/my-apps**, or in Asana: your profile photo, Settings, the Apps tab, then **Manage developer apps**. Under **Personal access tokens**, create a new token, name it something like `timesheet-compliance`, and copy it. Asana shows the value once.

Two things about that token that decide whether any of this works:

- **Use a personal access token, not an app connection.** The time tracking endpoints need `time_tracking_entries:read`. A token carries its creator's full user scope; an OAuth app connection may never have been granted it. A 403 on `/time_tracking_entries` is nearly always this.
- **It inherits its creator's permissions.** A token made by someone who can only see their own time returns only their own entries, and every team score built on it is quietly wrong rather than obviously broken. Create it from an account that is a **time reviewer or workspace admin**. `verify_setup.py` checks this by counting how many distinct submitters appear in the data, so you will not have to guess.

## 3. Give the token to the environment

Two ways, and they are not equivalent. Pick the second for anything scheduled.

### Option A, local only: a `.env` file

For running the scripts by hand on your own machine. Copy `.env.example` to `.env` and fill in:

```
ASANA_ACCESS_TOKEN=<the token>
ASANA_WORKSPACE_GID=<the workspace whose entries you are scoring>
```

`.env` is gitignored. The token goes in that file and nowhere else: not a commit, not a chat message, not a task description.

### Option B, for scheduled runs: an API credential on the cloud environment

This is the better option and it is not just a security preference. Anthropic's agent proxy attaches the key to requests for the hosts you name **after they leave the sandbox**, so the token never enters the container, never appears in an environment variable, and never lands in a file. Nothing running in the session can print it, log it, or commit it. It also opens network egress to that host, so it solves reachability at the same time: without it, a session whose network policy does not allow `app.asana.com` fails with a proxy 403 before it ever talks to Asana.

At [claude.ai/code](https://claude.ai/code), open the environment for editing. In **Update cloud environment**, find **API credentials** below **Environment variables**, then **Add credential**:

- **Credential type**: Bearer (the default)
- **Name**: `Asana timesheets`
- **Allowed websites**: `app.asana.com`
- **Custom headers**: one row, header name `Authorization`, prefix `Bearer`, value = the token

Select **Connect**. It saves immediately, separately from the dialog's Save changes button, and the value cannot be viewed again. There is no edit: to change it, delete and re-add.

Two catches worth knowing before you start:

- **It needs an organization admin role.** On Team and Enterprise that means an Owner, not an Admin. If you do not have it you will see a note instead of the credential list, even on your own environments. Ask an Owner to add it, which for us means Brigi in #help-me.
- **`ASANA_WORKSPACE_GID` still goes in Environment variables**, in the same dialog, `.env` format one pair per line. It is an identifier, not a secret, so it does not need the credential mechanism. Note that variables are copied into a session once at startup, so a running session keeps the values it began with and only later sessions pick up a change.

The scripts support both paths with no configuration. If `ASANA_ACCESS_TOKEN` is set they send the header themselves; if it is not, they send no Authorization header and let the proxy attach it. A 401 means neither happened, and the error says so.

## 3b. Verify before trusting anything

```bash
cd scripts && python verify_setup.py
```

It checks, in order: is there a usable credential, is `app.asana.com` reachable, who the credential authenticates as, whether time entries come back, **whether it sees all submitters or only its owner**, and whether `created_at` and `attributable_to` are actually populated. It exits non-zero when something would make a score misleading, and it prints where the logged time is currently attributed, most hours first, which is exactly the list you need for the attribution allowlist in step 6.

Run it once now, and again any time a score looks wrong.

## 4. Build the roster

Copy `config/roster.example.json` to `config/roster.json` and fill in one entry per active submitter. The real file is gitignored, because it holds names, work emails and Slack member IDs.

- **Asana user GID**: ask Claude to list workspace users through the Asana MCP, or read it out of the person's Asana profile URL.
- **Slack member ID**: their Slack profile, three-dot menu, Copy member ID. Starts with `U`.
- **escalation_contacts**: the people the weekly persistent-pattern draft is addressed to. They live in `roster.json` rather than `scoring.json` so no real person's details sit in a committed config file. Nothing in this skill ever messages them automatically.
- **Timezone**: an IANA name like `Europe/Budapest`, `Asia/Manila`, `Africa/Johannesburg`. This is what stops a Manila nudge firing at 22:30, so get it right.
- **daily_target_hours**: contracted hours per workday. Without it there is no coverage score at all.
- **target_confirmed**: set it to `false` for anyone whose contracted hours you have not confirmed, typically a part-time person. The scripts then warn on every run that that person's coverage sub-metric is provisional, instead of presenting a guess as a number.

Sanity check it before going further:

```bash
cd scripts
python who_is_behind.py --force
```

Every active person should appear in exactly one of the three output lists. If someone is missing, their entry failed validation and the script will have said which field.

## 5. Verify the approval endpoint

Asana's timesheet approval status API is recent, so confirm the exact collection path against this workspace before depending on it, then write it into `config/scoring.json` under `approval_endpoint.path`.

Until that path is filled in, `on_time_submission` is reported as unavailable, the other three weights are renormalized, and every score is flagged partial. That is the intended behaviour: a guessed endpoint path producing a confident number is worse than an honest gap. Do not put a path in there that you have not seen return data.

## 6. Run one baseline period before setting the attribution allowlist

Attribution carries 30% of the score, so it can sink the gate on its own. Before you switch it on properly:

1. Leave `attributable_project_gids` empty and score one full pay period.
2. Look at what `attributable_to` actually contains across the entries.
3. Fill the allowlist with the projects that are genuinely billable client work, and `excluded_project_gids` with the catch-alls.

While the allowlist is empty every score carries `attribution_loose_no_allowlist: true`, which means the metric counted any non-null attribution and cannot tell client work from a catch-all task. Useful as a baseline, not as a gate input.

## 7. The three Routines

Create these as scheduled Routines. Cron is evaluated in UTC, so convert from local time and remember it shifts with daylight saving.

**Nudge.** Do not run this hourly. The script only acts on people for whom local time is inside the nudge window (16:00 to 17:00 by default), so fire only on the UTC times that land inside that window for a timezone you actually have. Work it out from the roster:

| Timezone | Offset | 16:05 local is |
|---|---|---|
| Asia/Manila | UTC+8 | 08:05 UTC |
| Asia/Kolkata | UTC+5:30 | 10:35 UTC |
| Africa/Johannesburg | UTC+2 | 14:05 UTC |
| Europe/Budapest, summer | UTC+2 | 14:05 UTC |
| Europe/Budapest, winter | UTC+1 | 15:05 UTC |

Work the table from whatever timezones your own `roster.json` actually contains. For the four above, two Routines cover everything, because a half-hour offset needs a different cron minute:

```
5  8,14,15 * * 1-5     Manila, Johannesburg, and Budapest in both seasons
35 10      * * 1-5     India
```

That is four fires a weekday, and it is safe year-round: the 15:05 UTC fire is 17:05 in Budapest during summer, which falls outside the window and does nothing. Twenty runs a week instead of a hundred and twenty, for identical coverage.

Fire at five past the hour, not on the hour. The window opens at 16:00 local and a fire timed a minute early does nothing at all.

```
Prompt: Run the timesheet daily nudge. Follow playbooks/daily-nudge.md.
Send nothing if nobody is behind.
```

**Friday review.** The week closes Friday at 17:00 in each person's own timezone, so Manila closes nine hours before Budapest. The review has to run after the **last** cutoff, not the first: Budapest 17:00 is 15:00 UTC in summer and 16:00 UTC in winter, so `15 16 * * 5` clears everyone year-round.

```
Prompt: Run the Friday timesheet review for the week just finished.
Follow playbooks/friday-review.md.
```

**Biweekly gate.** Every second Monday, after the pay period closes.

```
Prompt: Run the biweekly timesheet gate for the two pay periods ending
<anchor Monday>. Follow playbooks/biweekly-gate.md.
```

The skill has to be reachable from those fresh sessions, so it needs to be in a repo the session clones or deployed to the organisation. A skill sitting only in someone's local folder will not load in a Routine.

## 8. Create the calendar invite by hand

One recurring Google Calendar event, created once, never automated:

- Friday, 15 minutes, before the cutoff.
- Guests: every submitter.
- Repeats weekly.
- One reminder, 10 minutes before.
- Title: "Submit your timesheet". Description: the deep link to the Timesheets page, and the two lines of how-to.

## One thing to know about the Slack DMs

The Slack connection here runs on a user token, so nudges arrive as direct messages **from you**, not from a bot. For a founder nudge that probably lands harder than a bot would. It also means the messages keep coming from your account while you are on holiday, and people will reply to you expecting a human. Decide that deliberately rather than discovering it.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
