---
name: setup-roles-and-record-access
description: "Design the record-visibility model: role hierarchy, org-wide defaults (OWD), and sharing rules — so users see exactly the records they should. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: security-access
---

# Roles & Record Access (Hierarchy, OWD, Sharing)

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Control which **records** each user can see. In Salesforce this is a layered model — get the order right and visibility "just works"; get it wrong and either everyone sees everything or reps can't see their own accounts.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- "Manage Roles", "Manage Sharing"; Metadata API for sharing rules
- `audit-profiles-permission-sets` done (object/field access) — this playbook is about *record* access

## Critical concept: the visibility layers (in order)
1. **Org-Wide Defaults (OWD)** — the baseline per object: Private / Public Read Only / Public Read/Write. Start **restrictive** (Private) and open up deliberately.
2. **Role hierarchy** — managers see records owned by people below them (record roll-up). Mirrors the reporting/management structure, not the org chart exactly.
3. **Sharing rules** — open access sideways (e.g. share a region's accounts with a team) beyond OWD + hierarchy.
4. (Manual/Apex sharing, teams) for exceptions.

Rule of thumb: **OWD as tight as possible, then open with hierarchy + sharing rules.** Opening OWD to Public is the #1 cause of "everyone sees everything."

## Automation level
Hybrid — API for auditing current OWD/roles/sharing; changes in Setup or via Metadata API.

## Steps
1. **Audit current state:** OWD per object; the role hierarchy + user-to-role assignments; existing sharing rules. Flag any object set to Public Read/Write that shouldn't be.
2. **Design the role hierarchy:** mirror who-manages-whom for record roll-up (drives both visibility and hierarchical reporting). Keep it as flat as reporting needs allow.
3. **Set OWD:** tighten to Private (or Public Read Only) where records should be owner/team-scoped (Leads, Opportunities, Accounts typically Private in B2B).
4. **Add sharing rules** for the legitimate sideways access (region teams, cross-functional visibility) — owner-based or criteria-based.
5. **Assign users to roles;** verify a sample rep sees their own + their team's records and not others'.
6. **Document + review** as part of `quarterly-org-cleanup`.

## Notes
- Role hierarchy drives BOTH record visibility and hierarchical report roll-up — design it once, deliberately.
- Public Read/Write OWD makes sharing rules pointless and leaks data — avoid unless truly needed.
- Pairs with `audit-profiles-permission-sets` (object/field access) and `reassign-inactive-owners` (ownership).

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
