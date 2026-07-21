---
name: association-labels-setup
description: "Model relationships between records with association labels (e.g. decision maker, billing contact, parent company). Audits current associations, defines labels, and uses them for segmentation, routing, and reporting."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Association Labels Setup

Go beyond "this contact is linked to this company" — label *how* records relate (decision maker, billing contact, influencer, parent/child company) so the relationships become usable in lists, workflows, and reports.

## Why This Matters

Plain associations lose the meaning of a relationship. In any real buying committee, one contact is the economic buyer, another is a blocker, a third is a champion — and treating them identically wrecks ABM targeting and deal strategy. Association labels capture that meaning, turning "10 contacts on this account" into "here's the decision maker and the billing contact," which segmentation, routing, and reporting can then act on.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Super Admin access to Settings > Data Management > Objects > Associations
- Labeled associations (beyond the default unlabeled association) generally require a Pro+/Enterprise context

## Critical Concept: Association Types vs Labels

An **association type** is the pairing of two object kinds (Contact↔Company). A **label** describes the role within that pairing (e.g. Contact → Company: "Decision maker"). Labels can be one-directional ("reports to") or paired. There are limits on how many labels an association type can have, so define a deliberate, small set — not one per whim.

## Plan

1. Audit current association types + labels in use (before state)
2. Define the label set you actually need (decision maker, billing, champion, parent/child)
3. Create labels on the relevant association types
4. Apply labels to key records; use them in lists/workflows/reports
5. Verify labels are used, not just created (after state)

## Before State

```python
import os, requests
from dotenv import load_dotenv

load_dotenv()
H = {"Authorization": f"Bearer {os.environ['HUBSPOT_ACCESS_TOKEN']}"}

# List association labels for the contact<->company association type
r = requests.get(
    "https://api.hubapi.com/crm/v4/associations/contact/company/labels",
    headers=H
)
print("Contact<->Company association labels:")
for lbl in r.json().get("results", []):
    print(f"  - {lbl.get('label')} (category={lbl.get('category')}, typeId={lbl.get('typeId')})")
```

Record: which association types already have labels, and whether they're used consistently. Often you'll find zero labels (everything unlabeled) — that's the gap.

## Execute

### Step 1: Define the label set
Keep it small and meaningful. Common B2B set for Contact↔Company: **Decision maker, Champion, Billing contact, Influencer, Blocker**. For Company↔Company: **Parent, Subsidiary**. For Contact↔Deal: **Decision maker, Point of contact**.

### Step 2: Create the labels
Settings > Data Management > Objects > select object > **Associations** > add labels to the relevant association type. (API: the `/crm/v4/associations/{from}/{to}/labels` endpoints.)

### Step 3: Apply + operationalize
Apply labels on key accounts (manually for top accounts, or via workflow/import for scale). Then use them: lists ("companies with a labeled Decision maker"), routing (notify the decision maker's owner), and reporting (deals with vs without an identified economic buyer — ties to `deal-stage-required-fields`).

## After State

**Verification checklist:**

1. A small, deliberate label set exists on the relevant association types (not sprawl).
2. Key accounts have labels applied (decision maker/billing at minimum).
3. At least one list/workflow/report actually uses a label (labels unused = wasted).
4. Labels are documented (what each means, when to apply).
5. Label limits per association type were respected.

## Key Technical Learnings

- **Unlabeled associations lose the relationship's meaning** — labels are what make buying-committee data usable.
- **Small, defined label set.** There are per-type limits, and sprawl defeats the purpose.
- **Create ≠ use.** A label that no list/workflow/report references is dead weight — operationalize it.
- **Powers ABM + deal strategy** — pairs with `custom-objects-setup` (buying committee) and `deal-stage-required-fields` (require an identified decision maker).
