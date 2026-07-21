---
name: field-level-security-audit
description: "Audit field-level security (FLS): which profiles/permission sets can view or edit each field, protect sensitive fields, and remove accidental exposure. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: security-access
---

# Field-Level Security Audit

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Object access says "you can see Accounts"; **field-level security** says "you can (or can't) see the Account's revenue field." FLS is where sensitive data quietly leaks or where reps can edit fields they shouldn't. This audit maps and tightens field access.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- "View Setup", "Manage Profiles and Permission Sets"; Tooling/Metadata API for a full FLS export
- `audit-profiles-permission-sets` done (FLS is set on profiles + permission sets)

## Critical concept
FLS is defined **per profile and per permission set**, per field, as Visible / Read-Only / Hidden. It overrides page layouts (a field on a layout is still hidden if FLS hides it). Sensitive fields (revenue, PII, comp, scoring internals) should be Hidden or Read-Only for most roles and Visible only where needed.

## Automation level
Hybrid — API/Tooling for discovery; changes in Setup or via Metadata API.

## Steps
1. **Inventory sensitive fields:** list fields holding PII, financials, internal scores, or compliance data across Lead, Contact, Account, Opportunity (and custom objects).
2. **Export FLS:** for each sensitive field, which profiles/permission sets have Visible / Edit. (FieldPermissions via Tooling API.)
3. **Flag exposure:** sensitive fields Visible/Editable to broad profiles or all users → tighten to Read-Only or Hidden except where required.
4. **Fix by permission set:** grant field access via permission sets (not by widening a profile), so it's targeted and auditable.
5. **Verify:** confirm a standard rep can't see/edit the sensitive fields; a privileged role can. Check reports/list views don't leak the field.
6. **Document + schedule review** (quarterly).

## Notes
- FLS overrides layouts — a "hidden" field on a layout is still exposed if FLS says Visible. Always check FLS, not just layouts.
- Grant sensitive-field access via permission sets, never by loosening a base profile.
- Pairs with `audit-profiles-permission-sets` and (for compliance) suppression/opt-out playbooks.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
