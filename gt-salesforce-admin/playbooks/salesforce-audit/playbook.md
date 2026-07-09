---
name: salesforce-audit
description: "Run a comprehensive Salesforce CRM org audit. Analyzes leads, contacts, accounts, opportunities, engagement, data quality, deliverability, and ownership. Use when starting an org cleanup, onboarding a new client, or performing quarterly health checks."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: audit-planning
---

# Salesforce CRM Org Audit

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Run a full diagnostic audit of a Salesforce org. This skill collects metrics across eight dimensions, grades each one, and produces a prioritized report with actionable recommendations.

The single biggest difference from a HubSpot audit: Salesforce splits people into two objects. A **Lead** is pre-conversion and has no Account. A **Contact** is post-conversion and is always tied to an Account. Every "people" metric below must be run against BOTH objects and reported separately, then summed where it makes sense.

## Setup

1. **Get the credentials.** Check `.env` for Salesforce credentials. If not set, ask the user to provide them:
   ```
   SF_USERNAME=user@company.com
   SF_PASSWORD=xxxx
   SF_SECURITY_TOKEN=xxxx
   SF_DOMAIN=login    # use "test" for a sandbox
   ```

2. **Install dependencies.** Use `uv` (not pip):
   ```bash
   uv pip install simple-salesforce python-dotenv
   ```

3. **Create the output directory** if it does not exist:
   ```bash
   mkdir -p reports
   ```

## Audit Dimensions

Run queries for each of the following eight dimensions. Collect exact counts for every metric. Where a metric applies to people, report Lead and Contact separately.

### 1. Database Size
- Total Leads (`IsConverted = false`)
- Total Contacts
- Total Accounts
- Total Opportunities (open vs closed)
- Converted Leads (`IsConverted = true`) still lingering as Leads

### 2. Email Deliverability
- Hard bounced Leads and Contacts (`EmailBouncedReason` is not null)
- Bounced date present (`EmailBouncedDate` is not null)
- Opted out of email (`HasOptedOutOfEmail = true`) on Lead and Contact
- Do Not Call (`DoNotCall = true`)
- Never-emailed records (no activity history of an email send)
- Invalid email format (regex check on `Email`)

### 3. Data Completeness
- Leads missing `Email`
- Contacts missing `Email`
- Leads missing `Company` (required on Lead, so blanks signal bad imports)
- Contacts missing `AccountId` (orphan contacts)
- Leads and Contacts missing `Industry`
- Missing `Country` / `State` (Lead, Contact, Account billing)
- Leads missing `Status`
- Leads missing `LeadSource`
- Leads missing `Rating` (breaks scoring and Agentforce)
- Missing `OwnerId` pointing to an active user
- Accounts missing `Website`
- Accounts missing `Industry`
- Opportunities missing `Amount`, `CloseDate`, `StageName`

### 4. Engagement Health
- Last activity distribution: active in last 30 days, 31-90, 91-180, 181-365, 365+, never (`LastActivityDate`)
- Leads with no activity since creation
- Contacts with no activity in 12+ months
- Open Opportunities with no activity in 60+ days

### 5. Duplicate Analysis
- Duplicate email addresses across Leads
- Duplicate email addresses across Contacts
- Lead/Contact email overlap (same person as both a Lead and a Contact — common and usually wrong)
- Accounts sharing the same `Website` domain
- Accounts with identical `Name` (exact; flag near-matches for Matching Rule review)

### 6. Owner Health
- Inactive Users (`IsActive = false`) who still own Leads
- Inactive Users who still own Contacts
- Inactive Users who still own Accounts
- Inactive Users who still own Opportunities
- Records owned by a Queue instead of a User (Leads especially)
- Records with no usable owner

### 7. Configuration & List Health
- Active vs inactive Validation Rules
- Whether Duplicate Rules and Matching Rules are configured per object
- Active Flows vs Process Builders vs legacy Workflow Rules
- List views with zero matching records
- Web-to-Lead forms with zero recent submissions
- Custom fields with zero population (dead fields)

### 8. Opportunity Pipeline Health
- Opportunities without `Amount`
- Opportunities without `CloseDate`
- Open Opportunities past their `CloseDate` (slipped)
- Opportunities per `StageName`
- Stale open Opportunities (no activity 60+ days)
- Average age by stage

## API Technical Notes

These details are critical for accurate results in Salesforce specifically:

- **Use SOQL via simple-salesforce.** Counts come from `sf.query("SELECT COUNT() FROM Lead WHERE ...")`. The `totalSize` field on the response holds the count.

- **Null checks use `= null`** in SOQL, not a separate operator:
  ```sql
  SELECT COUNT() FROM Lead WHERE Email = null AND IsConverted = false
  ```

- **The Lead/Contact split is mandatory.** Always exclude converted leads with `IsConverted = false` when counting "live" leads, or you double-count people who are now Contacts.

- **Query row limits**: SOQL via the REST API caps large result sets. For counts use `COUNT()` aggregate queries (cheap, no row cap). Only use the Bulk API when you need to pull the actual records (e.g. for an export CSV).

- **Inactive owners**: query `User` with `IsActive = false`, collect their Ids, then count records `WHERE OwnerId IN (:inactiveIds)`. SOQL `IN` lists are capped, so batch the Id list if there are many inactive users.

- **Bounce fields**: `EmailBouncedReason` and `EmailBouncedDate` exist on both Lead and Contact. A non-null `EmailBouncedReason` is the hard-bounce signal.

- **Activity dating**: `LastActivityDate` is the standard roll-up of the most recent completed Task or Event. Use it for engagement recency.

- **Duplicate and Matching Rules are Setup metadata**, not data. You cannot count "rules configured" through the data API alone; use the Tooling API (`sf.toolingexecute`) or report that this dimension needs a Setup check.

- **API limits**: orgs have a 24-hour rolling API call limit. Aggregate `COUNT()` queries are one call each, so the full audit is cheap. Add backoff on `REQUEST_LIMIT_EXCEEDED`.

## Script Structure

Write a single Python script (`scripts/audit_org.py`) that:

1. Loads credentials from `.env`
2. Initializes the client:
   ```python
   from simple_salesforce import Salesforce
   sf = Salesforce(
       username=os.getenv("SF_USERNAME"),
       password=os.getenv("SF_PASSWORD"),
       security_token=os.getenv("SF_SECURITY_TOKEN"),
       domain=os.getenv("SF_DOMAIN", "login"),
   )
   ```
3. Runs each dimension's `COUNT()` queries sequentially
4. Collects all results into a structured dict, Lead and Contact separated
5. Computes letter grades per dimension (see grading rubric)
6. Renders the markdown report
7. Saves to `reports/salesforce-audit-{YYYY-MM-DD}.md`

## Grading Rubric

| Grade | Meaning | Criteria |
|-------|---------|----------|
| A | Healthy | < 5% of records affected |
| B | Minor issues | 5-15% of records affected |
| C | Needs attention | 15-30% of records affected |
| D | Significant problems | 30-50% of records affected |
| F | Critical | > 50% of records affected |

For dimensions without a simple percentage (e.g., Owner Health, Configuration), use judgment based on affected records and business impact.

## Output Format

Save to `reports/salesforce-audit-{YYYY-MM-DD}.md`:

```markdown
# Salesforce CRM Audit Report

**Date:** YYYY-MM-DD
**Org:** [org-id / instance]

## Executive Summary

| Dimension | Grade | Key Finding |
|-----------|-------|-------------|
| Database Size | B | ~XX,000 leads, XX,000 contacts, XX,000 accounts |
| Email Deliverability | D | XX% hard bounced, XX% opted out |
| Data Completeness | F | XX% leads missing Rating, XX% missing Industry |
| Engagement Health | D | XX% never engaged, XX% inactive 12+ months |
| Duplicate Analysis | C | ~X,XXX duplicate account domains, X,XXX lead/contact overlaps |
| Owner Health | F | X inactive users own XX,XXX records |
| Configuration & List Health | C | No Duplicate Rules on Lead, XX dead custom fields |
| Opportunity Pipeline Health | C | XX% opps missing amount, XX slipped close dates |

**Overall Grade: X**

## Priority Recommendations

1. **[CRITICAL] Reassign inactive-owner records** — XX,XXX records owned by X
   deactivated users. Run `/reassign-inactive-owners`.
   *Effort: 2 hours | Fully scriptable*

2. **[CRITICAL] Suppress hard bounced** — XX,XXX hard bounces across leads and
   contacts. Run `/suppress-hard-bounced`.
   *Effort: 1 hour | Hybrid (API + suppression field)*

3. ...continue ranked by impact...

---

## Detailed Findings

### 1. Database Size

| Metric | Count |
|--------|-------|
| Total Leads (unconverted) | XX,XXX |
| Total Contacts | XX,XXX |
| Total Accounts | XX,XXX |
| Open Opportunities | X,XXX |

...continue for all 8 dimensions, Lead and Contact split where relevant...

---

## Next Steps

Run `/salesforce-implementation-plan` to generate a phased cleanup plan.
```

## Skill Prescription

After generating the audit, **prescribe a specific ordered list of skills the user should run.** Do not just present findings.

### Step 1: Map Findings to Skills

**Database Hygiene** (run first — deliverability and reporting impact):
| Finding | Skill | Priority |
|---------|-------|----------|
| Leads/Contacts missing email | `/delete-no-email-leads-contacts` | P0 |
| Hard bounced | `/suppress-hard-bounced` | P0 |
| Opted out / Do Not Call | `/suppress-opted-out` | P0 |
| Unengaged records | `/suppress-unengaged-leads` | P1 |
| Duplicate accounts | `/merge-duplicate-accounts` | P1 |
| Inactive owners with records | `/reassign-inactive-owners` | P1 |

**Data Enrichment** (run second):
| Finding | Skill | Priority |
|---------|-------|----------|
| Missing account name on contact | `/enrich-account-name` | P1 |
| Missing industry | `/enrich-industry` | P1 |
| Inconsistent geo | `/standardize-geo-values` | P2 |
| Missing geo | `/backfill-geo-data` | P2 |
| Missing/wrong lead status or opp stage | `/fix-lead-status-and-stages` | P1 |
| Unowned records | `/assign-unowned-records` | P1 |

**Segmentation & Scoring** (run third):
| Finding | Skill | Priority |
|---------|-------|----------|
| No ICP classification | `/create-icp-tiers` | P2 |
| Blank Rating / no scoring | `/build-lead-scoring` | P2 |
| No segment list views | `/build-list-views-and-reports` | P2 |

**Automation (Flow)** (run fourth — prevention):
| Finding | Skill | Priority |
|---------|-------|----------|
| No new-record hygiene | `/new-record-hygiene-flow` | P2 |
| High disengagement | `/engagement-suppression-flow` | P2 |
| No lead lifecycle automation | `/lead-lifecycle-flow` | P3 |
| No bounce monitoring | `/bounce-monitoring-flow` | P2 |

**Ongoing Maintenance** (run last):
| Finding | Skill | Priority |
|---------|-------|----------|
| Unused list views | `/cleanup-list-views` | P3 |
| Unused Web-to-Lead forms | `/cleanup-web-to-lead-forms` | P3 |
| Stale flows/workflows | `/cleanup-flows-and-workflows` | P3 |
| Dashboard clutter | `/cleanup-dashboards` | P3 |
| Opportunity pipeline issues | `/cleanup-opportunities` | P3 |
| Dead custom fields | `/cleanup-fields` | P3 |
| Inactive users | `/cleanup-inactive-users` | P3 |

### Step 2: Present the Ordered Prescription

After the report, present a numbered action list grouped into Immediate (this week), Next (weeks 2-3), Later (weeks 4-6), each line naming the skill and the count behind it.

### Step 3: Suggest Next Step

End with:
```
Ready to start? Run `/salesforce-implementation-plan` for the full phased plan,
or jump straight to the top finding's skill.
```

## After Running

- Print the saved report path
- Present the ordered skill prescription
- Highlight the top 3 critical findings
- Flag any finding with no matching skill
- Suggest `/salesforce-implementation-plan`

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
