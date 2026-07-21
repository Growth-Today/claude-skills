---
name: forecasting-setup
description: "Configure Collaborative Forecasting: forecast categories, forecast types, quotas, and the forecast hierarchy so leadership gets a reliable expected number. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: opportunities-sales
---

# Forecasting Setup

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Turn the pipeline into a number leadership can plan on. Salesforce **Collaborative Forecasting** rolls Opportunities up the role hierarchy by **forecast category**, against **quotas**.

## Prerequisites
- "Manage Quotas", forecasting enabled
- `sales-process-and-stages` (stages mapped to forecast categories) + `setup-roles-and-record-access` (the role hierarchy = the forecast hierarchy)
- Realistic close dates enforced (`validation-rules-setup`)

## Critical concept
- **Forecast categories** (Pipeline / Best Case / Commit / Omitted / Closed) come from each Opportunity's **stage mapping** — fix the stage→category mapping first (`sales-process-and-stages`).
- Forecast rolls up the **role hierarchy**, so that structure must be correct.
- Choose the **forecast type** (Opportunity Revenue, Product families, etc.). Set **quotas** per user/period.

## Automation level
Guided — Setup config; API/Data Loader to load quotas.

## Steps
1. Confirm stage→forecast-category mapping is sane; fix in the sales process if not.
2. Verify the role hierarchy = the desired forecast roll-up.
3. Enable the **forecast type**(s) you need; configure the forecast page.
4. **Load quotas** per rep/manager/period (Data Loader).
5. Validate: a manager sees their team's forecast rolled up correctly; weighted vs category views make sense.
6. Surface on the leadership dashboard (`revops-reports-and-dashboards`).

## Notes
- Garbage stages/close dates = garbage forecast — the earlier deal playbooks are prerequisites.
- Forecast roll-up follows the role hierarchy, not profiles — fix roles first.
- Pairs with `sales-process-and-stages`, `products-and-price-books`, reporting.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
