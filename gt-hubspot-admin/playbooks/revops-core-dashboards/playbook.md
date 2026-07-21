---
name: revops-core-dashboards
description: "Build the core RevOps dashboards every HubSpot portal needs: pipeline health, stage conversion, lifecycle velocity, forecast, and data quality. Turns raw CRM data into the handful of views leadership actually uses."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: reporting
---

# RevOps Core Dashboards

Stand up the small set of dashboards that make a HubSpot portal decision-ready: pipeline health, stage conversion, lifecycle velocity, forecast, and data-quality monitoring. This is the "build" counterpart to `cleanup-dashboards` — instead of removing clutter, you create the few reports that matter.

## Why This Matters

Most portals either have no dashboards or fifty stale ones nobody trusts. Leadership needs a handful of reliable views: is the pipeline healthy, where do deals stall, how fast do leads move, will we hit the number, and is the data even trustworthy. Building these deliberately (on the clean data and pipeline the earlier playbooks produced) is what turns the CRM from a database into a decision tool.

## Prerequisites

- Access to Reports > Dashboards (report creation permission)
- A clean pipeline (`deal-pipeline-architecture`) and lifecycle stages (`fix-lifecycle-stages`) — dashboards are only as good as the underlying model
- Governed properties (`property-architecture-governance`) so report fields are trustworthy

## Critical Concept: A Dashboard Tells One Story to One Audience

Each dashboard should answer a specific question for a specific audience — a leadership forecast dashboard is not a rep activity dashboard. Build few, focused dashboards, not one giant catch-all. Set sharing/permissions per audience and schedule email delivery so people don't have to go looking.

## Plan

1. Confirm the underlying model is clean (pipeline, lifecycle, properties)
2. Build the 5 core dashboards below
3. Set audience, sharing, and scheduled delivery
4. Verify each report matches source-of-truth numbers (after state)

## Execute — the 5 core dashboards

### 1. Pipeline Health (leadership + sales managers)
- Open deals by stage (count + amount)
- Weighted pipeline (amount × stage probability)
- Deals created vs closed this period
- Stale/rotting deals (ties to `deal-rotting-alerts`)

### 2. Stage Conversion / Funnel (RevOps)
- Funnel report across lifecycle or deal stages
- Stage-to-stage conversion rates
- Average time in each stage

### 3. Lifecycle Velocity (marketing + RevOps)
- Contacts by lifecycle stage over time
- MQL→SQL and SQL→Opportunity conversion + time (ties to `lead-status-taxonomy`)
- New contacts by source

### 4. Forecast (leadership)
- Forecast by close date / stage
- Deals by owner and expected close
- Goal attainment vs target (ties to Sales Hub forecasting)

### 5. Data Quality Monitor (RevOps / admin)
- Contacts/companies missing key properties
- Records with no owner, no lifecycle stage
- Duplicate counts (ties to the data-hygiene group + Data Quality Command Center)

For each: choose the report type in the custom report builder (see `custom-report-builder-guide`), add to the dashboard, set the audience/sharing, and schedule delivery (e.g. Monday 8am to leadership).

## After State

**Verification checklist:**

1. The 5 core dashboards exist, each scoped to one audience/question.
2. Numbers reconcile with source-of-truth (spot-check pipeline total vs the deals index).
3. Sharing/permissions are set per audience; scheduled delivery is on.
4. The Data Quality Monitor is reviewed in `weekly-cleanup-routine` / `quarterly-database-cleanup`.
5. Stale dashboards were removed first (`cleanup-dashboards`) so only trusted views remain.

## Key Technical Learnings

- **Few, focused dashboards beat many.** One story, one audience per dashboard.
- **Garbage in, garbage dashboard.** Build on a clean pipeline, lifecycle, and property layer or the numbers won't be trusted.
- **Schedule delivery.** A dashboard nobody opens is worthless — push it to inboxes.
- **The Data Quality Monitor closes the loop** — it makes hygiene visible and keeps the other playbooks honest.
- **Pairs with `custom-report-builder-guide`** for the how-to on each report type.
