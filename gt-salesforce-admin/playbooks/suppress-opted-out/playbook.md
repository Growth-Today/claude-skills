---
name: suppress-opted-out
description: "Suppress Opted-Out Records for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: database-hygiene
---

# Suppress Opted-Out and Do-Not-Call Records

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Handle `HasOptedOutOfEmail = true` and `DoNotCall = true` for compliance. These are legal signals, not optional.

## Prerequisites
- `simple-salesforce`, credentials in `.env`

## Automation level
Hybrid. API discovery confirms the flags are respected everywhere; the opt-out itself is already set by the standard fields.

## Steps
1. Count Leads and Contacts with `HasOptedOutOfEmail = true`.
2. Count `DoNotCall = true`.
3. Verify these records are excluded from every active marketing list view and the marketing tool sync. Export any that are NOT excluded as a compliance gap.
4. If a separate `Suppressed__c` field drives sends, set it true on all opted-out records.
5. Report compliance status.

## Notes
- Never re-enable opt-out flags. This playbook only verifies and enforces them.
- Respect regional law (GDPR, CAN-SPAM, CASL). Opt-out is permanent unless the contact re-subscribes.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
