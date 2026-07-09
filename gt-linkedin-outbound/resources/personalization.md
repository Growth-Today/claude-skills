---
name: personalization
description: Builds LinkedIn personalization strategies and AI prompts for outreach at scale. Use when the user asks about "personalize LinkedIn at scale", "LinkedIn first lines", "AI personalization for LinkedIn", "Clay prompts for LinkedIn", "LinkedIn profile signals", "post-based hook", "engagement signals", "data enrichment for LinkedIn", or needs to make DMs feel 1-to-1 at volume. Triggers on "first line generation LinkedIn", "personalization buckets LinkedIn", "strong hook", "lite hook", "Clay LinkedIn enrichment". Do NOT use for writing full DM sequences (use dm-sequence), connection notes (use connection-notes), or rented engine setup (use rented-engine).
---

# LinkedIn Personalization at Scale

You build personalization strategies that make LinkedIn DMs and connection notes feel 1-to-1 even at volume of hundreds-thousands of prospects per week. LinkedIn's signal density is exponentially higher than email - every prospect has a profile, and most have recent activity.

## Why LinkedIn Personalization Works Differently from Email

On email, personalization is hard because you're working from third-party data (firmographic, news, scraped). On LinkedIn, the prospect has hand-crafted their own signal:

| Signal source | Email available? | LinkedIn available? |
|---|---|---|
| Recent self-authored content (posts) | Rarely | Almost always - and FRESH |
| Engagement activity (what they liked/commented) | No | Yes |
| Self-identified traits (headline, About) | Indirect | Direct |
| Career trajectory | Sometimes via enrichment | Native |
| Mutual connections | No | Yes |

The implication: **on LinkedIn, you almost always have access to a real signal.** If your team is sending generic LinkedIn outbound, that's a process failure, not a data limitation.

## Process

1. **Audit available signals** - What does the prospect's profile expose? Posts, engagement, trajectory, headline?
2. **Pick personalization tier** - Strong hook (verbatim quote/reference) or Lite hook (conceptual reference)?
3. **Build the prompt or strategy** - Clay AI prompt, hook templates, or manual research framework
4. **Choose touchpoint** - Personalize the connection note, M1, both, or neither?

## The "Two Hooks Per Prospect" Rule

Before any prospect enters a campaign, they should have **at least two personalization hooks** captured in the enrichment row:

1. **A timely signal** - something happening right now: a recent post, a job change, a hiring round, a funding event, content they engaged with this month
2. **A homework detail** - something that proves you didn't just paste a templated mail-merge: their thesis from a podcast, a position they took in a comment thread, a side project, a stage of company growth

One hook is enough for an opener; the second hook is what carries the conversation past the first reply. Campaigns that ship with one-hook rows look like good outreach for one message and obvious spam by message two.

If the enrichment can't produce two hooks for a prospect, the right move is usually to drop them from the list rather than send a one-hook message. Volume from low-signal rows drags down the segment-level numbers and burns connections that could have been re-engaged later with better context.

Source: HeyReach's two-hook rule. See `resources/heyreach-knowledge-base.md`.

## The 6 Data Buckets (Ranked by Value)

Same buckets as email, but **the rank order shifts on LinkedIn:**

| Rank | Bucket | LinkedIn-specific notes |
|---|---|---|
| **1** | **Self-Authored Content** (posts, articles, comments they wrote) | Goldmine - the prospect handed you the hook |
| **2** | **Engaged Content** (what they liked, commented, shared) | Reveals what they care about, often more honest than what they post |
| **3** | **Self-Identified Traits** (headline, About, current role description) | Cheaper to scrape, lower performance - but a fallback |
| **4** | **Background Centric** (tenure, career trajectory, certifications, awards) | Useful for ATL personas - strategic identity |
| **5** | **Junk Drawer** (volunteer work, schools, languages, interests) | Lowest performance - often feels stalker-ish if used |
| **6** | **Company Level** (funding, hiring, M&A, news) | Strong for ATL, weaker than personal signals on LinkedIn |

## Hook Types

### Strong Hook (Verbatim Tie)

Direct quote or specific reference from their content.

**Pattern:**
```
Saw your post on [topic] - specifically your point about [exact claim].
[One-sentence genuine reaction].
```

**Why strong:** Proves you actually read it. Hard to fake. High signal of real human attention.

---

### Lite Hook (Conceptual Tie)

Reference the theme without quoting verbatim.

**Pattern:**
```
[Your industry] / [their company stage] usually surfaces [problem] - saw [Company] 
might be sitting in that exact phase.
```

**Why useful:** Easier to generate at scale via AI. Still feels relevant. Performance: ~70% of a strong hook.

---

### No Hook (Tension-Based)

When no signal exists, lead with shared context - what the prospect's role/seniority/industry typically experiences.

**Pattern:**
```
Most [role]s at [company stage] are dealing with [specific tension] right now.
```

**Why it still works:** Generic-feeling but at least relevant. Outperforms fake personalization (which is worse than no personalization).

---

## Touchpoint Strategy: Where to Personalize

You have limited personalization budget per prospect (manual research time + AI compute). Spend it where it earns the most.

| Touchpoint | Personalization ROI |
|---|---|
| Connection note (300 char) | HIGH - limited space forces specificity, biggest acceptance lift |
| M1 (post-acceptance) | HIGH - first DM = highest reply rate impact |
| M2A (reply continuation) | MEDIUM - they've already engaged; relevance > personalization here |
| M2B (no-reply bump) | MEDIUM - new angle matters more than personal hook |

**Rule:** If you can only personalize one touchpoint, personalize M1. The connection note benefits more from being short and signal-based, but M1 carries the conversational weight.

---

## AI Prompt Templates (Clay / Claygent)

### Prompt 1 - Recent Post Hook (Bucket 1)

```
Find the most recent post by {{firstName}} {{lastName}} at {{company}} on LinkedIn.

Extract:
- The main argument of the post (one sentence)
- The most distinctive claim or framing they used (one phrase)
- The general topic category (one tag)

Output a hook in this exact format:
"Saw your post on [topic] - specifically your point about [distinctive claim]. 
[One-sentence genuine reaction connecting to a related challenge in their world]."

Rules:
- Maximum 30 words
- No generic compliments ("great post", "loved this")
- Reference a specific claim they made - not the post topic generically
- Reaction must extend the thought, not flatter it

If no post is found in the last 60 days, output: "NO_RECENT_POST"
```

---

### Prompt 2 - Engagement Hook (Bucket 2)

```
Find a comment {{firstName}} {{lastName}} left on someone else's LinkedIn post in the 
last 30 days that relates to [TOPIC RELATED TO YOUR VALUE PROP].

Extract the gist of their comment (one sentence) and the post they were commenting on.

Output a hook:
"Saw your comment on [original post topic] - your take on [their comment gist] 
maps closely to what we see at [their type of company]."

Rules:
- Maximum 30 words
- Must reference the comment, not just the post they commented on
- Avoid creepy phrasing - "saw your comment" is fine; "I've been following all your activity" is not

If no relevant comment found, output: "NO_RELEVANT_ENGAGEMENT"
```

---

### Prompt 3 - Job Change Hook (Bucket 4)

```
Determine when {{firstName}} {{lastName}} started their current role at {{company}} 
based on LinkedIn experience section.

If less than 6 months ago, output a hook:
"Saw the move to {{company}} [X months] in - that transition usually means 
[specific challenge for their role and stage]. Following along."

Specific challenges by role:
- Sales leader: inheriting a forecast methodology that doesn't match the new comp plan
- Marketing leader: defending campaigns from the previous era while building new bets
- RevOps leader: 3 tools that don't talk to each other
- CTO: deciding whether to refactor or patch the current architecture
- People/HR leader: fixing comp benchmarks before the next hiring round

If start date is more than 6 months ago, output: "NOT_RECENT_HIRE"
```

---

### Prompt 4 - Two-Word Hook for the Subject of Their Post

```
Read {{firstName}}'s most recent post.

Identify the core noun-phrase the post is built around (the subject they're advocating for, 
warning about, or reframing).

Output that noun-phrase in 2-4 words, lowercase, suitable as a connection-note hook 
or DM opener prefix.

Examples: "the SDR efficiency myth", "Q1 forecast accuracy", "the build-vs-buy reset", 
"customer onboarding gravity"

Rules:
- 2-4 words only
- Lowercase
- Must come from the post itself, not invented
- No generic terms ("growth strategy", "modern marketing")
```

---

## Personalization Anti-Patterns

| ❌ Don't | ✅ Why |
|---|---|
| "I love your background!" | Generic, signals batch-and-blast |
| Quote their About section verbatim | Creepy, signals scraping |
| "I saw you went to [University]" | Junk Drawer - usually feels off-topic in B2B |
| "I noticed you've been at [Company] for [X] years" | Feels like a CRM enrichment, not a real observation |
| "I came across your profile and was impressed" | Burned phrase, instant decline |
| Reference a post that's >90 days old | Stale signal - reads as "I just searched your activity feed" |
| AI-paraphrase their post and feed it back | Detectable, condescending |

---

## Personalization Pitfalls Specific to LinkedIn

### The "Liked Your Post" Trap

If the only signal is that they liked someone else's post (not commented), the hook is usually too thin. A like is too low-friction to base outreach on. Use ONLY when:
- They liked something very specific to your value prop
- And the like is recent (<30 days)
- And no stronger signal exists

Otherwise, default to a tension-based opener instead.

### The Recycled Headline Hook

Quoting their headline back at them - "I see you help SaaS teams hit revenue targets" - feels generic because it IS generic. They wrote that for thousands of profile viewers. Use Buckets 1-2 instead whenever possible.

### The Stale Post Reference

Posts older than 60-90 days are "stale" signals. Referencing them tells the prospect "I dug back into your history to find something to say" - which feels invasive rather than attentive. Stay current.

---

## Fallback: When No Personal Signal Exists

If no posts, no engagement, no recent role change → don't fake it. Use **core-static relevance** instead:

| Fallback | Example |
|---|---|
| Demographic (buyer persona) | "Most VPs of Sales at [stage] are navigating..." |
| Firmographic (company segment) | "Series B SaaS companies usually hit a forecasting ceiling around..." |
| Firmographic (industry vertical) | "Healthtech go-to-market is dealing with [regulatory shift]..." |
| Firmographic (geo) | "European GTM teams are 6 months ahead of US peers on [trend]..." |
| Technographic (stack) | "Teams running [tool stack] usually struggle with [specific friction]..." |

A well-targeted tension-based opener outperforms a poorly-personalized one.

---

## Personalization at Scale: The Workflow

For campaigns of 500+ prospects:

```
1. Pull list (Sales Nav search → enrichment → Clay)
2. Run Clay enrichment to grab:
   - Most recent post (if any)
   - Most recent meaningful comment (if any)
   - Role start date (for job change signals)
   - Company funding/hiring signals (if applicable)
3. Bucket prospects by signal strength:
   - Tier A: strong signal (recent post or comment) → personalized M1 with strong hook
   - Tier B: medium signal (recent role change OR company trigger) → personalized M1 with lite hook
   - Tier C: no signal → tension-based M1 (no fake personalization)
4. Run AI prompt per tier to generate hooks
5. Manual spot-check 5% of generated hooks before sending
6. Send via HeyReach / Expandi / Lemlist
```

Manual review is non-optional. A poorly-generated hook ("Saw your post about pipelines - interesting take!") is worse than no hook.

---

## Examples

### Example 1 - Strong Hook (Bucket 1)

**Signal:** Prospect (VP RevOps) posted last week: "Most forecast accuracy issues aren't measurement problems, they're definition problems. Until your sales and marketing teams agree what 'qualified pipeline' means, every dashboard lies."

**Generated hook (M1):**
```
Saw your post on the qualified-pipeline definition gap - specifically your point that 
measurement is downstream of definition. Most teams I see solve the dashboard before 
they solve the definition, then wonder why the next quarter looks the same.

How are you tackling the alignment piece at [Company]?
```

---

### Example 2 - Lite Hook (Bucket 6 + Persona)

**Signal:** No recent posts. Company just announced Series B in last 30 days. Prospect is Head of Demand Gen.

**Generated hook (M1):**
```
Noticed [Company] just closed [round] - congrats. Most Heads of Demand Gen post-Series-B 
hit the same wall: the playbook that worked at seed doesn't scale, and the board's 
expectations move faster than the team's capacity to rebuild.

How are you staging the rebuild?
```

---

### Example 3 - No Hook (Tension-Based)

**Signal:** Prospect has no recent activity. Manager-level. No company triggers visible.

**Generated hook (M1):**
```
Most Marketing Ops Managers at companies your size are spending 4-6 hours/week 
fighting Excel to build campaign reports - usually because the data lives in 3 
tools that don't agree.

Curious whether that's the picture at [Company] too?
```

---

## Combines With

- **connection-request** - for which signals justify a note
- **dm-sequence** - for where to deploy the personalization (M1 typically)
- **rented-engine** - for understanding which Clay enrichments to run for which sender personas
- **gt-clay** - for the actual Clay table buildout

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Built and maintained by [Nikola Siljanoski](https://www.linkedin.com/in/nikola-siljanoski/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
