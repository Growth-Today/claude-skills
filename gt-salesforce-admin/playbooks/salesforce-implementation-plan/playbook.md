---
name: salesforce-implementation-plan
description: "Salesforce Implementation Plan for Salesforce. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: audit-planning
---

# Salesforce Implementation Plan

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Turn a `salesforce-audit` report into a phased, sequenced cleanup plan with effort estimates, dependencies, and automation feasibility.

## Setup
Read the most recent `reports/salesforce-audit-*.md`. If none exists, run `/salesforce-audit` first.

## How to build the plan

1. Parse every dimension graded C or worse.
2. Map each finding to its skill using the lookup in `salesforce-audit` (Skill Prescription section).
3. Sequence by dependency and impact, not by audit order:
   - **Phase 1 (week 1) — Stop the bleeding.** Deliverability and ownership: `/suppress-hard-bounced`, `/suppress-opted-out`, `/reassign-inactive-owners`, `/delete-no-email-leads-contacts`.
   - **Phase 2 (weeks 2-3) — Fix the data.** `/enrich-account-name`, `/enrich-industry`, `/fix-lead-status-and-stages`, `/standardize-geo-values`, `/merge-duplicate-accounts`, `/assign-unowned-records`.
   - **Phase 3 (weeks 4-5) — Targeting.** `/create-icp-tiers`, `/build-lead-scoring`, `/build-list-views-and-reports`.
   - **Phase 4 (week 6) — Prevention.** `/new-record-hygiene-flow`, `/bounce-monitoring-flow`, `/engagement-suppression-flow`, `/lead-lifecycle-flow`, plus the Setup-side guardrails: Validation Rules, Duplicate Rules, Matching Rules.
   - **Ongoing.** `/weekly-cleanup-routine`, `/quarterly-org-cleanup`.

## Dependencies to respect
- Reassign owners BEFORE building scoring or routing (scores route to active reps).
- Standardize geo and enrich industry BEFORE creating ICP tiers (tiers read those fields).
- Configure Duplicate/Matching Rules BEFORE bulk merge, so the merge does not recreate dupes.
- Set Validation Rules LAST in each phase, so backfills are not blocked by the rules you are about to add.

## Output
Save `reports/salesforce-implementation-plan-{YYYY-MM-DD}.md`: a phase-by-phase table with skill, finding, record count, effort estimate, automation level (fully scriptable / hybrid / Setup-only), and dependency notes. End with a one-line "start here" recommendation.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
