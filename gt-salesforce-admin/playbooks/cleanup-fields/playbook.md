---
name: cleanup-fields
description: "Cleanup Fields for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Cleanup Custom Fields

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Archive or delete unused custom fields across Lead, Contact, Account, Opportunity. Dead fields slow page loads and confuse users and AI agents.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- Tooling API access for utilization checks

## Automation level
Hybrid. Utilization analysis via Tooling API; deletion is a Setup action.

## Steps
1. List every custom field per object.
2. For each, check utilization: on a page layout? referenced in a report? used in a Validation Rule, Flow, or Apex? populated on any records?
3. Flag dead fields (zero usage everywhere) for safe removal.
4. Confirm with the user, then delete (or first deprecate by removing from layouts and waiting a cycle).
5. Report fields removed.

## Notes
- A field can be unpopulated but still referenced in Apex. Always check code references before deleting.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
