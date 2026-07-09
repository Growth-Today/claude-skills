---
name: reassign-inactive-owners
description: "Reassign Inactive-Owner Records for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: database-hygiene
---

# Reassign Records from Inactive Users

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Reassign Leads, Contacts, Accounts, and Opportunities owned by deactivated Users (`IsActive = false`) to active reps. Orphaned ownership breaks routing, reporting, and forecasting.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- "Modify All Data" or object-level edit on all four objects

## Automation level
Fully automated via Bulk Update.

## Steps
1. `SELECT Id, Name FROM User WHERE IsActive = false` -> collect inactive Ids.
2. For each object, count and export records `WHERE OwnerId IN (:inactiveIds)`. Batch the IN list (200 Ids max per query).
3. Decide the reassignment target with the user: a single active "house" owner, round-robin across a team, or by territory.
4. Bulk update `OwnerId` to the chosen active User. For Leads sitting in a Queue, decide whether to keep them queued or assign to a user.
5. Report counts moved per object.

## Notes
- Reassigning Opportunities changes forecast attribution. Confirm the rule with sales leadership.
- Pairs with `/cleanup-inactive-users` (run that to actually remove the users afterward).

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
