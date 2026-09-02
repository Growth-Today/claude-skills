---
name: daily-nudge
description: "Weekday nudge to the people whose hours are actually missing, sized to how long they have been behind. Slack DM plus email, in their own timezone."
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

## Plan

1. Ask the script who is behind.
2. Send one Slack DM and one email per target, tone set by the escalation level.
3. Report what you sent, and who you deliberately left alone.

## Before state

```bash
cd <skill>/scripts
python who_is_behind.py
```

Read the output before writing anything:

- `nudge_now` is your entire contact list. Nobody else gets a message.
- `on_track_do_not_contact` is the group you must not touch. It exists in the output so you can confirm the skip was deliberate.
- `outside_window` is people for whom it is not late afternoon locally yet. They get their nudge on a later run, not this one.

If `nudge_now` is empty, stop here. Say "nobody is behind, no messages sent" and finish. That is a successful run.

Check stderr too. If it warns that no entry carried `attributable_to` or `created_at`, the nudge still works (it only needs hours and dates), but flag it so nobody trusts the Friday score built on the same data.

## Execute

For each person in `nudge_now`, send a Slack DM to their `slack_member_id`, then the same substance by email. Use their real numbers from the JSON, never a rounded guess.

Tone by `escalation` value:

**`light`** (first or second day behind). One or two sentences, no guilt, easy to act on.

> Hey Ana, your timesheet is at 12 of 24 hours for this week so far. Two minutes now and it is done: <timesheet link>

**`firm`** (third or fourth day). Name the gap and the days, and say what it blocks.

> Ana, this is day 3 behind: 12 of 32 hours logged, and nothing at all for Mon, Tue or Wed. I need these before Friday cutoff or your client hours cannot be billed for the period. <timesheet link>

**`cc_lead`** (fifth day or more). Same as firm, plus copy `cc_slack_id` on a separate message. Do not add the lead to the person's DM. Telling someone off in front of their manager is a different act from asking their manager for help.

Rules for the copy:

- One ask per message. The ask is always "log your hours", never a list of process improvements.
- Include the deficit in hours and the missing dates. Specifics get action; "please update your timesheet" does not.
- Deep-link to the timesheet, not to the Asana home page.
- Never write the score, the ranking, or how anyone else is doing. This is a nudge, not a review.
- Never say a hard consequence you have not been told to say. "Your hours cannot be billed" is true. "This affects your pay" is not yours to claim.

## After state

Report in one short block:

- Who you messaged, at what escalation level, and the deficit for each.
- Who you skipped because they were on track, by name.
- Who fell outside the local time window and will be picked up on a later run.
- Any stderr warning, repeated in plain words.

## Key technical learnings

- Escalation is derived, not stored. `weekdays_behind_in_a_row` is recomputed from the entries on every run, so a missed run or a fresh container never resets someone's ladder or double-counts it.
- `deficit_hours` can read 0.0 while the person is still a target. That means the hours exist but were typed in days late, so they failed the same-day check. Nudge on the missing dates, not on a deficit that isn't there.
- The window check is what keeps this humane. Run the script hourly and each person is caught once, in their own afternoon. Never bypass it with `--force` on a real run.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
