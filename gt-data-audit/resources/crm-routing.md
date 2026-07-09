# CRM Routing

This skill is CRM-agnostic. The 10 dimensions, benchmarks, and scoring work identically regardless of CRM. This file is LIGHT "where to start" guidance only. It tells the person which reports and views to open first. It does NOT contain deep extraction queries (SOQL, API calls). Deep portal automation belongs in the dedicated admin skills.

The work is the same everywhere: filter to one tight ICP slice, pull a sample (100 to 200 records), run it through a verifier, map results back to the 10 dimensions, score, and prioritize fixes.

## HubSpot

- **Coverage and Freshness:** Contacts > "All Contacts" list. Filter on jobtitle, industry, annualrevenue. Add the "Last enriched" or a custom "Last updated" property as a column to read recency
- **Email Accuracy:** Settings > Health > Email Health dashboard for sending reputation and bounce trends. Export a sample for third-party verification
- **CRM Hygiene:** Settings > Objects > Companies > Manage duplicates. Run the same on Contacts
- **Governance:** Settings > Users and Teams for write access. Property history for field ownership
- **Deep HubSpot work:** defer to `gt-hubspot-admin`

## Salesforce

- **Coverage and Freshness:** Reports > Contacts and Accounts > new custom report with ICP filters. Add LastModifiedDate and any enrichment date field as columns
- **Email Accuracy:** Sales Cloud Email Insights, or a Validity Everest integration if installed. Export a sample for third-party verification
- **CRM Hygiene:** Setup > Duplicate Rules. Run the Duplicate Record Sets report
- **Governance:** Setup > Users for write access. Field History Tracking for ownership
- **Deep Salesforce work:** defer to the future `gt-salesforce-admin` skill

## Pipedrive

- **Coverage and Freshness:** People > Filters. Combine title, organization, and last activity date
- **Email Accuracy:** Native verification via Mailtastic, or export and run through ZeroBounce
- **CRM Hygiene:** Settings > Data > Merge duplicates
- **Governance:** Settings > Manage users for write access

## Close

- **Coverage and Freshness:** Smart Views with filters on lead and contact attributes
- **Email Accuracy:** Built-in email validation. Export a sample for a second opinion
- **CRM Hygiene:** Smart Views > duplicate detection
- **Governance:** Settings > Memberships and permissions

## Attio

- **Coverage and Freshness:** Views > Filters on record attributes. Add a "last modified" or enrichment attribute column
- **Email Accuracy:** Workflows with a verification integration, or export for third-party check
- **CRM Hygiene:** Built-in record merging
- **Governance:** Workspace settings > Members

## Other CRMs

For Folk, Notion CRMs, and custom databases, the principle holds:
1. Filter to your ICP slice
2. Export 100 to 200 records as CSV
3. Run through a verifier (ZeroBounce or similar)
4. Map results back to the 10-dimension framework
5. Score and prioritize fixes


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
