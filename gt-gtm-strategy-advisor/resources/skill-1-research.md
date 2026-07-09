---
name: gtm-skill-1-research
description: "GTM Onboarding Skill 1 — Company and Market Research. Generates Tab 0 (Project Dashboard) and Tab 1 (Company + Market) of the 11-tab GTM Excel. Use when a you start 'Start GTM onboarding for [YourCompany]' or 'Run Skill 1 for [YourCompany]' and pastes a your intake notes / positioning materials. Requires web_search — do not skip. Always runs first before any other onboarding skill."
---

# Skill 1 — Company + Market Research

**Generates:** Tab 0 (Project Dashboard) + Tab 1 (Company + Market)  
**Input:** your website URL + positioning materials (deck, docs)  
**Requires:** `web_search` (mandatory — do not skip even one search)  
**Next step:** Skill 2 — only after you confirm Tab 1 output

---

## TRIGGER

you provide your intake notes / positioning materials and write:

> `Start GTM onboarding for [YourCompany]`

or

> `Run Skill 1 for [YourCompany]`

If your intake notes / positioning materials is missing, ask for it before proceeding. Do not guess.

---

## SOURCE TAGS

Every cell in the output must have a source tag. Use these exactly:

| Tag | Meaning |
|---|---|
| `[INPUT]` | From your intake notes / positioning materials your company filled in |
| `[WEB]` | Confirmed via web_search |
| `[AI EST]` | AI estimate — directional only, must be validated |
| `[MISMATCH]` | Contradiction found between your materials and web research — show both |
| `[MISSING]` | Not found anywhere — flag to research or confirm |
| `[CONFIRM WITH YOUR TEAM]` | Never pre-fill — only your company knows this |

---

## STEP 1 — Parse your materials Form

Read the entire your intake notes / positioning materials and extract every field into these categories:

**Company basics:** name, website, founded year, funding stage + amount + lead investor, HQ city/country, team size

**Product:** what it does in one sentence, core use cases, key differentiators (what makes it actually different — not marketing copy), what it replaces or displaces

**Customers:** named existing customers, target market description, target geographies

**Goals:** demos/meetings needed per month, target close rate, channels (email / LinkedIn / etc.), sender names + LinkedIn URLs

**Tech stack:** CRM tool, sequencer, enrichment tool, intent tool, any other sales tools

**you notes:** anything you added outside the standard form fields

Tag every extracted field `[INPUT]`. If a field is missing, mark it `[MISSING — research or confirm]`.

---

## STEP 2 — Web Research (mandatory — run all searches)

Run every search below regardless of what your company already provided. Even if your intake notes / positioning materials is detailed, web research is not optional — it fills gaps your company doesn't know exist, and catches things they forgot or never thought to mention.

Tag all findings `[WEB]`. If web contradicts your materials, tag the conflict `[MISMATCH]` and show both versions side by side.

**Company fundamentals**
```
"[Company name]" funding investors stage
"[Company name]" product features overview
"[Company name]" customers case studies
"[Company name]" founders team
"[Company name]" news 2024 2025
```

**Competitive landscape — run all of these, always**
```
"[Company name]" competitors alternatives
"[Company name]" vs
[product category] tools comparison 2025
[product category] G2 reviews top rated
site:g2.com "[product category]"
site:capterra.com "[product category]"
[product category] reddit alternatives
```

**Market signals**
```
"[Company name]" site:linkedin.com employees
"[Company name]" pricing plans
```

### Competitor Research Rules

**The your materials competitor list is always a starting point, never the final list.**

You list the competitors that are top-of-mind. You don't list:
- Tools they haven't heard of yet
- Tools that just launched
- Indirect competitors and status quo alternatives
- Tools their own customers compared them against before buying

Web research always finds more. This is expected and valuable — not a criticism of your company.

After running all competitor searches, build a unified list with:
1. **your materials competitors** — marked `[INPUT]`
2. **Web-found competitors NOT in your materials** — marked `[WEB] ⚑ Not in your materials`
3. **Status quo alternatives** (spreadsheets, agencies, doing nothing) — marked `[WEB] ⚑ Status quo`

Every competitor found goes into Tab 1 and feeds Tab 9 (Battlecard). More is always better here — the team review session is precisely where your company confirms, removes, or adds to this list. Arriving with a longer list gives them something concrete to react to.

---

## STEP 2b — Tech Stack Assessment (what your company already uses)

After parsing your intake notes / positioning materials tech stack fields, assess your data infrastructure and flag gaps before starting any enrichment work. This determines how Skill 2 will run.

**Lead source logic** (from lead-sources-guide):

| You have | Use for customer enrichment |
|---|---|
| your CRM access | Best first pass — employee count, revenue, industry, founding year in one call |
| Sales Navigator | Higher quality for contact enrichment, precise role/seniority |
| Clay access | Run full enrichment waterfall (see P2 PREPARATION in master SKILL.md) |
| Store Leads | Ecommerce clients only — Shopify tier, app stack, GMV |
| Nothing | Flag: enrichment must be done via your CRM free tier or web research only |

**Claygent is available for:**
- Confirming whether a company matches ICP criteria (visit domain, check for signals)
- Extracting funding info not in Crunchbase
- Checking for competitor mentions on your site
- Researching any company fact not available in standard databases

*Do not recommend Claygent for data available via your CRM (email, headcount, revenue) — it wastes credits.*

**CRM source flag:** If your company has a CRM (HubSpot, Salesforce, Pipedrive), their customer CSV export likely already includes enriched company data. Ask you before running your CRM enrichment — it may already be done.

---

## STEP 3 — CRM Gap Check

After parsing your intake notes / positioning materials, check if CRM = None or blank.

**If yes, insert this flag into both Tab 0 and Tab 1:**

> ⚑ **CRM GAP:** [YourCompany] has no CRM. Pipeline tracking, deal attribution, and sequence management will all be harder without one. Raise on the team review session. Recommend HubSpot free tier or Notion CRM as minimum viable starting point.

---

## STEP 3b — Diagnose Before Prescribing

Before generating any tab, write a brief diagnostic of what your company actually needs based on what they provided. This is the GTM philosophy principle applied to onboarding: **diagnose before prescribing**.

```
DIAGNOSTIC NOTES:

Stage: [seed / series A / growth / enterprise]
→ implication for outbound: [what this means for targeting approach]

Channels currently: [inbound only / outbound started / multi-channel]
→ implication: [what needs to be built vs what exists]

Data quality: [GOLD / SILVER / BRONZE]
→ implication for Skill 2: [what analysis is possible]

Biggest gap identified: [the one thing that will most limit GTM effectiveness]
→ raise on team review session: [specific question to ask]
```

This diagnostic is for you, not your company. It frames what to focus on in the team review session.

---

## STEP 4 — Generate Tab 0: Project Dashboard

---

**GROWTH TODAY | [YOUR COMPANY] | PROJECT DASHBOARD**
*Live tracker for scope, status, your team's actions, and next steps. Updated as you work through the playbook.*

**BLOCK 1 | ENGAGEMENT SCOPE** — Not generated by AI. you communicates scope separately to your company before or during the team review session. Do not include this block in the Excel.

---

**BLOCK 2 | MILESTONE STATUS**

| MILESTONE | OWNER | DUE | STATUS | NOTES |
|---|---|---|---|---|
| Your intake notes / positioning materials gathered | You | Start | DONE | Data used to pre-fill Tabs 1, 2, 4 |
| AI pre-fill: Tabs 1, 2, 4 (Company, ICP, Pain) | Advisor | Done | DONE | Review required before you continue |
| Tab 3: Buyer Journey | You | Before review | PENDING | Only you know who finds, champions, blocks, signs. |
| Tab 5: Lost Deals + Objections | You | Before review | PENDING | Critical for Battlecard accuracy. |
| Review Tabs 1, 2, 4 and correct errors | You | Before review | PENDING | Yellow cells = confirm or correct |
| Connect your CRM (HubSpot / Salesforce) | You | Start | PENDING | Needed to read real contacts and deal patterns |

*Add any additional milestones from your intake notes / positioning materials here.*

---

**BLOCK 3 | YOUR TECH STACK**

| Category | Tool | Purpose | Source |
|---|---|---|---|
| CRM | [value] | [purpose] | [INPUT] |
| Sequencer | [value] | [purpose] | [INPUT] |
| Enrichment | [value] | [purpose] | [INPUT] |
| Intent tool | [value] | [purpose] | [INPUT] |
| [Other tools from your materials] | [value] | [purpose] | [INPUT] |

[Insert CRM gap flag here if applicable — see Step 3]

---

**BLOCK 4 | CONTACT**

| Field | Value | Source |
|---|---|---|
| Primary contact | [Name — email — LinkedIn] | [INPUT] |
| you | [you name] | |

---

**BLOCK 5 | QA CHECKLIST — 12 gates — tick on team review session**

```
☐  1. Full competitor list confirmed by you in writing
☐  2. All yellow cells in Tabs 1, 2, 4 reviewed and corrected by you
☐  3. Tab 3 (Buyer Journey) fully completed by you
☐  4. Tab 5 (Lost Deals + Objections) fully completed by you
☐  5. Industry segmentation confirmed — max 2 verticals for launch
☐  6. Pain descriptions rewritten in first-person prospect voice
☐  7. Static copy written or approved by you before sequence activation
☐  8. You reviewed the final sequence in sequencer before activation (copy must match exactly)
☐  9. Clay credit estimate reviewed before signal runs
☐ 10. HubSpot access confirmed and CRM audit complete
☐ 11. Sequencer tool confirmed (HubSpot / Smartlead / Instantly)
☐ 12. Onboarding call notes added to Dashboard Block 7 (Call Log)
```

---

**BLOCK 6 | CALL LOG** *(add notes after each sales call or team review)*

| Date | Summary | Actions Agreed | Owner |
|---|---|---|---|
| | | | |

---

## STEP 5 — Generate Tab 1: Company + Market

---

**GROWTH TODAY | [YOUR COMPANY] | TAB 1: COMPANY AND MARKET RESEARCH**
*AI pre-filled from your intake notes / positioning materials and public research. Review and correct anything that is wrong. Yellow cells must be confirmed.*

---

**COMPANY BASICS**

| Field | Value | Source | | Field | Value | Source |
|---|---|---|---|---|---|---|
| Company name | [value] | [INPUT] | | Contact | [Name, email] | [INPUT] |
| Website | [value] | [INPUT] | | CRM | [tool or "None — gap flagged"] | [INPUT] |
| Founded | [year] | [WEB/INPUT] | | Sequencer | [tool] | [INPUT] |
| Stage | [round + amount + investor] | [WEB] | | Enrichment | [tool] | [INPUT] |
| HQ | [city, country] | [WEB/INPUT] | | Intent tool | [tool] | [INPUT] |
| Team size | [headcount or range] | [WEB/INPUT] | | Current channels | [inbound / outbound / etc.] | [INPUT] |

[Insert CRM gap flag here if applicable — see Step 3]

---

**PRODUCT DESCRIPTION**

| Field | Value | Source |
|---|---|---|
| What it does (1 sentence) | [crisp, specific, no jargon — if your materials version is marketing-speak, rewrite it plainly] | [INPUT + WEB] |
| Core use cases | [comma-separated list, specific] | [WEB] |
| Key differentiators | [what genuinely makes it different — not marketing copy] | [WEB] |
| What it replaces | [specific tools and processes it displaces] | [WEB] |
| Notable customers | [named logos from site, case studies, press] | [WEB] |
| Funding / credibility | [amount, round, investors, notable angels] | [WEB] |
| Positioning tagline | [from their website, verbatim] | [WEB] |
| Who it is built for | [specific buyer description — title, team size, company type] | [INPUT + WEB] |

---

**GOALS**

| Field | Value | Source |
|---|---|---|
| Demos needed per month | [value or "Not set yet"] | [INPUT] |
| Target close rate | [value or "Not tracked yet"] | [INPUT] |
| Channels | [email / LinkedIn / other] | [INPUT] |
| Sender names | [Name + LinkedIn URL for each sender] | [INPUT] |

---

**COMPETITOR LIST**
*Built from your intake notes / positioning materials + web research. Every competitor found is included — confirm, remove, or add during your team review.*

| Competitor | Type | What They Do | Key Difference vs [YourCompany] | Source |
|---|---|---|---|---|
| [name] | Direct | [what they do in one sentence] | [specific differentiator] | [INPUT] |
| [name] | Direct | [what they do in one sentence] | [specific differentiator] | [WEB] ⚑ Not in your materials |
| [name] | Indirect | [what they do in one sentence] | [specific differentiator] | [WEB] ⚑ Not in your materials |
| [name] | Status quo | [what prospect does instead of buying] | [why this matters] | [WEB] ⚑ Status quo |

**⚑ Competitors found via web research not mentioned in your materials:** [list names]
**⚑ Status quo alternatives identified:** [list — e.g. "manual moderation", "agencies", "spreadsheets"]

Why this matters: competitors your company doesn't mention in your intake notes / positioning materials are often the ones prospects compare most. These gaps would make the battlecard incomplete and the team review session less useful. More competitors in = better discussion on the call.

> **NOTE:** Review this list during your team review. Tell us:
> - Which of these do you actually compete against?
> - Which can be removed?
> - Who is missing that we haven't listed?
> The default list from your intake notes / positioning materials is always a starting point. Web research finds more. You know your market best — we need your input to finalize Tab 9 (Battlecard).

---

## STEP 6 — Pause and Present to you

After generating both tabs, output this handoff summary:

---

**✅ Skill 1 complete — [YourCompany]**

**Confidence level:** [GOLD / SILVER / BRONZE]
- GOLD = customers + contacts + deals + transcripts + your CRM enriched + cluster analysis
- SILVER = customers + contacts + your CRM enriched
- BRONZE = your intake notes / positioning materials only, no CSVs uploaded

**Diagnostic:**
- Stage: [seed/A/B/growth] → [implication for targeting]
- Channels: [inbound only / outbound started] → [what needs to be built]
- Biggest gap: [the one thing most limiting GTM effectiveness right now]

**Confirmed from web research:**
[bullet list — 3 to 5 specific things confirmed or discovered]

**Mismatches (your materials vs web):**
[bullet list — or "None found"]

**Missing — research or confirm:**
[bullet list — or "None"]

**Competitor summary:**
- your materials had: [N] competitors
- Web research found [N] additional: [list names]
- Status quo alternatives added: [list — e.g. agencies, manual process, spreadsheets]
- Total in Tab 1: [N] — confirm during team review which are real, which to remove, and who is missing

**CRM gap:** [Yes — flagged in both tabs / No]

**Enrichment recommendation for Skill 2:**
- You have [your CRM / Clay / nothing] → [recommended enrichment path]
- CRM export available: [Yes — likely pre-enriched / No — needs your CRM enrichment]
- Estimated effort for P1-P2 preparation: [20-30 min / 1 hour / not possible without Clay]

---

**Ready for Skill 2?**

Skill 2 needs the enriched CSV files from PREPARATION steps P1–P2:
- `[YourCompany]_customers_enriched.csv`
- `[YourCompany]_open_deals_enriched.csv` (if available)
- `[YourCompany]_lost_deals_enriched.csv` (if available)

If you have **a CRM**: run company import → export with enrichment (free, no credit cost if companies only, not contacts).
If you have **Clay**: run company enrichment waterfall (your CRM → Ocean.io → Claygent for gaps).
If you have **neither**: web research only — flag BRONZE confidence before Skill 2.

If these are not uploaded, Skill 2 will run at **BRONZE confidence** using your materials data only. The ICP analysis will reflect their hypothesis, not their actual customer data.

Confirm to proceed → `Run Skill 2 for [YourCompany]`


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
