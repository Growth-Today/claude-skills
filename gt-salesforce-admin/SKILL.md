---
name: gt-salesforce-admin
description: Comprehensive Salesforce CRM administration toolkit by Growth Today (growthtoday.co). Use when the user asks about auditing a Salesforce org, CRM cleanup or data hygiene, RevOps maintenance, suppressing bounced or opted-out leads and contacts, enriching lead/contact/account data, fixing lead status or opportunity stages, building list views, reports, dashboards, lead scoring or ICP tiers, deduplicating with matching/duplicate rules, profiles/permission sets/roles/sharing and field-level security, validation rules, record types, Flow automation, lead routing, products/forecasting, Data Loader imports, Salesforce↔HubSpot sync, or Agentforce/AI readiness. Also triggers on "salesforce audit", "sfdc cleanup", "permission sets", "sharing rules", "validation rules", "record types", "salesforce flow", "opportunity stages", "forecasting", "data loader", "salesforce hubspot sync", "agentforce". Do NOT use for non-Salesforce CRMs (HubSpot, Pipedrive) — Salesforce org administration only.
license: MIT
metadata:
  author: growthtoday
  version: "2.0.0"
  category: crm-administration
---

# GT Salesforce Admin — Master Router

Master orchestrator for Salesforce CRM administration & RevOps: **52 playbooks across 8 sub-skills** covering audit, data hygiene, data model, segmentation, opportunities & sales, automation, reporting, security & access, and governance/integrations.

## Setup (run once per session)

1. Use Glob to find `**/gt-salesforce-admin/SKILL.md`.
2. The directory containing it is `SKILL_BASE`.
3. Sub-skills live at `{SKILL_BASE}/.claude/skills/<sub-skill>/gt-SKILL.md`.
4. Playbooks live at `{SKILL_BASE}/playbooks/<name>/playbook.md` (shared — sub-skills route to them).

Always resolve `SKILL_BASE` dynamically — never hardcode a path.

## The Salesforce object model (read before any playbook)

- **Lead** — pre-conversion person; `Status`, `Rating`, `IsConverted`. Does not exist in HubSpot.
- **Contact** — post-conversion person, tied to an Account via `AccountId`.
- **Account** — company (`OwnerId`, `Industry`, `BillingCountry`).
- **Opportunity** — deal (`StageName`, `Amount`, `CloseDate`, `IsClosed`, `IsWon`).
- **User** — the owner; `OwnerId` points here; deactivated = `IsActive=false`.
- **Lead/Contact split:** when auditing "people," query BOTH Lead and Contact. HubSpot "contacts" map to "Leads AND Contacts" here.

## How routing works

1. Read the request. 2. Match to ONE OR MORE sub-skills below. 3. Read that sub-skill's `gt-SKILL.md` (its playbook index + guidance). 4. Read the specific `{SKILL_BASE}/playbooks/<name>/playbook.md` before acting. 5. Full-org / recurring requests → use the cross-cutting playbooks.

## Sub-skill routing

| User intent | Sub-skill | Path |
|---|---|---|
| Dedup, suppression, deliverability, enrichment, cleanup, form cleanup | **sf-data-hygiene** | `{SKILL_BASE}/.claude/skills/sf-data-hygiene/gt-SKILL.md` |
| Validation rules, record types/layouts, formula/rollup, matching/duplicate rules, custom objects, field cleanup | **sf-data-model** | `{SKILL_BASE}/.claude/skills/sf-data-model/gt-SKILL.md` |
| List views, reports-as-segments, ICP tiers, lead scoring | **sf-segmentation** | `{SKILL_BASE}/.claude/skills/sf-segmentation/gt-SKILL.md` |
| Sales process/stages, lead conversion, products/price books, forecasting, campaigns | **sf-opportunities-sales** | `{SKILL_BASE}/.claude/skills/sf-opportunities-sales/gt-SKILL.md` |
| Flow patterns, lead routing, lifecycle & hygiene flows, flow cleanup | **sf-automation-flow** | `{SKILL_BASE}/.claude/skills/sf-automation-flow/gt-SKILL.md` |
| Custom report types, RevOps reports & dashboards | **sf-reporting** | `{SKILL_BASE}/.claude/skills/sf-reporting/gt-SKILL.md` |
| Profiles, permission sets, roles, OWD/sharing, field-level security | **sf-security-access** | `{SKILL_BASE}/.claude/skills/sf-security-access/gt-SKILL.md` |
| Users/ownership, Data Loader/imports, SF↔HubSpot sync, Agentforce/AI readiness | **sf-governance-integrations** | `{SKILL_BASE}/.claude/skills/sf-governance-integrations/gt-SKILL.md` |

## Cross-cutting playbooks (full-org / recurring)

- **salesforce-audit** — full diagnostic audit. Read `{SKILL_BASE}/playbooks/salesforce-audit/playbook.md`
- **salesforce-implementation-plan** — phased plan from an audit. Read `{SKILL_BASE}/playbooks/salesforce-implementation-plan/playbook.md`
- **weekly-cleanup-routine** — 5-minute weekly health check. Read `{SKILL_BASE}/playbooks/weekly-cleanup-routine/playbook.md`
- **quarterly-org-cleanup** — comprehensive quarterly audit. Read `{SKILL_BASE}/playbooks/quarterly-org-cleanup/playbook.md`

## Prerequisites (apply to most playbooks)

- Salesforce auth in `.env`: `SF_USERNAME`, `SF_PASSWORD`, `SF_SECURITY_TOKEN`, `SF_DOMAIN` (login|test). See `.env.example` + `requirements.txt` at the skill root.
- Python with `simple-salesforce` + `python-dotenv` (`pip install -r requirements.txt`).
- API Enabled + read/edit on the relevant objects/fields.
- Destructive ops: export a backup first (Recycle Bin is ~15 days only).

## Notes

- All playbooks are company-agnostic. Some are fully API-automated (SOQL/Bulk); many are Flow/Setup (UI) — each states its automation level.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
