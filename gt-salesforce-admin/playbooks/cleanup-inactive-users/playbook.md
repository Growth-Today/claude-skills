---
name: cleanup-inactive-users
description: "Cleanup Inactive Users for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Cleanup Inactive Users

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Deactivate non-employee Users and reassign their orphaned records. Pairs with `/assign-unowned-records` and `/reassign-inactive-owners`.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- "Manage Users" permission

## Automation level
Hybrid. Reassignment is scriptable; deactivation is a Setup action.

## Steps
1. List active Users who are no longer employees (cross-check with HR or a leavers list).
2. BEFORE deactivating, reassign their records with `/reassign-inactive-owners` logic.
3. Deactivate the users in Setup (you cannot delete Users in Salesforce, only deactivate).
4. Free up the licenses.
5. Report users deactivated and records moved.

## Notes
- You can never hard-delete a User in Salesforce; deactivation is the end state. Reassign first or records become orphaned.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
