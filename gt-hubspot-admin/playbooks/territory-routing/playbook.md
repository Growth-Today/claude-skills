---
name: territory-routing
description: "Route leads and accounts by territory — geography, segment, industry, or account ownership — so the right rep gets the right account. Builds criteria-based assignment with team round-robin inside each territory."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation
---

# Territory Routing

Assign leads and accounts to the right rep based on territory rules (region, segment, industry, or named-account ownership), with round-robin inside each territory. Extends `lead-routing-round-robin` from "any rep" to "the right rep for this account."

## Why This Matters

Flat round-robin ignores who *should* own an account — the EMEA rep should get EMEA leads, the enterprise rep should get enterprise accounts, and named accounts should route to their owner. Territory routing enforces coverage rules so accounts land with the rep who has the context and the quota for them, and prevents two reps working the same account.

## Prerequisites

- Access to Automation > Workflows
- Teams set up by territory/segment (`users-teams-setup`)
- Reliable routing inputs: country/region (`standardize-geo-values`), ICP tier (`create-icp-tiers`), industry (`enrich-industry`)
- `lead-routing-round-robin` in place (territory routing layers on top)

## Critical Concept: Match on Reliable, Standardized Fields

Territory rules are only as good as the fields they branch on. If country is "US"/"USA"/"United States" inconsistently, region routing misfires. Standardize the routing inputs first (`standardize-geo-values`, `create-icp-tiers`). Also decide precedence: **named-account ownership > territory > round-robin fallback.**

## Plan

1. Confirm routing inputs are standardized and reliable
2. Define the territory model + precedence rules
3. Build the routing workflow: named-account → territory branch → round-robin within team → fallback
4. Verify correct coverage; no account double-owned (after state)

## Execute

### Step 1: Define territories + precedence
Map territories (e.g. AMER/EMEA/APAC, or SMB/MM/ENT, or by industry) to teams. Set precedence: existing account owner wins; else territory rule; else fallback owner.

### Step 2: Build the workflow
Automation > Workflows (contact- or company-based):
1. Enrollment: lead qualifies (`lead-status-taxonomy`).
2. **First branch:** if the account already has an owner → keep it (don't reassign).
3. **Territory branches:** by region/segment/industry → target that territory's team.
4. **Within team:** rotate to owner (round-robin).
5. **Fallback:** unmatched → fallback owner.

### Step 3: Account-level consistency
Route on the **company/account** where possible so all contacts on an account share an owner (avoids split ownership). Use association to propagate owner from company to contacts.

## After State

**Verification checklist:**

1. Routing inputs (geo, tier, industry) are standardized.
2. Territory rules + precedence are defined and documented.
3. Named accounts stay with their owner; new leads route by territory; unmatched hit fallback.
4. No account is split across two owners.
5. Test leads for each territory route correctly. (Confirm, clean up.)

## Key Technical Learnings

- **Standardize inputs first** — inconsistent country/tier values silently misroute.
- **Precedence prevents chaos** — owner > territory > round-robin fallback.
- **Route at the account level** to avoid split ownership across a company's contacts.
- **Always a fallback** — the top routing gap is leads matching no territory.
- **Layers on `lead-routing-round-robin`** using `users-teams-setup`, `standardize-geo-values`, `create-icp-tiers`.
