---
name: new-record-hygiene-flow
description: "New Record Hygiene Flow for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation-flow
---

# New Record Hygiene Flow

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Auto-enrich and stage new Leads and Contacts on creation. Sets status, copies account name and industry, branches on completeness. The Salesforce equivalent of HubSpot new-contact-hygiene.

## Prerequisites
- Flow Builder access

## Automation level
Setup-only (Flow).

## Steps
1. Record-triggered Flow on Lead create: set default `Status`, default `LeadSource` if blank, normalize country/state to picklist values.
2. Record-triggered Flow on Contact create: copy `Account.Industry` and account name down if blank.
3. Branch: if email is missing or invalid, route to a "needs review" queue instead of the normal assignment.
4. Trigger enrichment (call out to the provider, or flag for the `/enrich-industry` batch).
5. Activate and test with a sample insert.

## Notes
- Keep the Flow lightweight; heavy callouts on every insert hit limits. Flag-and-batch is safer than synchronous enrichment.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
