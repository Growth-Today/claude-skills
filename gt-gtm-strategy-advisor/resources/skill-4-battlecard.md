---
name: gtm-skill-4-battlecard
description: "GTM Onboarding Skill 4 — Sales Battlecard. Generates Tab 9 (competitor displacement table + objection handling). Run after Skill 3 is confirmed. Always searches G2 and Reddit for each competitor before writing any cell. Every cell must be speakable in 10 seconds."
---

# Skill 4 — Sales Battlecard

**Generates:** Tab 9 (Competitor Displacement + Objection Handling)  
**Input:** Skill 1 (full competitor list + confirmed customers) + Skill 2 (pain language per persona) + Skill 3 (G2 research summary + competitive signals)  
**Requires:** web_search per competitor (mandatory — never write from training knowledge)  
**Next step:** Skill 5 (Messaging Matrix) — only after you confirm Tab 9

---

## CORE RULE — The AE Test

Every cell in Tab 9 must pass this test: **can an AE say it out loud in 10 seconds on a live call?**

If a cell takes more than 10 seconds to read aloud → it's too long. Cut it.

This is the most important rule in Skill 4. A battlecard that reads like a product brief will never be used on a call.

---

## INPUT REQUIRED

```
SKILL 1 OUTPUT: [full competitor list from research — all found, not just your materials]
SKILL 2 OUTPUT: [pain language per persona from Tab 4]
SKILL 3 OUTPUT: [G2 research summary per competitor — paste full]
TAB 5:          [Lost Deals + Objections — if you filled it, paste here]
                [If blank: "not provided" — objection rows get [PRELIMINARY] tag]
```

---

## STEP 1 — Build the Complete Competitor List

**Do not write any battlecard cells yet.** Confirm the list first.

Start from Skill 1's competitor list (which already includes your materials + web research findings).  
Then run additional searches to catch anything missed:

```
Search: "[product name] vs"                → comparison pages
Search: "[product name] alternative"        → substitutes
Search: "[product name]" site:g2.com        → G2 compare tab
Search: "[product name]" site:reddit.com    → what users actually say
Search: "[your website]/compare"          → if they have a compare page
```

Categorize every competitor:

| Type | Definition | Why it matters for the battlecard |
|---|---|---|
| **Direct** | Same category, same buyer, same job to be done | Head-to-head displacement — AE needs a clear "why us" |
| **Indirect** | Different approach, same buyer, overlapping use case | Education play — prospect may not see it as a choice |
| **Status quo** | What prospect does INSTEAD of buying (agencies, manual work, spreadsheets, doing nothing) | Most common real competitor — always include 2+ entries |

**Always include at least 2 status quo entries.** These are often what the prospect is actually comparing against, not a named tool.

Flag any competitors NOT previously in the list: `[NEW — found in Step 1 research]`

---

## STEP 2 — Research Each Competitor (mandatory before writing any cell)

For each competitor, run both searches. Use Skill 3's G2 summary if available — if not, run fresh.

```
Search A: "[competitor name] site:g2.com reviews"
  Extract: what customers LOVE (2-3 points) → "What They Do Well" column
  Extract: top 3 complaints in exact user language → "Where We Win" column

Search B: "[competitor name] cons problems" site:reddit.com OR site:g2.com
  Extract: real frustrations verbatim — what users say when not performing for the company
```

**After all competitor research, write this summary before generating any cells:**

```
COMPETITOR RESEARCH SUMMARY:

[Competitor A]:
  Strength (positive G2): [1 line — be honest]
  Top complaint (negative G2/Reddit): [exact user language]
  Displacement angle: [1 sentence — what to lead with]
  Renewal timing: [annual contract? when do they typically renew?]
  Category: [Direct / Indirect / Status quo]

[Competitor B]:
  [same format]
```

**Adjacent vendor opportunity**:  
For each competitor in the tech stack, note if they are an adjacent vendor whose customers can also be targeted:
- Competitor tool in stack → customer is using it NOW → displacement window
- Competitor tool recently removed from stack → they just switched → act within 2 weeks
- Engagement with competitor's LinkedIn page → category-aware prospect

---

## STEP 3 — Populate the 4 Battlecard Columns

### Column structure for the competitor displacement table (mandatory — all 6 columns)

```
Competitor | What They Do Well (be honest) | Where We Win | What to Say on a Call (10 sec max) | What NOT to Say | Your Notes
```

**Column 6 — "Your Notes" is mandatory.** Leave it blank with yellow fill. This is where your company:
- Confirms the displacement angle is accurate from their real sales experience
- Adds a specific customer story or proof point to the "What to Say" column
- Names any competitor they regularly see in deals that isn't already in the table
- Flags any cell that is wrong based on what they actually hear on calls

Never pre-fill this column. It has no source tag. It exists to be filled on the team review session.

---

### Column 1: "What They Do Well (be honest)"

**One sentence. The real strength. Source: positive G2 reviews.**

Why honesty matters: if the AE says something incorrect about a competitor, the prospect catches it immediately and loses trust. Be accurate.

```
BAD:  "They have some features for user research."
GOOD: "Large participant pool and strong brand recognition in video-based usability testing."

BAD:  "They're an established player."
GOOD: "Enterprise-grade survey platform with deep Salesforce integration and proven compliance at Fortune 500 scale."
```

### Column 2: "Where We Win"

**One sentence. Specific factual win. Source: their most common G2 complaint + this product's differentiator.**

The formula: `[Their top G2 complaint] → [how we solve exactly that]`

Must be verifiable. Never a generic claim.

```
BAD:  "We are faster and have better insights."
GOOD: "Live AI conversation vs async video — depth of insight is completely different, no manual analysis needed."

BAD:  "We're more affordable."
GOOD: "Replaces $40K agency research studies at a fraction of the cost — results in hours, not 8 weeks."
```

**Symptom-based displacement**:  
Where possible, frame the win around a visible business symptom the prospect is experiencing, not just a product feature:
- Output problem: "Research team can't keep up with product velocity"
- Midput problem: "80% of researcher time goes to scheduling and moderation"  
- Input problem: "No qual layer to explain why NPS is dropping"

### Column 3: "What to Say on a Call"

**Two sentences maximum. AE says this live.**

Sentence 1: acknowledge what the competitor does well (disarms the prospect, shows confidence)  
Sentence 2: the single sharpest reason to consider switching

**The 10-second test:** read it out loud. Starts at "one" and ends before "ten"? It passes.

```
BAD (too long):
"UserTesting is a well-established platform with a large participant pool, 
and while it does provide video recordings of usability sessions, the key 
difference is that Dialogue uses a live AI moderator that adapts in real time, 
which means you get much deeper qualitative insights without the manual analysis 
work that typically takes researchers days to complete..."

GOOD:
"UserTesting gives you video clips. We give you a conversation. 
The depth is completely different."
```

**Proof logos rule:** every company name used as proof in this column MUST be in Tab 1 Notable Customers. If not confirmed → remove it or mark `[VERIFY]`.

**What NOT to say** (add this as a 4th micro-column):
```
BAD format example: "We're better than them in every way."
BAD format example: "They're outdated and nobody uses them anymore."
BAD format example: "That tool is actually really bad." [trash-talk — kills credibility]
```

---

## STEP 4 — Objection Handling Section

**Source priority:**
1. Tab 5 (Lost Deals) — if you filled it, use real objections from real prospects
2. your intake notes / positioning materials — any objection signals your company flagged
3. Skill 2 pain language — reverse-engineer what objections each persona type raises
4. G2 research — what prospects say they almost didn't buy

**If Tab 5 is blank:** tag every objection row `[PRELIMINARY — based on AI analysis and your materials signals. Update after Tab 5 is filled in before team review.]`

**Per objection, output 6 fields:**

```
When they say:   [EXACT words the prospect uses — not paraphrased, not cleaned up]
                 BAD: "They express cost concerns"
                 GOOD: "It's too expensive" / "We don't have budget for this right now"

What they mean:  [the real underlying concern behind the words — 1 sentence]

Say this:        [max 2 sentences — addresses the underlying concern, not the surface words]
                 Never pivots to a product pitch. Makes prospect feel understood first.

Do NOT say:      [the defensive, vague, or arrogant version]

Persona:         [which job title is most likely to raise this objection]

Kills deal:      [Yes / No / Sometimes + brief reason]
```

**Writing rules for objection responses:**

```
STRUCTURE: 
1. Acknowledge (makes them feel heard)
2. Reframe (shifts the frame without being defensive)
3. Optional: discovery question (if timing-based objection)

BAD:
"You're right, those tools are excellent for collecting quantitative data,
and while they do serve an important purpose, the key thing to understand
about Dialogue is that it operates in a fundamentally different way..."
[too long, too defensive, sounds like a pitch]

GOOD:
"Surveys tell you what. Interviews tell you why. 
If you're deciding without the why, you're guessing."
[2 sentences, reframes without trashing the competitor, makes them think]
```

**Standard objections to always include** (customize language to your product):
- "We already have [competitor]" → displacement reframe
- "We just use surveys / [free tool]" → category education
- "We don't have a [role] to manage this" → core value prop flip
- "It's too expensive" → ROI reframe (what does current approach cost?)
- "We're not ready for this yet" → discovery question (what would need to change?)
- "Can you just send me more information?" → redirect to specificity

---

## STEP 5b — TRANSCRIPT UPDATES TO BATTLECARD (v3+ only)

After generating the standard battlecard content, check the transcript for any corrections or additions to competitors, objections, or displacement angles. Add a clearly labelled section at the bottom of Tab 9.

**Section header:**
```
TRANSCRIPT UPDATES TO BATTLECARD | [Your company] team review
```

**For each update, output:**
```
[MISMATCH #N] [Topic — 3–5 words]
Transcript: "[exact or paraphrased quote — include timestamp if available]"
Change applied: [what was added, corrected, or removed in the battlecard above]
AE note: [one sentence on how to use this in a live call]
```

**What to look for in the transcript:**
- Competitor mentioned on call that isn't in the battlecard
- Competitor de-prioritised ("we never actually see them in deals")
- Objection language that is more specific than your materials ("they always ask about X, not Y")
- A proof point, customer name, or specific stat mentioned on the call
- A "what to say" improvement based on how your company themselves frames it

**Example format:**
```
[MISMATCH #4] Zendesk AI added as competitor
Transcript: "Norm [10:25]: 'Zendesk HAS AI. We end up competing with them.'"
Change applied: Added Zendesk AI row to displacement table above.
AE note: Lead with action-taking vs CRM-bundled deflection. Do not trash Zendesk as a platform.

[MISMATCH #6] Sierra de-prioritised
Transcript: "Sierra not mentioned once on the call. Not a real competitor day-to-day."
Change applied: Sierra kept in battlecard but marked [LOWER PRIORITY — rarely encountered].
AE note: Do not lead with Sierra displacement in outbound. Focus on Gorgias AI / Intercom Fin.
```

**Mark these rows with orange fill** (PRELIMINARY updates) or green fill (confirmed on call).

---

## STEP 5 — Consistency Check

Before outputting Tab 9, check these 4 things. Report any issues found before you sees the output.

```
CHECK 1: Logo verification
  Every company name in "What to Say" column is in Tab 1 Notable Customers.
  If not confirmed → remove or mark [VERIFY].

CHECK 2: Differentiator consistency  
  No competitor cell contradicts Tab 1 differentiators or Tab 2 disqualifiers.
  Example catch: "30+ languages" as differentiator vs 
                 "non-English companies excluded" in Tab 2.

CHECK 3: Signal-battlecard alignment
  Every competitor referenced in Tab 6 tech stack signals appears in Tab 9.
  If a signal targets UserTesting customers, UserTesting must be in Tab 9.

CHECK 4: Status quo coverage
  At least 2 status quo entries are present.
  ("We use an agency" / "We do it manually" / "We use surveys" are all status quo)
```

Report format:
```
[CONSISTENCY ISSUE]: [Tab X] vs [Tab 9]
Description: [what contradicts what]
Fix applied: [what was changed — or "you to decide"]
```

---

## STEP 6 — Pause and Present to you

```
✅ Skill 4 complete — [YourCompany]

COMPETITOR LIST: [N] total entries
- From your materials:        [N] 
- Found in Skill 1:  [N] additional
- Found in Step 1 research: [N] new
- Status quo entries: [N]
- New competitors found this step: [list if any]

RESEARCH SUMMARY: G2 + Reddit searched for:
[list each competitor searched]

Key displacement angles discovered:
- [Competitor A]: [1-line angle]
- [Competitor B]: [1-line angle]
- [Status quo]: [1-line angle]

OBJECTION HANDLING: [N] objections
Source: [Tab 5 filled in by you / your materials signals only / AI analysis]
[If PRELIMINARY]: "You must review and add real examples from their sales conversations before the team review session."

CONSISTENCY CHECKS:
- Logo verification: [all OK / N issues — list]
- Differentiator conflicts: [none / N — list]
- Signal-battlecard alignment: [all OK / N gaps]
- Status quo coverage: [N entries — OK]

Please review:
1. Is the competitor list complete? This is the most common gap.
2. Is anything wrong in "What They Do Well"? (If AE says something wrong, prospect notices.)
3. Does "What to Say on a Call" actually sound like something your AE would say?
4. Any objections missing?

IMPORTANT: If you have real objection examples from lost deals or sales calls, paste them now. The current objection handling is [PRELIMINARY / confirmed from Tab 5].

Type "Tab 9 OK" to proceed to Tab 8 (Messaging Matrix)
Or give corrections first.
```

---

## WHAT TO PASS TO SKILL 5

```
SKILL 4 OUTPUT:
Full confirmed competitor list: [list — all types]
Consistency issues resolved: [yes/no + what was fixed]
Objection handling status: [PRELIMINARY / confirmed from Tab 5]
Key displacement angles: [1 line per competitor — feeds S1 hooks in messaging matrix]
Status quo alternatives: [list — feeds "What it replaces" framing in messaging]
```


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
