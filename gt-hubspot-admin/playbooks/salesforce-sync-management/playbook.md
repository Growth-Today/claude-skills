---
name: salesforce-sync-management
description: "Manage the HubSpot–Salesforce integration safely: audit synced objects and errors, configure sync rules and field mappings, avoid the duplicate trap, and coordinate changes so the two systems don't corrupt each other."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: governance
---

# Salesforce Sync Management

Keep the HubSpot–Salesforce integration healthy: understand what syncs which direction, audit sync errors, configure field mappings and sync rules, and — above all — coordinate changes so a well-meaning edit in one system doesn't corrupt the other.

## Why This Matters

A HubSpot–Salesforce sync is powerful and fragile. Bad field mappings, uncoordinated stage/property changes, and weak dedup rules produce duplicate records, overwritten data, and endless sync errors. Several other playbooks (cleanup-deals, fix-lifecycle-stages, property changes) explicitly warn "coordinate with the Salesforce admin" — this playbook is that coordination discipline.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Settings > Integrations > Salesforce (sync settings) and the Salesforce admin as a partner

## Critical Concept: Direction + Ownership per Field

For every synced object and field, know the **sync direction** (HS→SF, SF→HS, or bidirectional) and which system is the **source of truth**. Bidirectional sync on a field with two sources of truth causes overwrite wars. Also: HubSpot matches to Salesforce records to avoid duplicates — weak matching creates the classic duplicate trap. Never restructure synced pipelines/properties unilaterally.

## Plan

1. Audit synced objects, field mappings, and current sync errors (before state — `scripts/before.py`)
2. Confirm direction + source-of-truth per synced field
3. Fix mappings, tighten dedup/matching, resolve errors
4. Establish a change-coordination rule with the SF admin (after state)

## Before State

```bash
cd scripts
python before.py
```

`scripts/before.py` counts HubSpot records carrying a Salesforce ID (contacts/companies/deals) so you know how much is synced before changing anything. Also review Settings > Integrations > Salesforce > **sync health / errors** in the UI.

## Execute

### Step 1: Map what syncs
Document each synced object + field: direction and source of truth. Flag any bidirectional field where both systems can be authoritative (overwrite risk).

### Step 2: Fix mappings + matching
Correct wrong field mappings and mismatched types. Tighten record matching (email/domain) to avoid the duplicate trap. Set inclusion lists so only intended records sync.

### Step 3: Resolve sync errors
Work the sync error queue (validation failures, required-field mismatches, picklist mismatches). Many trace back to a HubSpot value that doesn't fit a Salesforce validation rule — fix at the source.

### Step 4: Coordination rule
Adopt: no changes to synced pipelines, properties, or picklists without notifying the SF admin. This is the discipline that protects both systems (referenced by `cleanup-deals`, `fix-lifecycle-stages`, `deal-pipeline-architecture`).

## After State

**Verification checklist:**

1. Every synced field's direction + source of truth is documented.
2. No bidirectional field has two competing sources of truth.
3. Record matching prevents duplicates (spot-check recent syncs).
4. The sync error queue is worked down and monitored.
5. A change-coordination rule with the SF admin is documented and followed.

## Key Technical Learnings

- **Direction + source of truth per field** is the whole game — bidirectional with two owners = overwrite wars.
- **Weak matching = the duplicate trap** — tighten email/domain matching.
- **Sync errors usually start with a value that fails a Salesforce rule** — fix at the source.
- **Never restructure synced objects unilaterally** — coordinate; other playbooks depend on this rule.
- **This is the coordination backbone** referenced across the deal/lifecycle playbooks.

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
