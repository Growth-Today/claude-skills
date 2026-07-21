---
name: funnel-cohort-reports
description: "Build funnel and cohort reports to see conversion, drop-off, and retention over time. Covers when to use funnel vs cohort, stage/step setup, and reading them for actionable insight."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: reporting
---

# Funnel & Cohort Reports

Two high-value report types most portals underuse: **funnel** (conversion and drop-off across ordered stages) and **cohort** (how groups behave over time, e.g. retention). Extends `custom-report-builder-guide` with the specifics of these two.

## Why This Matters

Funnel reports answer "where do we lose people?" — the single most actionable conversion question. Cohort reports answer "does behavior improve over time / do customers stick?" — critical for retention and lifecycle analysis. Both are built into HubSpot's report builder but require the right stage/step and time setup to be meaningful.

## Prerequisites

- Reports > Create custom report > Funnel / Cohort (higher tiers for some cohort features)
- Clean ordered stages: lifecycle (`fix-lifecycle-stages`) and/or deal stages (`deal-pipeline-architecture`)
- A reliable date property for the cohort grouping (e.g. became-customer date, signup date)

## Critical Concept: Funnel = Stages, Cohort = Time-Grouped Behavior

- **Funnel:** ordered steps (lifecycle stages, deal stages, or a sequence of events); shows conversion % and drop-off between each. Use for "where's the leak?"
- **Cohort:** groups records by a starting period (e.g. signup month) and tracks a behavior across subsequent periods. Use for retention/repeat-behavior.

Getting the ordered steps (funnel) or the cohort date + measured behavior (cohort) right is the whole setup.

## Plan

1. Pick the question → funnel or cohort
2. Funnel: define the ordered steps; Cohort: define the cohort date + measured behavior
3. Build, set filters/date range, choose visualization
4. Read for action; add to dashboards (after state)

## Execute

### Step 1: Funnel report
Reports > Create > **Funnel**. Choose the ordered steps (e.g. Lead → MQL → SQL → Opportunity → Customer, or deal stages). Set the date range and any segment filter (team, source). Read the biggest drop-off — that's where to focus.

### Step 2: Cohort report
Reports > Create > **Cohort**. Set the cohort property (grouping period, e.g. first-conversion month) and the behavior tracked over time (e.g. still-customer, repeat purchase). Read down a cohort row for retention decay; compare rows for improvement across cohorts.

### Step 3: Make them actionable
For funnels: pair the worst drop-off with a fix (routing, nurture, stage-gating). For cohorts: tie declining retention to churn-prevention. Add both to `revops-core-dashboards`.

## After State

**Verification checklist:**

1. Funnel steps are correctly ordered and reconcile with stage counts.
2. Cohort date + measured behavior are set so rows are interpretable.
3. Each report is tied to an action (fix the drop-off / address the churn).
4. Date ranges and filters are deliberate and documented.
5. Reports are on the relevant dashboards.

## Key Technical Learnings

- **Funnel finds the leak; cohort measures stickiness** — pick by question.
- **Ordered steps must be genuinely ordered** — a funnel on unordered stages is nonsense.
- **Cohort needs a clean start date** — the grouping property is the whole basis.
- **A report without an action is decoration** — tie each to a fix.
- **Extends `custom-report-builder-guide`; feeds `revops-core-dashboards`.**

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
