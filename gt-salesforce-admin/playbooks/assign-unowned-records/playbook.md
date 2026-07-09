---
name: assign-unowned-records
description: "Assign Unowned Records for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-enrichment
---

# Assign Unowned Records

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Assign owners to Leads, Contacts, and Accounts with no active owner or stuck in a default queue. Closes routing and reporting blind spots.

## Prerequisites
- `simple-salesforce`, credentials in `.env`

## Automation level
Fully automated via Bulk Update, or via an Assignment Rule for ongoing routing.

## Steps
1. Find records whose `OwnerId` is a Queue or an inactive User.
2. Decide routing: round-robin, by territory, by ICP tier, or a single house owner.
3. Bulk update `OwnerId` to active Users.
4. For ongoing coverage, turn on a Lead Assignment Rule so new records never land unowned.
5. Report counts assigned.

## Notes
- Pairs with `/reassign-inactive-owners` (run together for full ownership cleanup).

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
