---
name: gt-hubspot-admin
description: Comprehensive HubSpot CRM administration toolkit by Growth Today (growthtoday.co). Use when the user asks about auditing a HubSpot portal, CRM cleanup or data hygiene, RevOps maintenance, suppressing bounced or unsubscribed contacts, improving deliverability, enriching contact or company data, fixing lifecycle stages, building smart lists or lead scoring, classifying ICP tiers, deduplicating contacts or companies, reassigning owners, building deal pipelines, reporting and dashboards, users and permissions, or bounce, engagement, and lifecycle automation workflows. Also triggers on "hubspot audit", "hubspot cleanup", "ghost contacts", "hard bounce suppression", "fix lifecycle stage", "lead scoring", "smart lists", "ICP tiers", "duplicate contacts", "deal pipeline", "custom objects", "hubspot reporting", "user permissions", "hubspot workflow", "quarterly database cleanup". Do NOT use for non-HubSpot CRMs (Salesforce, Pipedrive) — HubSpot portal administration only.
license: MIT
metadata:
  author: growthtoday
  version: "2.0.1"
  category: crm-administration
---

# GT HubSpot Admin — Master Router

Master orchestrator for HubSpot CRM administration & RevOps: **68 playbooks across 7 sub-skills** covering audit, data hygiene, data model, segmentation, pipelines & deals, automation, reporting, and governance.

## Setup (run once per session)

Before loading any sub-skill or playbook, resolve this skill's install directory:

1. Use Glob to find `**/gt-hubspot-admin/SKILL.md`.
2. The directory containing it is `SKILL_BASE`.
3. Sub-skills live at `{SKILL_BASE}/.claude/skills/<sub-skill>/gt-SKILL.md`.
4. Playbooks live at `{SKILL_BASE}/playbooks/<name>/playbook.md` (shared — sub-skills route to them).

Always resolve `SKILL_BASE` dynamically — never hardcode a path.

## How routing works

1. Read the user's request.
2. Match it to ONE OR MORE sub-skills below.
3. Read that sub-skill's `gt-SKILL.md` — it holds the playbook index and guidance for that domain.
4. Read the specific `{SKILL_BASE}/playbooks/<name>/playbook.md` in full before acting.
5. If a playbook has a `scripts/` folder, those are runnable Python files (`requests` + `python-dotenv`) reading `HUBSPOT_ACCESS_TOKEN` from a `.env` in the playbook folder.
6. Full-portal or recurring requests → use the cross-cutting playbooks below.

## Sub-skill routing

| User intent | Sub-skill | Path |
|---|---|---|
| Dedup, suppression, deliverability, enrichment, cleanup routines | **hubspot-data-hygiene** | `{SKILL_BASE}/.claude/skills/hubspot-data-hygiene/gt-SKILL.md` |
| Properties, custom objects, associations, validation, imports | **hubspot-data-model** | `{SKILL_BASE}/.claude/skills/hubspot-data-model/gt-SKILL.md` |
| Lists, ICP tiers, lead scoring, lead status, marketing contacts | **hubspot-segmentation** | `{SKILL_BASE}/.claude/skills/hubspot-segmentation/gt-SKILL.md` |
| Deal pipelines, stages, forecasting, renewals | **hubspot-pipelines-deals** | `{SKILL_BASE}/.claude/skills/hubspot-pipelines-deals/gt-SKILL.md` |
| Workflows, lead routing, lifecycle & notification automation | **hubspot-automation** | `{SKILL_BASE}/.claude/skills/hubspot-automation/gt-SKILL.md` |
| Dashboards, custom reports, attribution, SLA/KPIs | **hubspot-reporting** | `{SKILL_BASE}/.claude/skills/hubspot-reporting/gt-SKILL.md` |
| Users, teams, permissions, security, privacy, integrations | **hubspot-governance** | `{SKILL_BASE}/.claude/skills/hubspot-governance/gt-SKILL.md` |

## Cross-cutting playbooks (full-portal / recurring)

Use these directly for whole-portal engagements; each references playbooks across multiple sub-skills.

- **hubspot-audit** — full diagnostic audit across 8 dimensions with grades. Read `{SKILL_BASE}/playbooks/hubspot-audit/playbook.md`
- **hubspot-implementation-plan** — phased plan from an audit report. Read `{SKILL_BASE}/playbooks/hubspot-implementation-plan/playbook.md`
- **weekly-cleanup-routine** — 5-minute weekly health check. Read `{SKILL_BASE}/playbooks/weekly-cleanup-routine/playbook.md`
- **quarterly-database-cleanup** — comprehensive quarterly audit with QoQ trends. Read `{SKILL_BASE}/playbooks/quarterly-database-cleanup/playbook.md`

## Prerequisites (apply to most playbooks)

- HubSpot private app API token as `HUBSPOT_ACCESS_TOKEN=pat-na1-xxxx`. Scripts load it from a `.env` in their own playbook folder (`playbooks/<name>/.env`) via `python-dotenv` — copy `.env.example` there. See `requirements.txt` at the skill root.
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`pip install -r requirements.txt`). `requests` + `python-dotenv` power the scripts; `hubspot-api-client` powers the SDK examples in the playbooks.
- Read access to the relevant HubSpot scopes (varies by playbook).

## Notes

- All playbooks are company-agnostic — no customer data, credentials, or proprietary references.
- Some playbooks are fully API-automated; others are hybrid (API discovery + manual UI) due to HubSpot API limits. Each playbook states its automation level.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
