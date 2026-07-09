---
name: fix-lead-status-and-stages
description: "Fix Lead Status and Opportunity Stages for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-enrichment
---

# Fix Lead Status and Opportunity Stages

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

The Salesforce equivalent of HubSpot lifecycle stages, split across two objects: Lead `Status` (pre-conversion) and Opportunity `StageName` (deal). Backfill missing, fix stuck, prevent future gaps.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- The org's defined Lead Status picklist and Opportunity sales process

## Automation level
Hybrid. API backfill + Flow for prevention + Validation Rule for enforcement.

## Steps
1. **Leads**: find `Status = null` or a value not in the active picklist. Map each to the correct status (new imports -> "Open - Not Contacted"; ones with activity -> "Working"; etc.).
2. **Opportunities**: find `StageName = null`, or open opps whose stage does not match their activity (e.g. an opp with a signed contract still in "Prospecting").
3. Bulk update to correct values.
4. Add a record-triggered Flow that sets a default status/stage on create.
5. Add a Validation Rule requiring Status on Lead and Stage on Opportunity. Add this LAST so the backfill is not blocked.
6. Report counts fixed.

## Notes
- Do not invent stages. Use the org's existing picklist and sales process exactly.
- Converted leads keep their final status; do not rewrite history.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
