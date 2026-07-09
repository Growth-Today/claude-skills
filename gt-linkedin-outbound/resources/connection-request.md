---
name: connection-request
description: Writes LinkedIn connection requests - the first cold touch. Use when the user asks to "write a connection request", "draft a connection note", "300 character note", "first LinkedIn touch", "should I send a note with my connection request", "no-note vs note", "connection invite copy", or needs the opening cold message on LinkedIn. Also triggers on "first DM", "initial LinkedIn message", "open the conversation". Do NOT use for follow-up DMs after acceptance (use dm-sequence), re-engaging old connections (use re-engagement), or InMail-only campaigns (use copywriting).
---

# Connection Request - First LinkedIn Touch

You write connection requests for B2B outbound on LinkedIn. The connection request is the equivalent of "knocking on the door" - the prospect sees your profile, your headline, and (optionally) a 300-character note. Acceptance is the gate to everything else.

## Core Decision: Note or No Note?

**Default: NO note** for cold outbound at scale.

Across most campaigns, no-note connection requests achieve **equal or higher** acceptance rates than noted ones - because:
- No note = the prospect evaluates your profile, not your pitch
- A weak note actively reduces acceptance (signals automation)
- Note-less requests bypass the "is this a salesperson" filter
- Industry data: noted requests average ~22% acceptance, no-note averages ~28-32%

**Send a note ONLY when:**
1. You have a strong, specific, verifiable signal (recent post, mutual event, job change <30 days)
2. You have a mutual connection worth name-dropping (with permission)
3. Your value prop is genuinely unusual and the prospect couldn't infer it from your headline
4. You're targeting a senior persona (VP+) where a note signals respect for their time

For everything else → just hit Connect.

For full reasoning and edge cases → see `{SKILL_BASE}/copywriting/examples/connection-notes.md`

## Process

1. **Confirm engine type** - Personal profile (founder-led, real human) or rented account (multi-account engine)? Tone differs.
2. **Confirm ICP & seniority** - Who's the target? ATL or BTL? Senior personas tolerate noted requests better; ICs tolerate no-note better.
3. **Identify the strongest signal** - Recent post? Job change? Hiring? Funding? Mutual? If yes → consider a noted request. If no → no-note.
4. **Pre-warm if possible** - Like or comment on their recent post 24-48 hours BEFORE sending the connection request. Lifts acceptance ~10-15 points.
5. **Optimize the sender's profile FIRST** - Headline, banner, about section, and recent posts on the sender's profile do more for acceptance than note copy. If the profile is generic, fix that before scaling.

## Reference

For full sub-skill flows:
- Connection note copywriting & no-note decision tree → `{SKILL_BASE}/copywriting/examples/connection-notes.md`
- Profile signal personalization (Clay, post-based hooks) → `{SKILL_BASE}/personalization/personalization.md`
- ATL connection request tone → `{SKILL_BASE}/copywriting/atl-messaging.md`
- BTL connection request tone → `{SKILL_BASE}/copywriting/btl-messaging.md`

## Sender Profile Checklist (Run BEFORE Sending Anything)

The sending profile is your "subject line" - it's what prospects evaluate when deciding to accept. Optimize this first or no copy will save you.

| Element | Standard |
|---|---|
| Profile photo | Real human, professional, no logos, no AI-generated |
| Banner | Either branded (matches their world) or simple - never a stock template |
| Headline | Outcome-focused: "Helping [ICP] do [outcome]" - not "Sales Director at [Company]" |
| About section | First 3 lines must hook - visible above the "see more" cut |
| Recent activity | At least 2-3 posts in the last 30 days, ideally on topics relevant to your ICP |
| Connections | 500+ minimum before scaling outbound (under 500 = "new account" red flag) |

## 300-Character Note Rules

If you decide to send a note:

- **Under 200 characters preferred** - short feels human, long feels automated
- **Reference one specific thing** - not their job title, something earned (a post, an event, a shared connection)
- **No pitch, no CTA, no calendar link** - the note is for getting connected, not selling
- **Never start with "Hi {{firstName}}, I came across your profile"** - burned phrase, instant decline
- **Never end with "Looking forward to connecting"** - generic, reduces acceptance
- **Use "you" / "your" - never "I" / "we"**
- **Read aloud test** - must sound like a peer, not a vendor

## 6 Allowed Connection Note Patterns

### 1. Recent Post Reference (strongest)
```
Saw your post on [topic] - [one-sentence genuine reaction]. 
Worth being connected.
```

### 2. Job Change Recognition
```
Saw the move to [company] - that transition usually means [specific challenge].
Following along.
```

### 3. Mutual Context (event, group, school)
```
We were both at [event] - didn't get to chat. 
Building out my [function] network in [industry].
```

### 4. Industry Peer
```
Building things in [industry] - your work at [company] is on my radar. 
Open to connecting?
```

### 5. Specific Hire / Team Signal
```
Saw [company] is scaling [team]. That phase is its own kind of chaos.
Worth being connected.
```

### 6. Curious Frame (when no signal exists - use sparingly)
```
Building a network of [role]s working through [common challenge].
You came up - open to connecting?
```

## What Connection Notes Must NEVER Do

- Pitch a product, tool, or service
- Mention your company name (gives away the sales motive)
- Include a calendar link or "Got 15 minutes?"
- Use any version of "I came across your profile"
- Reference the prospect's job title without context ("Saw you're a VP of Sales")
- Use emojis (🚀 ✨ 🎯 are instant declines on LinkedIn outbound)
- Quote the prospect's About section verbatim (creepy, signals scraping)

## ATL vs BTL Tone (Adjust by Seniority)

| Seniority | Tone | Example |
|---|---|---|
| **VP / C-Suite** | Peer-to-peer, brief, observation-led. Note recommended (signals respect). | "Your post on [strategic shift] - sharp framing. Worth being connected." |
| **Director** | Practitioner + strategic. Note optional. | "Saw [team scaling signal] at [company]. Following along." |
| **Manager** | Operational, casual, specific. No note often outperforms. | (No note) - let the profile do the work |
| **IC** | Casual, peer. No note almost always better. | (No note) |

## Examples

### Example 1 - VP Sales, recent post about pipeline visibility
**With note (300 chars):**
```
Your post on the gap between forecast accuracy and pipeline hygiene - sharp.
Most VPs I talk to either fix one or the other, never both. Worth being connected.
```

**No-note version:** Just send it. Headline + your last post on pipeline ops will do the work.

### Example 2 - Marketing Ops Manager, no specific signal
**Recommendation:** No note.
**Why:** Manager-level, no signal, generic note will reduce acceptance vs letting the sending profile speak for itself. If sender has good content on marketing ops in their feed, acceptance is higher.

### Example 3 - Founder of a Series A startup
**With note:**
```
Saw [Company] just raised - that phase usually means rebuilding GTM from scratch.
Building out my founder network around [function]. Open to connecting.
```

### Example 4 - Director of RevOps, hired 60 days ago
**With note:**
```
Saw the move to [Company] 2 months in. New RevOps role usually means inheriting 
3 tools that don't talk to each other. Following along - worth being connected.
```

## Anti-Patterns (Do Not Use)

```
❌ "Hi {{firstName}}, I came across your profile and wanted to connect."
❌ "Hi {{firstName}}, I'd love to add you to my professional network."
❌ "Hey {{firstName}}! 👋 Loved your work at {{company}} - would love to chat!"
❌ "Hi {{firstName}}, I help companies like {{company}} achieve [vague outcome]. Connect?"
❌ "Saw you're VP of Sales at {{company}} - open to a quick chat?"
```

Each of these averages <15% acceptance and trains the LinkedIn algorithm to treat your account as spam.

## Benchmark to Hit

| Stage | Target |
|---|---|
| Connection acceptance rate | 25-35% (good), 40%+ (great) |
| Time from accept → first DM | <2 hours (auto-trigger via HeyReach/Expandi or send manually) |
| Profile views before connect (paid sender behavior) | Helpful - visiting the profile 24-48h before requesting lifts acceptance |

## Engagement-First Warming (Highest-Lift Move)

Before sending the connection request:
1. **Day -2:** Visit the prospect's profile (they get a notification)
2. **Day -1:** Like one of their recent posts (genuine like, not on every post)
3. **Day -1:** Optionally comment something substantive on a post (not "Great post!")
4. **Day 0:** Send connection request (with or without note)

This sequence lifts acceptance by 10-15 points in most campaigns. It's the single highest-ROI tactic on this channel.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
