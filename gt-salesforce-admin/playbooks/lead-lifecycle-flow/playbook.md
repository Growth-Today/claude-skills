---
name: lead-lifecycle-flow
description: "Lead Lifecycle Flow for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation-flow
---

# Lead Lifecycle Flow

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Automate Lead Status progression and the triggers that move a Lead toward conversion. The Salesforce equivalent of HubSpot lifecycle-progression, adapted for the Lead-to-Opportunity model.

## Prerequisites
- Flow Builder access
- Defined Lead Status picklist and conversion criteria

## Automation level
Setup-only (Flow).

## Steps
1. New lead created -> set `Status = "Open - Not Contacted"`.
2. First activity logged -> `Status = "Working"`.
3. Qualified criteria met (e.g. meeting booked, score threshold) -> flag ready-to-convert and notify the owner.
4. On conversion, ensure Account, Contact, and Opportunity are created with correct defaults.
5. Build as record-triggered Flows, one per transition, each fired by its specific event.

## Notes
- Salesforce conversion creates three records at once. Make sure required fields on Account/Contact/Opportunity have defaults so conversion never fails.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
