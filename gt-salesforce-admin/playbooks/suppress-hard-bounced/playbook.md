---
name: suppress-hard-bounced
description: "Suppress Hard Bounced for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: database-hygiene
---

# Suppress Hard Bounced Leads and Contacts

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Flag hard-bounced records to protect sender reputation. In Salesforce the signal is `EmailBouncedReason` / `EmailBouncedDate` populated.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- A suppression field on Lead and Contact

## Automation level
Hybrid. API discovery + suppression-field flagging.

## Steps
1. Discover: `WHERE EmailBouncedReason != null` on Lead (unconverted) and Contact.
2. Export to CSV with the bounce reason and date.
3. Flag `Suppressed__c = true` in bulk.
4. Exclude from marketing sends via the connected tool.
5. Feed the count into `/review-bounced-records` for the weekly recovery pass.

## Notes
- A hard bounce is permanent (bad address). A soft bounce is temporary; do not suppress soft bounces here.
- Pairs with `/bounce-monitoring-flow` for ongoing prevention.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
