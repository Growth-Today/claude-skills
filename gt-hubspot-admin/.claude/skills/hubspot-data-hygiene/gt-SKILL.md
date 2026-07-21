---
name: hubspot-data-hygiene
description: HubSpot data hygiene, deduplication, deliverability, and enrichment. Use for CRM cleanup, duplicate contacts or companies, suppressing hard-bounced/unsubscribed/ghost contacts, bounce monitoring, engagement sunset, the Data Quality Command Center, contact data decay, enriching company name/industry/geo, standardizing values, and cleaning lists/forms. Triggers on "hubspot cleanup", "duplicate contacts", "dedupe", "hard bounce", "ghost contacts", "unsubscribe suppression", "data quality", "deliverability", "enrich contacts", "standardize geo", "clean lists". Do NOT use for property/object modelling (use hubspot-data-model) or owner/permission cleanup (use hubspot-governance).
---

# HubSpot Data Hygiene

Keep the database clean, deliverable, and complete. Read the relevant playbook in full before acting; paths are relative to `SKILL_BASE` (see the master router).

| Need | Playbook |
|---|---|
| Delete contacts with no email | `{SKILL_BASE}/playbooks/delete-no-email-contacts/playbook.md` |
| Merge duplicate companies | `{SKILL_BASE}/playbooks/merge-duplicate-companies/playbook.md` |
| Find & merge duplicate contacts | `{SKILL_BASE}/playbooks/dedupe-contacts/playbook.md` |
| Native data quality monitoring | `{SKILL_BASE}/playbooks/data-quality-command-center/playbook.md` |
| Find & route decayed records | `{SKILL_BASE}/playbooks/contact-data-decay-review/playbook.md` |
| Suppress hard-bounced | `{SKILL_BASE}/playbooks/suppress-hard-bounced/playbook.md` |
| Suppress global unsubscribes | `{SKILL_BASE}/playbooks/suppress-global-unsubscribes/playbook.md` |
| Suppress ghost contacts | `{SKILL_BASE}/playbooks/suppress-ghost-contacts/playbook.md` |
| Auto-suppress on bounce threshold | `{SKILL_BASE}/playbooks/bounce-monitoring-workflow/playbook.md` |
| Weekly bounced-contact review | `{SKILL_BASE}/playbooks/review-bounced-contacts/playbook.md` |
| Sunset dormant contacts | `{SKILL_BASE}/playbooks/engagement-suppression-workflow/playbook.md` |
| Clean unused lists | `{SKILL_BASE}/playbooks/cleanup-lists/playbook.md` |
| Clean unused forms | `{SKILL_BASE}/playbooks/cleanup-forms/playbook.md` |
| Backfill contact company name | `{SKILL_BASE}/playbooks/enrich-company-name/playbook.md` |
| Backfill contact industry | `{SKILL_BASE}/playbooks/enrich-industry/playbook.md` |
| Backfill geo data | `{SKILL_BASE}/playbooks/backfill-geo-data/playbook.md` |
| Standardize country/state/region | `{SKILL_BASE}/playbooks/standardize-geo-values/playbook.md` |

---

Part of **gt-hubspot-admin** · Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm · Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/) · More skills: https://www.growthtoday.co/claude-skills
