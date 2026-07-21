---
name: dedupe-contacts
description: "Find and merge duplicate contacts. Audits duplicates by email and by name+company, documents trusted match rules, and guides merging via HubSpot's duplicate management tool and the API — protecting the record you keep."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-hygiene
---

# Dedupe Contacts

Identify and merge duplicate contacts so reporting, routing, and outreach act on one record per person. Complements `merge-duplicate-companies` (which handles the company side).

## Why This Matters

Duplicate contacts split activity history, double-count in reports, trigger multiple emails, and break attribution. They creep in from imports, form fills, and integrations. HubSpot has a built-in duplicate management tool plus AI-suggested matches; the job is to review, merge safely, and document the match rules you trust so it stays under control.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Contacts + the Data Quality / Manage Duplicates tool (Super Admin or data quality tools access)

## Critical Concept: Merge Keeps the Primary Record

When you merge two contacts, one is the **primary** (surviving) record — it keeps its record ID and its property values win conflicts; the secondary's most activity is merged in. Choose the primary deliberately (usually the older, more complete, or owned record). Merges are **not bulk-undoable**, so review before merging.

## Plan

1. Audit duplicates by email and by name+company (before state — `scripts/before.py`)
2. Document the match rules you trust (email exact; name+company; phone)
3. Merge via HubSpot's Manage Duplicates tool (AI suggestions) + API for known cases
4. Choose primaries deliberately; verify no data loss (after state)

## Before State

```bash
cd scripts
python before.py
```

`scripts/before.py` reports exact-duplicate emails and likely duplicates by normalized name+company across a sample — the scope of the problem before you start merging.

## Execute

### Step 1: Start with the native tool
Data Management > Data Quality > **Manage duplicates**: review HubSpot's AI-suggested contact matches. Merge the clear ones, choosing the correct primary each time. This is the safest bulk path.

### Step 2: Document trusted match rules
Write down which signals you trust for a "same person" call — **email exact match** (highest confidence), **name + company**, **phone**. Only auto/bulk-merge on high-confidence rules; review the rest.

### Step 3: API for known cases
For a defined set (e.g. same email, different casing) you can merge via the API:

```python
# api_client.crm.contacts.public_object.merge(...) / POST /crm/v3/objects/contacts/merge
# body: {"primaryObjectId": "<keep>", "objectIdToMerge": "<remove>"}
```

Always resolve the primary first.

### Step 4: Prevent recurrence
Turn on/keep HubSpot's duplicate prevention, and fix the entry points (dedupe on import — `import-data-onboarding`; email validation — `property-validation-rules`).

## After State

**Verification checklist:**

1. Exact-email duplicates are resolved (re-run `before.py` — count drops).
2. Merges chose the correct primary (spot-check a few: activity + key props preserved).
3. Trusted match rules are documented.
4. Entry-point prevention is in place (import dedup + email validation).
5. Duplicate management review is folded into `weekly-cleanup-routine`.

## Key Technical Learnings

- **Email is the highest-confidence match** — merge freely on exact email; review name/phone matches.
- **Primary choice matters** — its ID survives and its values win conflicts; pick the fuller/owned record.
- **Merges aren't bulk-undoable** — review before, don't mass-merge on weak signals.
- **Prevention closes the loop** — dedup-on-import + email validation stop new duplicates.
- **Complements `merge-duplicate-companies`** for full deduplication.

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
