---
name: sales-process-and-stages
description: "Design Opportunity stages and Sales Processes that map to buyer commitments, with required fields per stage and realistic probabilities — the foundation for a trustworthy forecast. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: opportunities-sales
---

# Sales Process & Opportunity Stages

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Make the pipeline mean something. In Salesforce, **Sales Processes** define which Opportunity **stages** are available (per record type), each with a probability and forecast category. Stages should describe **buyer commitments**, not rep actions — that's what makes the forecast real.

## Prerequisites
- "Customize Application"
- `record-types-and-page-layouts` done (a Sales Process is tied to a record type)
- Alignment with sales leadership (this is a business decision)

## Critical concept
- A **Sales Process** = an ordered set of Opportunity stages, assigned to a record type (so New Business vs Renewal can have different stages).
- Each **stage** has a **Probability** (used for weighted pipeline) and a **Forecast Category** (Pipeline/Best Case/Commit/Closed).
- Stages = buyer commitments ("Proposal Reviewed", "Verbal Commit"), never rep actions ("Follow-up Sent") or zombie stages ("Nurture"). Enforce exit criteria with `validation-rules-setup` (required fields per stage).

## Automation level
Hybrid — API to audit current stages/usage; stage + process config in Setup / Metadata API.

## Steps
1. **Audit** current stages, probabilities, forecast categories, and open-deal counts per stage (find fake/zombie stages).
2. **Design** the stage list as buyer commitments; set honest probabilities (reuse historical stage-conversion where possible) and forecast categories.
3. **Configure** Sales Process(es) and attach to the right record types (`record-types-and-page-layouts`).
4. **Enforce exit criteria:** required fields per stage via validation rules (e.g. Amount + CloseDate before Proposal); restrict backward moves.
5. **Migrate** open deals off removed/renamed stages first.
6. **Verify** weighted pipeline (Σ Amount × Probability) is meaningful; forecast categories roll up correctly.

## Notes
- Multiple sales processes (via record types) are the SF equivalent of multiple HubSpot pipelines — split by process, not by team.
- Pairs with `validation-rules-setup` (stage gates), `record-types-and-page-layouts`, and reporting/forecast.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
