---
name: standardize-geo-values
description: "Standardize Geo Values for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-enrichment
---

# Standardize Geo Values

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Convert inconsistent country/state text into Salesforce State and Country Picklists (the native standardization mechanism). Required for reliable geographic segmentation and reporting.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- State and Country Picklists enabled in Setup (recommended) OR a mapping table

## Automation level
Hybrid. Setup enables the picklists; API/Flow remaps existing free-text values.

## Steps
1. Inventory distinct `Country` and `State` values across Lead, Contact, and Account (billing + shipping).
2. Build a mapping from variants ("US", "U.S.A.", "United States") to the canonical picklist value.
3. If State and Country Picklists are enabled, use the Setup "Scan" + "Fix" tool, or remap via API for values it cannot auto-resolve.
4. Bulk update to canonical values.
5. Report distinct-value count before and after (goal: collapse to the picklist set).

## Notes
- Enabling State and Country Picklists is a one-time Setup change that affects all objects. Test in a sandbox first.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
