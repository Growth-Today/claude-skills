---
name: campaigns-and-influence
description: "Set up Campaigns, Campaign Members, and Campaign Influence so marketing's impact on pipeline and revenue is measurable in Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: opportunities-sales
---

# Campaigns & Campaign Influence

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Connect marketing activity to pipeline. **Campaigns** track marketing efforts; **Campaign Members** link Leads/Contacts to them; **Campaign Influence** attributes Opportunities to the campaigns that touched them.

## Prerequisites
- "Marketing User" permission + campaign access
- `lead-conversion-mapping` (so campaign membership survives conversion)
- Marketing tool sync (HubSpot/Pardot/etc.) if campaigns come from there

## Critical concept
- **Campaign** = a marketing effort with a hierarchy, budget, and member statuses. **Campaign Member** = a Lead/Contact's relationship + status (Sent/Responded).
- **Campaign Influence** attributes Opportunities to campaigns (primary campaign source + optional customizable/multi-touch influence models) — this is how you report marketing-sourced/influenced pipeline.
- Keep campaign naming + member-status models consistent, or reporting is noise.

## Automation level
Hybrid — API/Data Loader for member import; setup + influence models in Setup.

## Steps
1. Define a **campaign naming convention** + standard member statuses.
2. Set up **Campaign Influence** (enable, choose model: primary source and/or customizable/multi-touch where licensed).
3. Ensure **campaign membership persists on lead conversion** and syncs from the marketing tool.
4. Add **Primary Campaign Source** on Opportunities (auto via automation where possible).
5. **Report:** marketing-sourced and influenced pipeline/revenue (needs campaign-aware report types — `custom-report-types`).

## Notes
- Multi-touch influence models may require higher editions/licenses — confirm before promising.
- Consistent naming + member statuses are what make campaign reporting trustworthy.
- Pairs with `lead-conversion-mapping`, `custom-report-types`, `salesforce-hubspot-sync`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
