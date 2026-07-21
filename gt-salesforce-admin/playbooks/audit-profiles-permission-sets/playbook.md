---
name: audit-profiles-permission-sets
description: "Audit and modernize access: profiles vs permission sets vs permission set groups, least-privilege review, and migration to a permission-set-based model. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: security-access
---

# Audit Profiles & Permission Sets

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Bring order to who-can-do-what. Salesforce is moving away from permission-heavy **profiles** toward **permission sets** and **permission set groups**; most orgs accumulate permission creep (broad access granted quickly, never reviewed). This audit surfaces over-permissioned users and gives you a clean, least-privilege model.

## Prerequisites
- `simple-salesforce`, credentials in `.env` (see `requirements.txt` at the skill root)
- "View Setup and Configuration" + "Manage Users"; Metadata/Tooling API access for a full export
- Ideally run `salesforce-audit` first

## Critical concept: profile vs permission set vs group
- **Profile** — one per user, sets the baseline (object/field defaults, login hours, page layout assignment). Keep profiles **minimal**.
- **Permission set** — additive grants layered on top; assign the same set to many users. This is where access should live.
- **Permission set group** — bundles permission sets by job function (e.g. "AE"), assigned as one unit; use **muting** to remove specific perms.
- The modern model: lean profiles + role-based permission set groups. Never grant "Modify All Data" broadly.

## Automation level
Hybrid — API/Tooling for discovery + audit; assignment changes in Setup or via Metadata API.

## Steps
1. **Inventory:** list profiles and their user counts; list permission sets + permission set groups and their assignments. (SOQL: `PermissionSetAssignment`, `PermissionSet`, `Profile`; counts of users per profile.)
2. **Flag dangerous perms:** find users/profiles/sets granting `PermissionsModifyAllData`, `PermissionsViewAllData`, `PermissionsManageUsers`, `PermissionsAuthorApex`. These are the blast-radius permissions — justify each.
3. **Find permission creep:** users with many overlapping sets, or profiles cloned per-person. Consolidate to role-based permission set groups.
4. **Design the target model:** lean baseline profiles + a permission set group per job function (AE, SDR, RevOps/Admin, Read-only). Map each user to one group.
5. **Migrate incrementally:** move object/field grants from profiles into permission sets; assign groups; remove redundant per-user sets. Test with a pilot user before rolling out.
6. **Document + schedule review:** record who has admin-level perms and re-review quarterly (fold into `quarterly-org-cleanup`).

## Notes
- Minimize users with "Modify All Data" / System Administrator — every one is a full-access account.
- Permission set groups + muting are the clean way to handle exceptions without cloning profiles.
- Pairs with `field-level-security-audit` and `setup-roles-and-record-access` for the full access picture.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
