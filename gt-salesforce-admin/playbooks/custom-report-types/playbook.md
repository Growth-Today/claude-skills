---
name: custom-report-types
description: "Create custom report types so you can report across related objects (e.g. Accounts with Opportunities with Products) — the prerequisite most missing reports actually need. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: reporting
---

# Custom Report Types

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Half of "I can't build that report" problems in Salesforce are a missing **custom report type (CRT)**. A report type defines which objects + relationships + fields are available to a report. Standard types cover the basics; CRTs unlock cross-object and custom-object reporting.

## Prerequisites
- "Manage Custom Report Types"
- Clear picture of the object relationships you need to report on
- `formula-and-rollup-fields` (so derived values are reportable)

## Critical concept
A CRT sets a **primary object** and up to 3 related objects, with each relationship as "with" (inner join) or "may or may not have" (outer join) — this choice changes the numbers. It also controls which fields (incl. lookups to other objects' fields) are exposable. Get the primary object + join type right; that's where cross-object reports go wrong.

## Automation level
Guided — Setup config (declarative).

## Steps
1. **List the reports the team can't build** and identify the object combos they need (e.g. Accounts w/ Opportunities w/ Products; Campaigns w/ Leads; Cases w/ Contacts).
2. **Create CRTs** with the correct primary object + relationships; choose join type deliberately ("with" vs "may or may not have").
3. **Expose the right fields** (including related-object and formula/rollup fields).
4. **Deploy CRTs** (mark Deployed, not In Development) and make available to the right profiles.
5. **Build/enable** the target reports on the new CRTs (feeds `revops-reports-and-dashboards`).

## Notes
- Join type ("with" vs "may/may not have") silently changes totals — pick it to match the question.
- CRTs are the unlock for cross-object + custom-object reporting; build them before blaming the report builder.
- Feeds `revops-reports-and-dashboards`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
