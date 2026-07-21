---
name: lead-status-taxonomy
description: "Define a clear lead status taxonomy and the MQL/SQL handoff. Audits current lead status values, standardizes them with entry/exit definitions, and aligns marketing and sales on when a lead is ready to route."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: segmentation
---

# Lead Status Taxonomy

Define what each lead status means, who owns it, and exactly when a lead is "ready for sales." This is the shared language that makes lifecycle reporting, routing, and the marketing↔sales handoff work.

## Why This Matters

"Lead status" and "lifecycle stage" are the two most-misused fields in HubSpot. When statuses are ad hoc ("Interested", "Warm", "Follow up") with no definitions, marketing and sales argue about what an MQL is, routing fires on the wrong trigger, and funnel reports are meaningless. A defined taxonomy — each status with an entry and exit definition — is the prerequisite for reliable routing (`lead-routing-round-robin`) and lifecycle dashboards.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Settings > Properties (to edit the Lead Status property options)
- Marketing + sales alignment on the MQL/SQL definition (this is a business agreement, not just config)

## Critical Concept: Lead Status ≠ Lifecycle Stage

**Lifecycle stage** = where the contact is in the overall journey (Subscriber→Lead→MQL→SQL→…). **Lead status** = the working sub-state *within* sales follow-up (New, Attempting, Connected, Qualified, Unqualified). Keep them distinct: lifecycle drives the funnel, lead status drives the rep's daily queue. The "ready to route to sales" moment is the bridge between them.

## Plan

1. Audit current lead status values and distribution (before state — `scripts/before.py`)
2. Define the target status set with entry/exit definitions
3. Map old values → new; update the property options
4. Backfill existing records; align the MQL→SQL handoff trigger
5. Verify + document the taxonomy (after state)

## Before State

Run the audit to see the current mess:

```bash
cd scripts
python before.py
```

`scripts/before.py` prints the distribution of `hs_lead_status` values so you can see the ad hoc/duplicate statuses to consolidate.

## Execute

### Step 1: Define the target set
Keep it small and defined. Example:

| Lead status | Entry definition | Owner |
|---|---|---|
| New | Just became a lead, no outreach yet | Marketing/SDR |
| Attempting | Outreach started, no connect yet | SDR |
| Connected | Two-way conversation happened | SDR |
| Qualified (→ route) | Meets MQL/SQL criteria → hand to AE | SDR→AE |
| Unqualified | Doesn't fit ICP / not now | SDR |

### Step 2: Map + update property options
Map every existing value to a target value. Update the Lead Status property options (Settings > Properties), then migrate old values to new (workflow or API), then remove the retired options (`cleanup-properties`).

### Step 3: Align the handoff
Define the single trigger for "ready for sales" (e.g. Lead status = Qualified, or lifecycle = MQL with score threshold) and use it as the enrollment trigger for `lead-routing-round-robin`. Marketing and sales must agree on this one definition.

### Step 4: Backfill
Set a sensible default (e.g. "New") for records with no lead status, and re-map any ad hoc values to the new set.

## After State

**Verification checklist:**

1. Lead status has a small, defined value set — no ad hoc/duplicate options remain (re-run `before.py`).
2. Every status has a written entry/exit definition and an owner.
3. Lifecycle stage and lead status are used distinctly (not duplicating each other).
4. The "ready for sales" trigger is defined and drives routing.
5. No records with blank lead status (backfilled to default).

## Key Technical Learnings

- **Lead status ≠ lifecycle stage.** Conflating them is the root of most funnel-reporting confusion.
- **Definitions beat labels.** A status without an entry definition will be applied inconsistently.
- **One agreed handoff trigger** is what ends the marketing-vs-sales MQL argument — and what routing depends on.
- **Keep the set small.** Every extra status is another thing to define, train, and report on.
- **Feeds `lead-routing-round-robin` and the lifecycle dashboards** in `revops-core-dashboards`.
