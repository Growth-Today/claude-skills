# Timesheet compliance loop

Internal Growth Today skill. It runs three jobs off Asana time entries: a weekday nudge to the people whose hours are genuinely missing, a Friday review, and a biweekly accuracy gate that decides when timesheets are trustworthy enough to drive payroll and client billing.

**This is an internal skill and should live in a private repo.** It is drafted here on a working branch for review. Before anything is merged, it needs to move to a private internal repo, because the workflow it encodes is about how we pay people. Nothing sensitive is committed (the roster is gitignored and only an example ships), but the destination is still internal by default.

## Why it exists

The reminders are the easy part. The hard part is knowing whether the hours mean anything. Someone can submit a timesheet on time, with the right total, that was invented from memory on Friday night and pointed at a catch-all task. That timesheet is worse than a late one, because it looks like data and it cannot be billed or defended to a client.

So the scoring puts most of its weight on the two things that make hours usable: were they logged as the work happened, and do we know whose budget they came out of.

## The one design rule

**The model never does the arithmetic.** Every hour, percentage and score comes from the Python in `scripts/`. Claude reads the computed JSON and writes the judgement and the messages. A hallucinated hour total in a payroll conversation is the exact failure this is built to avoid, and the split is what makes an LLM safe to put in this loop at all.

The second consequence of that split: there is nothing to keep in sync. Escalation level is derived from the entries themselves, and any past period recomputes on demand, so a missed run costs nothing and there is no log file to maintain or leak.

## What's here

```
SKILL.md                        router, read first
config/scoring.json             weights, thresholds, windows. Edit this, not the code
config/roster.example.json      copy to roster.json (gitignored) and fill in
scripts/verify_setup.py         run this first: is the setup trustworthy
scripts/fetch_entries.py        dump time entries for a date range
scripts/who_is_behind.py        who to nudge now, timezone aware, with escalation
scripts/score.py                score a window, or evaluate the gate
playbooks/daily-nudge.md        the weekday nudge
playbooks/friday-review.md      the Friday review and approval handoff
playbooks/biweekly-gate.md      the pay period gate
references/setup.md             one-time setup: token, env vars, roster, Routines
references/scoring-model.md     the four sub-metrics, weights, worked examples
references/make-scenarios.md    build spec if you move the heartbeat to Make
```

## Quick start

Full version in `references/setup.md`. The short one:

```bash
pip install -r requirements.txt
cp .env.example .env                       # add the Asana token and workspace GID
cp config/roster.example.json config/roster.json   # fill in your submitters
cd scripts && python verify_setup.py               # does any of this actually work
```

Three things people get wrong on the first try. A scheduled Routine starts a fresh container that never sees your local `.env`, so scheduled runs need an API credential on the cloud environment instead, which also opens egress to `app.asana.com`. A token created by someone who can only see their own time returns only their own entries, so every team score built on it is quietly wrong; `verify_setup.py` catches that. And the daily nudge should fire on the few UTC times that are late afternoon for your roster's timezones, not hourly, which is a sixfold difference in cost for identical coverage.

## Scheduled Routines or Make?

Both work. The default is Routines plus the bundled scripts, and the reason is not the one people expect.

| | Make | Scheduled Routines |
|---|---|---|
| Marginal cost | **Wins.** Around ten dollars a month | Tokens per fire |
| Build time | Half a day. Aggregating a timezone-aware roster is the fiddly part | **Wins.** The scripts are already written |
| Arithmetic accuracy | Deterministic | **Tie.** The math is in Python, not the model |
| Judgement | Cannot form one | **Wins.** Backfill patterns, coaching copy |
| Fails loudly | **Wins.** Run history, error handlers | A Routine that stops firing is quieter |

Determinism is the usual argument for a workflow platform, and it does not apply here because the calculations already live in Python. What Make genuinely wins is marginal cost and telling you when it breaks. If you want both, put the daily nudge in Make where there is no judgement to make, and keep the Friday review and the gate as Routines where the judgement is the entire point. Spec for that is in `references/make-scenarios.md`.

## What it will not do

- Mark a timesheet submitted or approved for someone. That decision carries payroll weight and stays with a person.
- Write per-person hours or scores into this repo. Reporting goes to Slack, Notion, or the terminal.
- Message someone who logged their hours. The script's on-track list exists so the skip is deliberate and visible.
- Copy a manager on a daily nudge. Every level of the daily ladder goes to the person alone. A repeated pattern produces a weekly draft for a human to review and send, and nothing more.
- Nudge outside a person's local afternoon. Nobody in Manila gets a DM at 22:30 because the scheduler runs on European time.

## Known gaps

- **The approval endpoint needs verifying.** Asana's timesheet approval status API is recent. Until someone confirms the path on our workspace and fills it into `config/scoring.json`, the on-time metric reports as unavailable and every score is flagged partial. Deliberate: a guessed path that returns a confident number is worse than an honest gap.
- **Attribution needs a baseline first.** It carries 30% of the score, so run one period with an empty allowlist, look at what people actually attribute to, then fill it in. A 30% weight on a metric nobody can satisfy makes the gate theatre.
- **Task hygiene comes before all of this.** If the work has no task to log against, hours land on catch-alls and attribution can never score, no matter how diligent anyone is.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
