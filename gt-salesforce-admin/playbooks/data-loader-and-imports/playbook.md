---
name: data-loader-and-imports
description: "Import, update, and mass-transfer Salesforce data safely with Data Loader / Import Wizard: field mapping, external IDs for upsert, dedupe on import, and backups before destructive ops. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-management
---

# Data Loader & Imports

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Get external data in — or bulk-update what's there — without creating a mess. Salesforce has two paths: the **Import Wizard** (simple, dedupe-aware, ≤50k) and **Data Loader** (Bulk API, upsert, all objects, millions). This playbook makes imports mapped, deduped, and reversible.

## Prerequisites
- "Import" / API + object edit permissions; Data Loader installed or the `simple-salesforce` scripts
- `matching-and-duplicate-rules` active (so imports don't create dupes)
- A backup/export before any update/delete

## Critical concept
- **Upsert needs an External ID field** (a unique key) to match existing records and avoid duplicates — without it, imports create new rows.
- **Import Wizard** applies duplicate rules and is safer for small business-user imports; **Data Loader** is for scale, upsert, and cross-object.
- Every destructive op needs a **backup first** — Salesforce only keeps deletes in the Recycle Bin ~15 days.

## Automation level
Hybrid — Data Loader / Import Wizard, or `simple-salesforce` Bulk API scripts.

## Steps
1. **Profile the file** first: row count, duplicates within the file, blanks in required/matching fields, format issues. Clean in the file.
2. **Pick the tool:** Import Wizard (small, dedupe) vs Data Loader (scale, upsert, custom objects).
3. **Map fields** to the correct API names; use an **External ID** for upsert to update-not-duplicate.
4. **Test batch** (10-20 rows) → verify mapping, dedupe, associations before the full run.
5. **Backup** (export) before any update/delete; run; verify counts + spot-check.
6. **Rollback** if wrong: Recycle Bin (deletes) or re-import the backup (updates) within the window.

## Notes
- No External ID = guaranteed duplicates on re-import. Always define the matching key.
- Backup before every destructive load — the Recycle Bin window is short and bulk deletes have no undo beyond it.
- Pairs with `matching-and-duplicate-rules`, `merge-duplicate-accounts`, and any playbook that seeds/updates data.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
