---
name: users-teams-setup
description: "Set up users and teams so routing, reporting, and record visibility work correctly. Audits current users and team assignments, designs a team structure, and assigns primary/additional teams following least-privilege onboarding."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: governance
---

# Users & Teams Setup

Structure users into teams that mirror how the business actually works, so lead routing, reporting rollups, and record visibility all behave predictably. This is the org-structure foundation the routing, reporting, and permission playbooks build on.

## Why This Matters

Teams are the backbone of routing ("assign to the AE team"), reporting ("pipeline by team"), and visibility (asset partitioning restricts by team). If users have no team, or the wrong primary team, round-robin breaks, dashboards misattribute, and reps see records they shouldn't. Getting users and teams right early prevents a painful retrofit later.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Super Admin access to Settings > Users & Teams
- Teams require a Sales/Service Hub Pro+ or Enterprise seat context; hierarchical teams require Enterprise

## Critical Concept: Primary vs Additional Teams

A user has **one primary team** (drives default ownership, routing, and reporting rollup) and can belong to **additional teams** (extra visibility). Hierarchical teams (Enterprise) let a manager's team roll up child teams' records. Assign the primary team deliberately — it's what routing and reporting use.

## Plan

1. Audit current users and their team assignments (before state)
2. Design the team structure (mirror the real org: by function/region/segment)
3. Create teams (parent/child if Enterprise)
4. Assign users to primary + additional teams
5. Verify coverage — no user without a team (after state)

## Before State

### Audit Script

```python
import os, requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
H = {"Authorization": f"Bearer {TOKEN}"}

users = requests.get("https://api.hubapi.com/settings/v3/users?limit=100", headers=H).json()
print(f"Total users: {len(users.get('results', []))}")
no_team = [u for u in users.get("results", []) if not u.get("primaryTeamId")]
print(f"Users with NO primary team: {len(no_team)}")
for u in no_team:
    print(f"  - {u.get('email')}")
```

Record: total users, users with no primary team, and the current team list (Settings > Users & Teams > Teams). Users without a team are the immediate gap.

## Execute

### Step 1: Design the team structure

Mirror how the business runs — common shapes: by function (Marketing, SDR, AE, CS), by region (EMEA, AMER), or by segment (SMB, Mid-Market, Enterprise). Keep it as flat as the reporting needs allow; every extra layer is maintenance.

### Step 2: Create teams

Settings > Users & Teams > **Teams** > Create team. On Enterprise, nest child teams under parents so records roll up. Set this up **before** bulk-adding users so you can assign teams during onboarding.

### Step 3: Assign users

For each user set the **primary team** (routing/reporting) and any **additional teams** (extra visibility). Assign owners/queues consistently with `assign-unowned-contacts` and the routing playbooks.

### Step 4: Onboarding default

Adopt a rule: no user is added without a primary team and a permission set (see `permission-sets-roles`). This keeps the structure clean as the team grows.

## After State

**Verification checklist:**

1. Every active user has a primary team (audit script shows 0 with no team).
2. Team structure matches the real org and the reporting you need.
3. Hierarchical rollups work as expected (Enterprise): a manager sees child-team records.
4. Routing/round-robin targets teams correctly (test one enrollment).
5. An onboarding rule (primary team + permission set on add) is documented.

## Key Technical Learnings

- **Primary team is the load-bearing field** — it drives routing, default ownership, and reporting rollup. Additional teams are visibility only.
- **Set up teams before adding users** so assignment happens at onboarding, not as a cleanup later.
- **Hierarchy is Enterprise-only** — don't design rollups you can't enforce on your tier.
- **No user without a team.** A teamless user is invisible to team routing and misattributed in reports.
- **Feeds routing + permissions + partitioning** — this playbook is the prerequisite for `lead-routing-round-robin`, `permission-sets-roles`, and `asset-partitioning`.

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
