---
description: Meta Ads campaign structure for B2B — full-funnel architecture, CBO vs ABO, budget split across prospecting/consideration/retargeting, and exclusions. Use for Meta campaign structure, funnel, CBO, ABO, budget allocation, prospecting vs retargeting, campaign objectives, Advantage+ Sales. Triggers on "campaign structure", "Meta funnel", "CBO", "ABO", "budget split", "prospecting campaign", "retargeting campaign", "Advantage+ campaign". Do NOT use for audience targeting details (use audiences) or creative (use creative).
---

# Meta Ads Campaign Setup (B2B)

You build a clean full-funnel structure, give the algorithm enough budget per ad set to learn, and let exclusions keep the funnel honest.

## Instructions

1. Choose the objective by stage (awareness vs leads vs conversions)
2. Build the three funnel layers and split budget by temperature
3. Use CBO for prospecting, ABO where you need control
4. Keep ad sets few and well-funded (learning phase needs volume)
5. Manage exclusions so prospecting does not pay to reach existing customers

## Objective by Stage

- **Top (awareness):** brand awareness / reach / video views. Deliverable is a retargeting pool, not immediate conversions.
- **Middle (consideration):** lead gen (Instant Forms) or traffic to gated value (guide, webinar, calculator).
- **Bottom (conversion / retargeting):** conversions or lead gen to warm, high-intent audiences with the strongest offer.

## Full-Funnel Budget Split (typical B2B)

| Layer | Audience | Budget | Job |
|-------|----------|--------|-----|
| Prospecting | Cold (broad + lookalikes) | 40-50% | Find new in-market people, build retargeting pool |
| Consideration | Video viewers, engagers, site visitors | 30-40% | Educate, capture lower-friction leads |
| Retargeting | High-intent signals, lead non-converters | 20-25% | Convert with proof + strong CTA |

## CBO vs ABO

- **CBO (Advantage Campaign Budget):** let Meta distribute budget across ad sets. Best for prospecting where you want the algorithm to find efficient delivery.
- **ABO (Ad Set Budget):** you control spend per ad set. Best for retargeting, where you want guaranteed budget on each specific warm audience.

## Ad Set Discipline (learning phase math)

- Keep **4-5 ads per ad set** — enough for the algorithm to optimise, not so many that budget spreads too thin for any one ad to gather data.
- Do **not** spin up ten ad sets with one audience each — overlap kills validity and spreads learning thin. Consolidate. In 2026 fewer, broader, better-funded ad sets beat heavy micro-segmentation (see audiences).
- Each ad set needs enough budget to clear **50 events/week** to exit the learning phase (see learning-phase).

## Exclusions (keep the funnel honest)

- Exclude **current customers** from prospecting — do not pay to acquire the already-acquired.
- Exclude **active CRM leads** from prospecting once they enter the pipeline.
- Exclude **recent converters** (30-60 days) from conversion retargeting.
- One caution: do not blanket-exclude all past purchasers everywhere — you lose repeat/expansion and the positive engagement signal. Exclude deliberately, per campaign goal.

## Advantage+ note

**Advantage+ Sales** automates audience, placement, and budget. **Advantage+ Shopping is an e-commerce/DTC product — out of scope for B2B; do not use it.** For B2B lead gen, a structured full-funnel with Instant Forms + CAPI + offline conversions controls lead quality far better than hands-off automation. You may test Advantage+ Sales as a prospecting engine, but judge it on SQL/pipeline and watch lead quality closely.

## Examples

Example 1: "How should I structure a B2B Meta account?"
→ Three layers: prospecting (CBO, 40-50%), consideration (30-40%), retargeting (ABO, 20-25%). 4-5 ads per ad set, consolidate ad sets, exclude current customers and active leads from prospecting.

Example 2: "Should I use CBO or ABO?"
→ CBO for prospecting (let Meta find efficiency), ABO for retargeting (guarantee budget on each warm audience). Either way, fund ad sets enough to clear 50 events/week.


## 2026 updates

For Opportunity Score, Advantage+ 2026 changes (25/wk threshold, Predictive Budget Allocation), gen-AI Creative Enhancements, Advantage+ Leads, and Threads placements → Read `resources/references/2026-ai-updates.md`.
## B2B guardrail

Before applying any generic Meta tactic or benchmark here, check `resources/references/b2b-vs-b2c-guardrail.md` — most public Meta advice is DTC/e-commerce and does not transfer to B2B.
---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
