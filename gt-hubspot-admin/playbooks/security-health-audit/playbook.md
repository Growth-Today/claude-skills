---
name: security-health-audit
description: "Audit and harden account security. Reviews Super Admin count, 2FA/SSO enforcement, inactive users and seat usage, and HubSpot's Security Health settings, then reassigns and deactivates stale users safely."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: governance
---

# Security Health Audit

Harden the portal: minimize Super Admins, enforce two-factor authentication, remove or deactivate stale users, and work through HubSpot's Security Health checklist. This protects the data layer that every other playbook depends on.

## Why This Matters

A HubSpot portal holds the company's entire contact database, pipeline, and often PII. The most common security gaps are boring but serious: too many Super Admins, users without 2FA, and departed employees who still have active seats (and still own records). A periodic security health pass closes these before they become an incident — and frees paid seats.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Super Admin access to Settings > Account Defaults > Security (Security Health) and Users & Teams

## Critical Concept: Deactivate, Don't Just Delete

Removing a user does not reassign the records they own — it can orphan contacts, companies, and deals. Always **reassign first** (see `reassign-deactivated-owners` and `cleanup-lead-owners`), then remove the seat. Deactivating stale users also recovers paid seats.

## Plan

1. Audit users: Super Admins, seat usage, likely-stale accounts (before state — `scripts/before.py`)
2. Work through HubSpot's Security Health checklist
3. Enforce 2FA (and SSO if available)
4. Reassign + deactivate stale users safely
5. Verify + schedule recurring review (after state)

## Before State

Run the user/security audit:

```bash
cd scripts
python before.py
```

`scripts/before.py` lists total users, Super Admin count and who, and users flagged for review — the evidence for the hardening steps. Also open Settings > Account Defaults > **Security** to see HubSpot's own Security Health recommendations.

## Execute

### Step 1: Work the Security Health checklist

Settings > Account Defaults > Security. Address each flagged item: 2FA enforcement, SSO, session timeout, and any account-level warnings HubSpot surfaces.

### Step 2: Minimize Super Admins

Cross-check with `permission-sets-roles` — downgrade any Super Admin who doesn't strictly need it. Target 2-3.

### Step 3: Enforce 2FA / SSO

Require two-factor authentication for all users (Settings > Account Defaults > Security). If the org has SSO, enforce it so access follows the identity provider (and offboarding is automatic).

### Step 4: Reassign + deactivate stale users

For departed or never-logging-in users: **first** reassign their owned records (`reassign-deactivated-owners`, `cleanup-lead-owners`), **then** remove/deactivate the seat. This avoids orphaned records and frees paid seats.

## After State

**Verification checklist:**

1. Super Admin count is minimal and justified.
2. 2FA is enforced for all users (SSO enforced if available).
3. No active seats for departed users; their records were reassigned first.
4. All Security Health checklist items are addressed or consciously accepted.
5. A recurring security review is scheduled (fold into `quarterly-database-cleanup`).

## Key Technical Learnings

- **Reassign before you remove.** Deleting a user orphans their records — always reassign first.
- **2FA and SSO are the highest-leverage controls.** They stop the most common account-takeover paths.
- **Super Admin sprawl is a security issue, not just a permissions one** — minimize it here and in `permission-sets-roles`.
- **Deactivating stale users saves money** by recovering paid seats.
- **Make it recurring.** Security drifts as people join and leave — audit on a schedule.
