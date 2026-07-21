---
name: forecasting-goals-setup
description: "Set up forecasting and goals in Sales Hub: configure the forecast tool, set team/rep goals, and use sales analytics to track attainment — so the pipeline turns into a number leadership can plan on."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: pipelines-deals
---

# Forecasting & Goals Setup

Configure HubSpot's forecast tool and goals so leadership gets a reliable expected number and reps have clear targets. Builds on a clean pipeline (`deal-pipeline-architecture`) and enforced data (`deal-stage-required-fields`).

## Why This Matters

A pipeline without a forecast is just a list of deals. The forecast tool + goals turn stage probabilities and close dates into an expected number, track attainment against target, and surface who's ahead or behind. It only works if the underlying pipeline is honest — which is why the earlier deal playbooks come first.

## Prerequisites

- Access to Sales > Forecast and Reports > Goals (Sales Hub Pro+/Enterprise for full forecasting)
- Clean pipeline with realistic stage probabilities (`deal-pipeline-architecture`)
- Required fields enforced so amount/close date are reliable (`deal-stage-required-fields`)

## Critical Concept: Forecast Categories vs Stage Probability

HubSpot forecasts from **close date + amount + stage probability** (weighted), and optionally from manually-set **forecast categories** (Commit / Best case / Pipeline / Omitted) reps assign per deal. Decide whether you run a **weighted** forecast (trusts stage probabilities) or a **manual/category** forecast (trusts rep judgement) — or both — before configuring.

## Plan

1. Confirm the pipeline + data are forecast-ready
2. Choose the forecast method (weighted / category / both)
3. Configure the forecast tool + forecast categories
4. Set team and rep goals; wire up attainment reporting (after state)

## Execute

### Step 1: Choose the method
Weighted (amount × stage probability) is automatic and objective; category (rep-assigned Commit/Best case) captures judgement. Many teams use both — weighted for the floor, commit for the call.

### Step 2: Configure forecasting
Sales > Forecast: set the pipeline(s) included, the forecast method, and (if using) forecast categories mapped to stages. Ensure close dates are firm (enforced via `deal-stage-required-fields`).

### Step 3: Set goals
Reports > Goals: set revenue/deal goals per team and per rep for the period, aligned to the forecast. Use the sales analytics tool to track attainment and spot coaching gaps.

### Step 4: Dashboard it
Add forecast + goal-attainment tiles to the leadership dashboard (`revops-core-dashboards`) so the number is visible, not buried in the forecast tab.

## After State

**Verification checklist:**

1. Forecast method is chosen and configured (weighted / category / both).
2. Only realistic pipelines are included; close dates are reliable.
3. Team + rep goals are set for the period.
4. Attainment is tracked (sales analytics) and surfaced on the leadership dashboard.
5. Forecast reconciles with weighted pipeline (spot-check).

## Key Technical Learnings

- **Garbage pipeline = garbage forecast.** The forecast is only as honest as stage probabilities and close dates.
- **Weighted vs category is a real choice** — objective math vs rep judgement; pick deliberately.
- **Goals give the forecast meaning** — a number without a target isn't actionable.
- **Surface it on a dashboard** — a forecast nobody sees doesn't drive behavior.
- **Depends on `deal-pipeline-architecture` + `deal-stage-required-fields`.**

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
