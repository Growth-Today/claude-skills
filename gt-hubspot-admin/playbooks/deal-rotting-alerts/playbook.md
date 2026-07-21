---
name: deal-rotting-alerts
description: "Stop deals from silently rotting in a stage. Sets a maximum age per deal stage, audits deals exceeding it, and builds date-based workflows that flag stale deals and alert owners, plus a RevOps dashboard for stuck pipeline."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: pipelines-deals
---

# Deal Rotting Alerts

Give every deal stage a maximum recommended age, then detect and surface deals that exceed it. Stale open deals are the quiet killer of forecast accuracy — they inflate open pipeline and hide the fact that a deal is already dead.

## Why This Matters

A deal sitting 120 days in "Proposal Reviewed" is not a real forecast — it's a corpse propping up the number. Without age thresholds, nobody notices until the quarter closes short. Setting a max age per stage (and alerting on breaches) forces a decision: advance it, or close it lost. HubSpot can highlight "rotting" deals in the board view, and a date-based workflow can proactively flag them and ping the owner.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Automation > Workflows and to Settings > Objects > Deals
- A stable pipeline (run `deal-pipeline-architecture` first so stages are meaningful)

## Critical Concept: Time-in-Stage vs Total Deal Age

HubSpot tracks `hs_time_in_dealstage` (how long the deal has sat in its *current* stage) separately from total deal age. Rotting should be measured **per stage**, because a healthy "Discovery" age is very different from a healthy "Verbal Commit" age. HubSpot's board also has a built-in **rotting setting** (highlight deals with no activity for N days) — use that for the visual cue, and the workflow below for proactive alerts.

## Plan

1. Audit current time-in-stage distribution per stage (before state — `scripts/before.py`)
2. Define a max-age threshold per stage
3. Turn on board rotting highlights + build a date-based alert workflow
4. Add a stale-deal dashboard/view for RevOps
5. Verify (after state)

## Before State

Run the audit script to see how long open deals have been sitting in their current stage:

```bash
cd scripts
python before.py
```

`scripts/before.py` prints, per stage, the count of open deals and how many exceed common age buckets (30/60/90 days) — this is the evidence for where thresholds are needed.

## Execute

### Step 1: Define max age per stage

Base thresholds on your real sales cycle. Example:

| Stage | Max recommended age (days) |
|---|---|
| Discovery Completed | 21 |
| Solution Fit Confirmed | 21 |
| Proposal Reviewed | 14 |
| Verbal Commit | 10 |
| Contract Sent | 7 |

### Step 2: Turn on board rotting highlights

Deals board > pipeline settings > **Edit stages / rotting**: set "highlight records with no activity" per stage so reps see stale deals visually. This is the passive cue.

### Step 3: Build the date-based alert workflow

Automation > Workflows > **Deal-based workflow**:

1. Enrollment trigger: `Time in current stage` (or `hs_time_in_dealstage`) is greater than your stage threshold, AND deal is open.
2. Action: create a task for the deal owner ("Stale deal — advance or close lost") and/or send an internal notification.
3. Optional: set a custom property `deal_health = At risk` so it's filterable/reportable.
4. Enable re-enrollment so newly-stale deals keep getting caught.

Because thresholds differ per stage, either build one workflow per stage or use branching on `dealstage` + threshold.

### Step 4: RevOps stale-deal dashboard

Create a saved deal view / report: open deals where `deal_health = At risk` (or time-in-stage over threshold), grouped by owner and stage. Add it to the RevOps dashboard so stale pipeline is visible weekly. (See the `reporting` group's `revops-core-dashboards`.)

## After State

**Verification checklist:**

1. Every active stage has a documented max-age threshold.
2. Board rotting highlights are enabled per stage.
3. The alert workflow is live with re-enrollment on; a test deal aged past threshold triggers a task/notification. (Confirm, then clean up the test.)
4. The stale-deal view/report exists and is on the RevOps dashboard.
5. Re-running `scripts/before.py` a few weeks later shows the over-threshold counts trending down (deals are being advanced or closed lost, not left to rot).

## Key Technical Learnings

- **Measure per stage, not overall.** `hs_time_in_dealstage` is the right property; total deal age hides stage-level rot.
- **Rotting = a forced decision.** The goal isn't to punish reps; it's to move stale deals to Closed Lost so the forecast reflects reality.
- **Board highlight (passive) + workflow (active)** together beat either alone — one nudges, the other guarantees follow-up.
- **Make it reportable.** A `deal_health` property turns rot into a dashboard metric, not just a task.
- **Feeds the forecast.** Combined with `deal-stage-required-fields`, weighted pipeline finally reflects live, real deals.
