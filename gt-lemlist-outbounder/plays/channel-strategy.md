---
name: channel-strategy
description: When Lemlist multichannel beats email-only or LinkedIn-only, and how to interleave email, LinkedIn, and calls. Read when deciding the channel mix for a campaign or routing a request to a sibling skill.
---

# Channel strategy — is multichannel worth it, and how

Multichannel is not "more channels = more replies." Each channel added is more infrastructure, more copy, and more that can break. Lemlist earns its place only when the channels are sequenced to compound. Otherwise route out.

## When Lemlist multichannel wins

- The buyer is **hard to reach on one channel alone** — senior, busy, or email-fatigued — and a LinkedIn touch or a call materially lifts the odds of a reply.
- You have a **real signal** worth surfacing across channels (see `signals-to-campaign.md`), so each touch reinforces the same relevant reason to talk.
- You can **staff the call and LinkedIn steps** — a call step no one makes is worse than no step.

## When to route out instead

| If the motion is really… | Route to |
|---|---|
| Pure email at volume, on dedicated cold infra | `gt-cold-email-writer` |
| LinkedIn-first / rented-engine, DM-led | `gt-linkedin-outbounder` |
| A deliverability or domain problem, not a channel-mix question | `gt-email-infra` |

Say which you picked and why before building anything.

## How to interleave the channels

The point of interleaving is **presence without pestering** — the prospect sees you in more than one place, but no single channel gets hammered.

- **Lead with the lower-friction channel** for the persona. For most B2B that's a LinkedIn view/engagement or a short email, not a cold call step one.
- **Space channels apart, not stacked.** Don't fire email + LinkedIn + call in the same 24h — it reads as automation. Alternate: email day 0, LinkedIn touch day 2-3, call day 5, follow-up email day 7.
- **One angle across channels.** The email and the LinkedIn step say the same thing differently; they never contradict or repeat verbatim.
- **Reply on any channel pauses the rest.** A LinkedIn reply stops the pending email step. Lemlist's conditional branches handle this — design for it.
- **Calls are for warm, not cold openers.** Slot call steps after a prospect has seen an email or LinkedIn touch, not as the first contact.

## Benchmarks to set expectations

Multichannel reply rates run above single-channel when the interleave is disciplined; a scattershot mix underperforms email-only. Judge on booked meetings over a 3-4 week arc, not day-3 opens.

## Execution (hand off to the Lemlist MCP)

```
get_campaigns → get_campaigns_stats            (see what already exists / how it performs)
→ decide multichannel vs route out →
propose_sequence                               (draft the interleaved arc)
→ human review of the channel mix →
(on go) create_campaign_with_sequence          (stage the campaign)
→ then design the steps in sequence-design.md, gate in readiness-checklist.md
```
