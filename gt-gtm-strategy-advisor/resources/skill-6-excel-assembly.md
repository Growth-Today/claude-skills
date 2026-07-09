---
name: gtm-skill-6-excel-assembly
description: "GTM Onboarding Skill 6 — Final Excel Assembly. Generates the complete 11-tab + STRATEGY + Dashboard GTM workbook as a downloadable .xlsx file. Run after all Skills 1-5 are confirmed by you. Uses the xlsx skill (openpyxl). Your company name goes in every tab header and the filename."
---

# Skill 6 — Excel Assembly

**Generates:** Complete 11-tab + STRATEGY + Dashboard `.xlsx` workbook  
**Input:** All Skills 1–5 outputs (confirmed by you)  
**Requires:** xlsx skill (openpyxl) — read `/mnt/skills/public/xlsx/SKILL.md` before starting  
**Output:** `[YourCompany]_GTM_Playbook_v1.xlsx`

---

## BEFORE STARTING — Read the xlsx skill

Read `/mnt/skills/public/xlsx/SKILL.md` for:
- openpyxl syntax for formatting, fonts, fills, column widths
- Formula construction rules (use Excel formulas, not hardcoded Python values)
- `scripts/recalc.py` for formula recalculation after generation
- Zero formula errors policy (#REF!, #DIV/0! etc.)

---

## PRE-FLIGHT CONSISTENCY CHECK

Before generating a single tab, run these 5 checks across all Skill outputs. Report any issues to you before proceeding — do not silently fix them.

```
CHECK 1: Logo verification
  Every company name used in Tab 8 S4 Enterprise AND Tab 9 "What to Say"
  must be in Tab 1 Notable Customers.
  If not confirmed → flag to you before generating.

CHECK 2: Differentiator consistency
  Tab 2 disqualifiers must not contradict Tab 1 differentiators.
  Example catch: "30+ languages" differentiator vs "non-English only" in disqualifiers.

CHECK 3: Tab 4 ↔ Tab 8 alignment
  Primary dimension in Tab 4 must match Tab 8 matrix structure exactly.
  Same dimension states, same personas.

CHECK 4: Tab 6 ↔ Tab 7 alignment
  Every signal name in Tab 7 Combo Plays must match exactly a signal in Tab 6.
  No renamed or paraphrased signal names.

CHECK 5: Tab 10 ↔ Tab 2 alignment
  Market sizing segments in Tab 10 must match vertical priorities in Tab 2.
  P1 verticals in Tab 2 → P1 in Tab 10. No orphan segments.
```

Report format:
```
PRE-FLIGHT RESULTS:
✅ Check 1 — Logos: [all OK / N issues — list]
✅ Check 2 — Differentiators: [OK / issue]
✅ Check 3 — Tab 4↔8: [OK / issue]
✅ Check 4 — Tab 6↔7: [OK / issue]
✅ Check 5 — Tab 10↔2: [OK / issue]

Proceeding to generation. / Flagging N issues to you before proceeding.
```

---

## TAB ORDER

```
TRANSCRIPT MISMATCHES  — [v3+ only — first tab if transcript provided]
Tab 0  — Project Dashboard
Tab 1  — Company + Market          [from Skill 1]
Tab 2  — ICP Hypothesis            [from Skill 2]
Tab 3  — Buyer Journey             [CONFIRM WITH YOUR TEAM (v1/v2) / AI pre-filled from transcript (v3+)]
Tab 4  — Pain per Persona          [from Skill 2]
Tab 5  — Lost Deals + Objections   [CONFIRM WITH YOUR TEAM — template only]
Tab 6  — Signal Library            [from Skill 3]
Tab 7  — Signal Combo Plays        [from Skill 3]
Tab 8  — Messaging Matrix          [from Skill 5]
Tab 9  — Battlecard                [from Skill 4]
Tab 10 — Market Sizing             [AI EST — generate here]
Tab 11 — Account Selection         [your CRM/Clay filters — generate here]
STRATEGY — Discussion doc          [generate here]
```

**Rule:** TRANSCRIPT MISMATCHES tab is ONLY generated when a transcript is provided. When present, it is always the first tab in the workbook — before Tab 0. It is the most important tab for you to review before the team review session.

---

## FORMATTING STANDARDS (apply to every tab)

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Color palette
HEADER_BG    = "1A1A2E"   # Dark navy — tab headers
HEADER_FONT  = "FFFFFF"   # White text on headers
SECTION_BG   = "E8EAF6"   # Light blue-grey — section dividers
YELLOW_REVIEW = "FFF9C4"  # Yellow — cells you must review
GREEN_DONE   = "E8F5E9"   # Light green — AI pre-filled, confirmed
ORANGE_WARN  = "FFF3E0"   # Orange — [AI EST] cells
RED_CONFIRM   = "FCE4EC"   # Pink — CONFIRM WITH YOUR TEAM cells (never pre-fill)
WHITE        = "FFFFFF"

# Standard fonts
def header_font(): return Font(name='Arial', bold=True, color=HEADER_FONT, size=11)
def body_font():   return Font(name='Arial', size=10)
def note_font():   return Font(name='Arial', size=9, italic=True, color='666666')

# Standard fills
def header_fill():  return PatternFill('solid', start_color=HEADER_BG)
def section_fill(): return PatternFill('solid', start_color=SECTION_BG)
def yellow_fill():  return PatternFill('solid', start_color=YELLOW_REVIEW)
def orange_fill():  return PatternFill('solid', start_color=ORANGE_WARN)
def red_fill():     return PatternFill('solid', start_color=RED_CONFIRM)
def green_fill():   return PatternFill('solid', start_color=GREEN_DONE)

# Column width defaults
DEFAULT_COL_WIDTH = 20
WIDE_COL_WIDTH    = 35
NARROW_COL_WIDTH  = 12
```

### Yellow cell rule (mandatory)
Mark YELLOW any cell where:
- You must review and correct AI pre-fill
- Data is [AI EST] and needs confirmation before use
- [VERIFY] flag is present
- your materials hypothesis contradicts web research [MISMATCH]

### Source tag placement
Every pre-filled cell must show its source tag — either in the cell value itself `"$6M Seed [WEB]"` or in the adjacent source column.

---

## TRANSCRIPT MISMATCHES TAB (v3+ only — generate first, before Tab 0)

Only generate this tab when a call transcript is provided. When present, this is always the first tab in the workbook.

**Purpose:** Documents every place where the transcript contradicts or adds to your intake notes / positioning materials, the CSV data, or the current playbook. This tab is you's primary preparation tool for the team review session — it shows exactly what changed and why.

**Column structure:**
```
#  |  Topic  |  your materials Said  |  Call / CSV Says  |  Severity  |  Action Required
```

**Severity levels:**
```
CRITICAL      — Changes the entire GTM approach (e.g. "no segmentation at all")
HIGH          — Changes a specific tab significantly (e.g. new competitor discovered)
MEDIUM        — Correction needed but limited impact (e.g. one KDM title removed)
LOW           — Minor clarification, no structural change
NEW SIGNAL    — Something useful found that wasn't in your materials at all
```

**What to scan for (check every one of these):**

| Category | What to look for |
|---|---|
| ICP corrections | Revenue floor walked back? Headcount floor different? Verticals reprioritised? |
| Disqualifiers | Any your materials disqualifier contradicted on the call? ("We actually signed X.") |
| Competitor list | New competitors mentioned that weren't in your materials? Any de-prioritised? |
| KDMs / buyer roles | Any title added, removed, or changed? New influencer or blocker named? |
| Buying triggers | New timing signal mentioned? Season? Platform event? |
| Sales cycle | Duration confirmed or contradicted? |
| Primary channel | Is outbound actually the top channel, or is it referrals/partners? |
| New signals | Any signal mentioned on call not in your materials at all? |
| Objections | Real objection language from the call that wasn't in your materials? |
| Pricing model | Any pricing detail confirmed, corrected, or contradicted? |

**Format per mismatch row:**
```
#[N]  |  [Topic, 3-5 words]  |  [What your materials said — be specific]  |  [What call/transcript said — include timestamp if possible, e.g. "Norm [27:55]: '...'"  |  [CRITICAL/HIGH/MEDIUM/LOW/NEW SIGNAL]  |  [Specific action: which tab to update, what to change]
```

**Note at bottom of tab:**
```
"KEY INSIGHT: [1–2 sentence summary of the single most important finding from the transcript 
               that changes the GTM approach]"

"BIGGEST ACTIONABLE FINDING: [the one thing you must fix before campaigns launch, 
                               based on the transcript]"
```

**Formatting:**
- CRITICAL rows: red fill
- HIGH rows: orange fill
- MEDIUM rows: yellow fill
- LOW rows: white
- NEW SIGNAL rows: green fill

---

## TAB 0 — Project Dashboard

Dashboard structure from Skill 1 output. Build with these blocks:

**Block 1 — Engagement Scope** — Do not generate. you communicates scope separately. It depends on the signed package, Clay ownership, GTM maturity, and credit limits — none of which the AI knows. Remove this block from the Dashboard entirely.

**Block 2 — Milestone Status** (table with: Milestone | Owner | Due | Status | Notes)
- Status values: DONE (green fill) / PENDING (yellow fill) / BLOCKED (red fill)

**Block 3 — Your Tech Stack** (CRM, Sequencer, Enrichment, Intent tool)
- Include CRM gap flag if applicable (orange fill + warning text)

**Block 4 — Contact** (Primary contact name, email, LinkedIn | you name)

**Block 5 — QA Checklist** (12 checkboxes — use ☐ symbol, you tick during review)
```
☐  1. Full competitor list confirmed by you in writing
☐  2. All yellow cells in Tabs 1, 2, 3, 4 reviewed and corrected
☐  3. Tab 3 (Buyer Journey) yellow cells confirmed — AI pre-fill is always provided
☐  4. Tab 5 (Lost Deals + Objections) fully completed by you
☐  5. Industry segmentation confirmed — max 2 verticals for launch
☐  6. Pain descriptions rewritten in first-person prospect voice
☐  7. Static copy written or approved by you before sequence activation
☐  8. You reviewed the sequence in sequencer before activation
☐  9. Clay credit estimate shared before signal runs
☐ 10. HubSpot access confirmed and CRM audit complete
☐ 11. Sequencer tool confirmed (HubSpot / Smartlead / Instantly)
☐ 12. Onboarding call notes added to Dashboard Block 7
```

**Block 6 — Call Log** (CONFIRM WITH YOUR TEAM — red fill, 5 blank rows: Date | Summary | Actions | Owner)

**Confidence banner** (top of Tab 0 AND Tab 1 — both tabs get the banner):
```
GOLD:   Dark green banner — "GOLD CONFIDENCE — All key inputs provided. High accuracy."
SILVER: Yellow banner     — "SILVER CONFIDENCE — Medium confidence. You must review Tab 4 carefully."
BRONZE: Orange banner     — "⚠ BRONZE CONFIDENCE — your intake notes / positioning materials only, no customer CSVs. Most persona content
                             is AI estimated. Request enriched customer CSV before team review session."
```

The banner on Tab 1 uses a shorter version: `"⚠ [CONFIDENCE LEVEL] — [one sentence reason]"` in the subtitle row (Row 2, below the tab title).

**Critical rule:** Tab 3 is ALWAYS AI pre-filled regardless of confidence level. A BRONZE playbook still has a fully filled Tab 3. The confidence banner does NOT change Tab 3's pre-fill status.

---

## TABS 1, 2, 4, 6, 7, 8, 9 — Transfer from Skills 1–5

For each of these tabs:
1. Take the exact output confirmed by you from the relevant skill
2. Apply formatting standards (headers, yellow cells, source tags)
3. Do NOT rewrite or reinterpret the content — transfer it exactly

**Tab header format for every tab:**
```
Row 1: "GROWTH TODAY  |  [YOUR COMPANY]  |  TAB [N]: [TAB NAME]"
       → Dark navy fill, white bold font, merged across all columns
Row 2: "[Brief instruction for your team — what to do with this tab]"
       → Light grey fill, italic font
```

**Confidence banner rule — Tab 1 gets a banner too:**
Tab 0 (Dashboard) gets the full confidence banner.
Tab 1 (Company + Market) gets a shortened version in Row 2 (the subtitle row):
```
BRONZE: "⚠ BRONZE CONFIDENCE — your intake notes / positioning materials only, no customer CSVs uploaded. Most persona content is AI estimated. Request enriched customer CSV before team review session."
SILVER: "SILVER CONFIDENCE — Customer data provided. Persona content based on real data. You must review yellow cells."
GOLD:   "GOLD CONFIDENCE — All key inputs provided. High confidence."
```
No other tabs need the banner — Tab 0 and Tab 1 are the two your company sees first.

---

**Tab 2 specific formatting rules (PRIMARY DIMENSION callout):**

Add a dedicated section BEFORE the firmographic table:
```
PRIMARY DIMENSION  |  The ONE variable that changes the core message completely
[Dimension name] — [N] states: [list states]
Why: [1–2 sentences — what is fundamentally different about each state? 
     Why can't the same message work for all states?]
```
This makes the messaging architecture visible to your company and the AE. It's the most important strategic insight in the whole playbook.

Both the firmographic table AND the verticals table must include two blank review columns:
- "Your Rank (1-3)" — blank, yellow fill
- "Your Notes" — blank, yellow fill

These are filled on the team review session. Never pre-fill them.

---

**Tab 9 specific formatting rules (Your Notes column):**

The competitor displacement table must include a blank "Your Notes" column as the last column. Green or yellow fill. This is where your company:
- Confirms the displacement angle is accurate
- Adds a real customer story or proof point
- Notes any competitor they regularly see in deals that isn't in the table

Never pre-fill this column.

---

## TAB 3 — Buyer Journey

**Tab 3 is ALWAYS AI pre-filled — at every confidence level, including BRONZE.**

This was validated by Dialogue AI v3 (BRONZE confidence = your materials only, no CSV, no transcript). Tab 3 was fully filled using your materials + Skill 2 persona analysis + ATL/BTL framework. The old "leave blank if no transcript" rule was wrong.

**What to pre-fill and from what source:**

| Column | Source | Fill rule |
|---|---|---|
| Typical Job Title | your materials KDMs + Skill 2 persona analysis | Always fill — your materials gives this |
| What They Care About | your materials pain data + ATL/BTL framework | Always fill from persona inference |
| What Convinces Them | your materials proof points + Skill 4 battlecard | Always fill — derive from product knowledge |
| What Blocks Them | your materials objections + Skill 4 objection handling | Always fill — derive from known friction |
| Do We Target Them? | your materials KDM list + Skill 2 | Always fill |
| Notes | ATL/BTL tag + any additional context | Always fill |

**Source tagging rules:**
- `[INPUT]` — directly from your intake notes / positioning materials
- `[PERSONA ANALYSIS]` — derived from Skill 2 persona mapping
- `[ATL/BTL]` — inferred from seniority of the role
- `[TRANSCRIPT — confirmed]` — when transcript available, direct quote or explicit confirmation
- `[TRANSCRIPT — inferred]` — when transcript available, logically derived

Every pre-filled cell gets yellow fill with its source tag. These cells are confirmed or corrected on the team review session — NOT blank and waiting for your company to write from scratch.

**Why this matters:** A blank Tab 3 gives your company nothing to react to. A pre-filled Tab 3 gives them something concrete to correct. Corrections are faster and more accurate than creation from scratch.

### What They Care About — derive from ATL/BTL framework
```
BTL personas (ICs, Managers):   daily operational pain, time savings, not looking bad to their boss
ATL personas (VPs, C-suite):    revenue impact, competitive risk, not scaling headcount, board optics
```
Apply this to every role. Even without your input, this is directionally right for 90% of companies.

### What Convinces Them — derive from product + persona
```
Champion:        Live demo using their actual use case. Seeing it work on their own data.
Economic buyer:  ROI calculation vs status quo (agency / current tool / headcount). Peer references.
Influencer:      Output quality. Integration with their existing tools.
Blocker:         Security certs. Short commitment (POC model). Industry reference customers.
End user:        Pilot study. Ease of setup. Output they can present to stakeholders same day.
```
Adapt to the specific product. These are always derivable from your materials + product knowledge.

### What Blocks Them — derive from Skill 4 objections + your materials
Extract from the objection handling section of Tab 9. The blockers per role are almost always the same objections, attributed to the most likely persona.

### Rows to include
```
Champion (finds the tool, pushes it internally)
Economic buyer (approves the budget)
Influencer (uses the output, has opinions)
Blocker (IT, legal, procurement, skeptic)
End user (runs the actual work day to day)
```

### Note at top — v1/v2 (no transcript) — YELLOW background
```
"AI pre-filled from Skill 2 persona analysis, ATL/BTL framework, and your materials data.
CONFIRM ON ONBOARDING CALL: Yellow cells = AI pre-filled from persona analysis.
Correct anything wrong. Add any nuances specific to your buyers."
```

### Note at top — v3+ (transcript available) — GREEN background
```
"AI pre-filled from call transcript. Yellow = AI pre-filled (confirm).
Green = confirmed from transcript. Correct anything wrong on call."
```

---

### BUYING PROCESS QUESTIONS — CONFIRM WITH YOUR TEAM section (at bottom of Tab 3)

Add this section AFTER the main buyer journey table. Red fill. CONFIRM WITH YOUR TEAM.

These questions cannot be answered by AI. They are asked on the team review session.

```
How long does a typical deal take from first contact to signed contract?
Who usually finds [Product] first — champion or executive? How did they find it?
What does the internal conversation look like before they buy?
What approval steps are required? (IT review, security, procurement)
What is the most common reason a deal stalls or dies?
What is the most common objection on a first call?
Which persona is easiest to get a demo with?
Which persona is hardest to close even after a demo?
```

These feed the STRATEGY tab recommendation and Tab 9 battlecard updates.

---

## TAB 5 — Lost Deals + Objections (CONFIRM WITH YOUR TEAM)

**If Tab 5 data was provided by you:** transfer and format it.

**If Tab 5 is blank (most common):**

Top section — "Sales Intelligence from your materials" (PRELIMINARY):
- Extract any objection signals from your intake notes / positioning materials
- Label every row: `[PRELIMINARY — based on your materials signals only. Add real examples below.]`
- Yellow fill on all PRELIMINARY rows

Main lost deals section: BLANK rows with red fill + CONFIRM WITH YOUR TEAM

Objection handling section: transfer from Skill 4 (Tab 9) — mark as PRELIMINARY if Tab 5 was blank.

Note at top:
```
"Only you know this. Please fill in real examples from your sales conversations
before the team review session. Even 3–5 real examples dramatically improves
the battlecard and objection handling. This directly feeds Tab 9."
```

---

## TAB 10 — Market Sizing (generate fresh)

**Mandatory banner at top (orange fill, prominent):**
```
⚠️ ALL numbers below are AI estimates [AI EST].
Confirm with a Clay pull before using in any planning or reporting.
Do not treat these as verified facts.
```

**TAM Breakdown by Segment table:**
Per segment, include:
- Segment name + exact filters used (geo, headcount, vertical, stage)
- Est. Companies in ICP `[AI EST]`
- Est. Reachable Contacts `[AI EST]` (note: KDMs per company assumption)
- Avg Deal Size Estimate `[AI EST]`
- Priority (P1/P2/P3 — must match Tab 2 vertical priorities)
- Notes
- Your Confirm column (blank, yellow fill)

Every number cell: orange fill + `[AI EST]` in cell or adjacent column.

**Signal Volume Estimates table:**
One row per Priority 1 and Priority 2 signal from Tab 6:
- Signal name (must match Tab 6 exactly)
- Est. Monthly New Records `[AI EST]`
- How to Pull (exact Clay method)
- Data Source
- Freshness (real-time / weekly / monthly)
- Notes (data lag warnings, timing nuances)

---

## TAB 11 — Account Selection (generate fresh)

your CRM and Clay filter definitions for building the first target list.
One row per ICP segment from Tab 2.

Per segment:
```
Segment name:        [from Tab 2]
your CRM filters:      [exact filter settings — industry, headcount, revenue, geo, stage]
Clay enrichment:     [what to enrich after your CRM pull]
Claygent validation: [prompt to confirm ICP fit]
Est. list size:      [AI EST]
Priority:            [P1/P2/P3]
```

Include a "How to use this tab" note:
```
"These are starting filter configurations. Run a test pull of 50 accounts
before running the full list. Validate Claygent prompt on test set first.
Estimated list sizes are AI estimates — actual Clay pull will give real numbers."
```

---

## STRATEGY TAB — Discussion Document (generate fresh)

Not a data tab. Designed for the team review session conversation.
Label clearly at top: `"DISCUSSION DOCUMENT — For use on the team review session. Not a deliverable."`

**★ RECOMMENDATION block — put this at the very top, before everything else:**
```
★ RECOMMENDATION FOR [YOUR COMPANY]: Start with [OPTION A/B] + [EXECUTION MODEL] for the first 30 days.
Reason: [2–3 sentences from Skill 1 diagnostic — stage, channel maturity, data quality, biggest gap]
```

**TOP 3 SIGNALS TO LAUNCH FIRST — structured table (before Part 1):**

| Signal | Why Launch First | Est. Volume | Expected Reply Rate | Clay Setup |
|---|---|---|---|---|
| [Signal name — exact from Tab 6] | [Why this one first — pain specificity, volume, or timing relevance] | [from Tab 10 volume estimate] | [from Tab 7 reply rate estimate] | [exact Clay workflow — 1 sentence] |
| [Signal 2] | [Why] | [volume] | [reply rate] | [Clay setup] |
| [Signal 3] | [Why] | [volume] | [reply rate] | [Clay setup] |

This table replaces the prose signal recommendations in earlier versions. It must be actionable: anyone reading the STRATEGY tab should be able to start the Clay build from row 1.

**Part 1 — Targeting Strategy**

Option A: Untiered (recommended for first 30 days)
- Run top 3 Priority 1 signals separately, one Clay table per signal
- Contact everyone who hits a signal — no scoring required
- Fastest to launch, validates which signals actually convert before investing in scoring

Option B: Tiered (after 30 days of signal data)
- Score accounts by signal count (using framework from Tab 7)
- Tier 1 (3 signals, 150+ pts): < 1 hour response, AE reviews before sending
- Tier 2 (2 signals, 50–149 pts): automated + light personalization, SDR monitors
- Tier 3 (1 signal, < 50 pts): fully automated, volume play

**Part 2 — Execution Model**

Three service packages — describe each, include yellow callout on each:
`"For pricing and scope details, speak to your you before selecting this motion."`

1:1 Assisted Motion
- GT populates CRM with signal context and pre-written messaging per account
- AE reviews every message before it goes out — nothing automated without approval
- Best for: Tier 1 accounts, high-value enterprise deals, relationship-driven sales
- AE workload: High per account, but research and draft are done — AE just approves or tweaks

Hybrid Motion
- TAM split before launch: Tier 1 accounts → AE-owned (1:1 Assisted)
- Tier 2–3 accounts → automated sequences
- Requires: clean CRM ownership rules before launch (AEs and automation cannot overlap)
- Best for: teams with both enterprise and SMB motion

1:Many Programmatic
- Signals trigger sequences automatically, AE only touches replies
- Highest volume, lowest personalization per message
- Best for: self-serve motion, high-volume SMB, inbound-assisted outbound

**Part 3 — Specific recommendation for your company:**
Based on Skill 1 diagnostic (stage, channels, data quality):
```
"For [YourCompany]: We recommend starting with [Option A/B] + [Execution Model]
for the first 30 days. Reason: [diagnostic from Skill 1 — stage, no outbound yet, etc.]
Move to [next step] after first [N] demos."
```

---

## GENERATION SEQUENCE

```python
# 1. Read xlsx skill before writing any code
# 2. Run pre-flight consistency check — report before generating
# 3. Create workbook, add all sheets in order
# 4. Populate each tab with content from confirmed skill outputs
# 5. Apply formatting (headers, yellow/orange/red fills, source tags)
# 6. Run scripts/recalc.py — verify zero formula errors
# 7. Save as [YourCompany]_GTM_Playbook_v1.xlsx
# 8. Copy to /mnt/user-data/outputs/
# 9. present_files to you
```

Filename: `[YourCompany]_GTM_Playbook_v1.xlsx`  
No spaces in filename — use underscores or CamelCase.

---

## FINAL HANDOFF SUMMARY

After file is generated and presented:

```
✅ ONBOARDING PACKAGE COMPLETE — [YourCompany]

File: [YourCompany]_GTM_Playbook_v1.xlsx
Confidence: [GOLD / SILVER / BRONZE]
Tabs: 11 + STRATEGY + Dashboard

PRE-FLIGHT: All 5 consistency checks passed / [N issues resolved — list]

PRIMARY DIMENSION: [name]
→ Drives all Tab 4 pain rows and Tab 8 messaging variants.

TOP 3 SIGNALS TO LAUNCH FIRST:
1. [Signal name] — [why + expected volume + Clay setup]
2. [Signal name] — [why + expected volume]
3. [Signal name] — [why + expected volume]

RECOMMENDED LAUNCH APPROACH:
[Option A/B] + [Execution model] for first 30 days.
[Specific reasoning from Skill 1 diagnostic]

WHAT YOU SHOULD DO BEFORE THE TEAM REVIEW:
☐ Review and correct Tab 3 yellow cells (Buyer Journey — AI pre-filled, needs confirmation)
☐ Fill Tab 5 (Lost Deals) — blocks battlecard finalization
☐ Confirm competitor list in Tab 9 — [N] competitors to validate
☐ Review yellow cells in Tabs 1, 2, 4 — correct anything wrong
☐ Confirm max 2 priority verticals for launch

MISMATCHES TO DISCUSS ON CALL:
[list from Skill 2 — your hypothesis vs data reality]

NEXT STEPS:
1. Save the Excel and review it with your team (allow 2–3 days)
2. Book team review session (1 hour)
3. Collect Tab 3 + Tab 5 before call
4. Run Clay pull on top 2 Priority 1 signals for volume validation
5. Confirm sequencer tool before call
```


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
