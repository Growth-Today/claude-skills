---
name: cleanup-dashboards
description: "Cleanup Dashboards for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Cleanup Dashboards

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Audit and consolidate dashboards: low-usage, broken source reports, duplicates.

## Prerequisites
- Access to Dashboards and the Report folder structure

## Automation level
Hybrid. The Tooling/Metadata API can list dashboards and last-viewed dates; consolidation is manual.

## Steps
1. List all dashboards with last-viewed/last-modified dates.
2. Flag dashboards not viewed in 90+ days, dashboards whose source reports are broken or deleted, and near-duplicate dashboards.
3. Confirm owners, then archive or delete.
4. Document the surviving set and their owners.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
