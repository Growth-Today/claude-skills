---
name: gtm-skill-3-signal-library
description: "GTM Onboarding Skill 3 — Signal Library and Combo Plays. Generates Tab 6 (Signal Library, 25+ signals across 7 categories) and Tab 7 (Signal Combo Plays, 5-8 plays). Run after Skill 2 is confirmed. Requires web_search for G2 competitor research."
---

# Skill 3 — Signal Library + Combo Plays

**Generates:** Tab 6 (Signal Library) + Tab 7 (Signal Combo Plays)  
**Input:** Skill 1 output (competitors) + Skill 2 output (winning segment + pain language)  
**Requires:** web_search for G2 competitor research (mandatory)  
**Next step:** Skill 4 (Battlecard) — only after you confirm Tab 6 + Tab 7

---

## CORE FRAMEWORK — Signal Performance Benchmarks

Before generating any signal, internalize these benchmarks. Every signal must be worth including.

| Outreach type | Reply rate | Contract value |
|---|---|---|
| Cold outreach (no signal) | 6–8% | Baseline |
| Single signal-based | 18–22% | 2–3x baseline |
| Multi-signal stacked (3+) | 35–40% | 3–4x baseline |
| Signal + ABM multi-touch | 36% meeting rate | Highest |

**3+ signals = always worth immediate outreach. Speed is the #1 lever — 50% of signal value is lost after 7 days.**

---

## SIGNAL SCORING FRAMEWORK

Every signal in Tab 6 gets a score and tier. Use these to populate the Priority column.

### Tier 1 — Hot (50–100 points) → Priority 1, launch first
| Signal type | Points | SLA |
|---|---|---|
| Demo / pricing page request | 100 | < 1 hour |
| 3+ pricing page visits in 7 days | 80 | < 1 hour |
| Champion job change to target account | 75 | < 24h |
| Multiple stakeholders from same account | 70 | < 24h |
| G2 comparison with competitor | 60 | < 24h |
| 5+ website visits in 2 weeks | 50 | < 24h |

### Tier 2 — Warm (20–49 points) → Priority 2, second wave
| Signal type | Points | SLA |
|---|---|---|
| Series A/B/C funding | 45 | < 24h (weeks 2–4 after) |
| Relevant job posting | 40 | < 24h |
| Bombora topic surge (70+) | 40 | < 24h |
| Case study download | 35 | < 24h |
| Competitor bad G2 review (identifiable) | 50 | < 24h |
| LinkedIn engagement with your content | 30 | < 72h |

### Tier 3 — Cool (5–19 points) → Priority 3, pipeline building
| Signal type | Points | SLA |
|---|---|---|
| Company expansion / new location | 15 | This week |
| Single website visit | 10 | This week |
| Social follow (no engagement) | 5 | Monitor |

**Recency multipliers — always apply:**
- Last 24 hours: 1.5x
- Last 7 days: 1.2x
- Last 14 days: 1.0x
- Last 30 days: 0.7x
- 30+ days: 0.3x

---

## OUTREACH CATEGORY PER SIGNAL

Every signal maps to one of the 4 outreach categories. This determines messaging type and personalization level.

| Category | Definition | Messaging |
|---|---|---|
| **Inbound** | Prospect knows you, took action on your property (pricing page, demo request) | 1:Many, low personalization — they came to you |
| **Postbound** | Prospect knows you, engaged with your content without buying intent | 1:Many + 1:1, medium personalization |
| **Bridgebound** | Prospect action NOT related to your marketing (job change, funding, hiring, competitor signal) | Signal-based personalization — most Tab 6 signals are here |
| **Outbound** | No signal, cold selection | 1:1 only, full personalization |

**Most Tab 6 signals are Bridgebound.** Inbound signals (website visitors, demo requests) go in the INBOUND category and get the fastest SLA.

---

## STEP 1 — Identify the Primary Buying Trigger

Before generating any signal, identify the ONE condition that most reliably precedes a purchase decision for your company. State it explicitly.

```
PRIMARY BUYING TRIGGER: [description]
Why: [causal chain — what changed in the prospect's world that made them start looking]
```

Examples by product type:
- Research tool: researcher headcount dropped but research demand didn't
- Mobile app builder: brand raised Series A and needs app before peak season
- Sales tool: SDR team doubled but reply rates dropped
- Compliance tool: missed an audit, need to fix before next one

This trigger becomes Priority 1 in Tab 6.

---

## STEP 2 — Competitor G2 Research (mandatory, run before writing any signals)

For every competitor in Skill 1's list, run these searches. The complaints become the Competitive signal category and feed Tab 9 (Battlecard).

```
Search: "[competitor name] site:g2.com reviews cons"
Extract: top 3 complaints in exact user language

Search: "[competitor name] problems reddit"
Extract: real frustrations — what users say when they think no one from the company is listening
```

After searching all competitors, write a competitor research summary:
```
[Competitor]:
  Top complaint (G2): [exact language]
  Reddit frustration: [exact language]
  Displacement angle: [1 sentence — what to say instead]
  Outreach timing window: [when their contract likely renews]
```

This feeds both Tab 6 (Competitive signals) and Tab 9 (Battlecard).

---

## STEP 3 — Signal Quality Check

Before including any signal, verify all 7 criteria. Signals that fail any criterion get cut or rewritten.

```
1. PRECISION     — pinpoints a distinct condition, not vague fit
   BAD:  "fast-growing company"
   GOOD: "1 UX researcher for 75+ employees, ratio below 1:75"

2. CAUSAL CHAIN  — direct link from signal → condition → pain → product solves it
   Must state: "Signal X → indicates Y → which causes pain Z → product solves by W"

3. TEMPORAL      — signals present or imminent need, not general fit
   "Just raised Series A" beats "Series A company"

4. DETECTABILITY — Clay can find this with a specific tool and filter
   If you cannot name the exact workflow → signal not ready

5. ACTIONABILITY — gives the AE/SDR something specific to say
   The opening line must reference this exact signal

6. PREDICTIVE    — causal reason this correlates with conversion (not just coincidence)

7. DEFENSIBLE    — hard for competitors to detect at the same time
   Earlier in buying journey = better
```

---

## STEP 4 — Generate Tab 6: Signal Library (minimum 25 signals, 7 categories)

Minimum 4 signals per category. Do not generate 3 and move on. Complete every category.

### Per signal, output all 10 fields:

```
Signal name:      [short, memorable, describes the condition exactly]
Category:         [one of 7 categories below]
Outreach type:    [Inbound / Postbound / Bridgebound / Outbound]
Score:            [points from framework above]
Priority:         [1 = launch first / 2 = second wave / 3 = pipeline]
Why intent:       [causal chain — signal → condition → pain → product solves]
                  Format: "[Signal X] → indicates [condition Y] → which causes [pain Z] → product solves by [W]"
                  Max 3 sentences. Must include transcript evidence if available.
Clay detection:   [exact tool + exact filter + exact field name or Claygent prompt]
Monthly volume:   [range] [AI EST]
Opening line:     [references this signal directly, MAX 8 WORDS, sounds like a real person]
Poke the Bear:    [forces prospect to confront implied pain — "How are you currently...?" or "What happens when...?"]
Your Priority:  [LEAVE BLANK — you fill 1/2/3 on team review session]
```

**Opening line rules — strictly enforced:**
- **MAX 12 WORDS.** This is a hard limit. The opening line is a signal reference, not an email.
- It must make the prospect think "how do they know that?" — not read like a template.
- Never says "I noticed" or "I saw that" as the first words — too common.
- Test: could this opening line apply to any company in the ICP? If yes → rewrite it.

**Good examples (≤12 words, Dialogue V3 standard):**
```
"Looks like [Company] is on Gorgias."                              (6 words)
"Congrats on the new role at [Company]."                           (7 words)
"Noticed your team is [X] people with no dedicated researcher."    (9 words)
"Your [Role] job post mentions running user research as a core responsibility." (11 words)
"Saw [Company] is expanding into [Market]."                        (6 words)
```

**Bad examples (too long — these are email drafts, not opening lines):**
```
"[Company] has [N] monthly App Store searches — with no app, competitors are capturing every one of those installs right now."
→ This is a message. The opening line is just: "[Company] has [N] App Store searches with no app."

"[Company] is already investing heavily in direct channels — curious if mobile is next."
→ Too long. Correct: "You're investing in Klaviyo and Attentive — is mobile next?"
```

**The test:** Read it out loud in 3 seconds or less. If it takes longer, it's too long.

**Poke the Bear rules:**
- Must be impossible to dismiss without thinking
- Format: "How are you currently handling X?" or "What happens when Y?"
- The question must create mild discomfort — they know the answer is bad

---

### CATEGORY HEADER FORMAT (mandatory for Tab 6 in Excel)

Every category section in Tab 6 gets a section header row in this format:
```
[CATEGORY NAME IN CAPS]  |  [One-line description of why this category matters]
```

Examples from gold standard:
```
TALENT & ORG SIGNALS  |  Hiring and org structure reveals pain before the company admits it
JOB POST SIGNALS  |  Pain in writing. The most underused signal category.
TECH STACK SIGNALS  |  What they have tells you what's missing
FUNDING SIGNALS  |  Fresh capital creates urgency. Outreach window: weeks 2-4 after announcement.
COMPETITIVE SIGNALS  |  Active frustration = highest purchase intent that exists.
STRATEGIC SIGNALS  |  Company-level events that create new buying needs.
INBOUND SIGNALS  |  Self-identified intent. Respond within 24 hours. FASTEST SLA IN THE LIBRARY.
```

The description after the pipe is not optional — it tells the AE/SDR WHY to care about this category at a glance.

---

### CATEGORY 1 — TALENT & ORG SIGNALS

Hiring and org structure reveals pain before the company admits it. Most underused category.

**What to look for:**
- Ratio of relevant staff to total headcount (the imbalance signal)
- Missing roles that create the problem this product solves
- New hires that open a 60-day evaluation window (days 14–45 peak)
- Departures that increase urgency and free up budget
- Job posts where JD language reveals the pain directly

**Clay detection methods:**
- LinkedIn headcount filter via Clay enrichment
- Job change API for new hires (track days-since-start, alert at day 14)
- Employee title count via Claygent: "Count employees with [title] at [company]"
- Claygent: "Does this company have a [title] role? Return yes/no + count"

**Signal scoring in this category:** New relevant leader hired = 75 pts (Tier 1). Relevant job post = 40 pts (Tier 2). Missing role = 40 pts (Tier 2). Leaving employee = 30 pts (Tier 2).

---

### CATEGORY 2 — JOB POST SIGNALS

Pain in writing. Job descriptions contain exact language about problems companies are trying to solve.

**What to look for:**
- Responsibilities that this product automates (the pain is literally written down)
- Required skills that indicate tool gaps
- Competitor tool named as a requirement — they're actively using it
- Seniority of the role (signals where they are in maturity curve)
- "Wear many hats" language = under-resourced team

**Clay detection methods:**
- Greenhouse, Lever, Ashby, LinkedIn Jobs via Clay scraper
- Claygent: "Does this job post at [company] mention [keyword]? Return yes/no + quote from JD"
- Job board APIs: search by keyword within job description text

---

### CATEGORY 3 — TECH STACK SIGNALS

What they have tells you what's missing and what to displace.

**What to look for:**
- Direct competitor in stack → displacement opportunity (Tier 2, 35–45 pts)
- Complementary tool → they invest in this category (buying intent)
- Survey-only or manual process → gap signal (very high priority)
- Tool combination that reveals the gap this product fills
- Stack change in last 90 days → switching momentum

**Clay detection methods:**
- BuiltWith, Datanyze, your CRM technographics via Clay enrichment
- Store Leads (ecommerce clients) — Shopify tier, app stack, GMV
- Claygent: "Does [company] use [tool] on their website? Return yes/no"
- Note: technographic data has 30–60 day lag — account for this in timing

---

### CATEGORY 4 — FUNDING SIGNALS

Fresh capital creates urgency and buying windows.

**Why funding works:**
- New budget available — board expects deployment
- Mandate for growth spending — investors want velocity  
- Scale pain emerges — what worked at Series A breaks at Series B
- Standardization moment — time to replace patchwork tools

**Timing framework (mandatory — do not outreach in week 1):**
- Week 1: Too early — they're celebrating, doing press. Monitor only.
- Weeks 2–4: PEAK WINDOW — planning spend, open to tools
- Weeks 5–8: Good — still allocating budget, hiring started
- Weeks 9+: Declining — budget likely committed already

**Scoring by round:** Seed/Pre-seed = 20 pts. Series A ($5–15M) = 35 pts. Series B ($15–50M) = 45 pts. Series C+ = 45 pts. IPO = 50 pts.

**Clay detection:** Crunchbase enrichment on ICP accounts, filter by round size, calculate weeks-since-announcement, route weeks 2–4 to SDR alert.

**Opening line rule:** Never lead with "I saw you raised money" — everyone does this. Reference the growth challenge the funding creates, not the funding itself.

---

### CATEGORY 5 — COMPETITIVE SIGNALS

Active frustration with a current tool = highest purchase intent signal that exists. The prospect has already identified their pain and is telling people about it.

**Signal scoring:**
- G2 comparison (your product vs competitor): 60 pts → < 24h SLA
- Churned competitor customer (bad review, identifiable): 50 pts → < 24h
- Competitor user visiting your website: 50 pts → < 1 hour
- In-cycle evaluation (actively comparing): 45 pts → < 24h
- Competitor contract renewal window (60–90 days before): 35 pts → This week
- Engaged with competitor LinkedIn content: 25 pts → < 72h

**Plays:**
- Bad review targeting: scrape G2/Capterra for negative reviews of competitors, match reviewers to LinkedIn profiles in Clay, reference their specific pain from the review
- Competitor LinkedIn followers: scrape followers via Clay/Phantombuster, filter to ICP, position your differentiator
- Renewal timing: track original BuiltWith detection date, flag accounts approaching 10–12 months

**Key rule:** Do NOT trash-talk the competitor. Position as an alternative, not a replacement. Bad reviews are public data — ethical to reference.

**For this category, use the G2 research from Step 2 above.**

---

### CATEGORY 6 — STRATEGIC SIGNALS

Company-level events that create buying needs that didn't exist before.

**What to look for:**
- New product or major feature launch (feedback need spikes immediately after)
- International expansion (creates multi-language research problem)
- Rebrand (always requires user validation)
- Appearance on growth/industry lists (curated high-fit audience)
- Blog post or conference talk about the exact problem this product solves → Bucket 1 personalization

**Clay detection:**
- PR Newswire RSS via Claygent
- Product Hunt launch monitoring
- LinkedIn company page monitoring
- Conference speaker lists via Claygent
- Claygent: "Did [company] announce a new product or market expansion in the last 90 days?"

---

### CATEGORY 7 — INBOUND SIGNALS

Someone from a target account showing intent on your own properties. **Priority response: < 24 hours. These are the hottest signals.**

**Signal scoring:**
- Pricing or demo page visited: 80–100 pts → < 1 hour
- Competitor comparison page visited: 60 pts → < 1 hour
- 5+ website visits in 2 weeks: 50 pts → < 24h
- Webinar attended: 25 pts → < 24h
- Content downloaded: 35 pts → < 24h
- LinkedIn ad engagement from ICP: 30 pts → < 72h

**Clay detection:**
- RB2B or Clearbit Reveal for website deanonymization → company name, employee data
- HubSpot reverse IP tracking
- LinkedIn Insight Tag
- Trigify for LinkedIn engagement tracking ($69–549/mo)
- Koala: product + website signal scoring (Free/$750/mo)
- Common Room: 50+ signal sources ($1K+/mo)

**Key rule:** Do NOT reference the exact signal ("I saw you visited our pricing page"). Reference the topic interest or the problem it implies.

---

## STEP 4b — NEW SIGNALS FROM TRANSCRIPT (v3+ only)

After generating the standard 7 categories, check the transcript for signals that weren't in your intake notes / positioning materials. These are often the most valuable signals because your company surfaced them from real deal experience.

**What to scan for:**
- Any buying trigger your company mentioned that isn't covered in the library
- Any timing signal ("companies come to us before BFCM", "after a platform migration")
- Any behaviour signal ("when they're hiring an extra CX person", "when they migrate CRM")
- Any competitor signal not already in the library

**For each new signal found, add a separate section at the bottom of Tab 6:**

```
NEW SIGNAL FROM CALL TRANSCRIPT | Not in your materials
[Timestamp reference if available — e.g. "Mehul [14:32]: '...'"]

[Signal name]:  [same 10-field format as above]
Source:         [TRANSCRIPT — [timestamp] — exact quote or paraphrase]
```

**Mark these rows with green fill** to distinguish them from your materials-derived signals.

**This section feeds the TRANSCRIPT MISMATCHES tab** — any new signal here should also appear as a NEW SIGNAL row in the mismatches tab.

---

## STEP 5 — Generate Tab 7: Signal Combo Plays (5–8 plays)

Signals from DIFFERENT categories combined = stronger intent than same-category stacking.

**Multi-signal performance:**
- 1 signal = Standard priority (18–22% reply rate)
- 2 signals = High priority (25–30% reply rate)
- 3+ signals = Reach out same day (35–40% reply rate)

**Clay scoring logic:**
- 1 point per signal present (or use the points framework for more precision)
- Score 2 = medium priority → automated sequence
- Score 3+ = top priority → trigger same-day manual outreach

**Per play, output all fields:**

```
Play name:    [describes the prospect archetype, not the signals — e.g. "The Overwhelmed Solo Researcher"]
Priority:     [1 = launch first / 2 / 3]
Category mix: [which signal categories are combined — e.g. Talent + Tech Stack + Funding]
Signal 1:     [exact name from Tab 6]
Signal 2:     [exact name from Tab 6]
Signal 3:     [optional — exact name from Tab 6]
Score:        [combined points]
Heat:         [Red Hot / Hot / Warm based on score + recency]
Why combo:    [why these together > sum of parts — causal reasoning]
Opening line: [references ALL detected signals naturally, max 25 words, impossible to ignore]
Volume:       [AI EST — monthly range]
Reply rate:   [AI EST — based on tier]
SLA:          [< 1h / < 24h / < 72h / This week]
Owner:        [AE / SDR / Automated]
Clay impl:    [how to build this as a scoring table in Clay]
```

**Opening line quality test:**  
Read it out loud. Does it sound like something a real person would send? Does it reference something specific they would recognize? If it could apply to any company in the ICP → rewrite it.

**No full email bodies in Tab 7.** Opening line only. Full sequence copy goes in a separate deliverable.

---

## STEP 6 — Pause and Present to you

```
✅ Skill 3 complete — [YourCompany]

Signal Library: [N] signals across 7 categories
- Talent/Org:      [N] signals — top signal: [name]
- Job Post:        [N] signals — top signal: [name]
- Tech Stack:      [N] signals — top signal: [name]
- Funding:         [N] signals
- Competitive:     [N] signals — G2 research run on: [competitor list]
- Strategic:       [N] signals
- Inbound:         [N] signals

Combo Plays: [N] plays
Priority 1 plays (launch these first):
1. [Play name] — Score: [X] pts — Reply rate est: [X]% — [signals combined]
2. [Play name] — Score: [X] pts — Reply rate est: [X]%
3. [Play name] — Score: [X] pts — Reply rate est: [X]%

Outreach category breakdown:
- Inbound signals: [N] — fastest SLA, highest intent
- Bridgebound signals: [N] — signal-based, bulk of the library
- Postbound signals: [N]

G2 competitor research summary:
[per competitor: top complaint + displacement angle]

Please review:
1. Are the Priority 1 signals the right ones to launch first?
2. Does the Clay detection method make sense for your current setup?
3. Any signals too expensive or slow to detect with your current tools?
4. Any obvious signals we missed for your specific market?

Type "Tab 6+7 OK" to proceed to Tab 9 (Battlecard)
Or give corrections first.
```

---

## WHAT TO PASS TO SKILL 4

```
SKILL 3 OUTPUT:
Priority 1 signals: [list with scores]
Competitor signals found: [list with G2 complaint themes + displacement angles]
Tech stack signals: [list with displacement angles]
Full competitor list confirmed: [yes/no — any new ones found in G2 research?]
Top combo plays: [names + signal combinations + scores]
Outreach categories per signal: [Inbound/Bridgebound breakdown]
G2 research summary per competitor: [paste full summary from Step 2]
```


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
