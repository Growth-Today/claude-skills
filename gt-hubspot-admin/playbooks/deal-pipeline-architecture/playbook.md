---
name: deal-pipeline-architecture
description: "Design a deal pipeline whose stages map to buyer commitments, not rep actions. Audits existing stages, removes fake and zombie stages, sets stage probabilities, and documents entry/exit criteria for reliable forecasting."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: pipelines-deals
---

# Deal Pipeline Architecture

Design (or redesign) a deal pipeline so every stage represents something the *buyer* has done, with clear entry and exit criteria and realistic win probabilities. This is the foundation that makes forecasting, conversion reporting, and deal-stage automation trustworthy.

## Why This Matters

Most unreliable HubSpot forecasts trace back to the pipeline, not the reps. Two failure patterns dominate: **fake stages** that describe what the rep is doing ("Follow-up sent") instead of what the buyer committed to, and **zombie stages** like "Nurture" or "Holding" that become graveyards for dead deals. Both inflate open pipeline and corrupt stage-conversion math. A pipeline built on buyer commitments — each with an entry criterion, an exit criterion, and a probability — turns the pipeline report into an actual forecast.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Settings > Objects > Deals (Super Admin or deal settings permission)
- Alignment with sales leadership on the actual sales process (this is a business decision, not just config)

## Critical Concept: Stages Are Buyer Commitments

Each stage must answer: *"What has the buyer done to be here?"* — not *"What has the rep done?"*

| Good (buyer commitment) | Bad (rep action / zombie) |
|---|---|
| Discovery Completed | Follow-up Sent |
| Proposal Reviewed with Buyer | Proposal Created |
| Verbal Commit | Nurture / Holding / On Hold |
| Contract Sent | Waiting to Hear Back |

Every stage needs three things: an **entry criterion** (what the buyer must have done to enter), an **exit criterion** (what moves it forward), and a **win probability** used for weighted forecasting.

## Plan

1. Audit the current pipeline(s), stages, and deal distribution (before state)
2. Redesign stages around buyer commitments; kill fake and zombie stages
3. Assign entry/exit criteria and probabilities to each stage
4. Apply the changes in HubSpot (UI config or API), coordinating with Salesforce if synced
5. Migrate deals stuck in removed stages
6. Verify and document (after state)

## Before State

### Audit Script

```python
import os
from hubspot import HubSpot
from dotenv import load_dotenv

load_dotenv()
api_client = HubSpot(access_token=os.getenv("HUBSPOT_ACCESS_TOKEN"))

# List all deal pipelines and their stages
pipelines = api_client.crm.pipelines.pipelines_api.get_all(object_type="deals")
for p in pipelines.results:
    print(f"\nPipeline: {p.label} (id={p.id})")
    for s in sorted(p.stages, key=lambda x: x.display_order):
        prob = s.metadata.get("probability", "n/a")
        print(f"  - {s.label} (id={s.id}) | probability={prob}")

# Count open deals per stage to find zombie/graveyard stages
result = api_client.crm.deals.search_api.do_search(
    public_object_search_request={
        "filterGroups": [{"filters": [{"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"}]}],
        "properties": ["dealstage", "amount"],
        "limit": 100
    }
)
print(f"\nOpen deals sampled: {len(result.results)} (paginate for full counts per dealstage)")
```

Record: number of pipelines, stage list per pipeline, probability per stage, open-deal count and total amount per stage. Flag any stage that holds many old open deals (zombie candidate) or that names a rep action (fake-stage candidate).

## Execute

### Step 1: Redesign the stages

Draft the target stage list with sales leadership. A typical B2B shape:

`Discovery Completed → Solution Fit Confirmed → Proposal Reviewed → Verbal Commit → Contract Sent → Closed Won / Closed Lost`

For each stage, write down the entry criterion, exit criterion, and probability. Delete or merge any fake/zombie stages surfaced in the audit.

### Step 2: Apply in HubSpot

**UI (recommended for stage edits):** Settings > Objects > Deals > Pipelines. Add/rename/reorder stages, set the win probability per stage, and set closed-won/closed-lost.

**API (for scripted/multi-portal setups):** stages can be created/updated via the Pipelines API:

```python
# Example: update a stage's label + probability
api_client.crm.pipelines.pipeline_stages_api.update(
    object_type="deals",
    pipeline_id="<pipeline_id>",
    stage_id="<stage_id>",
    pipeline_stage_input={
        "label": "Proposal Reviewed",
        "display_order": 3,
        "metadata": {"probability": "0.6"}
    }
)
```

### Step 3: Multiple pipelines (only if truly different processes)

Create a separate pipeline only when the sales *process* genuinely differs (e.g. New Business vs Renewals), not per team or region. More pipelines = more maintenance and split reporting.

### Step 4: Salesforce sync caution

If deals sync from Salesforce (`hs_salesforceopportunityid` present), stage mappings must be coordinated with the Salesforce admin — renaming or reordering stages can break the sync mapping. Do not restructure synced pipelines unilaterally.

### Step 5: Migrate stranded deals

When you remove or merge a stage, move its open deals to the closest valid stage first (bulk edit or API), so no deal is orphaned on a deleted stage.

## After State

**Verification checklist:**

1. Every stage names a buyer commitment (no rep-action or zombie stages remain).
2. Every stage has a documented entry criterion, exit criterion, and probability.
3. Weighted pipeline (Σ amount × probability) is now meaningful in the forecast/deal reports.
4. No open deals remain on removed/merged stages.
5. The stage design is documented somewhere the team can see it (not just in HubSpot).
6. If Salesforce-synced: the SFDC admin has confirmed the stage mapping still holds.

## Key Technical Learnings

- **Buyer commitments, not rep actions** is the single rule that fixes most pipelines. If a stage can be "true" without the buyer doing anything, it's a fake stage.
- **Kill zombie stages.** "Nurture"/"Holding" hide dead deals and inflate open pipeline. Dead deals belong in Closed Lost with a reason.
- **Probabilities only help if they're honest.** Reuse historical stage-conversion rates rather than round numbers where possible.
- **Fewer pipelines is better.** Split by process, never by team/region — that's what teams and views are for.
- **Pair this with `deal-stage-required-fields`** so each stage's exit criterion is actually enforced, and with `deal-rotting-alerts` so deals can't sit forever.
