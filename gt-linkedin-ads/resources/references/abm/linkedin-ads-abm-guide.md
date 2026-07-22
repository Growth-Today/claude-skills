# LinkedIn Ads for ABM — Guide

Ad formats, budget math, campaign structure, and optimization for Account-Based Marketing on LinkedIn. Benchmarks live in `{SKILL_BASE}/resources/references/benchmarks.md` (ZenABM 2026) — this guide covers *structure and method*; always read the numbers off that file, not from memory.

---

## Why LinkedIn for ABM

- **Best professional targeting** — filter by company, title, seniority, industry, function. No other platform matches this precision for B2B.
- **Company-list targeting** — upload account lists from the CRM to target named accounts (LinkedIn requires ~300 matched members to run).
- **Persona filtering on company lists** — push the account list, then layer native title/seniority filters to hit specific personas inside those accounts.
- **ABM-native** — your target buying committees are already active on LinkedIn.

**Limitation:** Google Display match rates are too low for B2B (people don't use work emails on Google accounts). LinkedIn is the primary ABM channel; Display can only supplement via retargeting on a separate no-index landing-page domain.

---

## Ad formats for ABM (which format, which stage)

| Format | Best for | ABM stage |
|---|---|---|
| **Single Image** | Workhorse; strongest conversion economics | All stages |
| **Thought Leader Ads** | Awareness, events, executive voice | Identified → Aware |
| **Carousel** | Multi-feature or comparison content | Interested |
| **Video** | Brand, product demo, case study | Aware → Interested |
| **Document Ads** | Lead magnets, guides, reports | Interested |
| **Text / Dynamic** | Cheap background impressions | Awareness (support) |
| **Conversation / Message** | Direct high-value offers — expensive; use sparingly, and note EU restrictions | Considering |

Read format-level CTR/CPC medians from `benchmarks.md`. **Evidence discipline:** never apply a benchmark without checking objective, geography, methodology, sample size, and account maturity — treat any single figure as a reference range, not a target.

---

## The budget math (the #1 reason ABM campaigns fail)

**Budget dilution** — too many ads on too little budget, so no ad ever gets enough spend to produce useful data.

```
Monthly budget ÷ 30 ÷ (avg CPC × 4 clicks) = max effective ads
```

Each ad needs enough daily spend for **3–4 clicks/day** to learn; below that you get slow learning, false reads, and wasted spend. Pull the CPC you plug in from `benchmarks.md` for the specific format — don't assume one blended number.

**Consequence at a typical mid-market budget:** you can usually run **one** campaign group effectively. Split by persona **OR** by intent, never both at once, or you dilute budget and hit LinkedIn's minimum-audience thresholds.

---

## Campaign structure

**Two layers, not a persona × intent matrix:**

| Layer | Stage | Content | Audience |
|---|---|---|---|
| **COLD** | Identified + Aware | Awareness, thought leadership, events | Full target-account list |
| **WARM** | Interested + Considering | Case studies, demos, comparisons | Retargeting (engaged accounts) |

**Group campaigns by shared intent (JTBD), not persona**, because: more engagements roll up per group (helps clear LinkedIn's 3-engagement API-data minimum), audiences stay above the 300-member floor, and classic campaigns hold one asset type so you need fewer of them.

**Audience sync flow:** CRM company lists → LinkedIn Campaign Manager (native persona filters) → ~48h to sync, min 300 matched members. As accounts cross engagement thresholds, an engagement connector (e.g. ZenABM or Fibbler) pushes data to the CRM, active lists update, and audiences move accounts COLD → WARM automatically.

---

## Optimization

**Test order (biggest lever first):** creative → audience refinement → offer/CTA → format mix.

**Common mistakes:** too many ads on too little budget; splitting persona × intent simultaneously; over-engineered account scoring (use LinkedIn engagement data, keep it simple); trusting website de-anonymization (<1% match — rely on LinkedIn's native engagement instead); no no-index landing-page domain (can't separate ABM traffic); running Message/Conversation ads at scale (expensive, and EU-restricted).

**Tooling (SaaS):** CRM (HubSpot/Salesforce) for workflows + audience sync + reporting; Campaign Manager for delivery; Clay/Apollo for list building + enrichment; **ZenABM** or **Fibbler** to push LinkedIn engagement → CRM with account scoring and intent (see `ads-outbound-signaling-guide.md`); Slack for BDR alerts. Match tools to the motion — don't buy a stack you won't operate.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
