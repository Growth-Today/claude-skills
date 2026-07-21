---
name: renewal-automation
description: "Automate the renewal motion: auto-create renewal deals ahead of contract end, assign owners, and trigger renewal tasks/sequences — so recurring revenue never slips through the cracks."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: pipelines-deals
---

# Renewal Automation

Make renewals systematic instead of manual: automatically spin up a renewal deal before each contract ends, put it in the renewals pipeline with an owner, and trigger the follow-up motion. Protects recurring revenue that's easy to lose to inattention.

## Why This Matters

Renewals are the cheapest revenue you have — and the easiest to lose by forgetting. Relying on reps to remember renewal dates guarantees leakage. Automating renewal-deal creation and the follow-up motion ensures every contract gets worked ahead of expiry, with clear ownership and a forecastable renewals pipeline.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Automation > Workflows and a **renewals pipeline** (`multiple-pipelines-setup`)
- A reliable renewal/contract-end date property (custom object subscription date, or deal property)

## Critical Concept: Trigger From a Reliable Date

Renewal automation is only as good as the **renewal date** it fires from. That date must live on a reliable field — a subscription custom object (`custom-objects-setup`), a company/deal property, or a synced source. If the date is missing or stale, the automation won't fire when it should. Fix the date source first.

## Plan

1. Confirm a reliable renewal-date source + a renewals pipeline exist
2. Define the lead time (e.g. create the renewal deal 90 days before contract end)
3. Build the workflow: create renewal deal, assign owner, set stage, trigger tasks/notifications
4. Verify renewals are created on time; nothing slips (after state)

## Execute

### Step 1: Confirm inputs
You need a trustworthy renewal date (see `custom-objects-setup` for a subscription object) and a renewals pipeline (`multiple-pipelines-setup`). Fix these first.

### Step 2: Define lead time + motion
Decide how far ahead to open the renewal (commonly 90/120 days) and the motion (owner = the account's CSM/AE, first task, renewal sequence).

### Step 3: Build the workflow
Automation > Workflows (date-based, off the renewal date):
1. Trigger: renewal date is in N days.
2. Action: **create a deal** in the renewals pipeline, associated to the company/contact, with amount = current contract value.
3. Assign the owner (round-robin or account owner — see `lead-routing-round-robin`).
4. Create the first renewal task + notify the owner; optionally enroll a renewal sequence.

### Step 4: Forecast renewals
Include the renewals pipeline in forecasting (`forecasting-goals-setup`) so recurring revenue is planned, not a surprise.

## After State

**Verification checklist:**

1. Renewal deals are auto-created the defined lead time before contract end.
2. Each renewal deal lands in the renewals pipeline with an owner + first task.
3. The renewal date source is reliable (no missing dates silently skipping renewals).
4. Renewals appear in the forecast.
5. A test contract with a near renewal date generates a renewal deal. (Confirm, clean up.)

## Key Technical Learnings

- **The renewal date is the whole ballgame** — automate off a reliable field or it silently fails.
- **Create ahead, with lead time** — a renewal opened the week it expires is already late.
- **Ownership + first task** turn an auto-created deal into actual follow-up.
- **Forecast renewals separately** so recurring revenue is planned.
- **Depends on `multiple-pipelines-setup`, `custom-objects-setup`, and `lead-routing-round-robin`.**
