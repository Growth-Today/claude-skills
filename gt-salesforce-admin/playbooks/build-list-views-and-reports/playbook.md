---
name: build-list-views-and-reports
description: "Build List Views and Reports for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: segmentation-scoring
---

# Build List Views and Reports

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Create the foundational segmented list views and reports an org needs (the Salesforce equivalent of HubSpot smart lists).

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- Report Builder access

## Automation level
Hybrid. Some list views can be created via the Metadata/Tooling API; most are built in the UI.

## Steps
1. Build a **master sendable** view: not bounced, not opted out, not suppressed, has email.
2. Build **ICP-based** views by tier (reads the field from `/create-icp-tiers`).
3. Build **persona** views by title/role.
4. Build **engagement** views: active last 30 / 90 days, dormant 180+.
5. Build the **Account, Contact & Opportunity Data Quality** report so the team can see gaps weekly.
6. Document each view's filter logic.

## Notes
- Keep filters dynamic so views stay current without manual refresh.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
