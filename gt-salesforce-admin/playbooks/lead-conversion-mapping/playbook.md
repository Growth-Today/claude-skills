---
name: lead-conversion-mapping
description: "Configure lead conversion so no data is lost: map custom Lead fields to Contact/Account/Opportunity, set conversion defaults, and dedupe on convert. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: opportunities-sales
---

# Lead Conversion Field Mapping

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

When a Lead converts, Salesforce creates/links a Contact, Account, and (optionally) Opportunity — but **custom Lead fields are lost unless mapped**. This playbook makes conversion clean, complete, and duplicate-safe.

## Prerequisites
- "Customize Application" + "Manage Leads"
- `matching-and-duplicate-rules` (so convert doesn't create dupes)
- Know which custom Lead fields must survive conversion

## Critical concept
Standard Lead fields map automatically; **custom Lead fields map only if you configure Lead field mapping** (Setup → Object Manager → Lead → Map Lead Fields), field-type-compatible with the target Contact/Account/Opportunity field. Unmapped data is silently dropped on convert.

## Automation level
Guided — Setup config; API/report to verify data retention post-convert.

## Steps
1. **Inventory custom Lead fields** and their intended target (Contact/Account/Opportunity). Create matching target fields where missing (compatible type).
2. **Configure Lead field mapping** for each custom field.
3. **Set conversion behavior:** default Opportunity creation on/off, default Lead Status = "Converted", and whether to use existing Account/Contact when matched (dedupe on convert via duplicate rules).
4. **Handle dedupe:** ensure conversion links to existing Contacts/Accounts rather than creating duplicates (matching/duplicate rules).
5. **Test a conversion** end to end: confirm all mapped fields land on the right records and no data is lost; confirm no duplicate Account/Contact.
6. **Document** the mapping for the team.

## Notes
- Unmapped custom fields are lost on convert — the #1 silent data loss in Salesforce. Audit this before any migration.
- Pairs with `matching-and-duplicate-rules` (avoid dupes on convert) and `fix-lead-status-and-stages`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
