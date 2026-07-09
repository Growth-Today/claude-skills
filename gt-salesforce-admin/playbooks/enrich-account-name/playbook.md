---
name: enrich-account-name
description: "Enrich Account Name for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-enrichment
---

# Enrich Contact Account Name

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Populate missing Contact-level account name from the associated Account record. Useful for reporting that reads the Contact directly.

## Prerequisites
- `simple-salesforce`, credentials in `.env`

## Automation level
Fully automated via Flow (preferred) or API backfill.

## Steps
1. Find Contacts with `AccountId` set but a blank account-name display field, or Contacts with no `AccountId` at all (these need `/assign-unowned-records` logic or matching first).
2. For contacts with an Account, a record-triggered Flow copies `Account.Name` into the target field on create and edit.
3. Backfill existing records via API in bulk.
4. Report counts.

## Notes
- Contacts in Salesforce already relate to an Account via `AccountId`; this is mainly for orgs that also keep a free-text company field on the Contact.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
