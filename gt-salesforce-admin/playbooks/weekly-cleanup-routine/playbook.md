---
name: weekly-cleanup-routine
description: "Weekly Cleanup Routine for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Weekly Cleanup Routine

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

A 5-minute weekly health check. The lightweight counterpart to the quarterly cleanup.

## Prerequisites
- `simple-salesforce`, credentials in `.env`

## Automation level
Mostly scriptable. One small script reports the week's deltas.

## Steps
1. Bounce monitoring: new bounces this week (feed `/review-bounced-records`).
2. New record quality: of records created this week, what percent are missing email, status, source, or owner.
3. Flow health: any Flow errors in the last 7 days.
4. List growth: did any segment list view spike or empty out unexpectedly.
5. Data quality sample: pull 20 random new records, eyeball completeness.
6. Log the five numbers so week-over-week trends are visible.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
