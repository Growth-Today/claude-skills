---
name: custom-objects-setup
description: "Decide when a custom object is warranted (vs a property or existing object) and set one up correctly: schema, properties, associations, and pipeline. Covers the data model builder and the Schemas API."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Custom Objects Setup

Model data that doesn't fit Contacts, Companies, Deals, or Tickets — subscriptions, licenses, properties, shipments, buying committees — as a custom object, but only when it's genuinely warranted. This playbook covers the decision, the schema design, and the setup.

## Why This Matters

Custom objects are powerful and irreversible-ish: once teams build workflows, reports, and integrations on a custom object, restructuring is painful. The most common mistakes are creating a custom object when a property or an existing object would do, and creating one without thinking through its associations. Getting the decision and the associations right up front avoids a costly rebuild.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Custom objects require an **Enterprise** tier (Marketing/Sales/Service/Ops Hub Enterprise)
- Super Admin access to Settings > Data Management > Objects (data model builder)
- Governed properties + naming conventions (`property-architecture-governance`)

## Critical Concept: Custom Object vs Property vs Existing Object

Use the decision test before building:

| Signal | Right choice |
|---|---|
| A single value describing a contact/company | **Property** (not an object) |
| Many records of the same kind, each with its own fields, related to a contact/company | **Custom object** |
| It's really a sales opportunity | **Deal** (existing object) |
| It's a support case | **Ticket** (existing object) |

Decide the primary **association** immediately: does this object belong to a Contact, a Company, both? That relationship is the hardest thing to change later.

## Plan

1. Audit existing objects/schemas so you don't duplicate (before state — `scripts/before.py`)
2. Run the decision test — confirm a custom object is actually warranted
3. Design the schema: name, primary display property, properties, associations
4. Create the object (data model builder or Schemas API) + its properties + associations
5. Add a pipeline if the object has stages; verify (after state)

## Before State

List existing object schemas (standard + custom) to avoid duplicating an object or property:

```bash
cd scripts
python before.py
```

`scripts/before.py` prints all object schemas (name, object type id, whether custom). Confirm the concept isn't already represented before creating anything.

## Execute

### Step 1: Confirm the decision
Run the decision test above. If a property or existing object fits, stop and do that instead (cheaper and simpler).

### Step 2: Design the schema
Define: object name (singular/plural), the **primary display property** (what labels each record), the core properties (with correct field types — see `property-architecture-governance`), and the associations to Contacts/Companies/Deals.

### Step 3: Create the object
**UI:** Settings > Data Management > Objects > Create custom object (data model builder). **API:** the Schemas API, e.g.:

```python
import os, requests
from dotenv import load_dotenv
load_dotenv()
H = {"Authorization": f"Bearer {os.environ['HUBSPOT_ACCESS_TOKEN']}", "Content-Type": "application/json"}
schema = {
    "name": "subscription",
    "labels": {"singular": "Subscription", "plural": "Subscriptions"},
    "primaryDisplayProperty": "subscription_name",
    "properties": [
        {"name": "subscription_name", "label": "Subscription Name", "type": "string", "fieldType": "text"},
        {"name": "mrr", "label": "MRR", "type": "number", "fieldType": "number"}
    ],
    "associatedObjects": ["CONTACT", "COMPANY"]
}
# requests.post("https://api.hubapi.com/crm/v3/schemas", headers=H, json=schema)
```

### Step 4: Associations + pipeline
Define association labels where needed (`association-labels-setup`). If the object moves through stages (e.g. onboarding), create a pipeline for it (`set up object pipelines`).

## After State

**Verification checklist:**

1. The decision test was applied — a property/existing object genuinely wouldn't have worked.
2. The object exists with the right primary display property and correctly-typed properties.
3. Associations to Contacts/Companies/Deals are correct (the hardest thing to change later).
4. If stage-based, a pipeline exists with meaningful stages.
5. The object isn't a duplicate of an existing one (confirmed in the before-state audit).

## Key Technical Learnings

- **Most "custom object" needs are actually a property or a Deal/Ticket.** Run the decision test first.
- **Associations are the load-bearing decision** — pick the primary relationship deliberately; it's the hardest to change.
- **Enterprise-only.** Don't design around custom objects on a non-Enterprise tier.
- **Reuse before create.** Audit existing schemas so you don't build a second object for the same concept.
- **Pairs with `association-labels-setup`, `calculated-rollup-properties`, and `property-architecture-governance`.**

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
