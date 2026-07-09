---
name: merge-duplicate-accounts
description: "Merge Duplicate Accounts for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: database-hygiene
---

# Merge Duplicate Accounts

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Find and merge duplicate Accounts. Salesforce has a native merge (unlike HubSpot, which has no bulk company merge API) plus Matching and Duplicate Rules to prevent recurrence.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- Permission to merge Accounts

## Automation level
Hybrid. API for discovery and CSV export; native merge UI or Apex `Database.merge` for the actual merge (max 3 records per merge call, child records auto-reparent to the surviving record).

## Steps
1. Discover by website domain: group Accounts on the host part of `Website`.
2. Discover by exact `Name` match. Flag near-matches (e.g. "Acme" vs "Acme Inc") for manual review, since SOQL cannot fuzzy match.
3. Export duplicate sets to CSV: each row a candidate group with Ids, name, website, owner, open opp count.
4. Pick the surviving record per group (most complete, most open opps, most recent activity).
5. Merge: native UI for small volumes, or Apex `Database.merge(master, duplicate)` in batches for large volumes. Children (Contacts, Opportunities, Cases, Activities) reparent automatically.
6. After merging, turn ON a Duplicate Rule + Matching Rule on Account (website + name) to stop recurrence.

## Notes
- The same company as two legitimate divisions may be two valid Accounts. Confirm before merging.
- Do NOT merge across record types without checking the page layout and required fields.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
