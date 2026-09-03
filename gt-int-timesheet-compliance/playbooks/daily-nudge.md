---
name: daily-nudge
description: "Weekday Slack DM to the people whose hours are actually missing, short, sized to how long they have been behind, in their own timezone, capped per week."
license: MIT
metadata:
  author: growthtoday
  version: "1.0.0"
  category: internal-ops
---

# Daily nudge

## Why this matters

A nudge that reaches everyone is a nudge nobody reads. The single fastest way to kill this whole system is to DM someone who logged their hours on time. So the script decides who is behind, and you contact only those people. If the target list comes back empty, the correct action is to send nothing at all and say so.

## Prerequisites

- `ASANA_ACCESS_TOKEN` and `ASANA_WORKSPACE_GID` are set. In a Routine these are environment variables on the remote environment, not a local `.env`.
- `config/roster.json` exists with a timezone and a daily target for every active person.
- Slack is connected. DMs go out with the person's `slack_member_id` as the channel.
- Email is off by default (`nudge.email_enabled` in `config/scoring.json`). The team lives in Slack, so a second channel is noise. Each target's `channels` field tells you what to use.

## Plan

1. Ask the script who is behind.
2. Send one short Slack DM per target, tone set by the escalation level.
3. Report what you sent, who you left alone, and who hit the weekly cap.

## Before state

```bash
cd <skill>/scripts
python who_is_behind.py
```

Read the output before writing anything:

- `nudge_now` is your entire contact list. Nobody else gets a message.
- `on_track_do_not_contact` is the group you must not touch. It exists in the output so you can confirm the skip was deliberate.
- `suppressed_by_weekly_cap` is people who are behind but have already had their four nudges this week. Do not message them. Say their name in the report so the silence is visible, and expect them in Friday's persistence draft.
- `outside_window` is people for whom it is not late afternoon locally yet. They get their nudge on a later run, not this one.

If `nudge_now` is empty, stop here. Say "nobody is behind, no messages sent" and finish. That is a successful run.

Check stderr too. If it warns that no entry carried `attributable_to` or `created_at`, the nudge still works (it only needs hours and dates), but flag it so nobody trusts the Friday score built on the same data.

## Execute

For each person in `nudge_now`, send one Slack DM to their `slack_member_id`. Send email only if their `channels` list includes it. Use the real numbers from the JSON, never a rounded guess.

**Keep it to one or two sentences.** This is a nudge, not a briefing. Anything longer gets skimmed, and a skimmed nudge is a wasted one.

Tone by `escalation` value:

**`light`** (first or second day behind):

> Hey Ana, timesheet is at 12 of 24 hours this week. Two minutes and it is done: <timesheet link>

**`firm`** (third day onward):

> Ana, day 3 behind: 12 of 32 hours, nothing logged Mon to Wed. These need to be in before Friday cutoff or the client hours cannot be billed. <timesheet link>

The tone stops escalating there. **The daily nudge never copies a manager, at any level**, and it stops entirely after four in one week. A pattern that survives that is handled once a week by the draft in `friday-review.md`, which a human reads and sends.

Rules for the copy:

- One ask. Always "log your hours", never a list of process improvements.
- Include the deficit and the missing dates. Specifics get action; "please update your timesheet" does not.
- Deep-link to the timesheet, not the Asana home page.
- Never write the score, a ranking, or how anyone else is doing.
- Never claim a consequence you were not told to claim. "Client hours cannot be billed" is true. "This affects your pay" is not yours to say.
- Never mention that a manager will be told, or that a pattern is being tracked. If it comes to that, a person says it, not a scheduled script.

## After state

Report in one short block:

- Who you messaged, at what escalation level, and the deficit for each.
- Who you skipped because they were on track, by name.
- Who hit the weekly cap, by name, with the count.
- Who fell outside the local time window and will be picked up on a later run.
- Any stderr warning, repeated in plain words.

## Key technical learnings

- Escalation is derived, not stored. `weekdays_behind_in_a_row` is recomputed from the entries on every run, so a missed run or a fresh container never resets someone's ladder or double-counts it.
- `deficit_hours` can read 0.0 while the person is still a target. That means the hours exist but were typed in days late, so they failed the same-day check. Nudge on the missing dates, not on a deficit that isn't there.
- The window check is what keeps this humane. The Routine fires on the handful of UTC times that fall inside 16:00 to 17:00 for a timezone on the roster, and each person is handled once, in their own afternoon. Never bypass it with `--force` on a real run.
- A fire that produces an empty `nudge_now` is not a wasted run. Most of them will be, once the habit sticks.
- The weekly count is recomputed from the entries, not stored, so it survives a missed run and a recycled container. It counts the weekdays this week on which the person would have been a target, reconstructed from what had actually been entered by each of those days.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
