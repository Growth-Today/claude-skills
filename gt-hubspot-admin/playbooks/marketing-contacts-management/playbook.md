---
name: marketing-contacts-management
description: "Control marketing-contact status to cut billing waste. Audits marketable contacts, sets non-marketing on unengaged/non-sendable records, and automates status so you only pay to market to contacts you actually email."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: segmentation
---

# Marketing Contacts Management

HubSpot bills on **marketing contacts**. This playbook makes sure you're only paying for contacts you actually market to — auditing marketable status, setting unengaged/non-sendable contacts to non-marketing, and automating it so the bill stays lean.

## Why This Matters

Every marketing contact counts toward your tier limit and cost. Databases fill with contacts nobody emails — unengaged, bounced, unsubscribed, internal, or test records — all silently marked marketable. Managing marketing-contact status is one of the highest-ROI admin tasks: it directly lowers cost and improves list quality without losing any data (non-marketing contacts still exist in the CRM).

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Marketing Hub with the marketing-contacts pricing model
- Access to Contacts + workflows

## Critical Concept: Non-Marketing ≠ Deleted

Setting a contact to **non-marketing** keeps the record (and all its data/history) but excludes it from marketing emails/ads and from the marketing-contact count/bill. It's reversible. The `hs_marketable_status` behavior and the timing of when set-as-non-marketing takes effect (typically the next billing update) are HubSpot-controlled — plan around the renewal date.

## Plan

1. Audit marketable contacts and how many are unengaged/non-sendable (before state)
2. Define which contacts should be non-marketing
3. Bulk set non-marketing (UI/list) + automate for the future
4. Verify the marketable count drops; no wanted contacts excluded (after state)

## Before State

```python
import os, requests
from dotenv import load_dotenv
load_dotenv()
H = {"Authorization": f"Bearer {os.environ['HUBSPOT_ACCESS_TOKEN']}", "Content-Type": "application/json"}

# Marketable contacts total
payload = {"filterGroups": [{"filters": [
    {"propertyName": "hs_marketable_status", "operator": "EQ", "value": "true"}
]}], "limit": 0}
r = requests.post("https://api.hubapi.com/crm/v3/objects/contacts/search", headers=H, json=payload)
print(f"Marketable contacts: {r.json().get('total')}")
```

Record: total marketable contacts, and how many are unengaged (no open/click 6-12m), bounced, unsubscribed, or internal/test — the reclaimable count.

## Execute

### Step 1: Define non-marketing criteria
Typical set: hard-bounced, globally unsubscribed, unengaged 12m+, internal/employee, and test/junk contacts. Coordinate with the suppression playbooks (much of this overlaps).

### Step 2: Bulk set non-marketing
Build lists for each criterion and set the contacts to **non-marketing** (via the list bulk action). Note: changes take effect at the next billing update — do this ahead of renewal.

### Step 3: Automate going forward
Build a workflow to set non-marketing automatically on the triggers you trust (e.g. hard bounce, global unsubscribe, long-term unengaged). This keeps the marketable count from creeping back up.

### Step 4: Guard against over-exclusion
Exclude contacts in active sequences/nurtures from the non-marketing rules so you don't cut live campaigns.

## After State

**Verification checklist:**

1. Marketable-contact count drops after the pass (re-run the audit).
2. Non-marketing was applied by defined criteria, not blindly.
3. No contacts in active campaigns were set non-marketing.
4. A workflow keeps unengaged/bounced/unsub contacts non-marketing automatically.
5. Timing was aligned with the billing update / renewal date.

## Key Technical Learnings

- **Non-marketing is reversible and lossless** — the record stays; it just leaves the bill and marketing sends.
- **Highest-ROI hygiene task** — directly lowers cost.
- **Timing matters** — changes hit at the next billing update; act before renewal.
- **Heavy overlap with suppression** — coordinate with `suppress-*` playbooks and `contact-data-decay-review`.
- **Protect active campaigns** — exclude in-sequence contacts from the rules.
