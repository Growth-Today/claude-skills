---
name: flow-builder-patterns
description: "Build Salesforce automation the modern way with Flow: record-triggered (before/after save), scheduled, and screen flows — plus migrating off retired Workflow Rules and Process Builder. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation
---

# Flow Builder Patterns

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Flow is Salesforce's automation engine (Workflow Rules + Process Builder are retired/going away). This playbook covers which Flow type to use when, the key performance rule, and how to migrate legacy automation — the foundation the automation playbooks build on.

## Prerequisites
- "Manage Flow"
- `cleanup-flows-and-workflows` (inventory + retire dead automation first)
- Governance: naming + one automation per object where possible (`quarterly-org-cleanup`)

## Critical concept — which Flow when
- **Record-triggered, before-save** — set fields on the same record on create/update. **Fastest**; use for field updates/validation instead of after-save or Process Builder.
- **Record-triggered, after-save** — related-record updates, sending emails, calling actions.
- **Scheduled Flow** — batch jobs (nightly hygiene, stale-record flags).
- **Screen Flow** — guided UI for users.
- Rule: prefer **before-save** for same-record updates; avoid multiple conflicting record-triggered flows per object (order isn't guaranteed) — consolidate.

## Automation level
Guided — Flow is UI-built; API/Tooling to inventory existing automation.

## Steps
1. **Inventory** existing Flows, Process Builders, Workflow Rules per object (`cleanup-flows-and-workflows`). Note conflicts/duplication.
2. **Choose the pattern** per need (before-save vs after-save vs scheduled vs screen).
3. **Migrate legacy:** rebuild Workflow Rules / Process Builder logic as record-triggered Flows; deactivate the legacy once verified. (Use Salesforce's Migrate to Flow tool where possible.)
4. **Consolidate** to ideally one record-triggered flow per object per timing (before/after), with sub-flows for modularity.
5. **Govern:** naming convention, description, an owner per flow; test in a sandbox before activating.

## Notes
- Before-save record-triggered Flow is the cheapest place to set fields — use it over Process Builder/after-save for same-record updates.
- Multiple record-triggered flows on one object have no guaranteed order — consolidate to avoid surprises.
- Foundation for `lead-routing-assignment`, `bounce-monitoring-flow`, `lead-lifecycle-flow`, `new-record-hygiene-flow`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
