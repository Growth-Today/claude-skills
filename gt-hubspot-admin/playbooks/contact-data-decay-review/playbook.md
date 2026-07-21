---
name: contact-data-decay-review
description: "Find and refresh decayed contact data. Identifies stale records (old last-activity, likely job changes, unengaged) and routes them to enrichment, re-verification, or suppression before decay corrupts targeting."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-hygiene
---

# Contact Data Decay Review

B2B contact data decays ~2-3% per month as people change jobs, emails bounce, and titles shift. This playbook finds the decayed records and routes each to the right action — re-verify, enrich, or suppress — before stale data wrecks targeting and deliverability.

## Why This Matters

A database quietly rots: emails that used to work start bouncing, titles go out of date, and once-engaged contacts go silent because they left the company. Targeting on decayed data lowers deliverability and conversion and inflates the marketable-contact bill. A periodic decay review keeps the database's *freshness* dimension healthy, complementing the suppression playbooks (which handle already-bounced contacts).

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Contacts, lists, and workflows

## Critical Concept: Decay ≠ Bounce

A bounced email is *known* bad (handle via `suppress-hard-bounced`). Decay is *suspected* stale — old last activity, no engagement in 6-12 months, or signals of a job change — where the data may still be valid but is at risk. Decay review is about triaging suspects, not deleting known-bad records.

## Plan

1. Define decay signals + thresholds for your business
2. Audit decayed records by signal (before state — inline query)
3. Route each segment: re-verify / enrich / re-engage / suppress
4. Verify freshness improved; schedule recurring review (after state)

## Before State

```python
import os, requests
from dotenv import load_dotenv
load_dotenv()
H = {"Authorization": f"Bearer {os.environ['HUBSPOT_ACCESS_TOKEN']}", "Content-Type": "application/json"}

# Contacts with no activity in ~12 months (adjust the date to your threshold)
payload = {"filterGroups": [{"filters": [
    {"propertyName": "notes_last_updated", "operator": "LT", "value": "1700000000000"}
]}], "limit": 0}
r = requests.post("https://api.hubapi.com/crm/v3/objects/contacts/search", headers=H, json=payload)
print(f"Contacts with stale last activity: {r.json().get('total')}")
```

Record counts by signal: no activity 12m+, no email engagement 6m+, missing/old title, and likely job-changers (if you have a signal source).

## Execute

### Step 1: Define signals + thresholds
Common signals: last activity > 12 months, no email open/click > 6 months, missing enrichment fields, job-change signal. Set thresholds that fit your sales cycle.

### Step 2: Route each segment
- **Re-verify:** run suspect emails through verification; hard-fails → suppression.
- **Enrich:** missing/old titles/company → `enrich-industry`, `enrich-company-name`, or an enrichment provider.
- **Re-engage:** unengaged-but-valid → the sunset/re-engagement flow (`engagement-suppression-workflow`, `reengagement-reenrollment`).
- **Suppress:** confirmed dead → suppression playbooks.

### Step 3: Reduce marketable-contact waste
Decayed, unengaged contacts you're paying for → set non-marketing where appropriate (`marketing-contacts-management`).

## After State

**Verification checklist:**

1. Decay signals + thresholds are defined and documented.
2. Each decayed segment was routed (re-verify / enrich / re-engage / suppress) — none left ignored.
3. Deliverability and engagement metrics improve after cleanup.
4. Marketable-contact count drops where dead contacts were set non-marketing.
5. Decay review is scheduled (quarterly) via `quarterly-database-cleanup`.

## Key Technical Learnings

- **Decay is a rate, not an event** — review on a schedule; a one-time pass doesn't hold.
- **Decay ≠ bounce** — triage suspects into re-verify/enrich/re-engage/suppress; don't mass-delete.
- **Freshness protects deliverability** — stale targeting quietly lowers inbox placement.
- **It saves money** — decayed unengaged contacts inflate the marketable bill.
- **Sits between enrichment and suppression** in the data-hygiene group.
