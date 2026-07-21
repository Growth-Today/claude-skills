---
name: import-data-onboarding
description: "Import external data into HubSpot without creating a mess. Covers pre-import cleanup, column mapping, deduplication on import, association imports (contacts↔companies↔deals), and post-import validation and rollback."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Import & Data Onboarding

Bring external data (a purchased list, a legacy CRM export, an event list) into HubSpot cleanly — mapped correctly, deduplicated, properly associated, and validated — so an import improves the database instead of polluting it.

## Why This Matters

A careless import is the fastest way to undo months of hygiene work: duplicate contacts, mis-mapped columns, orphaned records with no company association, and lifecycle stages clobbered. Imports also bypass most validation and stage-gating, so the discipline has to live in the import process itself. Done right, an import is a controlled, reversible operation with a clear before/after.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to CRM > Import and to the relevant object/property permissions
- Governed properties + validation in place (`property-architecture-governance`, `property-validation-rules`) so mapped columns land in the right, correctly-typed fields

## Critical Concept: HubSpot Dedupes on Unique IDs

On import, HubSpot matches existing records primarily by **unique identifiers** — Email (contacts), Record ID, and custom unique-value properties; Company name/domain matching is weaker. To update (not duplicate) existing records, your file must include the matching identifier column. No identifier = new records created = duplicates.

## Plan

1. Profile and clean the source file *before* importing (before state)
2. Decide create-vs-update strategy and the matching identifier
3. Map columns to the correct (governed) properties
4. Import objects and their associations in the right order
5. Validate results and know the rollback path (after state)

## Before State

Profile the source file before touching HubSpot:

- Row count, duplicate rows within the file (by email/domain)
- Blank required fields (email for contacts, name/domain for companies)
- Format issues (emails, phones, dates, numbers) — clean these in the file first
- Does the file contain the **matching identifier** (email / record ID) for updates?

```python
# Quick source-file profile (CSV) before import
import csv, collections
path = "source.csv"
with open(path, newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
print(f"rows: {len(rows)}")
emails = [r.get("Email", "").strip().lower() for r in rows if r.get("Email")]
dupes = [e for e, n in collections.Counter(emails).items() if n > 1]
print(f"rows with email: {len(emails)} | duplicate emails in file: {len(dupes)}")
print(f"rows missing email: {sum(1 for r in rows if not r.get('Email'))}")
```

## Execute

### Step 1: Create-vs-update strategy

Decide: create new only, update existing only, or both. Ensure the file includes the matching identifier (Email or Record ID) if updating. Never import a file without an identifier if the records might already exist.

### Step 2: Map columns to governed properties

In CRM > Import, map each column to the correct property (created in `property-architecture-governance`). Watch for: lifecycle stage columns (avoid clobbering — see forward-only rule in `fix-lifecycle-stages`), owner columns, and date/number formats matching the property type.

### Step 3: Import objects and associations in order

For multi-object imports use HubSpot's **"import multiple objects with associations"** (one file with both objects, or linked files), or import in order: companies → contacts (associate to companies) → deals (associate to contacts/companies). Associations imported after the fact require the matching keys in the file.

### Step 4: Small test batch first

Import a 10–20 row sample first. Verify mapping, dedup behavior, and associations on those before running the full file. This catches mapping mistakes cheaply.

## After State

**Verification checklist:**

1. Imported record count matches expected (new vs updated split as intended).
2. No new duplicates created — spot-check via `merge-duplicate-companies` / contact dedup.
3. Associations are correct (contacts linked to companies, deals to both).
4. Mapped fields landed in the right properties with correct formats; lifecycle stages not clobbered.
5. Rollback path is known: HubSpot import history lets you **delete records from a specific import**; use it if the import went wrong (within the retention window).

## Key Technical Learnings

- **No identifier column = guaranteed duplicates.** Email (contacts) or Record ID is the anti-duplicate key on update.
- **Clean the file first.** It's far cheaper to fix formats/dupes in the CSV than in HubSpot after import.
- **Test batch always.** A 20-row dry run surfaces mapping errors before they hit 50,000 rows.
- **Imports bypass validation & stage-gating.** The import process must carry the discipline — plus post-import checks.
- **Import history is your undo.** You can delete records from a specific import; know this before you run the big one.
