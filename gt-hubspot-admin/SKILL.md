---
name: gt-hubspot-admin
description: Comprehensive HubSpot CRM administration toolkit by Growth Today (growthtoday.co). Use when the user asks about auditing a HubSpot portal, CRM cleanup or data hygiene, RevOps maintenance, suppressing bounced or unsubscribed contacts, improving deliverability, enriching contact or company data, fixing lifecycle stages, building smart lists or lead scoring, classifying ICP tiers, deduplicating companies, reassigning owners from deactivated users, or building bounce, engagement, or lifecycle automation workflows. Also triggers on "hubspot audit", "hubspot cleanup", "ghost contacts", "hard bounce suppression", "fix lifecycle stage", "lead scoring", "smart lists", "ICP tiers", "duplicate companies", "deactivated owners", "hubspot workflow", "bounce monitoring", "sunset workflow", "geo data backfill", "quarterly database cleanup", "implementation plan after audit". Do NOT use for non-HubSpot CRMs (Salesforce, Pipedrive) — HubSpot portal administration only.
license: MIT
metadata:
  author: growthtoday
  version: "1.1.0"
  category: crm-administration
---

# GT HubSpot Admin

Master orchestrator skill for HubSpot CRM administration. Wraps 56 specialised playbooks covering audit, hygiene, enrichment, segmentation, automation, and ongoing maintenance.

## When to use this skill

Trigger on ANY HubSpot portal administration request: cleanup, audit, enrichment, suppression, deduplication, workflow building, list segmentation, lead scoring, owner management, lifecycle stage fixes, or routine maintenance. The skill routes the request to the right playbook below.

## How routing works

1. Read the user's request.
2. Match it to ONE OR MORE playbooks in the index below.
3. Read the matching `playbooks/<name>/playbook.md` file in full before acting.
4. If the playbook has a `scripts/` folder, those scripts are runnable Python files that call the HubSpot REST API via the `requests` library and read `.env` with `python-dotenv`. The inline code examples inside each `playbook.md` use the `hubspot-api-client` SDK instead — both read the same `HUBSPOT_ACCESS_TOKEN`.
5. If the request spans multiple playbooks (e.g. "do a full quarterly cleanup"), use `playbooks/quarterly-database-cleanup/playbook.md` or `playbooks/hubspot-implementation-plan/playbook.md` as the meta-orchestrator.

## Prerequisites (apply to most playbooks)

- HubSpot private app API token as `HUBSPOT_ACCESS_TOKEN=pat-na1-xxxx`. Scripts load it from a `.env` file **in their own playbook folder** (`playbooks/<name>/.env`) via `python-dotenv` — copy the provided `.env.example` there. See `requirements.txt` at the skill root.
- Python 3.10+ with dependencies installed: `pip install -r requirements.txt` (or `uv add requests python-dotenv hubspot-api-client`). `requests` + `python-dotenv` power the scripts; `hubspot-api-client` powers the SDK examples in the playbooks.
- Read access to the relevant HubSpot scopes (CRM objects, lists, properties, workflows, owners — varies by playbook)

Each playbook lists its own specific prerequisites and required scopes in its `## Prerequisites` section. Always check those before executing.

## Playbook index

### Audit & planning (2)

- **`hubspot-audit`** — full diagnostic audit across 8 dimensions (contacts, companies, deals, engagement, data quality, deliverability) with grades and prioritized recommendations. Use when starting a CRM cleanup, onboarding a new client, or running quarterly health checks.
- **`hubspot-implementation-plan`** — generate a phased implementation plan from an audit report. Creates prioritized, sequenced cleanup processes with effort estimates, dependencies, and automation feasibility. Use after `hubspot-audit`.

### Database hygiene (9)

- **`delete-no-email-contacts`** — delete contacts with no email address (cannot receive any communication, inflate billing). Fully automated via CRM Search and Batch Archive APIs.
- **`merge-duplicate-companies`** — identify duplicate companies by domain and name, export audit CSVs, guide merging. API for discovery, manual UI or third-party tools for merging.
- **`reassign-deactivated-owners`** — reassign contacts and companies from deactivated team members to active owners. Fully automated via Owners API and Batch Update API.
- **`suppress-ghost-contacts`** — suppress contacts who received marketing emails but never opened any. Hybrid: API for discovery, manual UI for suppression.
- **`suppress-global-unsubscribes`** — suppress globally unsubscribed contacts for legal compliance and reduced billing. Hybrid: API for discovery, manual UI for suppression.
- **`suppress-hard-bounced`** — suppress hard-bounced contacts to protect sender reputation. Hybrid: API for discovery, manual UI for suppression.
- **`dedupe-contacts`** — find and merge duplicate contacts by email and name+company; documents trusted match rules. Complements `merge-duplicate-companies`.
- **`data-quality-command-center`** — operate HubSpot's native Data Quality Command Center: monitor duplicates, formatting issues, and property anomalies, then automate recurring fixes.
- **`contact-data-decay-review`** — find decayed records (stale activity, job changes, unengaged) and route to re-verify / enrich / re-engage / suppress before decay corrupts targeting.

### Data enrichment (5)

- **`assign-unowned-contacts`** — assign owners to marketing contacts that have no owner. Closes blind spots in routing and reporting.
- **`enrich-company-name`** — populate missing contact company name fields from associated company records. HubSpot workflow + optional API backfill.
- **`enrich-industry`** — backfill contact-level industry from associated company records via HubSpot workflow. Enables industry-based segmentation.
- **`fix-lifecycle-stages`** — ensure all contacts and companies have appropriate lifecycle stages. Backfills missing, fixes stuck, prevents future gaps.
- **`standardize-geo-values`** — convert inconsistent country/state/region formats to standardized values. Required for reliable geographic segmentation.

### Segmentation & scoring (5)

- **`build-lead-scoring`** — build separate Fit and Engagement scoring models using HubSpot's new Lead Scoring tool. Replaces deprecated HubSpot Score property.
- **`build-smart-lists`** — create foundational segmented lists (master sendable, ICP-based, persona, engagement, behavioral) — all active/dynamic.
- **`create-icp-tiers`** — classify companies into ICP tiers based on firmographic data (industry + employee count). Creates custom property + 4 classification workflows.
- **`lead-status-taxonomy`** — define a clear lead status value set with entry/exit definitions and the MQL/SQL handoff trigger; distinct from lifecycle stage.
- **`marketing-contacts-management`** — control marketing-contact status to cut billing waste: set unengaged/non-sendable contacts non-marketing and automate it.

### Automation workflows (6)

- **`bounce-monitoring-workflow`** — auto-suppress contacts above a configurable bounce threshold, alert on hard bounces, flag for weekly review.
- **`engagement-suppression-workflow`** — two-tier sunset workflow that re-engages dormant contacts before suppression.
- **`lifecycle-progression-workflow`** — automate Lead → MQL → SQL → Opportunity → Customer transitions, each triggered by a specific event.
- **`new-contact-hygiene-workflow`** — auto-enrich and stage new contacts upon creation. Sets lifecycle stage, copies company name and industry, branches on completeness.
- **`lead-routing-round-robin`** — automatically route qualified leads to reps via round-robin + criteria, with a fallback owner and SLA task/notification.
- **`workflow-naming-governance`** — naming conventions, folders, ownership, and documentation so workflows don't conflict, duplicate, or run unmonitored.

### Governance, permissions & security (3)

- **`users-teams-setup`** — structure users into teams (primary + additional) so routing, reporting rollups, and record visibility work. Audits users with no team.
- **`permission-sets-roles`** — apply least-privilege access with reusable permission sets; define a role matrix by job function and minimize Super Admins.
- **`security-health-audit`** — harden the account: minimize Super Admins, enforce 2FA/SSO, and reassign + deactivate stale users safely (frees seats).

### Reporting & dashboards (2)

- **`revops-core-dashboards`** — build the core RevOps dashboards (pipeline health, stage conversion, lifecycle velocity, forecast, data quality) scoped to the right audience.
- **`custom-report-builder-guide`** — pick the right report type (single/cross-object/funnel/attribution/cohort) and build reports that reconcile with source-of-truth.

### Data model & properties (6)

- **`property-architecture-governance`** — bring order to property sprawl: naming conventions, property groups, correct field types, source-of-truth ownership, and a governance process. The "build" counterpart to `cleanup-properties`.
- **`property-validation-rules`** — prevent bad data at entry: convert free-text to dropdowns, configure validation rules (email/phone/number formats), and set required fields.
- **`import-data-onboarding`** — import external data cleanly: pre-import file cleanup, column mapping, dedup on import, association imports, and post-import validation + rollback.
- **`custom-objects-setup`** — decide when a custom object is warranted (vs a property/existing object) and set up its schema, properties, associations, and pipeline (Enterprise).
- **`association-labels-setup`** — label how records relate (decision maker, billing contact, parent/child) so relationships are usable in lists, workflows, and reports.
- **`calculated-rollup-properties`** — auto-derive values with calculation (same-record formulas) and rollup (aggregate across associated records) properties; no brittle workflows.

### Pipelines & deals (7)

- **`deal-pipeline-architecture`** — design deal stages around buyer commitments (not rep actions), remove fake/zombie stages, set entry/exit criteria and win probabilities. Foundation for reliable forecasting.
- **`deal-stage-required-fields`** — require the right deal properties before a deal can advance to each stage; restrict backward moves and lock closed deals. Enforces the pipeline's exit criteria.
- **`deal-rotting-alerts`** — set a max age per stage, audit deals that exceed it, and build date-based workflows + a dashboard to surface and act on stale pipeline.
- **`cleanup-deals`** — standardize deal data, remove test deals, address missing amounts/close dates. Coordinates with Salesforce sync.
- **`multiple-pipelines-setup`** — add additional deal pipelines only when the process genuinely differs; set distinct stages, permissions, and consolidated reporting.
- **`forecasting-goals-setup`** — configure the forecast tool and team/rep goals; track attainment with sales analytics.
- **`renewal-automation`** — auto-create renewal deals ahead of contract end, assign owners, and trigger the renewal motion so recurring revenue doesn't slip.

### Ongoing maintenance (11)

- **`backfill-geo-data`** — enrich missing geographic data (country, state, city) on contacts and companies via workflows, external providers, or IP-based geolocation.
- **`cleanup-dashboards`** — audit and consolidate reporting dashboards (manual — no dashboard API).
- **`cleanup-forms`** — remove unused, test, or deprecated forms (zero submissions, not embedded, dev leftovers).
- **`cleanup-lead-owners`** — remove non-employee users from HubSpot and reassign their orphaned records. Pairs with `assign-unowned-contacts`.
- **`cleanup-lists`** — remove unused, empty, or duplicate list definitions (zero members, not used by workflow/email, overlapping criteria).
- **`cleanup-properties`** — archive or delete unused custom properties across all object types (contacts, companies, deals).
- **`cleanup-workflows`** — remove inactive, test, or deprecated workflows (never enrolled, off 90+ days, test workflows).
- **`create-segment-lists`** — business segment lists for customers, partners, competitors, employees, ICP tiers, industries.
- **`quarterly-database-cleanup`** — comprehensive quarterly audit (list health, bounces, data quality, scoring, engagement, properties) with QoQ trend comparison.
- **`review-bounced-contacts`** — weekly manual review of contacts with 3+ bounce events: delete or attempt recovery.
- **`weekly-cleanup-routine`** — 5-minute weekly health check: bounce monitoring, new contact quality, workflow health, list growth, data quality sampling.

## Cross-playbook dependencies

A few playbooks reference each other. Resolve in this order if running together:

- `hubspot-audit` → `hubspot-implementation-plan` (audit feeds the plan)
- `cleanup-lead-owners` ↔ `assign-unowned-contacts` (run together for full ownership cleanup)
- `bounce-monitoring-workflow` → `review-bounced-contacts` (workflow flags, manual review processes)
- `weekly-cleanup-routine` and `quarterly-database-cleanup` reference most other playbooks as their components

## Notes

- All playbooks are company-agnostic — no customer data, credentials, or proprietary references.
- Some playbooks are fully API-automated; others are hybrid (API discovery + manual UI execution) due to HubSpot API limitations (e.g. `hs_marketable_status` is read-only, no bulk merge API for companies, no dashboards API). Each playbook clearly states its automation level.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
