---
name: sf-data-hygiene
description: Salesforce data hygiene, deduplication, deliverability, and enrichment. Use for org cleanup, duplicate accounts, suppressing hard-bounced/opted-out/unengaged Leads & Contacts, bounce monitoring, engagement sunset, enriching account/industry/geo, standardizing values, and cleaning web-to-lead forms. Triggers on "salesforce cleanup", "duplicate accounts", "hard bounce", "opted out", "suppress", "deliverability", "enrich", "standardize geo", "web-to-lead". Do NOT use for validation/matching-rule setup (use sf-data-model) or user/permission cleanup (use sf-governance-integrations).
---

# Salesforce Data Hygiene

Keep Leads, Contacts, and Accounts clean, deliverable, and complete. Read the playbook in full; paths relative to `SKILL_BASE` (see master router).

| Need | Playbook |
|---|---|
| Delete/quarantine no-email Leads & Contacts | `{SKILL_BASE}/playbooks/delete-no-email-leads-contacts/playbook.md` |
| Merge duplicate Accounts | `{SKILL_BASE}/playbooks/merge-duplicate-accounts/playbook.md` |
| Suppress unengaged | `{SKILL_BASE}/playbooks/suppress-unengaged-leads/playbook.md` |
| Handle opted-out / DoNotCall | `{SKILL_BASE}/playbooks/suppress-opted-out/playbook.md` |
| Suppress hard-bounced | `{SKILL_BASE}/playbooks/suppress-hard-bounced/playbook.md` |
| Auto-flag on bounce threshold (Flow) | `{SKILL_BASE}/playbooks/bounce-monitoring-flow/playbook.md` |
| Sunset dormant records (Flow) | `{SKILL_BASE}/playbooks/engagement-suppression-flow/playbook.md` |
| Weekly bounced-record review | `{SKILL_BASE}/playbooks/review-bounced-records/playbook.md` |
| Backfill account name | `{SKILL_BASE}/playbooks/enrich-account-name/playbook.md` |
| Backfill industry | `{SKILL_BASE}/playbooks/enrich-industry/playbook.md` |
| Backfill geo data | `{SKILL_BASE}/playbooks/backfill-geo-data/playbook.md` |
| Standardize country/state | `{SKILL_BASE}/playbooks/standardize-geo-values/playbook.md` |
| Clean web-to-lead forms | `{SKILL_BASE}/playbooks/cleanup-web-to-lead-forms/playbook.md` |

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
