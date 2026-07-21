---
name: revops-reports-and-dashboards
description: "Build the core RevOps reports and dashboards every Salesforce org needs: pipeline health, stage conversion, lead funnel, forecast, and data quality — each scoped to one audience. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: reporting
---

# RevOps Reports & Dashboards

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Stand up the handful of dashboards that make the org decision-ready, on clean data (`sales-process-and-stages`, `fix-lead-status-and-stages`) and the right report types (`custom-report-types`). Complement to `cleanup-dashboards` (which removes clutter).

## Prerequisites
- Report/dashboard creation permission; dynamic dashboards need the feature
- `custom-report-types` built; clean stages + lead status
- A running user for the dashboard (whose access defines what viewers see)

## Critical concept
A dashboard tells **one story to one audience**. Salesforce dashboards run as a **running user** (their access = the data shown) — set it deliberately (e.g. a role high in the hierarchy for leadership views). Build few, focused dashboards, not one giant catch-all.

## Automation level
Guided — report/dashboard config (declarative).

## Steps
1. Confirm the model is clean (stages, lead status, report types).
2. Build the **5 core dashboards**, each for one audience:
   - **Pipeline Health** — open opps by stage (count + amount), weighted pipeline, created vs closed, stale opps.
   - **Stage Conversion / Funnel** — stage-to-stage conversion + avg age in stage.
   - **Lead Funnel** — leads by status over time, MQL→SQL→conversion + time.
   - **Forecast** — by close date / forecast category, by owner vs quota.
   - **Data Quality** — records missing owner/key fields, duplicates, stale.
3. Set the **running user** per dashboard for correct visibility.
4. Set sharing + **subscriptions** (scheduled email) so people don't hunt for it.
5. Review the Data Quality dashboard in `weekly-cleanup-routine` / `quarterly-org-cleanup`.

## Notes
- Running user controls what a dashboard shows — a leadership dashboard needs a running user with broad access.
- Build on clean stages/report types or the numbers won't be trusted.
- Pairs with `custom-report-types` and `cleanup-dashboards`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
