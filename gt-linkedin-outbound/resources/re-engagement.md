---
name: re-engagement
description: Writes LinkedIn re-engagement DMs for dormant connections, ghosted prospects, and old leads. Use when the user asks to "re-engage on LinkedIn", "win back dormant connections", "old LinkedIn connections", "they ghosted me on LinkedIn", "reactivate LinkedIn leads", "ramp re-engagement LinkedIn", or needs to message connections from weeks/months ago. Triggers on "revive dead LinkedIn leads", "lost deal LinkedIn", "old LinkedIn DM follow up", "no-show LinkedIn". Do NOT use for follow-ups within an active sequence (use dm-sequence) or first-touch connection requests (use connection-request).
---

# LinkedIn Re-Engagement

You write DMs that revive cold LinkedIn connections, ghosted prospects, and contacts who went dark weeks or months ago. These are NOT follow-ups within an active sequence - these target connections from old campaigns, closed-lost deals, or accepted-but-never-replied prospects.

## When This Sub-Skill Applies

- Connections accepted >60 days ago who never replied
- Prospects who replied months ago but went dark mid-conversation
- Closed-lost deals from 6-12+ months ago
- Old leads from sequences that never converted
- Connections made before a major product/positioning change

## The 4-State Follow-up Model (Decision Framework)

Before drafting any re-engagement DM, identify which **state** the conversation sits in. Same surface-level "no reply" situation can mean four very different things, and the right action diverges sharply by state.

| State | What it looks like | Right action |
|---|---|---|
| **State 1: Not accepted** | Connection request pending 7+ days, no profile view, no engagement | Don't follow up. Withdraw the request. Route to email instead. |
| **State 2: Accepted, no reply** | Connection accepted but M1 sat unanswered for 5-7+ days | One follow-up max with a 7+ day delay. After that, tag as "Accepted - No Reply" and stop. |
| **State 3: Active, no reply** | They're posting / commenting / engaging with others, but ignoring your DM | Don't nudge. Wait for a new external signal or 3-4 weeks. Re-engagement happens *only* when something changes on their side. |
| **State 4: Replied once, then stalled** | One reply, then 7+ days of silence after your last message | One thoughtful contextual follow-up that references the prior exchange directly. Then stop. |

**The dangerous middle ground is State 3.** When a prospect is active on LinkedIn but ignoring your message, the instinct is to nudge again. The data says don't - another message rarely increases reply probability and often hardens the non-response. Wait for one of these signals before re-engaging:

- They post about a problem your offering solves
- They engage with content from your company or your team
- They change roles
- A material event in their company or industry creates new context

Until one of those lands, leave the thread alone. Tag and exclude from active sequences.

State 4 is where contextual judgment pays off - see Example 1 below for the right framing.

For the post-acceptance branching version of this same logic (still inside an active sequence), see `copywriting/examples/dm-sequence.md`. This sub-skill picks up where that one ends - when the sequence has run its course and the prospect needs to be revived from a colder state.

Source: HeyReach's 4-state framework. See `resources/heyreach-knowledge-base.md`.

## Process

1. **Understand the history** - When was last contact? What was discussed? Why did they go cold? Did anything change on their side?
2. **Identify the new angle** - What's changed since? (New trigger on their side, new offering on yours, new market context)
3. **Decide the framing** - Acknowledge the gap (more honest, often outperforms) OR pivot fresh as if M1 (cleaner, less awkward)
4. **Draft the DM** - 50-70 words, soft CTA, never aggressive

## Reference

For full context:
- DM tone & rules → `{SKILL_BASE}/copywriting/examples/dm-sequence.md`
- Personalization signals → `{SKILL_BASE}/personalization/personalization.md`

---

## Three Re-Engagement Types

### 1. No-Oriented Question (Re-open conversations)

Use when the prospect engaged previously (meeting, demo, real reply) but went dark mid-cycle. Counterintuitively, "no-oriented" questions outperform asks because they remove pressure.

**Pattern:**
```
[Acknowledge gap - 1 sentence]
[New context or what changed - 1-2 sentences]
[No-oriented question]
```

**Example:**
```
Been a few months since we last talked about [topic at the time].

A few things have shifted since - most relevant: [one specific change in their world 
or yours, like a new feature, market trend, regulatory shift, or relevant case study].

Would it be unreasonable to reconnect for 15 minutes?
```

Why it works: "Would it be unreasonable" / "Would it be crazy" / "Bad idea?" - the prospect's "no" actually means "no, it's not unreasonable" → which is a yes. This is documented to outperform "Want to chat?" by 30-50% on dormant prospects.

---

### 2. Closed-Lost Reactivation

Use when a deal was lost, the objection is known, and something has materially changed.

**Pattern:**
```
[Reference the original conversation - 1 sentence]
[Name the specific objection they gave - 1 sentence]
[What's changed since - 1-2 sentences]
[Soft CTA - "worth another look?"]
```

**Example:**
```
When we talked back in [month], you mentioned [specific objection] was the deal-breaker.

Since then we've [specific change - new feature, integration, pricing model, new 
case study with a comparable company]. [Comparable company] just hit [specific result].

Worth a fresh look - or did you go in a different direction?
```

The "or did you go in a different direction" is critical - it acknowledges they may have already solved it elsewhere, which makes the message feel respectful rather than pushy.

---

### 3. Ramp Re-Engagement (New Angle, No Reference)

Use when the previous touch was thin (just a connection accepted, or a one-line DM ignored). Best approach: pretend it never happened. Open as if it were M1, with a completely different angle from whatever was sent before.

**Pattern:**
```
[New angle - 10-15 words about a current trigger or insight]
[Develop it briefly - 1-2 sentences]
[Reference why they came to mind - 1 sentence]
[Soft CTA or open question]
```

**Example:**
```
Different angle than last time - [industry] just had [specific recent event: regulation, 
market shift, viral moment, funding cycle].

Most [role]s at [company stage] are dealing with [specific implication] right now and 
the playbook from 12 months ago doesn't apply anymore.

[Company] came to mind given [specific reason - recent post, hiring, news].

Worth a conversation if this is on your radar?
```

---

## Universal Rules

- **Maximum one re-engagement attempt every 60-90 days** - anything more frequent burns the connection
- **Never reference how many times you've tried** - "I've reached out a few times now" is a guaranteed disconnect
- **Never use guilt** - "Just wondering if you got my last message?" is the lowest-converting opener on LinkedIn
- **Never use "checking in"** - most-burned phrase in B2B outreach
- **Lead with what changed, not with the ask** - the bridge from "you went dark" to "can we talk" requires new context
- **If they did reply previously, reference WHAT they said** - proves you have continuity, not just a CRM reminder

---

## What to Avoid

| ❌ Don't say | ✅ Why |
|---|---|
| "Just checking in" | Most-burned phrase, signals automation |
| "Following up on my last message" | Confirms automation, shames them |
| "Did you get a chance to think about my proposal?" | Pressuring, obligation-based |
| "Bumping this to the top of your inbox" | Email language, looks templated in DM |
| "I noticed you didn't reply to my last message" | Guilt-tripping, instant-block tier |
| "Was the timing wrong before?" | Begging, low-status framing |

---

## Full Examples

### Example 1 - Connected 4 months ago, never replied (Ramp Re-Engagement)

**Context:** VP Sales at a Series B SaaS, accepted connection 4 months ago after a brief connection note about "building peer network." No DM was ever sent. New angle now exists: their company just posted Q4 results with growth concerns.

```
Different angle from where we left off - [industry] is going into Q1 with most VPs 
re-baselining the year, especially after Q4 numbers came in below the original plan.

The pattern we're seeing: rep capacity is fine, pipeline math isn't, and the fix is 
usually 2 quarters slower than the board wants.

[Company]'s Q4 release made me think you might be navigating exactly this.

Worth comparing notes if it's on your plate?
```

---

### Example 2 - Demo'd 6 months ago, lost the deal (Closed-Lost Reactivation)

**Context:** Director of Demand Gen, demo'd 6 months ago, said "we don't have budget right now and our existing tool is fine." Since then: budget cycle has reset (Q1), and a comparable company switched and got 3x results.

```
Quick re-engage - when we talked in [month], the blocker was budget timing and that 
your existing setup was working "well enough."

Since then [comparable company]'s demand gen team made the switch and tripled their 
SQL volume in 90 days - happy to share the breakdown if useful.

Q1 budgets are usually live by now - worth another look, or did you end up going 
in a different direction?
```

---

### Example 3 - Booked a meeting, no-showed, never rescheduled (No-Oriented)

**Context:** Manager-level prospect booked a 15-min intro call, no-showed, and stopped replying 3 months ago.

```
Realize we never got the call rescheduled after [month] - life gets in the way, 
no offense taken.

A couple of things have shifted on our side since (most relevant: [specific new 
thing they would care about given their role]).

Would it be unreasonable to put 15 minutes back on the calendar?
```

---

### Example 4 - Connected and exchanged 1-2 DMs months ago (Soft Reactivation)

**Context:** Had a brief exchange - 2 DMs deep - about a relevant topic, then they stopped replying mid-conversation 5 months ago.

```
Came back to our exchange from [month] on [specific topic they mentioned].

The [topic] landscape has changed in a way that makes that conversation more relevant 
now than it was then - [specific change with one detail].

If [topic] is still on your radar, happy to share what we've learned since. If not, 
no follow-up needed.
```

The "no follow-up needed" line is critical - it gives them permission to opt out without ghosting, which paradoxically increases reply rate.

---

## Cadence Rules

| Last contact | Re-engagement window |
|---|---|
| Connection accepted, never replied | 90 days minimum |
| One-way DM, no reply | 60-90 days |
| Brief reply exchange, then dark | 90-120 days |
| Booked meeting, no-show | 60 days |
| Closed-lost deal | 6-12 months (or when something material changes) |

After ONE re-engagement attempt with no reply: stop. Wait another 6+ months before trying again, with a completely different angle. Aggressive re-engagement on LinkedIn destroys both the connection and the sender's account standing.

---

## Weekly Re-Engagement Review (Operations)

Re-engagement is a manual-judgment task - it doesn't scale through automation, and it shouldn't. The right operating cadence is a 30-minute weekly review, capped at 10-15 prospects per week. Scarcity forces prioritization.

### The 4-step weekly workflow

1. **Filter for unanswered threads (≈5 min).** Open the unified inbox (HeyReach Unibox or equivalent). Filter for conversations where you sent the last message and there's been no reply for 7+ days.
2. **Cut the list to the 10-15 highest-value prospects (≈5-10 min).** Use the follow-up priority rule: strong ICP fit, real buying authority, strategic logo value, prior engagement signals. Everyone else gets handled by automation rules (tagged and excluded) - not weekly review.
3. **Quick signal check on each (≈10 min).** Have they posted recently? Engaged with your company's content? Changed roles? If yes → contextual re-engagement. If no → tag and pause.
4. **Decide, tag, move on (≈5-10 min).** For each thread, pick one of three actions: send one contextual DM, tag as "Active - No Reply" and exclude, or tag as "Stalled - Stop" and exit.

That's the whole loop. The point is structural restraint, not productivity.

### The Follow-up Priority Rule

| Prospect tier | Effort allocation |
|---|---|
| **High-value** (strategic logos, decision-makers, strong fit + prior engagement) | Manual review and tailored re-engagement DMs. The upside justifies the time. |
| **Medium-value** (solid ICP fit, no strong signals yet) | Structured automation only. 2-3 sequence steps, then exclude. If they engage, they move up. |
| **Low-value** (weak ICP, no authority, no engagement) | Exit early. Withdraw stale connection requests, add to LinkedIn exclude lists, don't recycle into new campaigns. |

The fastest way to lift overall reply rates is removing low-value threads from the queue - not adding more touches to high-value ones.

Source: HeyReach's "Follow-up Priority Rule." See `resources/heyreach-knowledge-base.md`.

---

## Combines With

- **dm-sequence** - for the initial M1+M2 sequence after a re-engagement reply lands
- **personalization** - to find the new signal that justifies re-engagement
- **rented-engine** - for account-safety considerations when re-engaging dormant lists at scale

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
