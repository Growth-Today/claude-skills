---
name: lead-routing-round-robin
description: "Automatically route and assign leads to the right rep. Builds round-robin and team-based assignment via workflows, with fallback owners and SLA notifications, so no lead sits unassigned."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation
---

# Lead Routing (Round-Robin)

Assign incoming leads to reps automatically and fairly — round-robin within a team, with rules for territory/segment and a fallback so nothing falls through. Unassigned leads are lost leads; routing closes that gap.

## Why This Matters

A lead with no owner gets no follow-up, no SLA, and no accountability — it just decays. Manual assignment doesn't scale and isn't fair. Round-robin (and criteria-based) routing via workflows ensures every qualifying lead lands with a rep instantly, distributes load evenly, and creates a task/notification so the rep acts fast.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Automation > Workflows
- Teams set up (`users-teams-setup`) — routing targets teams/queues
- Round-robin rotation of owners in workflows requires a Sales/Service Hub Pro+ context

## Critical Concept: Route on Qualification, Not Creation

Route leads when they *qualify* (e.g. become an MQL/SQL — see `lead-status-taxonomy`), not the instant any contact is created — otherwise you assign junk. Combine an enrollment trigger (qualified) with a rotation action (round-robin) and always define a **fallback owner** for records that don't match any rule.

## Plan

1. Audit currently unassigned / unevenly assigned leads (before state)
2. Define routing rules: which leads, to which team, by what criteria
3. Build the routing workflow (round-robin + criteria + fallback)
4. Add SLA task/notification on assignment
5. Verify even distribution and no unassigned qualified leads (after state)

## Before State

```python
import os, requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
H = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# Qualified leads with no owner (adjust the lifecycle/lead-status filter to your model)
payload = {
    "filterGroups": [{"filters": [
        {"propertyName": "hubspot_owner_id", "operator": "NOT_HAS_PROPERTY"},
        {"propertyName": "lifecyclestage", "operator": "EQ", "value": "marketingqualifiedlead"}
    ]}],
    "limit": 0
}
r = requests.post("https://api.hubapi.com/crm/v3/objects/contacts/search", headers=H, json=payload)
print(f"Unassigned MQLs: {r.json().get('total')}")
```

Record: count of qualified-but-unassigned leads, and current owner distribution (are some reps overloaded?). This is the case for routing.

## Execute

### Step 1: Define routing rules
Decide the segments and their target teams (e.g. by region, company size, or product interest), and the fallback owner for anything unmatched.

### Step 2: Build the routing workflow
Automation > Workflows > Contact-based:
1. Enrollment trigger: lead **qualifies** (e.g. lifecycle = MQL, or lead status = "Ready for sales").
2. Branch on criteria (region/segment) if needed.
3. Action: **Rotate record to owner** (round-robin) across the target team's users.
4. Fallback branch: if no criteria match, assign the fallback owner.

### Step 3: Add SLA task + notification
After assignment: create a task for the new owner ("New lead — follow up within X hours") and send an internal notification. This turns assignment into action.

### Step 4: Handle edge cases
Exclude existing-customer contacts and already-owned records from enrollment so you don't reassign live relationships.

## After State

**Verification checklist:**

1. Re-run the audit — qualified-but-unassigned leads trend to ~0.
2. Owner distribution is even across the target team (round-robin working).
3. A test lead that qualifies gets assigned + a task/notification fires. (Create, confirm, clean up.)
4. Unmatched leads land with the fallback owner, not nowhere.
5. Existing customers/owned records are not reassigned.

## Key Technical Learnings

- **Route on qualification, not creation** — otherwise you distribute junk and annoy reps.
- **Always define a fallback owner** — the #1 routing gap is records that match no rule.
- **Assignment without an SLA task is half a solution** — pair rotation with a task/notification.
- **Exclude owned + customer records** from enrollment to avoid hijacking live relationships.
- **Depends on `users-teams-setup` and `lead-status-taxonomy`** — teams are the routing target, lead status is the trigger.

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
