---
name: asset-partitioning
description: "Use asset partitioning to control which teams see and use which assets (lists, workflows, forms, content, reports). Set up team-based access for multi-brand, multi-region, or multi-BU accounts without clutter or cross-contamination."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: governance
---

# Asset Partitioning

Partition marketing/CRM assets by team so each business unit, brand, or region sees and uses only its own lists, workflows, forms, emails, and reports. Keeps large accounts organized and prevents one team from touching another's assets.

## Why This Matters

In a shared portal with multiple brands/regions/BUs, everyone sees everyone's assets by default — hundreds of lists and workflows, easy to edit the wrong one, and no boundary between teams. Asset partitioning assigns assets to teams so each group works in a clean, scoped view, reducing clutter and accidental cross-contamination.

## Prerequisites

- **Enterprise** tier (asset partitioning is an Enterprise feature)
- Teams set up (`users-teams-setup`) — partitioning assigns assets to teams
- Super Admin access

## Critical Concept: Partitioning Is Team-Based Visibility, Not Security

Asset partitioning controls which **team** an asset belongs to and who can see/edit it — it declutters and scopes work. It's not a hard security boundary for record data (that's permissions + `permission-sets-roles`). Assets can be assigned to one or multiple teams; a Super Admin still sees all.

## Plan

1. Confirm teams exist and map to the real BU/brand/region structure
2. Decide which asset types to partition and to which teams
3. Assign existing assets to teams; set defaults for new assets
4. Verify each team sees only its scope (after state)

## Execute

### Step 1: Map assets to teams
Decide the partition model (by brand / region / BU) and which asset types to partition: lists, workflows, forms, emails, landing pages, reports/dashboards.

### Step 2: Assign assets
For each asset type, assign existing assets to the owning team (bulk where possible). New assets: set them to be created under the creator's team so partitioning is maintained going forward.

### Step 3: Combine with permissions
Pair with `permission-sets-roles` so access level (view/edit) and asset scope (which team's assets) work together. Remember Super Admins see everything.

## After State

**Verification checklist:**

1. Teams map to the real BU/brand/region structure.
2. Key asset types are assigned to the correct teams.
3. A member of one team sees only their scoped assets (test with a non-admin).
4. New assets inherit the right team by default.
5. It's understood partitioning is organization/visibility, not record-level security.

## Key Technical Learnings

- **Partitioning = team-scoped visibility of assets**, not a data security control (use permissions for that).
- **Enterprise-only** — don't design around it on lower tiers.
- **Depends on a real team structure** (`users-teams-setup`) — partitioning is only as good as the teams.
- **Set new-asset defaults** or partitioning decays as people create ungrouped assets.
- **Pairs with `permission-sets-roles`** for the full access picture.
