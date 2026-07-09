---
name: engagement-suppression-flow
description: "Engagement Suppression Flow for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation-flow
---

# Engagement Suppression Flow

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

A two-stage sunset Flow that tries to re-engage dormant records before suppressing them.

## Prerequisites
- Flow Builder access
- Suppression field; a re-engagement email asset in the marketing tool

## Automation level
Setup-only (Flow).

## Steps
1. Stage 1: when a record hits 120 days no activity, enroll it in a re-engagement send and set a `Reengagement_Started__c` date.
2. Stage 2: if still no activity 30 days after the re-engagement send, set `Suppressed__c = true`.
3. Build as a Schedule-Triggered Flow with two decision branches.
4. Activate and review monthly.

## Notes
- Never suppress without the re-engagement attempt first; you lose recoverable pipeline otherwise.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
