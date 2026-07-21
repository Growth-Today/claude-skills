---
name: validation-rules-setup
description: "Prevent bad data at entry with Salesforce validation rules — required formats, conditional requirements, and guardrails on Leads, Contacts, Accounts, Opportunities. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Validation Rules Setup

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Stop junk data before it's saved. **Validation rules** run on save and block the record with an error if a condition fails — the cheapest data-quality control there is. This is the prevention layer that makes the hygiene playbooks a one-time fix, not a forever chore.

## Prerequisites
- "Customize Application" permission
- `data-model` context: know which fields matter per object and stage
- Pairs with `matching-and-duplicate-rules` (dedup) and `cleanup-fields`

## Critical concept
A validation rule is a formula that returns TRUE to **block** the save. It fires on UI, API, and import (unlike some UI-only controls), but keep them targeted — over-strict rules break integrations and imports (add a bypass via a custom permission or a "Bypass VR" checkbox for admins/integration users). Prefer **required fields + picklists** first, validation rules for conditional logic.

## Automation level
Hybrid — API/Tooling to audit existing rules + data gaps; rule creation in Setup or Metadata API.

## Steps
1. **Audit blanks + bad formats:** count records missing key fields (email, phone, amount, close date) and bad formats. This is the case for each rule.
2. **Decide rules per object/stage (progressive):** e.g. Opportunity requires Amount + CloseDate before Stage = Proposal; Lead requires a valid email format; Account requires Website for ICP tiering. Require more as the record advances.
3. **Write rules** with clear error messages placed on the offending field. Use `ISBLANK`, `REGEX`, `ISPICKVAL`, and stage checks.
4. **Add bypass** for integration/admin users (custom permission checked in the rule) so syncs (e.g. HubSpot→SF) don't break.
5. **Backfill existing gaps** (validation rules only apply going forward) — list + fix current non-compliant records.
6. **Test** on UI + a sample import; confirm the rule blocks bad data and lets good data through.

## Notes
- Validation rules apply to API/import too — great for enforcement, but that's why integration users need a bypass.
- Don't over-require early; it pushes users to enter junk to get past the save.
- Pairs with `matching-and-duplicate-rules`, `record-types-and-page-layouts`, `fix-lead-status-and-stages`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
