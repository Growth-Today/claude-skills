---
name: multiple-pipelines-setup
description: "Decide whether you actually need more than one deal pipeline and set additional pipelines up correctly — distinct stages, permissions, and reporting — without fragmenting the forecast."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: pipelines-deals
---

# Multiple Pipelines Setup

Add a second (or third) deal pipeline only when the sales *process* genuinely differs — e.g. New Business vs Renewals vs Partnerships — and set it up so reporting and permissions stay clean. Builds on `deal-pipeline-architecture`.

## Why This Matters

Teams over-create pipelines (one per team, region, or rep), which fragments reporting, confuses routing, and multiplies maintenance. The rule: a new pipeline is justified by a **different process with different stages**, not by org structure. Done right, multiple pipelines model genuinely different motions; done wrong, they're a reporting nightmare.

## Prerequisites

- Access to Settings > Objects > Deals > Pipelines (Super Admin or deal settings permission)
- `deal-pipeline-architecture` done (the primary pipeline is sound)
- Multiple pipelines / pipeline-level permissions require Pro+/Enterprise

## Critical Concept: Different Process, Not Different Team

Justify a pipeline by asking: *do the stages differ?* Renewals ("Upcoming → Negotiating → Renewed / Churned") genuinely differ from New Business — that warrants a pipeline. "AE team vs SDR team" does not — that's teams + views. Each pipeline also has its own stages, automation, and (Enterprise) access permissions.

## Plan

1. Audit current pipelines and whether each is justified by process (before state)
2. Design the new pipeline's stages (buyer/process commitments) with entry/exit + probabilities
3. Create it; set stage automation, required fields, and permissions
4. Route the right deals to the right pipeline; keep reporting consolidated where needed (after state)

## Execute

### Step 1: Justify it
Confirm the new motion has genuinely different stages. If not, use teams + saved views on the existing pipeline instead.

### Step 2: Build the pipeline
Settings > Objects > Deals > Pipelines > Create pipeline. Define stages as process/buyer commitments (reuse the discipline from `deal-pipeline-architecture`), set probabilities, closed-won/lost.

### Step 3: Configure per-pipeline rules
Apply required fields (`deal-stage-required-fields`), stage automation, and rotting thresholds (`deal-rotting-alerts`) to the new pipeline too. On Enterprise, set pipeline access permissions so only the right team uses it.

### Step 4: Routing + reporting
Ensure new deals land in the correct pipeline (creation defaults / workflow). For leadership, build reports that can view pipelines separately *and* a consolidated forecast so multiple pipelines don't hide the total.

## After State

**Verification checklist:**

1. Each pipeline is justified by a distinct process (not team/region).
2. New pipeline stages are process/buyer commitments with probabilities.
3. Required fields, automation, and rotting are configured per pipeline.
4. Deals route to the correct pipeline by default.
5. Reporting supports both per-pipeline and consolidated forecast views.

## Key Technical Learnings

- **Different process = new pipeline; different team = teams + views.** This one rule prevents most pipeline sprawl.
- **Every pipeline needs its own discipline** — required fields, automation, rotting — or the new one rots.
- **Consolidated reporting matters** — don't let multiple pipelines hide the total forecast.
- **Permissions are Enterprise** — don't design pipeline-level access you can't enforce.
- **Extends `deal-pipeline-architecture`** to multi-motion orgs.
