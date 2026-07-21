---
name: permission-sets-roles
description: "Apply least-privilege access with reusable permission sets. Audits over-permissioned users and excess Super Admins, defines a role matrix by job function, and standardizes onboarding so access is consistent and minimal."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: governance
---

# Permission Sets & Roles

Give every user exactly the access their job needs — no more — using reusable permission sets instead of hand-tuning each person. This reduces security risk, prevents accidental data changes, and makes onboarding one click instead of a checklist.

## Why This Matters

Two failure modes are everywhere: too many Super Admins (any of whom can delete data, change billing, or export everything), and per-user permissions tuned by hand (so no two reps have the same access and onboarding is guesswork). Permission sets fix both — define access once per role, assign consistently, and keep Super Admin to the few who truly need it.

## Prerequisites

- Super Admin access to Settings > Users & Teams > Permission Sets
- `users-teams-setup` done (teams exist and users are assigned)
- Custom permission sets require an Enterprise tier; on Pro you still standardize using the built-in presets and saved templates

## Critical Concept: Permission Sets Are Reusable Templates

A **permission set** bundles per-tool access (CRM object edit/view, workflows, properties, data quality tools, reporting, publishing, account settings) into a named template you assign to users. Change the set, and every assigned user updates. **Super Admin** overrides everything — treat it as break-glass, not a default.

## Plan

1. Audit current access: who is Super Admin, who looks over-permissioned (before state)
2. Define a role matrix (job function → access level)
3. Create a permission set per role
4. Reassign users to the right set; strip excess Super Admins
5. Verify least-privilege + standardize onboarding (after state)

## Before State

### Audit Script

```python
import os, requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
H = {"Authorization": f"Bearer {TOKEN}"}

users = requests.get("https://api.hubapi.com/settings/v3/users?limit=100", headers=H).json()
results = users.get("results", [])
supers = [u for u in results if u.get("superAdmin")]
print(f"Total users: {len(results)}")
print(f"Super Admins: {len(supers)}")
for u in supers:
    print(f"  - {u.get('email')}")
print("\nReview: is every Super Admin above truly necessary? Most orgs need 2-3.")
```

Record: total users, Super Admin count and who, and (from the UI) which users have non-standard, hand-tuned permissions. Excess Super Admins are the top finding.

## Execute

### Step 1: Define the role matrix

Map job functions to access. Example:

| Role | Access level |
|---|---|
| SDR | View/edit contacts + own deals; no settings; no export |
| AE | Edit own deals + pipeline; no property/settings edit |
| RevOps / Admin | Properties, workflows, data quality, reporting; not billing |
| Super Admin | Everything (2-3 people max) |

### Step 2: Create permission sets

Settings > Users & Teams > **Permission Sets** > create one per role from the matrix. Be explicit about the settings-level permissions (edit property settings, data quality tools access, workflow edit) — those are the ones that cause damage when over-granted.

### Step 3: Reassign users + strip excess Super Admin

Assign each user the permission set for their role. Remove Super Admin from anyone who doesn't strictly need it (downgrade to the RevOps/Admin set). Coordinate before removing — confirm no one relies on a Super-Admin-only action.

### Step 4: Standardize onboarding

Rule: new users get a **permission set by role + a primary team** (with `users-teams-setup`) — never hand-tuned. This keeps access consistent and auditable.

## After State

**Verification checklist:**

1. Super Admin count is minimal (typically 2-3) and every one is justified.
2. Every user is on a role-based permission set, not hand-tuned access.
3. Settings-level permissions (property edit, workflows, data quality) are limited to admin roles.
4. A documented role matrix exists.
5. Onboarding uses "permission set + primary team" as the default.

## Key Technical Learnings

- **Fewest Super Admins possible.** Every Super Admin is a full-access, full-blast-radius account.
- **Sets over per-user tuning.** Reusable sets make access consistent, auditable, and one-click to onboard.
- **Guard the settings-level permissions.** Property edit, workflow edit, and data quality tools cause the most accidental damage — restrict to admins.
- **Least privilege is a process, not a one-time pass** — re-review during `quarterly-database-cleanup`.
- **Depends on `users-teams-setup`** and pairs with `security-health-audit` for the full governance picture.
