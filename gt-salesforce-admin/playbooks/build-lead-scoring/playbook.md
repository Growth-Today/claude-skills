---
name: build-lead-scoring
description: "Build Lead Scoring for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: segmentation-scoring
---

# Build Lead Scoring

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Build a Fit and Engagement scoring model. Blank Lead `Rating` silently breaks routing and Agentforce, so this is higher impact than it looks.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- Einstein Lead Scoring (if licensed) OR a custom formula field approach

## Automation level
Hybrid. Setup builds the model/fields; API backfills historical Rating.

## Steps
1. Define **Fit** (firmographic: industry, employee count, ICP tier) and **Engagement** (behavioral: activity recency, email opens, form fills) as two separate scores. Do not collapse them into one.
2. If Einstein Lead Scoring is available, configure it. Otherwise build two custom number fields populated by formula or a scheduled Flow.
3. Map the combined score to the standard `Rating` picklist (Hot / Warm / Cold) so existing views and Agentforce read it.
4. Backfill `Rating` on existing leads via API.
5. Report Rating fill rate and distribution.

## Notes
- Keep Fit and Engagement separate so a high-fit, low-engagement lead is nurtured, not discarded.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
