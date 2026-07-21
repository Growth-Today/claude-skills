---
name: data-quality-command-center
description: "Operate HubSpot's native Data Quality Command Center: monitor duplicates, formatting issues, property anomalies, and unused/problem properties from one place, and turn recurring fixes into automation."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-hygiene
---

# Data Quality Command Center

Use HubSpot's built-in Data Quality Command Center as the ongoing monitor for the whole hygiene layer — duplicates, format issues, property anomalies, and sync errors — instead of hunting problems manually.

## Why This Matters

The hygiene playbooks fix specific problems; the Command Center is the dashboard that surfaces them continuously in one place. It flags formatting issues (spacing, casing), property insights (unused, all-blank), duplicate volume, and record anomalies — so admins catch drift early rather than during a quarterly fire drill.

## Prerequisites

- Super Admin, or a user with **Data quality tools access** + view permissions
- Access via Data Management > Data Quality

## Critical Concept: Monitor, Then Automate

The Command Center is diagnostic — it shows what's wrong. The value comes from routing recurring issues to fixes: formatting issues → a format-automation workflow (`data-formatting-automation`), duplicates → `dedupe-contacts` / `merge-duplicate-companies`, unused properties → `cleanup-properties`. Monitor centrally, fix with the specific playbook, automate what recurs.

## Plan

1. Open the Command Center and record the baseline across its tabs (before state)
2. Triage each category to the right fix playbook
3. Automate recurring formatting fixes
4. Set a review cadence (after state)

## Execute

### Step 1: Read the Command Center
Data Management > Data Quality. Review each area: **duplicates** (contact + company volume vs limits), **formatting issues** (auto-fixable format problems), **property insights** (unused, all-blank, low-fill properties), and any **sync/integration errors**.

### Step 2: Triage to fix playbooks
- Duplicates → `dedupe-contacts`, `merge-duplicate-companies`
- Formatting issues → apply HubSpot's suggested fixes; recurring ones → `data-formatting-automation`
- Unused/blank properties → `cleanup-properties`
- Sync errors → `salesforce-sync-management` / integration owner

### Step 3: Automate recurring fixes
For formatting issues that keep reappearing (casing, whitespace, phone format), build a workflow to normalize on create/update so the Command Center stops flagging them.

### Step 4: Cadence
Add a Command Center review to `weekly-cleanup-routine` (quick scan) and `quarterly-database-cleanup` (deep pass).

## After State

**Verification checklist:**

1. Baseline captured across duplicates / formatting / property insights.
2. Each flagged category is routed to a specific fix playbook.
3. Recurring formatting issues are auto-normalized (fewer flags over time).
4. Duplicate volume is under HubSpot's alert threshold.
5. Command Center review is on the weekly + quarterly cadence.

## Key Technical Learnings

- **It's the hygiene dashboard** — one place to see drift instead of manual hunting.
- **Diagnostic, not a fixer** — pair every category with a specific fix playbook.
- **Automate the recurring** — formatting issues that keep returning belong in a workflow.
- **Permissions-gated** — needs Super Admin or data quality tools access.
- **Ties the whole data-hygiene group together** and feeds the Data Quality tile in `revops-core-dashboards`.
