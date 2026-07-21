---
name: deal-stage-required-fields
description: "Enforce data completeness by requiring the right deal properties before a deal can advance to each stage. Audits blank required fields per stage, configures stage-gating via pipeline rules, restricts backward moves, and locks closed deals."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: pipelines-deals
---

# Deal Stage Required Fields

Make the pipeline's exit criteria enforceable: require specific deal properties to be filled before a deal can move into a given stage. This is how a pipeline design (see `deal-pipeline-architecture`) becomes actual data discipline instead of a suggestion.

## Why This Matters

A forecast is only as good as the data behind each deal. If a rep can drag a deal to "Proposal Sent" without an amount, a close date, or a named decision maker, the forecast is built on blanks. HubSpot lets you gate each stage with required properties — if the rep can't name the economic buyer by the Proposal stage, the deal shouldn't be allowed there. Stage-gating turns "please fill in the fields" into "you can't move forward until you do."

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Settings > Objects > Deals > Pipelines > Edit stage properties (Super Admin or deal settings permission)
- A finalized stage design with documented exit criteria (run `deal-pipeline-architecture` first)

## Critical Concept: Required Properties Are Set Per Stage

In HubSpot, required-to-advance properties are configured **per stage** under the pipeline's stage settings ("Set required properties" / "Conditional stage properties"). They fire when a user moves a deal *into* that stage in the UI. Note: stage-gating is a UI guardrail — records moved by **imports, workflows, or the API can bypass it**, so pair it with validation and monitoring.

## Plan

1. Audit how many open deals are missing key properties at each stage (before state)
2. Decide the required properties per stage (progressive: more required as the deal advances)
3. Configure required properties per stage + backward-move and closed-deal rules
4. Backfill or flag existing non-compliant deals
5. Verify and monitor (after state)

## Before State

### Audit Script

```python
import os
from hubspot import HubSpot
from dotenv import load_dotenv

load_dotenv()
api_client = HubSpot(access_token=os.getenv("HUBSPOT_ACCESS_TOKEN"))

# Example: open deals in later stages missing amount / close date
KEY_PROPS = ["amount", "closedate", "hubspot_owner_id"]
for prop in KEY_PROPS:
    result = api_client.crm.deals.search_api.do_search(
        public_object_search_request={
            "filterGroups": [{"filters": [
                {"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"},
                {"propertyName": prop, "operator": "NOT_HAS_PROPERTY"}
            ]}],
            "limit": 0
        }
    )
    print(f"Open deals missing {prop}: {result.total}")
```

Record: per key property, how many open deals are missing it. This quantifies the current data gap and builds the case for stage-gating.

## Execute

### Step 1: Define required properties per stage (progressive)

Require more as commitment rises. Example:

| Stage | Newly required properties |
|---|---|
| Discovery Completed | Deal owner, Amount (estimate), Close date |
| Proposal Reviewed | Decision maker / Economic buyer contact, Confirmed amount |
| Verbal Commit | Close date (firm), Next step |
| Closed Won | Won reason, Products/line items |
| Closed Lost | Closed lost reason |

### Step 2: Configure in HubSpot

Settings > Objects > Deals > Pipelines > select pipeline > for each stage: **Set required properties** the rep must complete to move a deal into that stage. Add a clear helper description so reps know why.

### Step 3: Add guardrails via pipeline rules

In the same pipeline settings: **restrict backward stage moves** (allow only with a reason, or restrict to admins) and **limit editing of closed deals** so won/lost deals stay frozen for accurate reporting.

### Step 4: Backfill / flag existing non-compliant deals

Stage-gating only applies going forward. For the existing gaps found in the audit: build a list/view of open deals missing required properties and route to owners to complete, or use a workflow to notify the deal owner. (An internal-notification workflow for this pairs well — see the `automation` group.)

### Step 5: Close the API/import bypass

Because API/import/workflow writes bypass stage-gating, add a validation rule on the property where supported (e.g. amount format) and monitor completeness with the audit script on a schedule.

## After State

**Verification checklist:**

1. Each stage has the intended required properties configured.
2. Moving a test deal forward without a required field is blocked in the UI. (Create a test deal, try to advance it, confirm the block, then delete it.)
3. Backward moves and closed-deal edits are restricted per policy.
4. Count of open deals missing required properties is trending down after owner backfill.
5. A scheduled/periodic completeness check is in place (re-run the audit script).

## Key Technical Learnings

- **Progressive requirements beat all-at-once.** Requiring everything at stage 1 pushes reps to create junk deals late; require more as the buyer commits more.
- **UI-only enforcement has a hole.** Imports, workflows, and API writes skip stage-gating — layer validation rules + monitoring on top for the fields that matter most.
- **Required + reason-gated backward moves** stop reps from sandbagging by yo-yoing stages.
- **Lock closed deals** so historical win/loss reporting doesn't shift under you.
- **This enforces `deal-pipeline-architecture`'s exit criteria** and feeds clean data to `deal-rotting-alerts` and the reporting playbooks.

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
