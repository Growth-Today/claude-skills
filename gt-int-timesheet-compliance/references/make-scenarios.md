---
name: make-scenarios
description: "Build spec for running the timesheet heartbeat in Make instead of scheduled Claude Code Routines: three scenarios, module by module, with the exact API calls and the trade-off against the default setup."
license: MIT
metadata:
  author: growthtoday
  version: "1.0.0"
  category: internal-ops
---

# Running the heartbeat in Make

This is a build spec, not a live scenario. There is no Make connection in this skill's tool set, so nobody can create these scenarios from a Claude session. Someone clicks them together in Make's own interface using the configuration below.

## Should you?

The default setup in this skill runs the whole loop from scheduled Routines and the bundled scripts. Make is worth the extra platform in two situations:

1. **Marginal cost matters more than build time.** Three scenarios on a Core plan run around ten dollars a month for this volume. A Routine costs tokens per fire, and the daily nudge is the expensive part.
2. **You want it to fail loudly.** Make keeps run history and error handlers, so a scenario that stops working tells you. A Routine that quietly stops firing is easier to miss.

It is not worth it for accuracy. The reason people reach for a workflow platform is determinism, and this skill already gets that by putting every calculation in Python. The model reads computed JSON and writes messages. It never adds up minutes.

The honest split, if you want both: Make runs the daily nudge, where determinism and cost matter and there is no judgement to make. Routines keep the Friday review and the gate, where the judgement is the whole point and Make cannot form one.

## Shared setup

- **Connections**: Asana (or the generic HTTP module), Slack with a bot that can DM, Gmail, Google Calendar.
- **Credential**: the same Asana personal access token, stored in Make's keychain. If the Asana app's own API-call module returns 403 on a time tracking endpoint, its connection lacks the `time_tracking_entries:read` scope. Use the generic HTTP module with a bearer header instead.
- **Roster**: a Make data store or a Google Sheet with the same columns as `config/roster.json`. Keep one copy of the truth. Two rosters drifting apart is a bug you will not notice for a month.
- **Timezone**: Make schedules run in the organisation's timezone. Set it once and remember it when reading a schedule.
- **Error handler on every scenario**: a route that Slack DMs the owner on failure.

## Scenario A, the daily nudge

1. **Schedule.** Weekdays, on the specific hours that are late afternoon for the timezones in your roster. Not hourly. For a roster spanning Manila and Central European Time that is two fires a day, not twenty-four, and the saving is the whole cost argument for using Make at all.

2. **Fetch this week's entries.** HTTP GET, paginating on `next_page.offset` until it comes back empty.

```
GET https://app.asana.com/api/1.0/time_tracking_entries
    ?workspace={{workspace_gid}}
    &entered_on_start_date={{monday}}
    &entered_on_end_date={{today}}
    &opt_fields=duration_minutes,entered_on,created_at,created_by.gid,
                created_by.name,attributable_to.gid,attributable_to.name
    &limit=100

Authorization: Bearer {{keychain.asana_pat}}
```

3. **Get the roster** and iterate it.

4. **Aggregate per person.** Sum `duration_minutes` grouped by `created_by.gid`. Expected is workdays elapsed this week times `daily_target_hours`. This is the step that takes the longest to build in Make: an array aggregator feeding an iterator, with the grouping key set correctly. It is twenty lines of Python in `who_is_behind.py` and it is the main reason the Python path is faster to stand up.

5. **Two flags, not one.** Flag a person if week-to-date hours are under 80% of expected, **or** if any workday this week has no entry created within a day of itself. The second flag is what catches backfilling while there is still time to fix it, and it is the one people forget to build.

6. **Router.**
   - Behind: Slack "Create a message" with `channel` set to the person's member ID, then Gmail send. Escalate the copy on how many weekdays in a row they have been behind: light for one or two, firm for three or four, copy the squad lead beyond that.
   - On track: no modules at all. Contacting compliant people is what gets the whole system muted, so the branch that does nothing is doing real work.

## Scenario B, the weekly ritual

1. **The calendar invite, run once then disable.** Google Calendar create-event, Friday, 15 minutes, before cutoff, guests set to every submitter, recurrence `RRULE:FREQ=WEEKLY;BYDAY=FR`, one reminder ten minutes before. One run, one recurring event, nothing to maintain.

2. **Thursday morning.** Slack channel message: timesheets close tomorrow, reply in thread when yours is in. One thread a week keeps the confirmations in one place.

3. **Watch that thread.** Slack watch-messages, match a confirmation, mark the person's Asana proxy task complete. Treat it as a signal only. Friday scores the real entries, and a gap between what someone said and what they logged is its own conversation.

## Scenario C, Friday review

Only build this if you are not using the Routine for it. Make can produce the table. It cannot tell you that eighty logged hours were reconstructed on Friday night and that the client attribution underneath them is a guess, which is the sentence the review exists to produce.

1. Fire after cutoff on Friday.
2. Fetch Monday to Friday entries for all submitters.
3. Read each person's weekly approval status, if the endpoint is configured. If it is not, do not substitute the Slack confirmation for it.
4. Compute the four sub-metrics with the weights from `config/scoring.json`. Keep one copy of those weights. Weights that drift between Make and the config file give you two different answers to the same question.
5. Post the digest, DM the reviewer, create the Asana approval task.

## Things that will bite

- **The 403.** Almost always the missing `time_tracking_entries:read` scope on an app connection rather than a bad token. Switch to the HTTP module with the token.
- **Pagination.** `/time_tracking_entries` pages at 100. A fortnight for a full team clears that easily, and a scenario that reads only the first page produces numbers that look plausible and are wrong.
- **The approval endpoint.** It is recent. Verify it against the workspace before Scenario C depends on it, and leave the on-time metric out rather than guessing a path.
- **Two sources of truth.** The roster and the weights should exist once. Every copy is a future bug.

---

*Internal skill by [Growth Today](https://www.growthtoday.co), maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
