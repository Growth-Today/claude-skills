---
name: quarterly-org-cleanup
description: "Quarterly Org Cleanup for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Quarterly Org Cleanup

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Comprehensive quarterly audit with quarter-over-quarter trend comparison. The meta-orchestrator for routine maintenance.

## Prerequisites
- All hygiene, enrichment, and maintenance playbooks available

## Automation level
Orchestrator. Runs other playbooks as components.

## Steps
1. Run `/salesforce-audit` and save the dated report.
2. Compare to last quarter's report: which dimensions improved, which regressed.
3. Re-run the hygiene playbooks that regressed: bounces, opt-outs, inactive owners, duplicates.
4. Re-check data completeness and scoring fill rates.
5. Review Flows, fields, list views, dashboards for new clutter.
6. Produce a QoQ trend summary with grades then-vs-now and the next quarter's priorities.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
