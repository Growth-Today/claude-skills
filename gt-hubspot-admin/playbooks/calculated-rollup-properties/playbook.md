---
name: calculated-rollup-properties
description: "Build calculation and rollup properties that derive values automatically (sums, counts, min/max, formulas) across a record and its associated records — so key metrics stay live without manual updates or workflows."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Calculated & Rollup Properties

Create properties whose values are computed automatically — a formula on the record (e.g. days since last contact), or a rollup across associated records (e.g. total open deal amount on a company). These keep derived metrics accurate without workflows or manual edits.

## Why This Matters

Teams constantly rebuild the same derived numbers with brittle workflows or by hand: total deal value per account, number of open deals, average deal size, days since last activity. Calculation and rollup properties compute these natively and stay current automatically. They're more reliable than workflow-maintained fields (which drift) and they unlock better scoring, segmentation, and reporting.

## Prerequisites

- Super Admin / "Edit property settings" access to Settings > Properties
- Governed properties with correct types (`property-architecture-governance`) — calculations depend on numeric/date source fields being the right type
- Rollups across associated records require the objects to be associated (`association-labels-setup` / standard associations); some calculation features are tier-gated (Pro/Enterprise)

## Critical Concept: Calculation vs Rollup

- **Calculation property**: a formula using other properties **on the same record** (e.g. `price × quantity`, or a date difference).
- **Rollup property**: aggregates a property **across associated records** (e.g. SUM of `amount` on a company's associated deals; COUNT of open deals; MIN/MAX of a date).

Both recalculate automatically. Choose based on whether the inputs live on the same record (calculation) or on related records (rollup).

## Plan

1. Identify the derived metrics teams currently maintain by hand or via workflow
2. Classify each as a calculation (same record) or rollup (across associations)
3. Build the properties with the correct source fields and operation
4. Replace the brittle workflow/manual versions
5. Verify values are correct and live (after state)

## Execute

### Step 1: Inventory derived metrics
Common candidates:
- **Company rollups:** total open deal amount, count of open deals, count of contacts, most recent deal close date.
- **Deal calculations:** margin (`amount − cost`), weighted amount (`amount × probability`).
- **Contact calculations:** days since last activity/contacted.

### Step 2: Build the properties
Settings > Properties > create property > field type **Calculation**. Choose:
- **Calculation (same record):** build the formula from the record's own numeric/date properties.
- **Rollup (associated records):** pick the associated object + property + operation (SUM / COUNT / MIN / MAX / AVG).

### Step 3: Retire the brittle versions
Where a workflow was maintaining the same number, disable it and point reports/lists at the calculated property instead (fewer moving parts, no drift).

### Step 4: Use downstream
Feed these into lead/account scoring, segmentation (e.g. "companies with >$50k open pipeline"), and dashboards (`revops-core-dashboards`).

## After State

**Verification checklist:**

1. Key derived metrics exist as calculation/rollup properties (not hand-maintained).
2. Spot-check a few records: the computed value matches a manual calculation.
3. Workflows that previously maintained these numbers are retired (no duplication/drift).
4. Source properties are the correct type (numbers/dates), so calculations don't error.
5. At least one list/report/score now uses a calculated property.

## Key Technical Learnings

- **Calculation = same record; rollup = across associations.** Pick by where the inputs live.
- **They beat workflow-maintained fields** — auto-recalculating means no drift and fewer moving parts.
- **Source field types must be correct** — a "number" stored as text won't calculate. Fix types first (`property-architecture-governance`).
- **Tier + association dependencies apply** — rollups need associations; some features need Pro/Enterprise.
- **Feeds scoring, segmentation, and dashboards** with live, trustworthy derived metrics.

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
