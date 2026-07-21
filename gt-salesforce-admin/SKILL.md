---
name: gt-salesforce-admin
description: Comprehensive Salesforce CRM administration toolkit by Growth Today (growthtoday.co). Use when the user asks about auditing a Salesforce org, CRM cleanup or data hygiene, RevOps maintenance, suppressing bounced or opted-out leads and contacts, improving deliverability, enriching lead contact or account data, fixing lead status or opportunity stages, building list views lead scoring or ICP tiers, deduplicating accounts leads and contacts, reassigning records from inactive users, or building bounce, engagement, or lifecycle automation with Flow. Also triggers on "salesforce audit", "salesforce cleanup", "sfdc audit", "stale leads", "fix lead status", "opportunity stage cleanup", "lead scoring salesforce", "matching rules", "duplicate rules", "duplicate accounts", "inactive owners", "salesforce flow", "validation rules", "lead conversion", "cleanup list views or flows or fields". Do NOT use for non-Salesforce CRMs (HubSpot, Pipedrive) — Salesforce org administration only.
license: MIT
metadata:
  author: growthtoday
  version: "1.0.1"
  category: crm-administration
---

# GT Salesforce Admin

Master orchestrator skill for Salesforce CRM administration. Wraps 39 specialised playbooks covering audit, hygiene, enrichment, segmentation, automation, and ongoing maintenance.

This is the Salesforce twin of `gt-hubspot-admin`. The structure mirrors it, but every playbook is ported to the Salesforce object model, API, and tooling. The key difference: Salesforce splits the pre-conversion Lead and the post-conversion Contact into two separate objects, uses Account and Opportunity instead of Company and Deal, has no native enrichment engine, and enforces data quality through Validation Rules, Matching Rules, and Duplicate Rules rather than HubSpot-style properties and workflows.

## When to use this skill

Trigger on ANY Salesforce org administration request: cleanup, audit, enrichment, suppression, deduplication, Flow building, list view or report segmentation, lead scoring, owner management, lead status or opportunity stage fixes, or routine maintenance. The skill routes the request to the right playbook below.

## How routing works

1. Read the user's request.
2. Match it to ONE OR MORE playbooks in the index below.
3. Read the matching `playbooks/<name>/playbook.md` file in full before acting.
4. If the playbook has a `scripts/` folder, those scripts are runnable Python files using the `simple-salesforce` package via `uv`.
5. If the request spans multiple playbooks (e.g. "do a full quarterly cleanup"), use `playbooks/quarterly-org-cleanup/playbook.md` or `playbooks/salesforce-implementation-plan/playbook.md` as the meta-orchestrator.

## The Salesforce object model (read before any playbook)

This is what makes Salesforce different from HubSpot. Every playbook assumes this model.

- **Lead** — a pre-conversion person. Not yet tied to an Account or Opportunity. Has `Status` (Lead Status), `Rating`, `LeadSource`, `IsConverted`, `ConvertedContactId`, `ConvertedAccountId`, `ConvertedOpportunityId`. This object does not exist in HubSpot, where everyone is a Contact.
- **Contact** — a post-conversion person, always tied to an Account via `AccountId`. Equivalent to a HubSpot contact after lifecycle progression.
- **Account** — a company. Equivalent to a HubSpot company. Has `OwnerId`, `Industry`, `Website`, `BillingCountry`, `BillingState`.
- **Opportunity** — a deal. Equivalent to a HubSpot deal. Has `StageName`, `Amount`, `CloseDate`, `IsClosed`, `IsWon`, `OwnerId`.
- **User** — the owner record. `OwnerId` on any object points to a User. A deactivated user has `IsActive = false`. Equivalent to a HubSpot owner.
- **Lead/Contact split rule**: when auditing "people," you must query BOTH Lead and Contact. A bounce, a missing field, or an inactive owner can exist on either. HubSpot playbooks that say "contacts" map to "Leads AND Contacts" here.

## Prerequisites (apply to most playbooks)

- A Salesforce connected app or username + password + security token, stored in `.env`:
  ```
  SF_USERNAME=user@company.com
  SF_PASSWORD=xxxx
  SF_SECURITY_TOKEN=xxxx
  SF_DOMAIN=login   # or test for sandbox
  ```
- Python with `simple-salesforce` installed via `uv`
- API Enabled permission and read/edit access to the relevant objects and fields (varies by playbook)
- For any destructive operation: a Data Loader export backup first. Salesforce has no undo for bulk deletes beyond the 15-day Recycle Bin.

Each playbook lists its own specific prerequisites in its `## Prerequisites` section. Always check those before executing.

## Playbook index

### Audit & planning (2)

- **`salesforce-audit`** — full diagnostic audit across 8 dimensions (leads, contacts, accounts, opportunities, engagement, data quality, deliverability, ownership) with grades and prioritized recommendations. Use when starting an org cleanup, onboarding a new client, or running quarterly health checks.
- **`salesforce-implementation-plan`** — generate a phased implementation plan from an audit report. Creates prioritized, sequenced cleanup processes with effort estimates, dependencies, and automation feasibility. Use after `salesforce-audit`.

### Database hygiene (6)

- **`delete-no-email-leads-contacts`** — delete or quarantine Leads and Contacts with no email address (cannot be emailed, distort reporting). API via SOQL + Bulk API.
- **`merge-duplicate-accounts`** — identify duplicate Accounts by website and name, export audit CSVs, guide merging via native merge (max 3 records, auto-reparents children) or Duplicate Rules.
- **`reassign-inactive-owners`** — reassign Leads, Contacts, Accounts, and Opportunities from deactivated Users (`IsActive = false`) to active reps. API via Bulk Update.
- **`suppress-unengaged-leads`** — flag Leads and Contacts that received marketing email but never opened any. Sets a suppression field; pairs with marketing tool sync.
- **`suppress-opted-out`** — handle `HasOptedOutOfEmail = true` and `DoNotCall = true` records for compliance. API discovery + field flagging.
- **`suppress-hard-bounced`** — flag hard-bounced Leads and Contacts (`EmailBouncedReason` / `EmailBouncedDate` populated) to protect sender reputation. API discovery + suppression field.

### Data enrichment (5)

- **`assign-unowned-records`** — assign owners to Leads, Contacts, and Accounts that have no active owner or sit in a default queue. Closes routing and reporting blind spots.
- **`enrich-account-name`** — populate missing Contact-level account name from the associated Account record via Flow + optional API backfill.
- **`enrich-industry`** — backfill Lead and Contact industry from the associated Account, or from a third-party source. Salesforce has no native enrichment, so this uses Flow plus an external provider.
- **`fix-lead-status-and-stages`** — ensure all Leads have a valid `Status` and all Opportunities a valid `StageName`. Backfills missing, fixes stuck, prevents future gaps. The Salesforce equivalent of HubSpot lifecycle stages, split across Lead Status and Opportunity Stage.
- **`standardize-geo-values`** — convert inconsistent country/state values to State and Country Picklists (Salesforce native standardization). Required for reliable geographic segmentation.

### Segmentation & scoring (3)

- **`build-lead-scoring`** — build a Fit and Engagement scoring model using Einstein Lead Scoring or a custom formula field on Lead `Rating`. Replaces blank Rating, which silently breaks routing and Agentforce.
- **`build-list-views-and-reports`** — create foundational segmented list views and reports (master sendable, ICP-based, persona, engagement, behavioral).
- **`create-icp-tiers`** — classify Accounts into ICP tiers based on firmographic data (industry + employee count). Creates a custom picklist field + classification via Flow or batch update.

### Automation (Flow) (4)

- **`bounce-monitoring-flow`** — scheduled Flow to auto-flag records above a bounce threshold, alert on hard bounces, flag for weekly review.
- **`engagement-suppression-flow`** — two-stage sunset Flow that re-engages dormant records before suppression.
- **`lead-lifecycle-flow`** — automate Lead Status progression and Lead-to-Opportunity conversion triggers, each fired by a specific event.
- **`new-record-hygiene-flow`** — auto-enrich and stage new Leads and Contacts on creation. Sets Lead Status, copies Account name and industry, branches on completeness.

### Data model (4)

- **`validation-rules-setup`** — prevent bad data at entry with validation rules (required formats, conditional requirements, stage gates) + integration bypass.
- **`record-types-and-page-layouts`** — support different processes on one object (record types drive Opportunity stages; layouts tailor fields per team).
- **`formula-and-rollup-fields`** — auto-derive values (same-record formulas, child→parent roll-up summaries) instead of brittle Flows.
- **`matching-and-duplicate-rules`** — prevent duplicates at create/edit (matching rules + alert/block duplicate rules); complements merge cleanup.

### Security & access (3)

- **`audit-profiles-permission-sets`** — audit profiles vs permission sets vs permission set groups, flag dangerous perms (Modify/View All Data), and migrate to a least-privilege, permission-set-based model.
- **`setup-roles-and-record-access`** — design the record-visibility model: role hierarchy, org-wide defaults (OWD), and sharing rules.
- **`field-level-security-audit`** — map FLS per profile/permission set, protect sensitive fields, and remove accidental exposure.

### Ongoing maintenance (12)

- **`backfill-geo-data`** — enrich missing geographic data (country, state, city) on Leads, Contacts, and Accounts via Flow, external providers, or IP-based geolocation.
- **`cleanup-dashboards`** — audit and consolidate dashboards (low-usage, broken source reports, duplicates).
- **`cleanup-opportunities`** — standardize pipelines and record types, remove test Opportunities, fix missing Amount/CloseDate, address stale open deals.
- **`cleanup-web-to-lead-forms`** — remove unused, test, or deprecated Web-to-Lead forms and their routing.
- **`cleanup-inactive-users`** — deactivate non-employee Users and reassign their orphaned records. Pairs with `assign-unowned-records`.
- **`cleanup-list-views`** — remove unused, empty, or duplicate list view definitions across objects.
- **`cleanup-fields`** — archive or delete unused custom fields across Lead, Contact, Account, Opportunity. Flag dead fields (not on a layout, not in a report, not in a Validation Rule, not in Apex).
- **`cleanup-flows-and-workflows`** — remove inactive, test, or deprecated Flows, Process Builders, and legacy Workflow Rules.
- **`create-segment-list-views`** — business segment list views for customers, partners, competitors, employees, ICP tiers, industries.
- **`quarterly-org-cleanup`** — comprehensive quarterly audit (record quality, bounces, duplicates, scoring, engagement, fields) with QoQ trend comparison.
- **`review-bounced-records`** — weekly manual review of Leads and Contacts with repeated bounces: delete or attempt recovery.
- **`weekly-cleanup-routine`** — 5-minute weekly health check: bounce monitoring, new record quality, Flow health, list view growth, data quality sampling.

## Cross-playbook dependencies

Resolve in this order if running together:

- `salesforce-audit` → `salesforce-implementation-plan` (audit feeds the plan)
- `cleanup-inactive-users` ↔ `assign-unowned-records` (run together for full ownership cleanup)
- `bounce-monitoring-flow` → `review-bounced-records` (Flow flags, manual review processes)
- `weekly-cleanup-routine` and `quarterly-org-cleanup` reference most other playbooks as their components

## Salesforce vs HubSpot — playbook mapping

For anyone porting from `gt-hubspot-admin`, this is the 1:1 map. Same logic, different object model.

| HubSpot playbook | Salesforce playbook | What changed |
|------------------|---------------------|--------------|
| delete-no-email-contacts | delete-no-email-leads-contacts | runs on Lead AND Contact |
| merge-duplicate-companies | merge-duplicate-accounts | native merge + Duplicate Rules, not third-party only |
| reassign-deactivated-owners | reassign-inactive-owners | OwnerId → User, IsActive = false |
| suppress-ghost-contacts | suppress-unengaged-leads | Lead AND Contact |
| suppress-global-unsubscribes | suppress-opted-out | HasOptedOutOfEmail, DoNotCall |
| suppress-hard-bounced | suppress-hard-bounced | EmailBouncedReason / EmailBouncedDate |
| fix-lifecycle-stages | fix-lead-status-and-stages | split across Lead Status + Opportunity Stage |
| build-smart-lists | build-list-views-and-reports | list views + reports, not smart lists |
| bounce-monitoring-workflow | bounce-monitoring-flow | Flow, not Workflow |
| (all workflow playbooks) | (all flow playbooks) | Flow Builder, not HubSpot Workflows |

## Notes

- All playbooks are company-agnostic — no customer data, credentials, or proprietary references.
- Salesforce has stronger native data-quality enforcement than HubSpot (Validation Rules, Matching Rules, Duplicate Rules) but no native enrichment, so enrichment playbooks always require a third-party source (Apollo, Clearbit, Default, Clay).
- Some playbooks are fully API-automated; others are hybrid (API discovery + manual Setup execution) due to the fact that Matching Rules, Duplicate Rules, Validation Rules, and Flows are configured in Setup, not via the data API. Each playbook clearly states its automation level.
- Always back up with Data Loader before any bulk delete or update. The Recycle Bin holds deleted records for 15 days only.

---

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
