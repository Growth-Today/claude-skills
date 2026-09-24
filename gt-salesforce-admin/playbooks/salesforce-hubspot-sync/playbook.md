---
name: salesforce-hubspot-sync
description: "Manage the Salesforce↔HubSpot integration safely: sync direction and field mappings per field, inclusion lists, dedupe, and change coordination so the two systems don't overwrite each other. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: integrations
---

# Salesforce ↔ HubSpot Sync

Created by [Growth Today](https://www.growthtoday.co) - AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Keep the two CRMs in harmony. A bad sync produces duplicates, overwrite wars, and endless sync errors. This is the Salesforce-side coordination discipline (twin of the HubSpot skill's sync playbook).

## Prerequisites
- Access to the HubSpot-Salesforce connector settings + Salesforce "Customize Application"
- `matching-and-duplicate-rules` (dedupe) + `validation-rules-setup` (with an integration-user bypass)
- The HubSpot admin as a partner (this is a two-system change)

## Critical concept
For every synced object/field, know the **sync direction** (SF→HS, HS→SF, bidirectional) and the **source of truth**. Bidirectional on a field with two owners = overwrite wars. Validation rules can **block the sync** - give the integration user a bypass. Inclusion lists control **which** records sync.

## Automation level
Hybrid - connector settings + SF config; API to audit synced records/errors.

## Steps
1. **Map what syncs:** each object/field → direction + source of truth. Flag bidirectional fields with two owners (overwrite risk).
2. **Fix mappings + types;** set the **inclusion list** so only intended records sync.
3. **Dedupe:** ensure the connector matches to existing records (email/domain) - pair with duplicate rules to avoid dupes on both sides.
4. **Bypass validation for the integration user** so legitimate syncs aren't blocked by validation rules.
5. **Work the sync error queue;** most errors are an SF validation rule or required-field mismatch - fix at the source.
6. **Coordination rule:** no changes to synced fields/picklists/stages without notifying the HubSpot admin.

## Notes
- Direction + source of truth per field is the whole game - bidirectional with two owners causes overwrite wars.
- Validation rules can silently block sync - bypass for the integration user.
- Twin of HubSpot's salesforce-sync-management; pairs with `matching-and-duplicate-rules`, `validation-rules-setup`.

---
Created by [Growth Today](https://www.growthtoday.co) - AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
