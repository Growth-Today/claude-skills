---
name: enrich-industry
description: "Enrich Industry for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-enrichment
---

# Enrich Industry

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Backfill Lead and Contact industry. Salesforce has NO native enrichment (unlike HubSpot), so this requires a third-party source plus a Flow.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- A third-party enrichment source: Apollo, Clearbit, Default, or a Clay table feeding Salesforce

## Automation level
Hybrid. Flow copies `Account.Industry` to the Contact where present; third-party fills the rest.

## Steps
1. For Contacts tied to an Account that has `Industry`, a Flow copies `Account.Industry` down to the Contact.
2. For Leads (no Account) and Accounts with a blank `Industry`, push them to the enrichment provider keyed on email domain or website.
3. Write the returned industry back via API, mapped to your `Industry` picklist values (do not write free text).
4. Report fill rate before and after.

## Notes
- Map provider industries to your picklist. Unmapped free text breaks segmentation, which is the whole point of enriching.
- For new records, fold this into `/new-record-hygiene-flow`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
