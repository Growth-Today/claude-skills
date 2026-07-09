---
name: linkedin-metrics-benchmarks
version: 1.0
updated: 2026-05-01
description: LinkedIn metrics to track, benchmarks, and diagnostics for outbound DM campaigns. Use when analyzing campaign performance, setting benchmarks, or optimizing LinkedIn outreach metrics.
---

# LinkedIn Metrics & Benchmarks

## Metrics to Track

**Note: LinkedIn does NOT expose open rate** for connection requests or DMs. Unlike email, you cannot see whether a DM was read (the "seen" indicator is unreliable and not exportable). Focus on **acceptance rate**, **reply rate**, and **meeting rate**. These are the only three metrics that matter for connection-based outreach.

**InMail is the exception.** InMail bypasses the connection layer entirely (it's a paid message that goes to non-connections), so there's no acceptance rate to track. The primary metric for InMail is **response rate**. See the dedicated InMail benchmarks section below.

### 2X Levers (Metrics you can realistically double)

| Metric | Below baseline | Typical | Strong | Elite |
|--------|---------------|---------|--------|-------|
| Connection acceptance rate | <13% | ~21% | 25-32% | 33%+ |
| DM reply rate (post-acceptance) | <13% | ~22% | 25-33% | 33%+ |
| Meeting rate (replies → booked) | <10% | 15-20% | 20-30% | 35%+ |

**Source:** Numbers based on HeyReach's analysis of 96,051 LinkedIn outreach campaigns. Below 13% on either acceptance or reply rate means something structural is off (targeting, profile, or angle) - fix the foundation before tweaking copy. The full benchmark provenance is in `resources/heyreach-knowledge-base.md`.

**Aspirational benchmarks (older, less defensible):** Some agency clients reference LeadLoft's older numbers (50%+ acceptance, 30%+ reply rate) as targets. Track the gap, but don't promise these - they predate the 2026 algorithm tightening and the rise of AI-saturated inboxes.

**Acceptance rate is the gating metric.** If acceptance is <20%, nothing downstream works. Fix the connection layer first (sender profile, note vs. no-note, ICP fit) before touching DM copy.

---

## Performance by Outreach Type

### Connection Acceptance Rate

| Outreach Type | Acceptance Rate |
|---------------|-----------------|
| Cold connection, no signal, no note | 20-25% |
| Cold connection, no signal, with note | 18-25% |
| Signal-based (job change, post engagement, hiring) | 35-45% |
| Engagement-warmed (liked/commented before requesting) | 40-55% |
| Multi-signal stacked | 50-60% |
| Mutual connections (5+) | 45-60% |

### DM Reply Rate (post-acceptance)

| Outreach Type | Reply Rate |
|---------------|------------|
| Cold DM (no signal, generic angle) | 5-8% |
| Signal-based DM | 18-25% |
| Multi-signal stacked | 30-40% |
| Engagement-warmed sequence | 25-35% |
| Champion job change DM | 25-35% |
| Voice note DM (BTL, well-targeted) | 30-40% |

### InMail Response Rate (no acceptance gate - paid channel)

| Outreach Type | Response Rate |
|---------------|---------------|
| Cold InMail, no signal, generic | 7-12% |
| Signal-based InMail (recent post, role change, hiring) | 18-25% |
| Recruitment InMail to passive candidate (well-targeted) | 25-40% |
| Recruitment InMail to active candidate ("Open to Work") | 35-50% |
| Executive search / retained recruiting | 30-45% |
| HR / Marketing services pitch (cold) | 8-15% |
| Sponsored InMail / Conversation Ads (paid promoted) | 3-5% |

InMail performs differently from connection-based outreach because the prospect has not opted in - so response rates are typically lower than a well-warmed DM, but you bypass the connection gate entirely. Recruitment use cases routinely outperform sales because the message itself is the value (a job opportunity), not a pitch attached to a conversation. See the dedicated InMail benchmarks section below for full operating guidance.

---

## DM Structure Checklist

```
Opening (observation/signal) + Develop (1-2 sentences) + Soft close (genuine question)
```

| Target | Max Words | Hard Rule |
|--------|-----------|-----------|
| ATL (VPs, C-Level) | 40-50 words | No pitch, no product name in M1, strategic language |
| BTL (Managers, ICs) | 50-70 words | Operational language, name daily friction, no pitch in M1 |
| Connection note (if used) | 150-220 chars | Under 300 char hard cap, signal-based only |

---

## Account Safety & Deliverability Benchmarks

LinkedIn doesn't have "deliverability" the way email does - but it has account health metrics that matter just as much. A restricted account is the LinkedIn equivalent of a blacklisted domain.

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Account restriction rate (per month) | <2% | 2-5% | >5% |
| Connection invitation withdrawal rate | <30% | 30-50% | >50% |
| Pending connection requests (queue depth) | <500 | 500-1000 | >1000 |
| Daily connection requests sent | 15-18 | 19-22 | >22 |
| Weekly connection requests sent | 80-90 | 91-99 | >100 (hard cap) |
| Daily DMs sent | <50 | 50-80 | >80 |

**Withdrawal rule:** Withdraw pending invitations after 14 days. A queue >1000 pending invitations triggers LinkedIn's anti-spam systems.

**Hard cap:** LinkedIn enforces ~100 connection requests per week per account. Operate at 80-90 to leave headroom.

For full account safety operating procedure → see `rented-engine/rented-engine.md`

---

## InMail Benchmarks (Sales Navigator / Recruiter / Premium)

InMail is LinkedIn's paid messaging product that lets you contact people you're not connected to. It bypasses the connection request entirely. You pay in **credits**, which are tied to the LinkedIn paid plan you're on.

InMail matters most for industries where outbound conversations need to start fast and where the receiver is used to (or expecting) cold outreach: recruitment, talent acquisition, executive search, HR consulting, marketing services, and B2B sales into hard-to-reach senior roles.

### Who uses InMail and why

| Industry / Use case | Why InMail fits |
|---|---|
| Recruitment & Talent Acquisition | Candidates expect role-based outreach. The message itself is the value (a job opportunity). Highest response rates of any InMail use case. |
| Executive search | Candidates often won't accept random connection requests. InMail bypasses that gate. |
| HR consulting / People-ops services | Buyers (CHROs, VP People) get hit hard with connection requests and ignore most of them. A well-targeted InMail with a clear subject can break through. |
| Marketing services agencies | Buyers (CMOs, VP Marketing) are the same. InMail's subject line gives a way to lead with the offer or signal directly. |
| B2B sales to senior decision-makers | When the prospect is selective about connections (older execs, board members, etc.), InMail reaches them without asking for the social commitment first. |
| Time-sensitive outreach | When you need a response in days, not weeks, InMail skips the 5-7 day acceptance wait. |

### InMail credit math

Credits come with the paid plan and don't roll over indefinitely.

| Plan | Monthly InMail credits | Notes |
|---|---|---|
| Premium Career | 5 | Mostly individual job-seekers |
| Premium Business | 15 | Light B2B use |
| Sales Navigator Core | 50 | Standard sales use |
| Sales Navigator Advanced | 50 | Same credit count, more team features |
| Sales Navigator Advanced Plus | 50 | Plus CRM sync, integrations |
| Recruiter Lite | 30 | Single recruiter use |
| Recruiter (Corporate) | 100-150 | Team / agency recruitment |

**Credit refund rule:** LinkedIn refunds the credit if the recipient responds (positively OR negatively) within 90 days. So well-targeted InMails effectively cost nothing in credits - poorly-targeted blasts burn credits with no recovery.

**Banking rule:** Unused credits roll over up to 3x your monthly allocation (cap), then they stop accumulating.

### InMail metrics that matter

| Metric | Below baseline | Typical | Strong | Elite |
|---|---|---|---|---|
| Open rate (subject line driving this) | <40% | 60-70% | 70-80% | 85%+ |
| Response rate (overall) | <8% | 10-18% | 20-30% | 35%+ |
| Response rate (recruitment context) | <15% | 20-30% | 35-45% | 50%+ |
| Credit recovery rate (% refunded) | <50% | 60-70% | 75-85% | 90%+ |
| Meeting rate (responses → booked) | <10% | 15-25% | 25-35% | 40%+ |

Open rate matters here in a way it doesn't for DMs - InMail has a subject line that the recipient sees in their inbox, and a weak subject means the message never gets opened. Track open rate separately from response rate to find whether the subject or the body is the problem.

### Subject line rules (InMail-specific)

Unlike DMs, InMail has a subject line. Treat it like a cold email subject.

- **Mobile cap: ~40 characters visible.** Anything over 40 gets truncated. Front-load the most important word.
- **Lead with the signal or context, not the offer.** "Re: your post on activation onboarding" beats "Quick chat about [Product]."
- **No clickbait.** "Important question" or "Re: your team" gets opened then immediately deleted - response rate craters.
- **No "RE:" or "FW:" tricks.** LinkedIn's algorithm flags these and reduces deliverability.
- **Recruitment use case:** Lead with the role or company name. "Senior PM role at [Company]" outperforms "Career opportunity" by 2-3x in open rate.

### Body length rules

| Use case | Max words | Notes |
|---|---|---|
| Sales / B2B InMail to senior buyers | 80-120 | Slightly longer than a DM because the subject sets context. Still no pitch in the first paragraph. |
| Recruitment InMail | 100-150 | Role description, comp band, why this candidate specifically, soft CTA |
| Executive search | 60-90 | Discrete, peer-to-peer, no role details upfront (those come on the call) |
| HR / Marketing services pitch | 80-120 | Lead with a signal or insight, not a demo ask |

### When NOT to use InMail

- **Long sales cycles where relationship building matters more than speed.** Use a connection request and content engagement instead - the relationship compounds.
- **Mid-market and SMB sales.** Connection-request-based outreach is cheaper, scales better, and converts at similar rates for these segments.
- **Generic prospecting at scale.** InMail credits are limited and expensive per-credit; burning them on low-signal lists destroys the ROI.
- **Re-engaging existing connections.** They're already connected - DM them instead. InMail to a 1st-degree connection is wasted credits.
- **When the prospect is active on LinkedIn and accepts connections readily.** Connection request + DM is free and equally effective.

### Sponsored InMail (Conversation Ads) - separate channel

Sponsored InMail (rebranded "Conversation Ads") is the paid ad version - bulk-promoted messages that show up in the recipient's inbox with a "Sponsored" tag. Different rules entirely:

- Lower response rates (3-5% typical) because recipients know it's an ad
- Pay-per-send model, not credit-based
- Best for awareness campaigns and high-volume top-of-funnel, not 1:1 outreach
- Belongs in `gt-linkedin-ads` skill territory, not outbound copy

If your team is using "InMail" loosely to mean Conversation Ads, that's a different motion entirely. Sales Nav / Recruiter / Premium InMail credits go through the standard inbox and look like a regular message; Conversation Ads are flagged as sponsored.

### Quick InMail diagnostics

| Symptom | Likely cause | Fix |
|---|---|---|
| Low open rate (<40%) | Subject line is weak or too long for mobile | Rewrite subject under 40 chars, lead with signal/role/context |
| High open rate, low response (<10%) | Body opens with a pitch, or wrong target | Rewrite first paragraph as observation/signal, sharpen ICP |
| Recruitment InMail underperforming | Generic role pitch, no candidate-specific reason | Reference one specific thing from their profile that ties to the role |
| Burning credits with no refunds | Too cold, too generic, not targeted enough | Reduce volume, layer signals, treat each InMail like a 1:1 send |
| Sales Nav InMail working but low meeting rate | Body is good but CTA is too soft or too aggressive | Test offering specific times vs. open-ended ("worth a quick chat") |

For full InMail copy frameworks → see `copywriting/copywriting.md` (InMail subsection).

---

## Sequence Performance (GT Standard)

For full sequence structure, timing, thread rules, and DM content → see `copywriting/examples/dm-sequence.md`

### General Performance Logic

**Connection request** - The gate. If acceptance <25%, nothing else matters. Test note vs. no-note, sender profile quality, and warming flow first.

**M1 (post-acceptance opener)** - Carries the majority of replies in the sequence. Most important to optimize. Test angle, opening line, and length. Never pitch here.

**M2A (reply continuation)** - Triggered by a reply to M1. Acknowledge briefly, deepen one element, soft CTA. Reply→meeting conversion happens here.

**M2B (no-reply bump)** - Adds **30-50% reply lift** vs. stopping after M1. NEW angle - never reference M1. Treat as fresh first message with different entry point.

**Why M2 matters operationally:** HeyReach's analysis found that ~10.7% of campaigns where connections were accepted generated zero replies after M1. That's 1-in-10 campaigns where the opener landed nothing - until M2 with a new angle ran. Skipping M2 throws away ~40% of pipeline potential on average and 100% on the unlucky 10%.

After M2B with no reply → stop the sequence. Do NOT add M3, M4, or "checking in" messages - these tank account safety scores and acceptance on future requests. Re-engage 60-90 days later according to `copywriting/re-engagement.md`.

---

## Touchpoint ROI

Where to invest personalization effort, ranked by impact per minute spent:

| Touchpoint | ROI | Notes |
|------------|-----|-------|
| Sender profile (one-time) | Highest | Affects every campaign forever - fix first |
| Engagement-warming (per prospect) | Very high | +10-15pts acceptance, takes 30 sec/prospect |
| M1 opening line | Very high | First 10 words determine whether they read past line 1 |
| M1 signal hook | High | Drives reply rate by 10-15pts when strong |
| Connection note (when used) | Moderate | Often equal performance with or without - A/B test |
| M2B angle freshness | High | Choosing a new angle drives 30-50% reply lift |
| M2A acknowledgment | Moderate | Just don't be robotic - low downside, low upside |

---

## Diagnostic Decision Tree

The fastest way to find what's broken in a LinkedIn campaign: read two metrics together, not one in isolation.

| Acceptance rate | Reply rate | Volume / Meetings | Root cause | Fix |
|---|---|---|---|---|
| **Low** | **Low** | - | **Targeting** problem | Wrong ICP, weak warming, or sender profile pushes prospects away. Fix the foundation before touching downstream copy. |
| **High** | **Low** | - | **Messaging** problem | List is right, opener isn't landing. Test new angles, sharpen personalization, remove product/company name from M1. |
| **High** | **High** | Few meetings | **Conversion** problem | Meeting CTA isn't direct enough, or conversations aren't being moved to email/booking link in time. Tighten the ask. |
| Decent | Decent | Volume too low | **Infrastructure** problem | Need more accounts in rotation, or daily activity is too conservative. See `rented-engine/rented-engine.md`. |

Source: Adapted from HeyReach's diagnostic framework based on 96,051 campaigns. See `resources/heyreach-knowledge-base.md`.

This is the **primary diagnostic tool** when a campaign is underperforming. Run it weekly, not monthly - by month-end, the decay curve has compounded.

## Campaign Phase Metrics (Decay Curve)

Every campaign follows the same arc. Use these numbers to know which phase you're in:

| Phase | Window | Expected acceptance trend | Expected reply trend | Action |
|---|---|---|---|---|
| **Launch** | Days 1-10 | Peak - best-fit prospects respond first | Peak | Don't change anything. Let it run. Capture data. |
| **Plateau** | Weeks 2-3 | -3 to -8 pts vs. Launch | -3 to -8 pts vs. Launch | Rotate in fresh senders, A/B test a new angle, push non-responders to email. **Don't add volume.** |
| **Fatigue zone** | Week 4+ | -10+ pts; <20% absolute | "Accepted but silent" >60-70% | Either kill-and-relaunch with new segment + senders, OR run a re-engagement sweep. **Withdraw all pending invitations >14 days old.** |

### Decay signal thresholds (early warning)

- Acceptance rate falling with flat send volume → entering plateau
- "Accepted but silent" ratio above 60-70% → entering fatigue zone
- Time-to-first-reply stretching from 2-3 days to over a week → segment is exhausted
- Positive reply ratio declining (more "not interested" replies than "tell me more") → angle is stale

Source: HeyReach decay framework. See `resources/heyreach-knowledge-base.md`.

## Quick Diagnostics (Symptom-Level)

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Low acceptance rate (<20%) | Sender profile weak OR ICP mismatch OR poor warming | Audit profile, check ICP fit, add engagement-warming flow |
| High acceptance, low reply (<10%) | Generic M1, pitch in M1, or wrong angle | Stronger signal, remove product/company name from M1, test new angle |
| Replies but no meetings | Weak CTA or poor qualification | Clearer ask in M2A, better ICP targeting upstream |
| Account restricted | Volume too high OR too many withdrawals OR generic copy reported | Pause 7-14 days, review per `rented-engine/rented-engine.md` recovery flow |
| High withdrawal rate (>50%) | Bad ICP or weak hook | Tighten list, improve sender relevance, reduce volume per account |
| Pending queue >1000 | Volume outpacing acceptance | Withdraw invitations >14 days old, pause and rebuild |
| Acceptance fine, M2B replies near zero | M2B references M1 or repeats angle | Rewrite M2B as fresh opener with new angle |

---

## Optimization Priorities

### If Acceptance Rate Low (<25%)

1. Audit sender profile (banner, headline, recent activity, photo)
2. Add engagement-warming step (visit profile → like/comment → wait 24h → request)
3. Test no-note vs. note - note often hurts when generic
4. Tighten ICP - weak fit kills acceptance more than weak copy
5. Check mutual connection count - <5 mutuals on a cold profile lowers acceptance

### If Reply Rate Low (<15%)

1. Strengthen signal in M1 - recent post, engagement, job change beat generic ICP angles
2. Cut M1 length - 40-70 words max, ATL closer to 40
3. Remove product/company name from M1 entirely
4. Replace closed questions with one open genuine question
5. Test M2B angle freshness - most M2Bs underperform because they reference M1

### If Meeting Rate Low (<20% of replies)

1. Qualify better in M2A - clearer ask, specific value
2. Reduce friction (offer 2 specific times, not "do you have 15 min next week")
3. Follow up within 24h of reply - not 48h
4. Move to email or call after 2 reply exchanges - LinkedIn DM is a poor closing channel

### If Account Health Declining

1. Reduce daily connection requests to 10-12
2. Withdraw all pending requests >14 days old
3. Pause sequencer for 48h
4. Review recent copy - generic templated outreach gets reported
5. See `rented-engine/rented-engine.md` restriction recovery flow

---

## Reporting Cadence - Right vs. Wrong Metrics

When LinkedIn becomes a primary channel, the way performance is measured has to change. Email-era metrics misread LinkedIn campaigns systematically.

### Track weekly (primary metrics)

- **Meetings booked from LinkedIn** - the only output metric that matters. Everything else helps explain *why* this number moves.
- **Connection-to-conversation rate** - how efficiently connections turn into actual two-way exchanges. Low rate = messaging or follow-up needs work.
- **Conversation-to-meeting rate** - conversion efficiency. Low rate with high conversation volume = sharpen the close.
- **Pipeline velocity** - average days from first touchpoint to booked meeting. Real number to share with leadership instead of "results take time."

### Track monthly (secondary metrics)

- **Reply rate by message variant** - compare opening angles and follow-up approaches. Scale what works, retire the rest.
- **Acceptance rate by prospect segment** - by role, industry, company stage. Shift volume toward the segments where the targeting is sharpest.
- **Multi-channel conversion rate** - how many LinkedIn-non-converters book through the email follow-up. Validates the LinkedIn-first-not-LinkedIn-only approach.

### Stop tracking entirely

- Total LinkedIn connections accumulated
- Messages sent per week (vanity volume)
- Generic engagement metrics from the sender's organic content (track those separately under `gt-linkedin-content`)

If reps are evaluated on volume, they'll optimize for volume. If they're evaluated on conversations and meetings, they'll optimize for quality.

Source: HeyReach's framework for LinkedIn-first measurement. See `resources/heyreach-knowledge-base.md`.

---

## 90-Day Pilot Expectations

LinkedIn outbound is a compounding channel, not a Day-14 channel. Set internal and client expectations against this timeline:

| Window | Realistic outcome | Wrong question to ask |
|---|---|---|
| **Month 1** | Foundation, learning, first data flowing. Insights, not meetings. | "How many meetings have we booked?" |
| **Month 2** | First consistent meeting flow. Some real conversations converting. Optimization signal becomes legible. | "Why isn't this scaling yet?" |
| **Month 3+** | Compounding. Meeting volume becomes predictable and improvable week over week. | "When do we cut this?" |

A campaign judged on Day 14 metrics will get killed before it has a chance to compound. Every pilot proposal and client review should anchor here.

---

## What Not to Track on LinkedIn

These metrics are unreliable, exportable inconsistently, or actively misleading:

- **Profile views** - Not a campaign metric. Vanity number.
- **"Seen" indicator on DMs** - Unreliable, often delayed, not exportable from any sequencer.
- **Post likes/comments from prospects** - Useful as a signal input, not as a campaign output.
- **Follower growth from outbound campaigns** - Conflates organic and outbound. Track separately.

---

## Combines with

| Skill | Why |
|-------|-----|
| `gt-linkedin-outbound` | Main skill - routing and sequence structure |
| `gt-signal-sourcer` | Improve acceptance and reply rates with better signals |
| `gt-list-building` | Fix low-acceptance issues caused by weak ICP fit |
| `gt-linkedin-content` | Sender profile and content layer that lifts every metric here |
| `gt-clay` | Personalization data feeding M1 hooks |

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Built and maintained by [Nikola Siljanoski](https://www.linkedin.com/in/nikola-siljanoski/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*