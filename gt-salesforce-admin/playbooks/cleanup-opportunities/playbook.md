---
name: cleanup-opportunities
description: "Cleanup Opportunities for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Cleanup Opportunities

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Standardize pipelines and record types, remove test opportunities, fix missing Amount/CloseDate, address stale open deals.

## Prerequisites
- `simple-salesforce`, credentials in `.env`

## Automation level
Hybrid. API for discovery and field fixes; stage/pipeline standardization may need Setup.

## Steps
1. Find test/junk opps (name patterns, zero amount, internal accounts).
2. Find open opps past `CloseDate` (slipped) and stale opps (no activity 60+ days). Decide: update close date, mark closed-lost, or reassign.
3. Backfill missing `Amount` and `CloseDate` where recoverable; flag the rest.
4. Standardize record types and stage picklists to the org's sales process.
5. Report counts.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
