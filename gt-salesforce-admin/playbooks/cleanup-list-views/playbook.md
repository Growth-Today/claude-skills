---
name: cleanup-list-views
description: "Cleanup List Views for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Cleanup List Views

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Remove unused, empty, or duplicate list view definitions across objects.

## Prerequisites
- Access to the objects and their list views

## Automation level
Hybrid. Tooling API can enumerate list views; cleanup is mostly manual.

## Steps
1. Enumerate list views per object (Lead, Contact, Account, Opportunity).
2. Flag views with zero matching records, near-duplicate filters, and personal views abandoned by inactive users.
3. Confirm not referenced by a report or a team process.
4. Delete or consolidate.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
