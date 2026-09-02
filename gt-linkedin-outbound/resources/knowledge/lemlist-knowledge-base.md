---
name: lemlist-knowledge-base
version: 1.0
updated: 2026-08-05
description: The dedicated multi-channel reference for gt-linkedin-outbound. Covers Lemlist, the tool Growth Today defaults to when a motion needs email and LinkedIn (and WhatsApp) in one coordinated sequence, plus the multi-channel coordination rules that apply whatever tool runs the sequence. Use when planning email-plus-LinkedIn outreach, voice-note or WhatsApp steps, or deciding between a LinkedIn-only engine and a multi-channel one.
---

# Lemlist Knowledge Base (multi-channel)

Lemlist is the tool Growth Today defaults to when a campaign needs more than one channel in a single coordinated sequence. HeyReach is the LinkedIn-only rented-engine workhorse (see `resources/knowledge/heyreach-knowledge-base.md`); Lemlist is the one we reach for when email, LinkedIn, and WhatsApp need to run as one flow with conditional logic across channels.

This file is the multi-channel home for the skill. It catalogs what Lemlist uniquely adds, the channel-coordination rules that hold whatever tool you use, and where each insight is consumed across the sub-skills. When the underlying facts change (pricing, channel coverage), this is the place to revisit before pushing edits into the sub-skills.

---

## How to use this file

- **Planning an email-plus-LinkedIn motion?** Read the multi-channel coordination rules below, then build the per-channel copy in the copywriting sub-skill and the cadence in the sequences sub-skill.
- **Deciding which tool?** Use the "When Lemlist vs when HeyReach" section.
- **Looking up a Lemlist capability or the current pricing?** Verify against the official source before quoting it to a client (see Sources).

---

## Source 1 - Growth Today internal sequencing SOP

**Source:** Growth Today's internal "Sequencing Tool Recommendations" SOP (the same source of truth the `gt-cold-email` skill uses). This is our own tested stance, not a vendor claim.

### What this source uniquely contributes

- **Lemlist is Growth Today's preferred multi-channel tool.** When a sequence needs email and LinkedIn (and now WhatsApp) in one workflow, Lemlist is the default. For email-only volume sending, Growth Today uses a dedicated email engine instead; for LinkedIn-only at rented-engine scale, HeyReach.
- **AI voice notes, native.** Lemlist supports AI-generated LinkedIn voice notes inside the sequence. This is the standout differentiator for a warm, human-feeling multi-channel step, and it is why the copywriting sub-skill's voice-note guidance assumes a tool that can send them.
- **One workflow across channels.** Email plus LinkedIn in a single sequence, with WhatsApp added as a channel (2026). The value is conditional logic across channels in one place, not stitching two tools together.
- **Email warmup is built in.** Warmup ships with the tool, so a multi-channel motion does not need a separate warmup product for the email side.
- **Cost frame (verify before quoting).** Per Growth Today's SOP, the entry tier is about $99 per user per month and bundles several email inboxes plus one LinkedIn account; a LinkedIn-only user still sits at roughly the same price as a LinkedIn-only tool, and bulk options lower the per-user cost at volume. Pricing moves, so confirm the current number on the official source before putting it in a proposal.

### Embedded into

| Sub-skill | What it informs |
|---|---|
| `resources/copywriting/copywriting.md` | Voice-note scripts assume a tool (Lemlist) that sends AI voice notes natively |
| `resources/sequences/drip-campaigns.md` | Multi-channel cadence: where an email step or a voice note sits alongside the LinkedIn touches |
| `resources/sequences/dm-sequence.md` | The channel-coordination rule at the no-reply step (pause the other channel on reply) |
| `SKILL.md` | The "Multi-channel coordination" core rule and the Lemlist row in the tooling table |

---

## Multi-channel coordination rules (apply whatever tool runs the sequence)

These are the rules the skill enforces for any email-plus-LinkedIn motion. They hold in Lemlist, in a two-tool setup, or anywhere else.

- **Different angle per channel.** The LinkedIn DM and Email 1 must open with different angles, never the same line pasted into two inboxes. A prospect who sees the identical message on two channels reads it as automation.
- **Reply on one channel pauses the other, immediately.** The moment a prospect replies on LinkedIn, pause the email sequence for that person (and vice versa). Nothing reads as "bot" faster than a scheduled email landing after a live LinkedIn reply.
- **LinkedIn leads, email supports.** In a LinkedIn-first motion, LinkedIn is the primary channel and email is the support channel for prospects who engaged on LinkedIn but did not convert there (see `resources/strategy/linkedin-first-engine.md`).
- **Coordinated multi-channel outperforms single-channel** (industry-reported, roughly a 45-60% lift per the HeyReach source; validate against the account's own data, do not present as a Growth Today-measured figure).
- **One prospect, one owner.** In a rented engine, keep a prospect on a single sending identity across channels so the conversation stays coherent and the account limits stay clean.

---

## When Lemlist vs when HeyReach

| Use Lemlist when... | Use HeyReach when... |
|---|---|
| The motion needs email + LinkedIn (+ WhatsApp) in one coordinated sequence | The motion is LinkedIn-only at rented-engine, multi-account scale |
| You want AI voice notes as a step | You are rotating many sender accounts within one campaign |
| A single operator runs a mixed-channel cadence | Account safety and per-account volume ceilings are the main constraint |

Both are named as neutral tools Growth Today uses; the choice is about the motion, not a ranking.

---

## What is NOT pulled in

For transparency:

- **Product UI click-paths and screenshots.** These belong in Lemlist's own help center, not in a copy and strategy skill. Point to the official docs instead.
- **Exact live pricing and tier tables.** Pricing shifts; the skill carries only a rough frame and a "verify on the official source" note, never a hardcoded price list.
- **Vendor benchmark numbers presented as ours.** Any third-party figure stays labeled as an industry-reported claim to validate.
- **Affiliate or referral links.** Not placed inside playbook logic.

---

## Refresh cadence

Re-check the channel coverage and the pricing frame quarterly, or whenever a client proposal needs a current number. Confirm against the official Lemlist source before quoting. When channel coverage changes (a new channel, a change to voice notes), update the copywriting and sequences sub-skills that assume today's capabilities.

## Sources

- Growth Today internal "Sequencing Tool Recommendations" SOP (our tested stance).
- Official Lemlist documentation at help.lemlist.com for current features and pricing (verify before quoting).

---

## Combines with

| Skill / file | Why |
|---|---|
| `gt-linkedin-outbound` | Main skill; the multi-channel coordination lives here |
| `gt-cold-email` | Owns the email side of a multi-channel motion; the two skills share the sequencing-tool SOP |
| `gt-clay` | Clay pushes enriched leads and custom variables into the sequence |
| `gt-signal-sourcer` | Signals decide which channel opens and with what angle |

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
