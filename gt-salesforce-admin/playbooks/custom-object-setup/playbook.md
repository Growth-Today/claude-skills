---
name: custom-object-setup
description: "Decide when a custom object is warranted (vs a field or standard object) and set one up correctly: relationships, fields, page layouts, tabs, and reporting. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Custom Object Setup

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Model data that doesn't fit Lead/Contact/Account/Opportunity (subscriptions, assets, projects) as a **custom object** — but only when warranted. The hardest thing to change later is the relationship, so decide it deliberately.

## Prerequisites
- "Customize Application"
- `formula-and-rollup-fields` (roll-up summaries need master-detail)
- Clear picture of how the object relates to standard objects

## Critical concept — decision + relationship
- Use a **field** for a single attribute; a **standard object** if it's really an Opportunity/Case; a **custom object** for many records of a new kind with their own fields.
- **Relationship type is the key decision:** **Master-detail** (tight: cascade delete, roll-up summaries, inherits sharing) vs **Lookup** (loose: independent, optional). Master-detail unlocks roll-ups but couples lifecycle/sharing.
- Once workflows/reports/integrations depend on it, restructuring is painful — get it right up front.

## Automation level
Guided — Setup config; Data Loader to seed records.

## Steps
1. **Run the decision test** — confirm a field/standard object won't do.
2. **Design:** object name, the **relationship** (master-detail vs lookup) to the parent, fields (correct types), record types if needed.
3. **Create** the object + tab; build **page layouts**; set **object + field permissions** via permission sets (`audit-profiles-permission-sets`, `field-level-security-audit`).
4. **Add roll-ups/formulas** (`formula-and-rollup-fields`) if master-detail.
5. **Create custom report types** so it's reportable (`custom-report-types`).
6. **Seed data** via Data Loader (`data-loader-and-imports`).

## Notes
- Master-detail vs lookup is the load-bearing choice — master-detail for roll-ups + shared lifecycle, lookup for independence.
- Most "custom object" needs are actually a field or a standard object — test first.
- Pairs with `formula-and-rollup-fields`, `custom-report-types`, security playbooks.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
