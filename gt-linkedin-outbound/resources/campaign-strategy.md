---
name: campaign-strategy
description: LinkedIn campaign-level strategy and lifecycle. Use when planning a campaign from scratch, diagnosing a campaign that's losing steam, structuring micro-segments, deciding when to relaunch vs. revive, or building outbound that doesn't die after 2 weeks. Triggers on "LinkedIn campaign strategy", "campaign decay", "campaign plateau", "micro-segmentation", "multi-account math", "campaign launch plan", "campaign lifecycle", "why is my campaign decaying", "kill and relaunch", "rotate fresh senders". This is the campaign-LEVEL view - for the copy that goes inside the campaign steps, use connection-request, connection-notes, dm-sequence, atl-messaging, btl-messaging.
---

# LinkedIn Campaign Strategy - Building Campaigns That Don't Die After Week Two

You design and diagnose LinkedIn outbound campaigns at the lifecycle level. Most campaigns that fail don't fail because of bad copy. They fail because they were structured for a good Day 1 and nothing more - one big list, one angle, one sender, no plan for what happens when the easy replies dry up.

This sub-skill is the campaign-level view. The copy that goes inside the steps lives in `copywriting/examples/connection-request.md`, `copywriting/examples/connection-notes.md`, `copywriting/examples/dm-sequence.md`, `copywriting/atl-messaging.md`, and `copywriting/btl-messaging.md`. Account safety and infrastructure live in `rented-engine/rented-engine.md`. This file is about how to *put a campaign together* so it produces pipeline for 60-90 days, not 14.

## The Campaign Decay Curve

Every LinkedIn campaign follows the same arc. Knowing where you are on it determines what to do next.

```
Replies
  ▲
  │     ╱╲
  │   ╱    ╲___
  │  ╱         ╲___
  │ ╱              ╲____
  │╱                    ╲____
  └────────────────────────────────► Time
   Days 1-10    Weeks 2-3      Week 4+
   (LAUNCH)    (PLATEAU)      (FATIGUE)
```

### Phase 1: Launch (Days 1-10)

Acceptance and reply rates peak here. You front-loaded your best-fit prospects, the angle is fresh, and the highest-intent people respond first.

What to do: don't break it. Don't pitch in M1. Don't add volume. Let the data come in clean so you can compare against it later.

If acceptance is below 25% even in the launch window, the problem is upstream (ICP, profile, list quality) - not in the sequence. Fix the upstream before you spend time on copy.

### Phase 2: Plateau (Weeks 2-3)

Numbers dip. Your highest-intent prospects already responded (or didn't). What's left is the rest of the segment - less perfect fits, slower decision-makers, less urgent timing. The angle that worked in week one starts losing its edge.

This is normal. Most teams misread the plateau as failure and either blast more volume (wrong) or kill the campaign (worse). The fix is structural:

- **Rotate in fresh senders.** Highest-impact lever. Add another LinkedIn account to the campaign. Five accounts at 25/day each gets you 125 daily touches with no single account under pressure.
- **A/B test a new angle.** If your hook was ROI-focused, try a problem-focused one. If you led with your product, lead with their context.
- **Push non-responders to email.** Multi-channel coordination earns its keep here. Non-responders move from LinkedIn to an email sequence (Instantly or Smartlead) automatically.
- **Adjust timing.** Tuesday-Thursday outperforms Monday and Friday for most B2B audiences. If your data shows a pattern, use it.

### Phase 3: Fatigue zone (Week 4+)

Without intervention, here's what you'll see:

- Acceptance rate dropping while send volume stays flat
- "Accepted but silent" ratio climbing above 60-70%
- Time-to-first-reply stretching from days to over a week
- Positive reply ratio declining (more "not interested" than "tell me more")

Before doing anything else: **withdraw all pending connection requests older than 14 days.** A queue >1000 pending invitations triggers LinkedIn's anti-spam systems and quietly drags down acceptance on every new request from that account.

Then pick one of two paths:

**Option 1: Kill and relaunch.** Pause, duplicate the campaign, exclude already-contacted leads, add fresh senders, update message angles, and launch against a new micro-segment. Cleaner reset. You're not salvaging a tired campaign - you're building a sharper one on top of what you learned.

**Option 2: Revive with a repositioned angle.** "I know I've reached out a couple of times, and I'll make this the last one. We just [launched X / helped Y achieve Z]. If the timing ever becomes right, you know where to find me." Works better than it should. Sometimes acknowledging that the angle didn't land is what gets the reply.

The cleaner play is to plan for all three phases before launching. But if you're reading this mid-campaign, now you know your options.

## Foundation Before You Launch

Three things matter before a single message goes out. Skip them and the campaign will underperform regardless of copy quality.

### 1. Profile audit (1-2 hours per rep, one-time fix)

The sender's profile is what every prospect sees before deciding to accept. By Phase 2 of any campaign, more prospects start checking the profile before responding. A weak profile suppresses reply rates across every campaign that profile ever runs.

Fix:
- Headshot is professional and recent
- Headline speaks to the prospect's pain, not your job title ("Helping B2B sales teams fix outbound pipeline" beats "Account Executive at [Company]")
- About / summary opens with the value proposition, not your career history
- Banner image reinforces the same message visually
- Recent posting activity exists (even one post a month is enough)
- Featured section has 2-3 relevant artifacts (case study, customer quote, talk)

LinkedIn's January 2026 "Entity Alignment" update means the platform now checks whether the profile's expertise area matches who you're reaching out to. Misalignment quietly drops visibility. Profile-level optimization is now an algorithmic concern, not just a first-impression one.

For deeper sender-profile guidance specific to outbound, see `copywriting/examples/connection-request.md`.

### 2. ICP precision (the micro-segmentation move)

The single biggest mistake in LinkedIn campaign design: one big list of "everyone who matches our ICP."

A monolithic list means everyone in the campaign hits the same fatigue curve at the same time. When it decays, you have nothing to rotate into. Better approach: define your ICP at a level of granularity that creates 3-5 micro-segments, each with a different trigger or angle.

Example: instead of "VPs of Sales at SaaS companies, 50-500 employees", break it into:

| Micro-segment | Trigger / signal | Angle |
|---|---|---|
| VPs hired in last 90 days | New role | Their first-90-days priorities (pipeline health vs. team build-out) |
| VPs at companies that raised Series A/B in last 6 months | Funding | Scaling outbound post-raise without breaking what works |
| VPs who posted about pipeline or outbound in last 30 days | Content signal | Direct reference to their post |
| VPs at companies hiring SDRs aggressively | Growth signal | They're scaling outbound; what's the playbook? |
| VPs who engaged with your or your team's content | Warm signal | Continuation of a real (if brief) interaction |

Launch with the highest-intent first (job change, content signal). Rotate into the next as performance plateaus.

This decision - made before any copy is written - separates campaigns that produce pipeline for 90 days from campaigns that have a good two weeks and run out.

For tactical signal-sourcing, see `personalization/personalization.md` and the GT signal-sourcing skill.

### 3. List building in Sales Navigator

Sales Navigator is non-negotiable for serious LinkedIn outbound. Advanced filters (title, seniority, headcount, industry, time in role), Boolean search, and buying intent signals are not optional.

The single highest-impact filter most teams skip: **"Posted on LinkedIn in the last 30 days."** Reaching out to someone who hasn't logged in since 2023 isn't outreach, it's wishful thinking. Filtering on recent activity surfaces prospects who actually use the platform - they'll see your request and evaluate it. Adding this filter alone tends to lift acceptance rates immediately.

Other Sales Nav filters worth using:
- Mutual connections ≥5 (quietly lifts acceptance)
- Time in role ≤6 months (new-role signal, evaluating tools)
- Time in role ≥3 years (settled, harder to reach but higher buying authority)
- Posted on a relevant topic (Boolean search)

Build several smaller segmented lists, not one big one. Two hundred highly qualified, trigger-based prospects outperform 2,000 generic title matches in both reply rate and campaign longevity - because you can rotate fresh segments in as performance ebbs.

For full list-building methodology, see the GT list-building skill.

## Multi-Account Math (The Structural Lever for Safe Scale)

LinkedIn caps connection requests at 20-40 per day per account (with the weekly hard ceiling of ~100). One account can never produce serious volume.

The math that matters:

| Account count | Daily connection requests (at 18/day each) | Weekly | Notes |
|---|---|---|---|
| 1 account | 18 | 90 | Single point of failure. One restriction = pipeline stops. |
| 3 accounts | 54 | 270 | Reasonable for an SDR + 2 support profiles |
| 5 accounts | 90 | 450 | Standard agency rented engine for one client |
| 10 accounts | 180 | 900 | Full ABM blast across a 5-10K account list |

HeyReach (and Expandi, La Growth Machine) auto-rotate sends across all senders attached to a campaign. No rep needs to track who sent what. All replies surface in a unified inbox.

One account hammering a list is the slow path to restriction. Five accounts rotated within one campaign distribute load and let conversations land at safer per-account volumes.

For account sourcing, anti-detect browsers, proxies, and warmup, see `rented-engine/rented-engine.md`.

## Multi-Channel Coordination

Combining LinkedIn and email in a coordinated sequence lifts results 45-60% over single-channel. The flow:

1. LinkedIn connection request + 2-3 follow-ups (HeyReach or similar)
2. No response after the LinkedIn sequence → automatically pushed to email (Instantly or Smartlead via native integration)
3. Email engagement → LinkedIn re-engagement or manual follow-up
4. Reply on either channel → pause both

One nuance from the 2026 algorithm tightening: external links in LinkedIn DMs are increasingly flagged. Keep early-stage messages link-free. Describe the resource and offer to send it on reply. Drop the actual link only after they ask.

For the LinkedIn copy side of multi-channel sequencing, see `copywriting/examples/dm-sequence.md` (Multi-Channel Coordination section). For the email side, see the GT cold-email skill.

## Common Campaign-Level Mistakes

Most LinkedIn campaign failures are structural, not creative. The mistakes below are baked into the campaign before a single message goes out.

| Mistake | Why it kills the campaign |
|---|---|
| One big undifferentiated list | Everyone hits fatigue at the same time. Nothing to rotate into. |
| One sender account doing 100 invites/day | LinkedIn cap is 20-40/day. Restriction is a matter of when, not if. |
| Skipping follow-ups (M2) | 10.7% of campaigns generate zero replies after acceptance. M1 alone leaves ~40% of pipeline on the table. |
| Sending more volume when metrics drop | Accelerates list burnout. The right move is a new segment, fresh angle, or new senders. |
| Generic copy in M1 | Connection accepted ≠ permission to pitch. M1 with a product mention drops reply rate by 30-50%. |
| Weak sender profile | Suppresses reply rates across every campaign forever. Fix the profile once, lift everything. |
| No exit plan for non-responders | They sit in the queue indefinitely or get nudged to death. Both hurt the sender's account. |

## The 3-Day Campaign Setup Playbook

If the campaign is being built from scratch, three focused days get a properly structured one running.

### Day 1: Foundation (≈1 hour)
- Audit each sender's profile (headshot, headline, summary, banner, recent activity)
- Define 3-5 micro-segments from the broader ICP using different trigger signals
- Build the first segmented list in Sales Navigator with the "active in last 30 days" filter applied
- Confirm anti-detect browser and proxy setup if running rented accounts

Goal: everything is in place before a single message goes out.

### Day 2: Campaign setup (1-2 hours)
- Create the campaign in HeyReach (or chosen tool)
- Assign 2-3 sender accounts; configure daily limits per sender (15-18 connection requests/day)
- Build the sequence: connection request → 2-3 follow-ups with conditional logic for connected vs. non-connected
- Set auto-withdrawal for unanswered connection requests at 14 days
- Connect inbox sync so replies pause the sequence automatically

Goal: a campaign structured for the full decay curve, not just Day 1.

### Day 3: Launch and baseline (≈30 minutes)
- Launch against the highest-intent micro-segment first
- Record starting benchmarks: acceptance rate, reply rate, time-to-first-reply
- Block 30 minutes at the end of Week 2 to review trends (not the snapshot - the direction)

Goal: live with a baseline to measure against, and a calendar reminder to actually look.

## What to Track at the Campaign Level

Snapshot metrics mislead. Trend metrics tell the truth.

| Metric | Snapshot view | Trend view |
|---|---|---|
| Acceptance rate | "We're at 22%" | "We were at 28% Week 1, now we're at 22%, dropping ~3pts/week" |
| Reply rate | "We're at 18%" | "Reply rate held at 22% for two weeks, now sliding" |
| "Accepted but silent" ratio | "60%" | "Was 40% in Week 1, climbing 5pts/week" |
| Time-to-first-reply | "3 days average" | "Was 2 days in Week 1, now 5 days" |
| Positive reply ratio | "70/30 positive/negative" | "Started 80/20, now 60/40" |

A campaign at 22% reply rate but declining week-over-week is in worse shape than one at 18% holding steady for three weeks. Track weekly trends. Chasing a "good" aggregate number while your best segments are already exhausted is how pipelines quietly die.

For the full benchmark and diagnostic tables, see `resources/linkedin-metrics-benchmarks.md`.

## Combines With

- **connection-request** & **connection-notes** - copy for the first touch
- **dm-sequence** - copy for M1, M2A, M2B (the steps inside the campaign)
- **personalization** - sourcing the signals that drive micro-segmentation
- **rented-engine** - account infrastructure when running multi-account
- **re-engagement** - what to do with the prospects who go silent
- **linkedin-first-engine** - the strategic case for making LinkedIn the primary channel

---

*Source: Adapted from HeyReach's "LinkedIn outreach strategy for 2026" - https://www.heyreach.io/blog/linkedin-outreach-strategy. See also `resources/heyreach-knowledge-base.md` for the full external reference map.*

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
