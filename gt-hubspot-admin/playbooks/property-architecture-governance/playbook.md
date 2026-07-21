---
name: property-architecture-governance
description: "Bring order to property sprawl. Audits custom properties across objects, establishes naming conventions and property groups, assigns ownership, and defines a governance process so the data model stays clean as the portal scales."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Property Architecture & Governance

Design and govern the property layer of the CRM: consistent naming, sensible property groups, the right field types, clear ownership, and a process that stops property sprawl before it starts. This is the "build" counterpart to `cleanup-properties` (which removes the mess) — here you prevent the mess.

## Why This Matters

Properties are where every dependency in HubSpot lives — reports, workflows, lists, integrations, and views all reference them. Left ungoverned, teams create near-duplicate fields ("Industry", "industry_2", "Vertical"), pick the wrong field type (free-text where a dropdown belongs), and nobody knows which property is the source of truth. The result is unreliable segmentation and reporting. A governed property layer is the foundation the reporting, scoring, and automation playbooks depend on.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Settings > Properties (Super Admin or "Edit property settings" permission)
- Ideally run `cleanup-properties` first to remove unused fields before standardizing what remains

## Critical Concept: Field Type Is a One-Way Door (Mostly)

Choosing the right field type up front matters because some conversions are lossy or impossible (e.g. free-text → dropdown requires value mapping; number → text loses calculation ability). Governance means deciding the type deliberately:

| Data | Right type | Wrong type (common mistake) |
|---|---|---|
| Industry, Region, Tier | Dropdown / multi-select | Single-line text (creates variants) |
| Revenue, Employees | Number | Text |
| Renewal date | Date picker | Text |
| Consent / flags | Single checkbox / dropdown | Free text |

## Plan

1. Audit all custom properties per object: count, field types, unused, duplicates (before state)
2. Define naming conventions + property group structure
3. Consolidate duplicates and fix wrong field types (with value mapping)
4. Assign property ownership and document the source-of-truth field for each concept
5. Stand up a lightweight governance process (before state → ongoing)

## Before State

### Audit Script

```python
import os
from hubspot import HubSpot
from dotenv import load_dotenv

load_dotenv()
api_client = HubSpot(access_token=os.getenv("HUBSPOT_ACCESS_TOKEN"))

for obj in ["contacts", "companies", "deals"]:
    props = api_client.crm.properties.core_api.get_all(object_type=obj)
    custom = [p for p in props.results if not p.hubspot_defined]
    print(f"\n{obj}: {len(custom)} custom properties")
    # Flag field-type smells and naming inconsistencies
    text_fields = [p.name for p in custom if p.field_type in ("text", "textarea")]
    print(f"  free-text fields (dropdown candidates): {len(text_fields)}")
    # naive duplicate detector on normalized labels
    seen = {}
    for p in custom:
        key = p.label.lower().replace(" ", "").replace("_", "")
        seen.setdefault(key, []).append(p.name)
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    if dupes:
        print(f"  possible duplicates: {dupes}")
```

Record: custom property count per object, free-text fields that should be dropdowns, and likely duplicate concepts. This is the sprawl baseline.

## Execute

### Step 1: Naming convention

Adopt one convention and document it, e.g. `Title Case labels`, internal names lowercase with prefixes by source (`sf_` for Salesforce-synced, `calc_` for calculated). Consistency matters more than the exact scheme.

### Step 2: Property groups

Group properties by function under Settings > Properties (e.g. "Firmographics", "Scoring", "Lifecycle", "Consent"). Groups make records readable and help reps find fields.

### Step 3: Consolidate duplicates + fix field types

For each duplicate concept, pick the source-of-truth property, migrate values from the duplicates into it (workflow or API), then archive the duplicates (`cleanup-properties`). For wrong field types, create the correctly-typed property, map + migrate values, then retire the old one. Never delete a property still referenced by a workflow/report — check dependencies first.

### Step 4: Ownership + source of truth

For each key concept (industry, tier, owner, revenue), document the single source-of-truth property and who owns changes to it. Put this in a shared property dictionary.

### Step 5: Governance process

Adopt a simple rule: new custom properties require a named owner and a reason, and are reviewed quarterly (fold into `quarterly-database-cleanup`). This prevents the sprawl from returning.

## After State

**Verification checklist:**

1. Every custom property belongs to a named property group.
2. No unresolved duplicate concepts remain (audit script shows no duplicate labels).
3. Key concepts use the correct field type (dropdowns instead of free-text where it matters).
4. A property dictionary exists naming the source-of-truth field + owner for each concept.
5. A governance rule (owner + reason + quarterly review) is documented.

## Key Technical Learnings

- **Field type is (mostly) a one-way door.** Decide dropdown-vs-text deliberately; fixing it later means value mapping and migration.
- **Dependencies first.** A property may power a workflow, report, or integration — always check before archiving/retyping.
- **Naming consistency > naming perfection.** Any documented convention beats an undocumented "best" one.
- **Governance is the point.** Cleanup is one-time; the owner+reason+review rule is what keeps the model clean.
- **This underpins everything downstream** — scoring, segmentation, reporting, and validation all assume trustworthy properties.
