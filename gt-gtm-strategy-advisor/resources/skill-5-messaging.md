---
name: gtm-skill-5-messaging
description: "GTM Onboarding Skill 5 — Messaging Matrix. Generates Tab 8 (18 messaging variants using the 5-sentence framework). Run after Skill 2 (primary dimension confirmed) and Skill 1 (confirmed customer logos)."
---

# Skill 5 — Messaging Matrix

**Generates:** Tab 8 (18 messaging variants — 5-sentence framework)  
**Input:** Skill 1 (confirmed logos) + Skill 2 (primary dimension + pain language bank) + Skill 4 (displacement angles)  
**Next step:** Skill 6 (Excel Assembly) — only after you confirm Tab 8

---

## CORE PRINCIPLE — The 5-Sentence Framework

Every variant is built from exactly 5 sentence types. S3 is always identical. The other 4 change based on the dimensions identified in Skill 2.

```
S1 — Hook             changes by PERSONA (always)
S2 — Consequence      changes by the SECOND DIMENSION (whatever Skill 2 identified)
S3 — Solution         NEVER CHANGES — identical in every variant
S4 — Differentiator   changes by COMPANY SIZE (or last dimension if size is not used)
S5 — CTA              changes by COMPANY SIZE + ATL/BTL split
```

S2 is not always researcher presence. S2 is whatever the second most important messaging dimension is for your company. For some companies it is funding stage. For others it is vertical. For others it is researcher presence. Skill 2 tells you what it is.

**Test before generating:** read any assembled variant out loud. Does it sound like something a real person would send? Or does it sound like AI copy? If the latter — rewrite it.

---

## ATL vs BTL SPLIT — applies before writing any sentence

Before writing S1, determine the seniority of each persona. This changes everything.

**ATL (Above-the-Line) — VP, C-Level, Director:**
- Think strategic, past and future
- Care about: revenue impact, risk, competitive positioning, board optics
- Message length: 2–3 sentences MAXIMUM
- Language: "strategic initiative", "revenue impact", "competitive advantage"
- Fatal mistake: operational details → instant delegation to subordinate

**BTL (Below-the-Line) — Manager, IC, End User:**
- Think tactical, present
- Care about: daily pain, time savings, workflow, looking good to their boss
- Message length: 3–4 sentences acceptable
- Language: "stop spending X hours on", "never deal with Y again", "save Z hours/week"
- Fatal mistake: ROI framing and strategic language → doesn't resonate, too abstract

**For Dialogue AI:**
- Consumer Insight VP/Director → ATL treatment (strategic, board-level)
- UX Researcher (solo, 1 person) → BTL treatment (operational, daily pain)
- Product Manager → BTL (tactical, workflow)
- VP Product → ATL if enterprise, BTL if seed-stage startup

Apply this split to S1 and S5 especially.

---

## INPUT REQUIRED

```
SKILL 1 OUTPUT:  [confirmed customer logos — for S4 Enterprise only]
SKILL 2 OUTPUT:  [primary dimension + states + persona types + pain language bank]
SKILL 4 OUTPUT:  [displacement angles per competitor — feeds S4 differentiator]
```

---

## STEP 1 — Confirm Variant Structure from Skill 2

Paste the Skill 2 dimension output. Extract the dimensions and their states. Do not assume.

```
DIMENSIONS FROM SKILL 2:
  Dimension 1: [name] — [N states]: [list]
  Dimension 2: [name] — [N states]: [list]
  Dimension 3: [name, if applicable] — [N states]: [list]
  Dimension 4: [name, if applicable] — [N states]: [list]

Total variants: [D1 states] x [D2 states] x [D3 if applicable] x [D4 if applicable]

PERSONALIZATION VARIABLES (not dimensions — Clay handles these):
  [variable]: changes [opening line / proof logo]
```

### DIMENSIONS FOR YOUR COMPANY — mandatory table at top of Tab 8

**Before any variants, Tab 8 must open with this reference table.** This is what the Dialogue V3 playbook had and it makes the whole matrix readable — without it, 18 rows of S1–S5 are impossible to navigate.

Format (4 columns):
```
Dimension | Values | Changes which sentence | Why this is a dimension and not personalization
```

Example (Dialogue AI V3):
```
1. Persona          | Product / UX Research / Consumer Insight     | S1 (core pain hook)    | A PM, a UXR, and a CI Manager have completely different daily pain. Same product, completely different reason to buy.
2. Researcher       | No researcher / 1 researcher / 2+ researchers | S2 (consequence)       | The consequence of the pain is different at each state. No researcher = validation skipped. 1 researcher = backlog. 2+ = scale problem.
3. Company size     | SMB / Enterprise                              | S4 (proof) + S5 (CTA)  | SMB gets speed/ease messaging, no logos. Enterprise gets confirmed customer logos and a pilot offer.
4. Industry         | Ecom / Health / Fintech / Consumer tech        | Opening line + proof only — NOT S1 or S2 | An ecom PM and a health PM have the same core pain. Industry changes which proof logo is most relevant — not the message structure.
```

After this table, add the S3 STATIC sentence callout:
```
S3 STATIC SENTENCE — identical in all [N] variants:
"[the sentence]"
```

Then the variant rows begin.

---

### NOTE FOR ADAPTATIONS — footer at bottom of Tab 8

After the personalization layer table, add this note:
```
"NOTE FOR ADAPTATIONS: If industry drives structurally different S1 and S2 (different core pain),
add it as a dimension column above. If industry only changes the opening line and proof logo,
keep it as a personalization variable handled in Clay."
```

This orients whoever later adapts the playbook for a different company.

---

### Tab 8 column structure

One column per dimension, then the 5 sentence columns. The column headers come from the dimension names.

**2 dimensions** (e.g. Persona x Company size):
```
Persona | Company size | S1 | S2 | S3 | S4 | S5 | Framework | Level (ATL/BTL)
```

**3 dimensions** (e.g. Persona x Researcher x Company size):
```
Persona | Researcher | Company size | S1 | S2 | S3 | S4 | S5 | Framework | Level
```

**4 dimensions** (e.g. Persona x Researcher x Size x Industry):
```
Persona | Researcher | Company size | Industry | S1 | S2 | S3 | S4 | S5 | Framework | Level
```

**The Level column (ATL/BTL) is mandatory** — it tells the SDR/AE which version they are sending and governs length, tone, and CTA style. Never omit it.

If industry is a dimension: it gets a column. If it is a personalization variable: it does NOT get a column. It appears in the Clay layer section below the matrix.

---

## STEP 2 — Write the 9 Building-Block Sentences First

Write every unique sentence BEFORE assembling any variant. This prevents inconsistency.

### S1 — Hook Sentences (one per persona type)

**Source:** Tab 4 Core Pain column from Skill 2. Take the best pain statement per persona and adapt to direct address.

**Rules:**
- Direct address ("You…") or clear first-person framing
- Specific scenario — not a generic complaint
- Max 20 words
- Must make the reader think: "that's exactly my situation"
- BTL personas: operational, present-tense, daily frustration
- ATL personas: strategic, past-and-future, competitive or revenue framing

```
BAD (generic): "User research is hard to scale."
GOOD (BTL):    "You make product decisions every week, but getting real user 
                feedback takes weeks you don't have."
GOOD (ATL):    "Your product teams are shipping faster — but without user 
                validation, you're scaling risk, not growth."
```

**Write one S1 per persona. For ATL personas, write an ATL version.**

### S2 — Consequence Sentences (one per primary dimension state)

**NOT another pain statement.** S2 answers: what does S1 FORCE you to do, or PREVENT you from doing?

S1 + S2 must form a cause-and-effect arc. Test: if S1 and S2 could be swapped — S2 is wrong.

```
BAD (restates S1):  "I don't have time to do interviews myself."
GOOD (consequence): "Without a dedicated researcher, you're either skipping 
                     validation or waiting on an agency."
```

Write one S2 per primary dimension state (e.g. one for "No researcher", one for "1 researcher", one for "2+ researchers").

### S3 — Static Solution Sentence (write ONCE, never change)

**This sentence is IDENTICAL in all variants. It never changes.**

Must contain:
1. The product name
2. What it does mechanically (the how)
3. The key differentiator (what makes it different from everything else)

```
Rules:
- Complete standalone sentence
- Max 25 words
- Includes product name + mechanism + differentiator
- No marketing language

Example: "Dialogue is an AI platform that runs live qualitative interviews 
at scale, automatically — no scheduling, no moderator needed."
```

Write this sentence. Then do not change it in any variant. If it needs changing for any variant — the sentence is wrong. Rewrite it.

### S4 — Differentiator Sentences (one per company size)

**SMB version:**
- Speed and ease — no logos needed
- Specific outcome + plain language
- Focus: time-to-insight, no expertise required

```
Example: "No scheduling, no coordination — real interviews with real users, 
results in hours not weeks."
```

**Enterprise version:**
- Confirmed logos ONLY — check Tab 1 Notable Customers before writing
- Never use aspirational logos
- Never use "companies like X" — only specific confirmed names

```
Example: "Wayfair and Square use it to validate features before building — 
enterprise depth at startup speed."
```

**Rule:** If you cannot fill Enterprise S4 with confirmed logos → write `[TO ADD — confirm enterprise logos during team review]`

### S5 — CTA Sentences (one per company size)

**Rules:**
- Always includes: specific time commitment + specific offer
- SMB: lower commitment, demo with their own use case
- Enterprise: slightly higher ask, pilot offer or proof-of-concept

```
BAD: "Want to chat?"
BAD: "Would you be open to a quick call?"
GOOD (SMB):        "Worth a 20-minute look? I'll show you how it works using 
                    your actual research question."
GOOD (Enterprise): "Open to a pilot? We can run one study end to end so your 
                    team can evaluate the quality before committing."
```

**ATL CTA variant:** Frame around strategic outcome, not the product demo.
```
GOOD (ATL): "15 minutes to see how [Company] is handling this at scale?"
```

---

## STEP 3 — Framework Selection per Variant

Before assembling, assign one of the 8 allowed cold email frameworks to each variant group. This determines the feel of the assembled email.

| Framework | Best for |
|---|---|
| Before/After | BTL — show current state vs desired, clear transformation |
| Ask Before Pitch | Any persona — open-ended question leads, earns right to pitch |
| Do the Math | BTL — calculate the cost of the problem (time, money) |
| Challenge of Similar Companies | Any — "companies doing X often struggle with Y" |
| Pattern Interrupt | ATL — break expectations, unconventional opener |
| Neutral Insight | ATL — share a third-party insight, build trust first |
| Typical Problems by Role | BTL — role-specific pain that prompts reflection |
| Upfront Value | Any — give something useful before asking |

For the standard 18-variant matrix, assign frameworks to variant groups, not each individual variant. Example: all Product persona variants use "Do the Math", all CI persona variants use "Challenge of Similar Companies".

---

## STEP 4 — Assemble the Full Matrix

Now assemble every variant from the building blocks.

**Output format per variant:**

```
#[N] | [Persona] / [Dimension state] / [Size] | Framework: [name] | Level: [ATL/BTL]

S1: [hook for this persona]
S2: [consequence for this dimension state]
S3: [always identical]
S4: [differentiator for this company size]
S5: [CTA for this company size]

Assembled:
[S1] [S2] [S3] [S4] [S5]

SDR checklist:
☐ Under 90 words?
☐ Single CTA?
☐ Social proof specific (not vague)?
☐ No bullets?
☐ Reads like a real person sent it?
```

**Check for each variant before moving on:**
- S1 and S2 form a cause-and-effect arc (not two pains)
- S3 is word-for-word identical to all other S3s
- S4 Enterprise uses ONLY confirmed logos from Tab 1
- S5 includes time commitment + specific offer
- Total word count: 60–90 words (BTL) or 40–60 words (ATL)

---

## STEP 5 — Personalization Layer (Clay-ready table)

After assembling variants, generate a dedicated **TICKETING TOOL / PLATFORM PERSONALIZATION LAYER** table at the bottom of Tab 8. This is what you plugs directly into Clay to generate custom first lines at scale.

**Format: one row per detectable tech stack variable or persona signal.**

```
Tool / Signal | Opening Line (Clay variable) | Integration proof swap (S4) | Signal to detect | Clay detection method
```

**Rules:**
- One row per tool/signal. Not per persona — the tool is the variable the opening line references.
- Opening line column = the exact Clay formula output. Should be ≤12 words. Reads like a human typed it.
- Integration proof swap = what changes in S4 when this tool is detected. Only the tool-specific phrase changes.
- Signal to detect = the BuiltWith/Store Leads/Claygent condition that triggers this row.
- Clay detection method = exact implementation (BuiltWith field, Claygent prompt, etc.).

**Example output (for a CX AI product):**

| Tool / Signal | Opening Line | S4 Integration Proof Swap | Signal | Clay Detection |
|---|---|---|---|---|
| Gorgias detected | "Saw [Company] is on Gorgias." | "We overlay on Gorgias — no migration." | Gorgias in BuiltWith at D2C brand | BuiltWith: gorgias_detected = true |
| Zendesk detected | "Saw [Company] runs Zendesk." | "We work on top of Zendesk — no migration." | Zendesk in BuiltWith at D2C brand | BuiltWith: zendesk_detected = true |
| No tool detected | "[Company] is on Shopify with a [size] team." | Lead with speed to value, no tool reference | Shopify + no AI tool detected | BuiltWith: shopify + absence of AI CX tools |

**For your company, adapt to your actual detectable signals:**
- Ecommerce/mobile: Shopify Plus, Klaviyo, Recharge, Attentive, Tapcart
- CX/support: Gorgias, Zendesk, Intercom, Forethought
- Sales tools: Salesforce, HubSpot, Outreach, Gong

**The goal:** anyone can take this table, copy the columns into Clay, and have personalised opening lines generating automatically with no further instructions.

**Note at bottom of table:**
```
"This layer personalises the opening line only. The S1–S5 structure does not change.
 Every row in this table maps to one column in the Clay table."
```

---

## STEP 6 — Assembly Test

Before presenting to you, assemble and read variant #01 out loud as a complete email.

```
ASSEMBLY TEST — Variant #01:

Subject: [write one subject line per assembled variant]
Body: [S1. S2. S3. S4. S5.]
Word count: [N]

Does this sound like something a real person would send?
Does it lead with pain, not features?
Is the CTA soft enough that someone might actually reply?

If any answer is NO → rewrite before presenting.
```

Subject line rules (from cold-email/subject-lines):
- 3–5 words max
- No question marks in subject line
- References something specific: their company name, role, or a signal
- Never: "Quick question", "Following up", "Checking in"
- Good examples: "research at [Company]", "[Company]'s UXR team", "usability testing"

---

## STEP 7 — Pause and Present to you

```
✅ Skill 5 complete — [YourCompany]

VARIANT STRUCTURE: [N] variants
([dimension states] × [personas] × [sizes])
Frameworks assigned: [list per persona group]
ATL/BTL split: [which personas got ATL treatment]

S3 STATIC SENTENCE (appears identically in all [N] variants):
"[the sentence]"
— Confirm this is accurate and complete before proceeding.

S4 ENTERPRISE LOGOS USED: [list]
— All confirmed from Tab 1. If any are wrong, correct them now.
— If missing: [TO ADD — confirm enterprise logos]

PERSONALIZATION LAYER:
- Product persona: [bucket + Clay prompt summary]
- UX/Research persona: [bucket + Clay prompt summary]
- CI persona: [bucket + Clay prompt summary]

ASSEMBLY TEST — Variant #01 (read this out loud):
Subject: [subject line]
[assembled email]
Word count: [N]

Does that sound like a real email your AE would send?

Please review:
1. Does S1 for each persona feel like their exact situation?
2. Does S2 feel like a CONSEQUENCE of S1, not a second complaint?
3. Is S3 accurate, complete, and specific enough?
4. Are the enterprise logos correct and confirmed?
5. Does S5 feel like something a real person would send?

Type "Tab 8 OK" to proceed to Skill 6 (Excel Assembly)
Or give corrections first.
```

---

## WHAT TO PASS TO SKILL 6

```
SKILL 5 OUTPUT:
Static S3 sentence: [confirmed text]
Variant count: [N]
All [N] variants: [confirmed by you]
Enterprise logos confirmed: [list]
Framework per persona group: [list]
ATL/BTL split: [which personas]
Personalization Clay prompts: [per persona]
Subject lines: [one per variant or per variant group]
```


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
