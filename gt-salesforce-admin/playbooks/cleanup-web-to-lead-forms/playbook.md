---
name: cleanup-web-to-lead-forms
description: "Cleanup Web-to-Lead Forms for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Cleanup Web-to-Lead Forms

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Remove unused, test, or deprecated Web-to-Lead forms and their routing.

## Prerequisites
- Access to Setup (Web-to-Lead) and the website/landing pages

## Automation level
Hybrid. Discovery via lead source analysis; removal is manual.

## Steps
1. List active Web-to-Lead endpoints and the pages embedding them.
2. Check `LeadSource` / form-name fields for which forms produced leads in the last 90 days.
3. Flag forms with zero recent submissions, test forms, and dev leftovers.
4. Confirm not embedded anywhere live, then retire.
5. Verify assignment rules still route the surviving forms correctly.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
