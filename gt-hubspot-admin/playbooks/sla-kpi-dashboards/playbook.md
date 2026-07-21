---
name: sla-kpi-dashboards
description: "Build SLA and KPI dashboards that hold the go-to-market motion accountable: lead response time, follow-up SLAs, stage aging, pipeline coverage, and data-quality KPIs — with clear thresholds."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: reporting
---

# SLA & KPI Dashboards

Build the accountability layer: dashboards that track service-level agreements (lead response time, follow-up cadence) and the operating KPIs (stage aging, pipeline coverage, data quality) — each with a threshold so "good vs bad" is unambiguous.

## Why This Matters

Vanity dashboards show activity; SLA/KPI dashboards show whether the machine is meeting its commitments. "Median lead response time = 4 hours against a 1-hour SLA" is actionable; "1,200 activities this week" is not. Defining SLAs with thresholds turns reporting into management.

## Prerequisites

- Reports/dashboard access (`revops-core-dashboards` set up first)
- Agreed SLAs and KPI thresholds (a business decision — align sales + marketing)
- Supporting data: routing timestamps, `hs_time_in_dealstage` (`deal-rotting-alerts`), lead status (`lead-status-taxonomy`)

## Critical Concept: A KPI Without a Threshold Isn't a KPI

Every metric on these dashboards needs a target and a red/green line: response time < 1h, first follow-up < 24h, no deal > N days in stage, pipeline coverage ≥ 3× quota, <2% records missing key fields. Without thresholds you have numbers, not accountability.

## Plan

1. Agree the SLAs + KPI thresholds with the teams
2. Confirm the supporting data exists (timestamps, stage times, statuses)
3. Build the SLA/KPI reports with thresholds visualized
4. Assign owners + review cadence (after state)

## Execute

### Step 1: Define SLAs + KPIs with thresholds
Examples:
- **Lead response time** (assignment → first activity) vs SLA (e.g. <1h).
- **First follow-up** within 24h of assignment.
- **Stage aging** — deals over the rotting threshold (`deal-rotting-alerts`).
- **Pipeline coverage** — open pipeline ÷ quota (target ≥ 3×).
- **Data-quality KPIs** — % records missing owner/lifecycle/key fields (target < 2%).

### Step 2: Build the reports
Use the custom report builder (`custom-report-builder-guide`); where response time isn't a native property, derive it (calculated property or a workflow timestamp). Visualize the threshold (goal line / color).

### Step 3: Assemble the dashboard
Group into an "Operations / SLA" dashboard, scoped to RevOps + managers, with scheduled delivery. Pair breaches with notifications (`internal-notification-workflows`).

## After State

**Verification checklist:**

1. Each metric has a documented threshold/target.
2. Supporting data exists (response timestamps, stage times) — derive where missing.
3. The SLA/KPI dashboard is live, scoped, and scheduled.
4. Breaches trigger notifications, not just red tiles.
5. An owner reviews it on a cadence (weekly ops review).

## Key Technical Learnings

- **Threshold or it's not a KPI** — every tile needs a target and a red/green line.
- **Response-time SLAs often need a derived metric** — assignment→first-activity isn't native; build it.
- **Pair dashboards with alerts** — a red tile nobody sees changes nothing (`internal-notification-workflows`).
- **SLAs are a business agreement** — align the teams before you measure them.
- **Builds on `revops-core-dashboards`, `deal-rotting-alerts`, `lead-status-taxonomy`.**
