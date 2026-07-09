---
name: bounce-monitoring-flow
description: "Bounce Monitoring Flow for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation-flow
---

# Bounce Monitoring Flow

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

A scheduled Flow that auto-flags records above a bounce threshold, alerts on hard bounces, and queues them for review. The Salesforce equivalent of the HubSpot bounce-monitoring workflow.

## Prerequisites
- Flow Builder access
- Suppression field on Lead and Contact

## Automation level
Setup-only (Flow). No data API needed once built.

## Steps
1. Build a Schedule-Triggered Flow running daily.
2. Entry: records where `EmailBouncedReason != null` and `Suppressed__c = false`.
3. Action: set `Suppressed__c = true`, post to a Chatter group or send an alert email to the admin.
4. Add the records to a "Bounced - review" list view for `/review-bounced-records`.
5. Activate and monitor the first run.

## Notes
- Schedule-Triggered Flows have governor limits on records per run. For very large orgs, batch by `CreatedDate` window.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
