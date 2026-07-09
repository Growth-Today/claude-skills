---
name: suppress-unengaged-leads
description: "Suppress Unengaged Leads and Contacts for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: database-hygiene
---

# Suppress Unengaged Leads and Contacts

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Flag Leads and Contacts that received marketing email but never engaged. Protects sender reputation and focuses outreach.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- A suppression field (`Suppressed__c` checkbox) on Lead and Contact, or a marketing-tool sync field

## Automation level
Hybrid. API discovery + suppression-field flagging. Actual send suppression happens in the connected marketing tool (Pardot/Account Engagement, Marketo, HubSpot).

## Steps
1. Define "unengaged": no `LastActivityDate` in 180+ days AND has been emailed (check activity history or the marketing sync field).
2. Discover on Lead and Contact separately, export to CSV.
3. Flag `Suppressed__c = true` in bulk.
4. Hand the list to the marketing tool to exclude from sends.
5. Report counts.

## Notes
- Do not delete; suppression preserves the record for re-engagement later.
- Pairs with `/engagement-suppression-flow` to automate this going forward.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
