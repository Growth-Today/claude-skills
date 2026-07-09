---
name: cleanup-flows-and-workflows
description: "Cleanup Flows and Workflows for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Cleanup Flows and Workflows

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Remove inactive, test, or deprecated Flows, Process Builders, and legacy Workflow Rules.

## Prerequisites
- Flow and automation admin access

## Automation level
Hybrid. Tooling API can list automations and status; cleanup is manual and must be careful.

## Steps
1. List all Flows, Process Builders, and Workflow Rules with active/inactive status and last-modified date.
2. Flag: inactive 90+ days, test/duplicate automations, and Process Builders/Workflow Rules that should migrate to Flow (Salesforce is retiring both).
3. Confirm no active dependency, then deactivate and archive.
4. Note any migration candidates for a separate project.

## Notes
- Never delete an automation without checking what triggers it and what it updates. Deactivate first, watch for a cycle, then delete.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
