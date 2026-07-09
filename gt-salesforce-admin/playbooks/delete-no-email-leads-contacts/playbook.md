---
name: delete-no-email-leads-contacts
description: "Delete No-Email Leads and Contacts for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: database-hygiene
---

# Delete or Quarantine No-Email Leads and Contacts

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Leads and Contacts with no email cannot be emailed and distort reporting. Unlike HubSpot, deleting does not change billing, but it does clean routing and segmentation.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- Data Loader export backup of both objects first (Recycle Bin holds 15 days only)

## Automation level
Fully automated via SOQL discovery + Bulk API. Default to quarantine (set a `Suppressed__c` flag or move to a "No Email" queue), not hard delete, unless the user explicitly asks to delete.

## Steps
1. Discover: `SELECT Id, Name, CreatedDate FROM Lead WHERE Email = null AND IsConverted = false` and the same on Contact (`Email = null`).
2. Export both to CSV under `output/`.
3. Decide with the user: quarantine (recommended) or delete.
4. Quarantine: bulk update `Suppressed__c = true` (create the field if missing, see note).
5. Delete: bulk delete via the Bulk API, in batches of 200.
6. Report counts before and after.

## Notes
- Contacts with no email but a valid phone may still be callable; check `Phone` before deleting and prefer quarantine.
- Converted leads are excluded so you never touch a record that became a Contact.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
