---
name: backfill-geo-data
description: "Backfill Geo Data for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: ongoing-maintenance
---

# Backfill Geo Data

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Enrich missing geographic data (country, state, city) on Leads, Contacts, and Accounts via Flow, external providers, or IP-based geolocation.

## Prerequisites
- `simple-salesforce`, credentials in `.env`
- An enrichment or IP-geolocation source for records with no usable location

## Automation level
Hybrid.

## Steps
1. Find records missing country/state/city.
2. Where an Account has the data, copy down to its Contacts via Flow.
3. For the rest, enrich via provider keyed on email domain or company.
4. Write back mapped to the State/Country Picklist values (coordinate with `/standardize-geo-values`).
5. Report fill rate.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
