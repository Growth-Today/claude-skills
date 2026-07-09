---
name: create-icp-tiers
description: "Create ICP Tiers for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: segmentation-scoring
---

# Create ICP Tiers

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Classify Accounts into ICP tiers from firmographic data (industry + employee count). Creates a custom picklist field plus classification logic.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- `Industry` and employee-count fields populated (run `/enrich-industry` first if sparse)

## Automation level
Hybrid. Setup creates the field; Flow or API classifies.

## Steps
1. Create a custom picklist `ICP_Tier__c` on Account (Tier 1 / Tier 2 / Tier 3 / Out of ICP).
2. Define the rule per tier (e.g. Tier 1 = target industry AND 200+ employees).
3. Classify existing Accounts via API batch update.
4. Add a record-triggered Flow to classify new and updated Accounts.
5. Roll the tier down to related Leads/Contacts if your views need it.
6. Report tier distribution.

## Notes
- Run AFTER enrich-industry and standardize-geo, since the rule reads those fields.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
