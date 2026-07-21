---
name: workflow-naming-governance
description: "Stop workflow chaos before it starts. Establishes naming conventions, folders, ownership, and documentation for workflows so automations don't conflict, duplicate, or run silently unmonitored."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation
---

# Workflow Naming & Governance

Bring order to automation: a naming convention, folder structure, owner per workflow, and light documentation so workflows don't multiply, conflict, or run unnoticed. This is the "build discipline" counterpart to `cleanup-workflows` (which removes the mess).

## Why This Matters

Workflows are among the most powerful — and most easily abused — parts of HubSpot. As teams scale, they get duplicated, half-edited, and left active with no owner or documentation, producing conflicting automation and surprises ("why did this contact get three emails?"). A naming + governance standard makes the automation layer legible and safe to change.

## Prerequisites

- Access to Automation > Workflows
- Ideally `cleanup-workflows` run first to remove dead/test workflows before standardizing what remains

## Critical Concept: A Workflow Needs a Name, a Home, and an Owner

Every workflow should be self-describing from its name, live in a logical folder, and have a named owner responsible for it. Undocumented, unowned workflows are how conflicting automation and silent failures happen.

## Plan

1. Inventory active workflows and note naming/folder/owner gaps (before state)
2. Adopt a naming convention + folder structure
3. Rename and refile existing workflows; assign owners
4. Document purpose + owner; set a review cadence
5. Verify the layer is legible (after state)

## Execute

### Step 1: Naming convention
Adopt a prefix-based scheme so purpose is obvious at a glance, e.g.:
`[TEAM] TYPE: Description` → `[SALES] ROUTING: MQL round-robin`, `[OPS] HYGIENE: Set default lifecycle stage`, `[MKTG] NURTURE: Trial day-3 email`.
Common TYPE tags: ROUTING, HYGIENE, NURTURE, NOTIFY, LIFECYCLE, SUPPRESS.

### Step 2: Folder structure
Create folders by team or function (Sales, Marketing, Ops, Lifecycle) and file every workflow into one. No workflow in the root.

### Step 3: Assign owners + document
For each active workflow, set a named owner and a one-line purpose (in the workflow description field). Owners are accountable for changes and monitoring.

### Step 4: Review cadence + change rule
Adopt a rule: new workflows follow the naming convention, go in a folder, and have an owner + description before activation. Review active workflows in `quarterly-database-cleanup` for conflicts and staleness.

## After State

**Verification checklist:**

1. Every active workflow follows the naming convention.
2. No workflow sits in the root — all are foldered by team/function.
3. Every active workflow has a named owner + a one-line purpose.
4. A change rule (name + folder + owner + description before activation) is documented.
5. Workflow review is folded into the quarterly routine.

## Key Technical Learnings

- **Self-describing names prevent conflicts.** If you can't tell what a workflow does from its name, that's the bug.
- **Ownership is accountability.** An unowned workflow is one nobody monitors and everyone's afraid to touch.
- **Govern at activation.** The cheapest time to enforce the standard is before the workflow goes live.
- **Pairs with `cleanup-workflows`** — clean up once, then this keeps it clean.
- **Legible automation is safe automation** — you can only change what you can understand.

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
