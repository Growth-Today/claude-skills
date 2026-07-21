---
name: matching-and-duplicate-rules
description: "Prevent duplicates at the source with Salesforce matching rules + duplicate rules — flag or block dupes on create/edit across Leads, Contacts, Accounts. The prevention layer that complements merge cleanup. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Matching & Duplicate Rules

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Stop duplicates from being created, instead of merging them forever. **Matching rules** define what "same record" means (by email, name+company, website); **duplicate rules** decide what happens on create/edit (alert or block) using those matching rules. This is the build/prevention counterpart to `merge-duplicate-accounts`.

## Prerequisites
- "Customize Application"
- Decide the trusted match criteria per object (see `merge-duplicate-accounts` for discovery)
- Run a dedup pass first so you start clean

## Critical concept
- **Matching rule** — the "same as" logic (exact/fuzzy on email, name, company, website). Salesforce ships standard rules; create custom ones for your definition.
- **Duplicate rule** — ties a matching rule to an action on **create/edit**: **Alert** (warn, allow) or **Block** (prevent save). Applies on UI and (optionally) API/import.
- Cross-object: Lead↔Contact matching catches a lead that's already a contact. This directly protects routing, reporting, and Agentforce/AI quality.

## Automation level
Hybrid — API/report to size the duplicate problem; rules built in Setup or Metadata API.

## Steps
1. **Size the problem:** count likely dupes by email (Lead+Contact) and by website/name (Account) — see `merge-duplicate-accounts`.
2. **Define matching rules:** email exact (highest confidence), name + company, account website/name. Activate them.
3. **Create duplicate rules:** start with **Alert** (learn the noise), then move high-confidence ones (exact email) to **Block**. Decide whether to enforce on API/import (bypass for trusted integration users if needed).
4. **Cross-object:** enable Lead-to-Contact matching so new leads flag existing contacts.
5. **Clean existing dupes** (`merge-duplicate-accounts` + Lead/Contact merge) so prevention starts from a clean base.
6. **Monitor:** review the Duplicate Record Sets / exception report weekly (fold into `weekly-cleanup-routine`).

## Notes
- Alert first, Block once you trust the rule — blocking on a noisy rule frustrates users and integrations.
- Prevention + periodic merge = duplicates stay solved (treat it as release-readiness, especially before Agentforce/AI).
- Complements `merge-duplicate-accounts` (discovery/merge) and `validation-rules-setup`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
