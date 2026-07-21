---
name: attribution-reporting-setup
description: "Set up attribution reporting to show which sources, channels, and touches drive deals and revenue. Covers attribution report types, models, and the tracking prerequisites so credit is assigned honestly."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: reporting
---

# Attribution Reporting Setup

Show marketing's impact on pipeline and revenue with attribution reports — which sources, campaigns, and interactions influenced deals. Extends the reporting group beyond activity metrics to "what actually drove revenue."

## Why This Matters

Without attribution, marketing reports on activity (clicks, MQLs) and sales reports on outcomes (deals) — and nobody connects them. Attribution reporting links touches to deals/revenue so you can defend and optimize spend. It's also easy to get wrong: the model you pick (first-touch, last-touch, multi-touch) tells very different stories, so the setup must be deliberate.

## Prerequisites

- Reports > Create custom report > Attribution (Marketing Hub Professional+ for deal-create attribution; **revenue** attribution needs Marketing Hub Enterprise)
- Tracking prerequisites: tracking code on the site, campaigns tagged, and consistent source data
- Clean lifecycle + deal data (`fix-lifecycle-stages`, `deal-pipeline-architecture`)

## Critical Concept: The Model Determines the Story

- **First-touch:** credits the source that first found the contact (good for demand-gen/awareness).
- **Last-touch:** credits the final interaction before conversion (good for closing channels).
- **Multi-touch (linear/W-shaped/etc.):** distributes credit across the journey (most balanced, higher tiers).

Pick the model(s) that match the question. Reporting first-touch as if it were revenue-driving is a classic misuse.

## Plan

1. Confirm tracking + campaign tagging are in place
2. Decide the questions + the model(s) for each
3. Build deal-create (and revenue, if Enterprise) attribution reports
4. Validate credit assignment; add to the leadership dashboard (after state)

## Execute

### Step 1: Prerequisites check
Confirm the tracking code is live, campaigns/UTMs are tagged consistently, and original/latest source data is populated. Attribution is only as good as this tracking.

### Step 2: Build the reports
Reports > Create custom report > **Attribution**. Choose the subject (deal-create or revenue), the attribution model, and the breakdown (by source, campaign, channel, content). Build a first-touch AND a multi-touch view where the tier allows — they answer different questions.

### Step 3: Validate + socialize
Sanity-check that credited sources match reality (spot-check a known deal's journey). Add the attribution report to the leadership/marketing dashboard (`revops-core-dashboards`) with the model clearly labeled.

## After State

**Verification checklist:**

1. Tracking + campaign tagging are confirmed (attribution has real inputs).
2. The attribution model(s) match the questions and are labeled on the report.
3. Deal-create (and revenue, if Enterprise) attribution reports exist.
4. Credit assignment passes a spot-check against a known deal journey.
5. Reports are on a dashboard, with the model noted so no one misreads them.

## Key Technical Learnings

- **The model is the message** — first vs last vs multi-touch tell different stories; choose per question.
- **Attribution needs tracking** — no tracking code / untagged campaigns = meaningless credit.
- **Tier-gated** — revenue attribution is Marketing Hub Enterprise; plan around it.
- **Always label the model** on the report so stakeholders don't misinterpret.
- **Feeds `revops-core-dashboards`** and pairs with `custom-report-builder-guide`.
