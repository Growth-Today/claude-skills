---
name: gtm-skill-2-icp-persona
description: "GTM Onboarding Skill 2 — ICP Hypothesis and Pain per Persona. Generates Tab 2 (ICP Hypothesis) and Tab 4 (Pain per Persona). Run after Skill 1 is confirmed. Requires your CRM customer data from Preparation P1-P2. Core goal: validate or challenge your hypothesis against actual customer data — not confirm it."
---

# Skill 2 — ICP Hypothesis + Pain per Persona

**Generates:** Tab 2 (ICP Hypothesis) + Tab 4 (Pain per Persona)  
**Input:** Skill 1 output + your CRM customer data (P1-P2) + optional cluster analysis  
**Requires:** Skill 1 confirmed by you  
**Next step:** Skill 3 (Signal Library) — only after you confirm Tab 2 + Tab 4

---

## CORE PRINCIPLE — Diagnose, Don't Confirm

You filled your intake notes / positioning materials with their best hypothesis. That hypothesis is often wrong.

Most teams describe their dream customer — the large enterprise they want.  
80% of their actual paying customers are often much smaller, or a different vertical entirely.

Our job is to find where your materials hypothesis **diverges from actual customer data** and surface that divergence before the team review session. This is the primary value of Skill 2.

**Never execute your stated hypothesis blindly. Always test it against data first.**

---

## INPUT REQUIRED

```
SKILL 1 OUTPUT:     [paste confirmed research summary from Skill 1]
YOUR MATERIALS:     [paste or "already in project"]
CUSTOMERS CSV:      [enriched from your CRM P2, or "not provided"]
CONTACTS CSV:       [if available, or "not provided"]
OPEN DEALS CSV:     [enriched from your CRM P2, or "not provided"]
CLOSED LOST CSV:    [enriched from your CRM P2, or "not provided"]
CLUSTER ANALYSIS:   [paste any clustering output, or "not provided"]
```

---

## WHAT EACH CSV TELLS US

**Current paying customers** — who actually pays vs who your company thinks pays. Mandatory minimum: Company Name + Domain. The patterns in this list are the real ICP.

**Contacts at customers** — job title of the person who actually bought. If your company says "VP Product is the champion" but every signed contract came from a UX Researcher, that changes everything about outbound persona targeting. Feeds Tab 3 (Buyer Journey) with real data.

**Open deals** — emerging segments your company hasn't noticed yet. A new vertical in open deals may signal an opportunity they're not pursuing.

**Closed lost / churned** — what distinguishes a won deal from a lost one tells us more than won deals alone. Consistent churn in a segment = do not target that segment in outbound.

**Cluster analysis** — if you have a clustering output (e.g. from Clay), use it as the primary cluster input. Reduces manual analysis time significantly.

---

## STEP 1 — Scale Check and Data Summary

Before any analysis, assess what was provided and state:

```
DATA SUMMARY:

Customers:  [N records] | Fields: [list] | your CRM-enriched: [yes/no]
Contacts:   [N records] | Fields: [list] | Job titles: [yes/no]
Open deals: [N records] | Fields: [list]
Lost/churn: [N records] | Fields: [list]
Cluster analysis: [provided yes/no] | [N records]

SCALE DECISION:
- Up to 200 companies     → analyze all records directly
- 200–500 companies       → stratified sample of 200
                            Method: 67 newest + 67 oldest + 66 random
                            Tell you: "Sampling 200 from [N]. Full list preserved for Clay."
- 500+ companies          → Claude cannot analyze raw CSV at this scale
                            Option A: Use cluster analysis output as primary input
                            Option B: Ask you to run Clay cluster analysis, paste output here
                            Tell you: "CSV too large. Need a cluster analysis output."

CONFIDENCE: [GOLD / SILVER / BRONZE]
- GOLD   = customers + contacts + deals + transcripts + CRM enriched + cluster analysis
- SILVER = customers + contacts + your CRM enriched
- BRONZE = customers only (not enriched) OR your intake notes / positioning materials only

DATA QUALITY NOTES:
[flag messy formatting, missing domains, encoding issues — proceed if Company Domain is present]
```

---

## STEP 2 — Identify the Messaging Dimensions

Every company is different. The number and type of dimensions that drive messaging structure must be derived from your intake notes / positioning materials, web research, and customer data — never assumed in advance.

### The core test for any dimension

Ask: if prospect A and B are identical except variable X, does the message need to completely change?
- YES → X is a messaging dimension. It gets its own column in Tab 4 and Tab 8.
- NO → X is a personalization variable. It changes the opening line or proof logo, but not the message structure.

### Segmentation vs personalization — the most important distinction

| Layer | What changes | How it works | Managed where |
|---|---|---|---|
| Segmentation dimension | S1 and S2 (core pain hook and consequence) | Different message structure — the prospect's situation is fundamentally different | Tab 4 rows + Tab 8 columns |
| Personalization variable | Opening line and proof logo only | Same message structure, customized at send time | Clay opening line + logo swap |

**The most common mistake:** treating industry as a segmentation dimension when it is actually a personalization variable. Industry usually changes the opening line and proof logo — not the core pain structure. But for some products, industry genuinely drives a different use case and different pain — in that case it belongs as a dimension.

### How to evaluate each candidate dimension

For each variable (industry, company size, researcher presence, funding stage, vertical, etc.), ask:
1. Do prospects in different states of this variable have genuinely different core pain? (Tab 4 test)
2. Would an AE send a structurally different email to each state? (Tab 8 test)
3. Is the difference detectable and actionable before sending? (Clay/signal test)

If all three are YES: it is a dimension. Add it as a column in Tab 4 and Tab 8.
If only #3 is YES: it is a personalization variable. Handle it in the Clay opening line layer.

### Common dimensions by product type

These are starting hypotheses — always validate against data:

| Product type | Common dimensions | Usually personalization only |
|---|---|---|
| Research tools | Persona, researcher presence, company size | Industry, funding stage |
| Sales tools | Persona, team size, CRM maturity | Industry, company stage |
| Ecommerce tools | Platform (Shopify vs custom), GMV tier | Industry vertical |
| HR / people tools | Company size, HR maturity, existing stack | Industry, geography |
| Vertical SaaS | Vertical IS the dimension (by definition) | Company size within vertical |

The number of dimensions varies by company. Some companies need 2 (persona x company size). Others need 4 (persona x researcher x size x vertical). Neither is wrong. More dimensions = more variants = more maintenance. Only add a dimension if it genuinely changes the message.

### State the dimensions explicitly before generating any tab

```
MESSAGING DIMENSIONS FOR [YOUR COMPANY]:
  Dimension 1: [name] — States: [list]
  Dimension 2: [name] — States: [list]
  Dimension 3: [name, if applicable] — States: [list]
  Dimension 4: [name, if applicable] — States: [list]

Evidence from data: [what CSV/your materials/web shows for each]
Your hypothesis (your materials): [what you assumed]
Match: [CONFIRMED / MISMATCH per dimension]

Tab 4 structure: [D1 states] x [D2 states] x [D3 if applicable] = [N rows]
Tab 8 structure: [same — N variants]

PERSONALIZATION VARIABLES (not dimensions):
  [variable]: changes [opening line / proof logo / CTA phrasing] — handled by Clay
```

**ICP Scoring framework** (from list-building define-icp — use to validate dimension priority):

| Criterion | Weight | What to look for in CSV |
|---|---|---|
| Industry match | 20 pts | Which verticals dominate paying customers? |
| Company size | 15 pts | Headcount sweet spot — floor AND ceiling |
| Revenue range | 15 pts | Revenue range in your CRM-enriched data |
| Geography | 10 pts | HQ location patterns |
| Technology fit | 15 pts | Tech stack from your CRM/BuiltWith |
| Growth signals | 10 pts | Funding stage at time of purchase |
| Intent signals | 15 pts | What triggered the purchase? |

---

## STEP 3 — Mismatch Analysis

For every case where customer data contradicts your materials hypothesis, flag it explicitly.  
This is the core value Skill 2 provides that your company cannot get themselves.

**Common mismatch patterns to look for:**
```
SIZE MISMATCH:    You assume enterprise, data shows SMB dominates
VERTICAL MISMATCH: You assume fintech, data shows ecommerce is 60% of revenue
PERSONA MISMATCH:  You assume VP Product champions, contacts show UX Researcher signs
STAGE MISMATCH:    You assume Series B+, but customers were Seed/A at time of purchase
DIMENSION MISMATCH: You assume vertical is the dimension, data shows researcher presence matters more
```

**For each mismatch, output:**
```
[MISMATCH]: [field name]
You assumed (your materials):  [X]
Data shows (CSV):     [Y]
Delta:                [quantify — "70% of customers are SMB vs your enterprise hypothesis"]
Implication:          [what this means for the GTM strategy]
Option A:             [pursue data reality — what this requires]
Option B:             [pursue stated hypothesis — what data is missing to validate it]
Raise on team review session: YES
```

---

## STEP 4 — Generate Tab 2: ICP Hypothesis

**Tab 2 = PRIMARY DIMENSION callout + firmographic + verticals + technographic + disqualifiers.**  
No signal detection logic here — that goes to Tab 6.

### PRIMARY DIMENSION section (MANDATORY — goes at the very top of Tab 2, before everything else)

This section makes the messaging architecture visible to your company. Without it, the rest of the playbook is hard to navigate.

Format:
```
PRIMARY DIMENSION  |  The ONE variable that changes the core message completely

[Dimension name] — [N] states: [list all states]
Why: [1–2 sentences explaining what is FUNDAMENTALLY DIFFERENT about each state.
     Why can't the same message work across all states?]
```

Example (Dialogue AI):
```
PRIMARY DIMENSION  |  The ONE variable that changes the core message completely

RESEARCHER PRESENCE — 3 states: No researcher / 1 researcher / 2+ researchers
Why: A PM with no researcher and a solo UXR at a 100-person company 
     have completely different daily pain, different buying triggers, and different 
     objections — even though they'd buy the same product.
```

**Always state the primary dimension BEFORE generating any other section of Tab 2.**

If Skill 2 Step 2 identified multiple dimensions, list the primary one here. Secondary dimensions go in Tab 8 (messaging matrix). Only one dimension goes in Tab 2.

---

### Writing rules for the Why column:

Write boundary logic, not benefits:
```
BAD:  "Small teams benefit most from our speed."
GOOD: "Below 50 rarely has budget. Above 500 usually has a full research team already."
```

### Firmographic section

Per segment, output:
```
Segment:         [Revenue / Headcount / Stage / Geography]
Our Hypothesis:  [specific range with floor AND ceiling]
Why:             [boundary logic — 1 sentence, no adjectives]
Fit Signal:      [observable, Clay-detectable characteristic]
Data says:       [what CSV shows — count + %]
You assume:     [what your materials say]
Flag:            [CONFIRMED / MISMATCH / AI EST — no data]
Your Rank:      [blank — fill 1-3 during team review]
Your Notes:     [blank]
```

### Verticals section

Per vertical, output:
```
Vertical:        [name]
Priority:        [High — ICP score /100 / Medium / Lower]
Why:             [strategic fit — 1 sentence]
Confirmed:       [N customers from CSV — or "0 [AI EST]" if no data]
Examples:        [confirmed names first, aspirational second]
Flag:            [CONFIRMED / AI EST / MISMATCH]
Your Rank:      [blank]
Your Notes:     [blank]
```

**ICP Scoring per vertical** (apply 100-point framework from list-building):
- Industry match (20) + company size (15) + revenue (15) + geo (10) + tech fit (15) + growth signals (10) + intent (15)
- Verticals scoring 80+ → High priority
- Verticals scoring 60-79 → Medium priority  
- Verticals scoring below 60 → Lower priority or exclude

### Technographic section

Good-fit signals in their tech stack — things Clay/BuiltWith can detect:
```
Signal:          [tool name or stack pattern]
What It Tells Us: [what this reveals about the prospect's situation]
How to Find It:  [BuiltWith / Clay / your CRM technographics]
Priority:        [Very High / High / Medium]
Your Confirm?:  [blank — yellow fill]
```

### Disqualifiers section

Explicit "do not target" criteria — companies that look like ICP but aren't:
```
Disqualifier:    [specific criterion]
Why Exclude:     [concrete reason — wasted budget, wrong use case, consistent churn]
```

Always include at least:
- Direct competitors (exclude from all campaigns)
- Any segment that consistently churns (from closed lost CSV)
- Any segment your company explicitly flagged as wrong fit
- `[TO ADD — from Tab 5 Lost Deals]` placeholder row for churn patterns

---

## STEP 5 — Generate Tab 4: Pain per Persona

Structure: **[PRIMARY DIMENSION STATES] × [PERSONA TYPES]**

Do not assume the dimension. Use what Step 2 identified.

### Persona types to include (from contacts CSV or your materials if no CSV):

| Persona | Typical titles | Buying committee role |
|---|---|---|
| Product | PM, Head of Product, VP Product, CPO | Champion or Economic Buyer |
| UX / User Research | UX Researcher, UXR, Head of Research, Design Researcher | Champion or End User |
| Consumer Insight | Consumer Insights Manager, Director of Insights, Market Research Lead | Champion or Economic Buyer |
| [Add others if CSV shows different patterns] | | |

### Per pain row, output all 7 fields:

**Core Pain** — first person, specific scenario, emotional state. Max 2 sentences.  
Source priority: G2 reviews from Skill 1 research → customer quotes → your materials → AI estimate.  
Use exact language from reviews where available. This is what goes into S1 of the messaging matrix.

**What They Have Tried** — specific tools + specific failure reason. Not vague.

**How [Product] Fixes This** — plain and specific. No marketing language.

**Proof** — "Company X. Specific outcome with numbers." If not confirmed: `[TO ADD]`

**Best Signal to Find This Person** — specific Clay-detectable condition. Feeds Tab 6.

**Personalization angle** — which of the 6 personalization buckets applies most to this persona:
- Self-authored content (highest value — LinkedIn posts, talks, articles)
- Self-identified traits (their LinkedIn headline, bio)
- Company level (funding, job posts, news)
- Background centric (tenure, career trajectory)

**Source tag** — [G2], [CSV-quote], [INPUT], [AI EST]

### Writing rules:

```
Core Pain — GOOD: "I send a survey and get 200 responses but still don't know 
                   why users are dropping off. I'm guessing."
Core Pain — BAD:  "Product teams struggle with getting user insights efficiently."

What Tried — GOOD: "Typeform surveys. Fast to send but no follow-up questions. 
                    Can't surface the why."
What Tried — BAD:  "Traditional research methods that don't scale."

Proof — GOOD: "Wayfair. Research team scaled output without adding headcount."
Proof — BAD:  "Enterprise customers have seen significant improvements."
```

Add at bottom of tab:
> *"These words should sound like something YOUR customer would say, not marketing language. Fix anything that doesn't match how your customers actually describe the problem."*

---

## STEP 6 — Pause and Present to you

```
✅ Skill 2 complete — [YourCompany]

CONFIDENCE: [GOLD / SILVER / BRONZE]
Records analyzed: [N customers / N contacts / N open / N lost]

PRIMARY DIMENSION: [name]
Tab 4 structure: [N states] × [N personas] = [N rows]

MISMATCHES FOUND: [N]
[For each: you assumed X, data shows Y, delta %, implication]

These should be the first thing discussed on the team review session.
You may not be aware of them.

ICP Summary:
- Winning segment (what data shows): [description]
- Your hypothesis: [description]
- Match: [yes / partial / mismatch]

Tab 2: [N] verticals ([N] data-confirmed / [N] MISMATCH / [N] AI EST)
Tab 4: [N] pain rows ([N/total] have confirmed proof points)

ICP Score summary:
[Top vertical]: [score]/100 → [tier]
[Second vertical]: [score]/100 → [tier]

Please review:
1. Is the primary dimension right for your company?
2. Do the mismatches reflect reality?
3. Does pain language sound like your actual customers?
4. Any proof points I missed?

Type "Tab 2+4 OK" to proceed to Tab 6+7 (Signal Library)
Or give corrections first.
```

---

## WHAT TO PASS TO SKILL 3

```
SKILL 2 OUTPUT:
Primary dimension: [name + states]
Persona types: [list]
Winning segment (data shows): [description]
Your hypothesis: [description]
Mismatch summary: [yes/no + brief]
Confirmed verticals with counts: [list]
ICP scores per vertical: [list with scores]
Pain language bank: [key first-person phrases from Tab 4]
Competitors from Skill 1: [full list]
Tech stack signals from CSV: [tools visible in your CRM enrichment]
Best personalization buckets per persona: [list]
```


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
