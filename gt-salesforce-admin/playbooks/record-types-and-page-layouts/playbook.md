---
name: record-types-and-page-layouts
description: "Use record types + page layouts to support different business processes on one object (e.g. New Business vs Renewal opportunities) with the right picklist values and fields per team. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Record Types & Page Layouts

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Serve different processes on the same object without cloning objects. **Record types** control which picklist values (e.g. sales process / stages) and page layout a record uses; **page layouts** control which fields/related lists a user sees. Together they tailor Leads/Opportunities/etc. per team or motion.

## Prerequisites
- "Customize Application"
- A clear picture of the distinct processes (e.g. New Business vs Renewal, SMB vs Enterprise)
- Pairs with sales-process setup (opportunity stages) and `audit-profiles-permission-sets` (record type assignment is per profile/permission set)

## Critical concept
- **Record type** = a variant of an object: its own picklist value sets (crucially, its own **Sales Process** = Opportunity stages) and a default page layout, assigned per profile/permission set.
- **Page layout** = field/section/related-list arrangement + which fields are required/read-only on the layout (note: FLS still overrides layouts — see `field-level-security-audit`).
- Don't over-create record types (each adds maintenance). Create one only when the process genuinely differs.

## Automation level
Guided/hybrid — design + Setup config; Metadata API for bulk changes.

## Steps
1. **Identify distinct processes** per object (Opportunity: New Business vs Renewal; Lead: Inbound vs Partner). One record type per genuinely different process only.
2. **Create record types** and their picklist value sets / Sales Process (stages) per type.
3. **Build page layouts** per record type/persona: expose the right fields, set layout-level required fields, trim clutter for reps.
4. **Assign** record types + layouts per profile/permission set; set defaults.
5. **Verify** a rep on each process sees the correct stages, fields, and layout.

## Notes
- Record types drive which Opportunity **stages** appear — this is how multiple sales processes coexist (the SF equivalent of multiple HubSpot pipelines).
- FLS overrides page layouts; use `field-level-security-audit` for true field access.
- Pairs with `validation-rules-setup` and the opportunities/sales-process playbooks.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
