---
name: drip-campaigns
description: LinkedIn drip campaign setup, sequence templates, and step-by-step build inside HeyReach (or similar tools). Use when the user is setting up a new drip campaign, asking about sequence templates, configuring daily steps, choosing wait times between messages, importing leads, or troubleshooting a drip campaign that's underperforming. Triggers on "drip campaign", "sequence templates", "campaign template", "sequence cadence", "sequence setup", "HeyReach setup", "lead import", "wait time between messages", "Day 0 Day 1 Day 3", "campaign builder". This is the SETUP and STRUCTURE guide; for the copy that goes inside the sequence steps, route to dm-sequence, connection-request, or connection-notes.
---

# LinkedIn Drip Campaign Setup

A drip campaign is a sequence of automated steps that engages a prospect over time - connection request, profile view, post engagement, M1, M2, and so on. Done well, it builds familiarity before the offer. Done badly, it's a pitch with extra steps.

This sub-skill is about the structure: what steps to use, in what order, with what timing. The copy for each step lives elsewhere:
- Connection request copy → `copywriting/examples/connection-request.md`
- Connection note copy → `copywriting/examples/connection-notes.md`
- Post-acceptance DM sequence → `copywriting/examples/dm-sequence.md`
- Personalization at scale → `personalization/personalization.md`

Setup walkthrough below uses HeyReach as the example tool because it's the GT default, but the same logic works in Expandi, La Growth Machine, and Lemlist with minor UI differences.

## Before You Build: Three Things That Determine Whether the Campaign Will Work

### 1. One clear goal per campaign

The single most common drip campaign failure: trying to do too much in one campaign.

Pick one goal. Examples:
- Promote a lead magnet (ebook, research report)
- Book intro meetings
- Drive demo sign-ups
- Warm up prospects before a product launch
- Promote a specific webinar or event

Trying for multiple goals makes the sequence longer and reduces effectiveness across all of them. One campaign, one goal.

### 2. ICP precision

Vague ICP produces vague campaigns. Tight ICP produces tight ones.

Examples of usable ICP:
- CMOs at healthcare companies under 100 employees in the UK
- B2B startup founders in the US, 11-50 employees, currently hiring SDRs
- Customer service leaders at companies with 1000+ employees in the UAE

Build the prospect list in Sales Navigator with the "Posted in last 30 days" filter applied. That filter alone tends to lift acceptance rates because you're reaching people who actually use LinkedIn.

For deeper list-building tactics, see the GT list-building skill. For the strategic case for micro-segmentation, see `resources/campaign-strategy.md`.

### 3. Profile warmup

Your sender's profile is part of the campaign whether you want it to be. Prospects will check it before deciding to accept or reply.

Quick audit before launch:
- Profile photo is clear and professional
- Headline speaks to ICP pain, not your job title
- About section reads as a value proposition, not a resume
- Banner reinforces the same message visually
- Recent posting activity exists (even one post a month is enough)

A weak profile suppresses reply rates across every campaign that profile ever runs. For full sender-profile guidance, see `copywriting/examples/connection-request.md`.

## Step-by-Step: Building a Drip Campaign in HeyReach

### Step 1: Import leads

From the dashboard, go to the Leads icon (third on the left) → "Add Leads" (top right corner).

Lead import sources HeyReach supports:
- LinkedIn search URL
- Sales Navigator URL
- LinkedIn post reactors (everyone who liked or commented on a post)
- Webinar attendees (CSV upload)
- Custom CSV file

The Sales Navigator import is the most common - paste the saved-search URL and HeyReach pulls the entire list. No CSV exports, no manual cleanup.

### Step 2: Start the campaign

Go to the Campaigns icon (fifth on the left) → "Start new campaign" → name the campaign.

Naming convention worth using: `[ICP-segment]_[angle]_[month]`. Example: `VPSales_NewRole_Jan26`. Lets you track variants over time without renaming.

### Step 3: Select leads and exclusions

Pick the lead list. Then exclude:
- Leads from other lead lists (don't double-target)
- Leads already contacted in another HeyReach campaign
- Leads messaged from another sender account already
- Leads contacted by the same sender in another campaign

Skipping these exclusions is how prospects end up in two campaigns simultaneously - then they get a message from you on Monday and a different one on Wednesday. That's the fastest way to get reported.

### Step 4: Select senders

Pick which LinkedIn accounts run this campaign. For multi-account rotation, attach 3-10 senders. HeyReach distributes sends across them automatically and surfaces all replies in the unified inbox (Unibox).

For account sourcing and infrastructure setup, see `rented-engine/rented-engine.md`.

### Step 5: Build the sequence

Two options:
- **Custom sequence:** Build step-by-step from the action library (more flexible)
- **Template:** Start from one of HeyReach's pre-built templates

HeyReach's 7 pre-built templates and what they fit:

| Template | Best for |
|---|---|
| Partnership proposal | Reaching out to potential partners or affiliates |
| Engagement response sequence | Following up on prospects who liked or commented on your post |
| Comment follow-up sequence | Continuing a conversation that started in a public comment thread |
| New connection nurture | Warming up prospects who recently accepted you, no specific signal |
| Value-first outreach | Lead-magnet-first outreach (resource → relationship → ask) |
| Social proof sequence | Pitching with case studies and customer quotes upfront |
| Expand your network sequence | Pure network-building, no sales angle |

Treat templates as starting points, not as scripts. The default copy is generic and will need to be rewritten for each ICP. The structure is what's reusable.

### Step 6: Set step actions and timing

Common drip actions inside a sequence:
- View profile (warming, no message)
- Like a recent post (warming, no message)
- Send connection request (with or without note)
- Send message (after acceptance)
- Send InMail (paid, bypasses connection gate)
- Find email (HeyReach pulls verified email for multi-channel handoff)
- Add to Instantly campaign or list (multi-channel handoff to email)

Wait times between steps matter:
- Connection request → M1 (after acceptance): 30-60 seconds (auto-trigger on accept)
- M1 → M2 (no reply): 3-5 days minimum, 7+ days for senior prospects
- Profile view → connection request: 24-48 hours (looks human)
- Like post → connection request: 24-48 hours

Configure daily limits per sender at this step (15-18 connection requests/day is the GT default). HeyReach enforces these as hard caps and distributes them proportionally across all active campaigns the sender runs.

### Step 7: Auto-withdrawal and reply detection

Two non-negotiables in the campaign config:

1. **Auto-withdraw pending invitations after 14 days.** Pending invitations sitting in LinkedIn's queue past 14 days hurt account health. A queue >1000 pending triggers anti-spam systems.
2. **Reply detection.** Connect inbox sync so any reply pauses the sequence automatically. No prospect should get an automated bump after they've replied.

### Step 8: Review and launch

Review:
- Sender accounts attached and warmed
- Daily limits set
- Sequence structure correct
- Wait times realistic
- Auto-withdrawal on
- Reply detection on
- M1 and M2 copy reviewed (different angles, no product mention in M1)
- Working hours set (9am-5pm in account's stated time zone)

Launch against the highest-intent micro-segment first. Record starting benchmarks: acceptance rate, reply rate, time-to-first-reply.

### Step 9: Track and optimize

You can edit message *copy* in an active campaign. You can NOT edit sequence *step structure* in an active campaign. Plan structure carefully upfront - copy can iterate freely.

What to monitor weekly (not daily, not monthly):
- Acceptance rate trend (declining = entering plateau)
- Reply rate trend (declining = angle going stale)
- Accepted-but-silent ratio (above 60-70% = entering fatigue zone)

For full diagnostic guidance, see `resources/linkedin-metrics-benchmarks.md`.

## Three Drip Campaign Templates Worth Adapting

These are starting points. Each needs to be rewritten for the specific ICP, signal, and offer.

### Template 1: Standard Drip (Cold, no signal)

```
Day 0 - Send connection request with light note
"Hi {{First Name}}, I've been speaking with a few leaders in {{industry}} 
lately and thought it'd be good to connect."

Day 1 - M1 (after acceptance, point out the pain you've noticed)
"Hi {{First Name}}, thanks for accepting. I've been speaking with a few 
{{role}}s in {{industry}} lately and one pattern keeps coming up: 
{{specific problem}}. Curious how you're approaching it at {{Company}}."

Day 3 - Light proof (case study or social proof)
"We've helped several teams in similar situations achieve {{specific 
outcome}} without {{common fear/objection}}."

Day 5 - Soft CTA
"If this is relevant, open to a quick chat to see if it applies?"

Day 8 - Bump if no reply
"Just checking back on this, {{First Name}}."
```

Caveat on Day 8: "just checking back" is one of the worst-performing phrases on LinkedIn. If you keep this step, rewrite the copy to follow the M2B pattern from `copywriting/examples/dm-sequence.md` (new angle, never reference M1).

### Template 2: Engagement-First Drip (For prospects active on LinkedIn)

```
Day 0 - Engage with their post
Like or comment thoughtfully on a recent post they wrote.

Day 1 - Connection request with content-based note
"Hi {{First Name}}, I enjoyed your post on {{topic}}, especially your 
point about {{specific insight}}. Thought I'd connect."

Day 2 - M1 (continuation of the conversation)
"Thanks for connecting, {{First Name}}. Curious how you're currently 
approaching {{related challenge they mentioned}}?"

Day 5 - Add value
"Most teams I see run into {{problem}} when doing this. One thing that 
helps is {{insight}}."

Day 8 - Share proof + soft CTA
"If it's useful, happy to share what worked for {{comparable team}}. 
Worth a quick chat?"

Day 12 - Final bump (M2B pattern)
[New angle entirely - don't reference previous messages]
```

This template is the best-performing of the three because Day 0 (engagement) lifts acceptance and warms the conversation before the request lands.

### Template 3: Credibility-First Drip (For ABM-style outreach)

```
Day 0 - Connection request, no note (or short generic note)

Day 1 - M1 (lead with credibility)
"Thanks for connecting, {{First Name}}. Recently we helped a 
{{similar company/role}} achieve {{specific result}} in {{timeframe}}."

Day 4 - Relevance check
"Curious if {{related problem}} is something you're focused on right now?"

Day 7 - Soft CTA
"Happy to share what we did and see if it applies to your situation."

Day 10 - Bump (M2B pattern - new angle)
[New angle entirely]
```

Best for higher ACV deals where the social proof is the strongest hook.

## Six Common Drip Campaign Mistakes

### 1. Poor personalization

Your prospects can smell weak personalization from miles away. The litmus test: "If someone sent me this message, would I respond?" If no, the message isn't there yet.

Bad: "Hi Sam, I'd love to connect and tell you about our solution."

Better: "Hi Sam, I came across your post on outbound sales for SaaS teams. I really liked your point about follow-ups. How many follow-up messages do you typically send if you don't get a response?"

The first centers on you. The second references something specific they wrote and asks about them.

For personalization at scale (Clay prompts, profile signals, six data buckets), see `personalization/personalization.md`.

### 2. Targeting the wrong audience

A subject angle for B2B marketing managers won't apply to B2C marketing managers. Tighten the ICP and run separate campaigns for distinct audience segments.

### 3. No clear CTA - or too many CTAs

Common CTA failures:
- No clear call-to-action at all
- A CTA in M1 (too soon - they JUST accepted)
- Multiple CTAs in one message ("book a call OR reply OR check out our case study")

One CTA per message. The CTA escalates across the sequence: M1 has no CTA at all (just a question). M2 has a soft CTA. Later steps can have a meeting ask.

### 4. Weak sender profile

If the profile is poorly put together, prospects will judge based on it. They'll ignore connection requests, dismiss messages, and the campaign underperforms regardless of copy quality. Fix the profile first.

### 5. Not stopping when you should

A good salesperson knows when to withdraw and stop messaging. After 2-3 follow-ups with no response, the right move is to tag, exclude, and revisit later (60-90 days, new angle). Continuing to push damages the sender's reputation more than it produces replies.

For the discipline of when to stop, see `resources/follow-up-system.md`.

### 6. Not optimizing based on data

A drip campaign isn't "set and forget." Watch the metrics weekly. Low acceptance? Test the connection note (or test no-note). Replies but no meetings? Sharpen the CTA. Identify where the issue is and fix that one thing - not everything at once.

For full diagnostic patterns, see `resources/linkedin-metrics-benchmarks.md`.

## Healthy Metric Ranges

For a benchmarks deep-dive with the 96K-campaign HeyReach dataset, see `resources/linkedin-metrics-benchmarks.md`. Quick reference for drip campaigns:

| Metric | Below baseline | Typical | Strong | Elite |
|---|---|---|---|---|
| Connection acceptance rate | <13% | ~21% | 25-32% | 33%+ |
| Reply rate (post-acceptance) | <13% | ~22% | 25-33% | 33%+ |
| Meeting / call booking rate | <10% (of replies) | 15-25% | 25-35% | 35%+ |

If your reply rate drops sharply after a particular message in the drip sequence, that's the message to rewrite. Diagnose by step, not by aggregate.

## Combines With

- **connection-request** & **connection-notes** - copy for the first touch (Day 0 step)
- **dm-sequence** - copy for M1 and M2 (the message steps)
- **personalization** - personalization at scale across the sequence
- **rented-engine** - account infrastructure for multi-sender campaigns
- **campaign-strategy** - the lifecycle view (decay curve, micro-segmentation, multi-account math)
- **follow-up-system** - the discipline of when to stop drip-following

---

*Source: Adapted from HeyReach's "A comprehensive guide to LinkedIn drip campaigns" - https://www.heyreach.io/blog/linkedin-drip-campaigns. See also `resources/heyreach-knowledge-base.md` for the full external reference map.*

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
