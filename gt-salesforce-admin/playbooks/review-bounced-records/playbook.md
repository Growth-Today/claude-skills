---
name: review-bounced-records
description: "Review Bounced Records for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Review Bounced Records

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Weekly manual review of Leads and Contacts with repeated bounces: delete, attempt recovery, or confirm suppression.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- Output from `/bounce-monitoring-flow` or `/suppress-hard-bounced`

## Automation level
Hybrid. API pulls the list; the decision is manual.

## Steps
1. Pull records flagged by the bounce-monitoring Flow this week.
2. For each: is the email a typo (recoverable) or a dead address (delete/suppress)?
3. Attempt recovery on high-value accounts (re-find the email via enrichment).
4. Confirm suppression on the rest.
5. Log counts for the weekly routine.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
