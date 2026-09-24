---
name: sequence-design
description: GT cadence design for a Lemlist multichannel sequence — step count, spacing, channel interleave, condition branches, and A/B discipline. Read when building or editing the steps of a campaign. Ends with the MCP hand-off.
---

# Sequence design — the cadence inside the campaign

Channel-strategy decides the mix; this play decides the shape of the steps. A good Lemlist sequence produces conversations over a 3-4 week arc, not a burst on day one.

## GT cadence defaults

- **5-7 steps over ~3-4 weeks.** Enough to build presence, not enough to become noise.
- **Front-load value, back-load the ask.** Early steps earn attention; the soft CTA lives in the middle, the graceful exit at the end.
- **Spacing:** 2-4 days between steps. Tighter than 2 days reads automated; wider than 5 loses the thread.
- **One CTA per step**, soft. Change the angle between steps, not the number of asks.

## Channel interleave

Alternate channels rather than stacking them (full rules in `channel-strategy.md`). A typical arc:

```
Day 0   Email 1        (short, signal-led, one angle)
Day 2   LinkedIn touch (view / light engagement / connection)
Day 4   Email 2        (same angle, new proof)
Day 6   Call step      (warm, references the prior touches)
Day 9   Email 3        (soft breakup, leaves the door open)
```

## Condition branches

Lemlist sequences are conditional — the next step depends on what the lead did. Design the branches, don't leave them default:

- **Replied on any channel →** stop the sequence. No further sends.
- **Opened / engaged but silent →** continue, lightly escalate the proof, keep the same angle.
- **No engagement at all →** switch the angle once, then exit. Don't just repeat.
- **Bounced / unsubscribed →** suppress immediately; never route to another channel as a workaround.

## A/B discipline

- Test **one variable at a time** — subject line, or opener, or CTA. Never all three.
- Keep variants running until the sample is real; don't call a winner on a handful of sends.
- A/B the **highest-leverage step first** (usually the first email's subject and opener).
- Log what won so the next campaign starts ahead, not from zero.

For product-specific step mechanics and copy tips, call Lemlist's own `load_skill` (campaign-builder, copywriting). This play is the GT judgment; those are the mechanics.

## Execution (hand off to the Lemlist MCP)

```
get_campaign_sequences                         (read the current steps)
add_sequence_step / update_sequence_step       (build or edit each step — human-gated)
set_ab_variant                                 (stage the A/B on the chosen step)
preview_sequence_update                        (see the change before it's live)
→ then run readiness-checklist.md before any launch
```

Every `add_`/`update_`/`set_` here is a write — stage it, show it, wait for the explicit human go.
