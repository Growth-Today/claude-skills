---
name: formula-and-rollup-fields
description: "Derive values automatically with formula fields and roll-up summary fields (e.g. account-level open pipeline, days since last activity) instead of brittle Flows or manual updates. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Formula & Roll-Up Summary Fields

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Compute derived values natively so they're always accurate. **Formula fields** calculate on the record from its own fields; **roll-up summary fields** aggregate child records up to a master (SUM/COUNT/MIN/MAX). These beat workflow-maintained fields (which drift) and unlock scoring, segmentation, and reporting.

## Prerequisites
- "Customize Application"
- Correct field types on source fields (numbers/dates), so calculations don't error
- Roll-up summaries require a **master-detail** relationship (or use a Flow/DLRS for lookup relationships)

## Critical concept
- **Formula field** — same-record calculation (e.g. `Amount * Probability`, `TODAY() - LastActivityDate`). Recalculates on view/save.
- **Roll-up summary** — aggregates **child → parent** across a master-detail link (e.g. COUNT of open Opportunities on an Account, SUM of Amount). Native only on master-detail; for lookup relationships use a record-triggered Flow or the DLRS package.
- Both auto-update — no drift, no maintenance, unlike Flow-maintained number fields.

## Automation level
Guided — Setup config (declarative). No script needed.

## Steps
1. **Inventory derived metrics** teams maintain by hand or Flow: account open-pipeline amount, count of open opps, days since last activity, deal margin, weighted amount.
2. **Classify:** same-record → formula; child-to-parent aggregate → roll-up summary (needs master-detail) else Flow/DLRS.
3. **Build the fields** with correct return types; validate a few records against a manual calc.
4. **Retire brittle equivalents:** disable any Flow/Workflow maintaining the same number; point reports/list views at the new field.
5. **Feed downstream:** use in lead/account scoring, ICP tiering, list views, and dashboards.

## Notes
- Roll-up summary is master-detail only — for lookup relationships use a record-triggered Flow or Declarative Lookup Rollup Summaries (DLRS).
- Fix source field types first (a number stored as text won't calculate).
- Feeds `create-icp-tiers`, `build-lead-scoring`, reporting.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
