---
name: friday-review
description: "Friday timesheet review: score the week, write the per-person read, post the digest, and open the approval task. The judgement layer on top of the numbers."
license: MIT
metadata:
  author: growthtoday
  version: "1.0.0"
  category: internal-ops
---

# Friday review

## Why this matters

The numbers alone do not tell you anything worth acting on. "38 of 40 hours" reads like success. "38 hours, 32 of them typed in on Friday after 23:00, all against one catch-all task" is a completely different situation, and only the second version tells you what to do about it. Reading that difference is the whole reason this step exists rather than a table posted by a scheduler.

## Prerequisites

- Same environment and roster as the daily nudge.
- The week you are reviewing has finished, or is finishing today. Running this on a Wednesday scores a partial week and the coverage number will look alarming for no reason.

## Plan

1. Score the week.
2. Read each person's row for the pattern behind the score.
3. Post the digest, DM the reviewer, open the approval task.

## Before state

Score Monday to Friday of the week just gone:

```bash
cd <skill>/scripts
python fetch_entries.py --start <monday> --end <friday> --out /tmp/week.json
python score.py --start <monday> --end <friday> --entries /tmp/week.json
```

Read stderr first. Three warnings change what you are allowed to claim:

- Approval endpoint not configured, so `on_time_submission` is `null` and the other three weights were renormalized. Say the score is partial. Do not present it as final.
- No `created_at` on any entry, so hygiene degraded to "any entry counts". The anti-backfill signal is gone. Say so.
- No `attributable_to` on any entry, so attribution could not be scored at all. That is a data problem to fix before the gate means anything.

## Execute

Read every person's row and name the pattern, not the number. The row gives you what you need:

| What you see | What it means | What to say |
|---|---|---|
| High coverage, low hygiene, high `backfilled_share_of_hours` | Hours reconstructed from memory, not tracked | The total is fine, the accuracy underneath it is not. Ask them to log at the end of each day, not the end of the week. |
| High hygiene, low coverage | Logging daily but under target | Usually a real capacity or expectation question, not a discipline one. Ask before assuming. |
| High coverage and hygiene, low attribution | Hours land on catch-all tasks | Fix the task structure, not the person. Nobody can attribute time to a project that has no task for the work. |
| `no_entries_at_all` true | Nothing logged all week | Check they were actually working. Leave and sickness look identical in this data. |
| Everything high | Working as intended | Say it out loud. A review that only names problems trains people to dread it. |

Then deliver three things:

1. **A digest** in the management channel: team mean, the count below the individual floor, and one line per person that pairs the score with the pattern. Rank nobody publicly. A sorted leaderboard of colleagues is a different tool with different consequences.
2. **A DM to the reviewer** with the same content plus the deep link to the Asana Timesheets overview, so approving is one click from the message.
3. **An Asana task** "Approve timesheets, week of <date>" assigned to the reviewer, with the digest in the description. This is what makes the approval itself trackable.

Do not set anyone's timesheet to submitted or approved. That decision carries payroll weight and stays with a person.

### Then check for a pattern, once a week

The daily nudge only ever talks to the person. This is the one place a repeated problem goes further, and it goes as a draft, never as a sent message.

```bash
python score.py --weeks 3
```

Read the `persistence` block. Someone is flagged when either condition holds:

- their weekly score fell below the individual floor in at least 2 of the last 3 weeks, or
- they ran 4 or more straight weekdays behind inside any one of those weeks.

Both matter because they catch different people. The first catches someone quietly under-logging. The second catches someone whose totals look fine because they reconstruct the whole week on Friday: the streak is computed from what had actually been entered on each day, so a backfiller shows up as behind all week even though the finished timesheet looks complete.

If `flagged` is empty, say so and stop. Do not write a draft nobody needs.

If it is not empty, write **one draft message addressed to the people in `escalation_contacts`** and hand it over for a human to send. Not one draft per person, one draft covering the week.

The draft should:

- Name each flagged person, the specific condition they met, and the numbers behind it.
- Say what the nudges have already done: how many they got, at what level, over how many weeks. That is the difference between "they are ignoring the process" and "nobody has actually asked them yet".
- Separate the two failure shapes explicitly. Under-logging and backfilling need different conversations, and lumping them together produces a useless one.
- Propose one action per person, and keep it proportionate. The first time someone appears, the action is usually a conversation, not a consequence.
- Stay short. This is a prompt for a manager to act, not a case file.

Deliver it as a draft in the chat or terminal. Do not Slack it to anyone, and do not send it to the flagged person. The whole point of the weekly cadence is that a human reads it first.

## After state

- Digest posted, reviewer DMed, approval task created, all three confirmed.
- Every claim in the digest traceable to a field in the script output.
- Any degraded metric stated in the digest itself, not just noted in the terminal.

## Key technical learnings

- `days_logged_on_time` is the honest headline, more than the score. Ten workdays and four qualifying days is a sentence anyone understands without knowing the weights.
- Weight renormalization is silent unless you look. When `weights_renormalized` is true the composite was computed over three metrics, so it is not comparable to a four-metric score from a later period. Never chart the two together without saying which is which.
- Coverage punishes over-logging as hard as under-logging, by design. Someone at 95 hours against 80 expected is not a hero, they are either miscounting or working in a way we should know about.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
