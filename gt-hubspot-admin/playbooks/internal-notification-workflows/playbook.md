---
name: internal-notification-workflows
description: "Build internal-notification workflows that alert the right person at the right moment — new assignment, high-value deal, stuck record, SLA breach — without creating notification fatigue."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation
---

# Internal Notification Workflows

Set up the internal alerts that make automation actionable: notify an owner when they're assigned a lead, flag leadership on a high-value deal, warn when a record is stuck or an SLA is about to breach — while keeping alerts few enough that people still read them.

## Why This Matters

Automation that changes data silently is only half useful — someone has to *act*. Well-placed notifications turn "the system did something" into "the rep followed up in 5 minutes." But too many alerts train people to ignore all of them. The skill is notifying on the few moments that truly need a human, through the right channel.

## Prerequisites

- Access to Automation > Workflows
- Owners/teams set up (`users-teams-setup`) so notifications target the right person
- Optional: a connected Slack/Teams integration for channel notifications

## Critical Concept: Notify on Action-Required Moments Only

Every notification should map to a decision or action. "A contact was created" is not action-required; "a $50k deal has been stuck 14 days" is. Route notifications by urgency: **task** (do later), **in-app/email** (soon), **Slack/Teams** (now). Over-notifying is the fastest way to make all alerts worthless.

## Plan

1. Inventory the action-required moments worth an alert
2. Choose the channel per moment (task / email / Slack)
3. Build the notification workflows
4. Tune volume so alerts stay meaningful (after state)

## Execute

### Step 1: Pick the moments
High-value, action-required examples:
- New lead assigned → notify owner (task + email) — pairs with routing.
- High-value deal created/won → notify manager/leadership.
- Deal stuck past threshold → notify owner (ties to `deal-rotting-alerts`).
- SLA about to breach (no first response in X hrs) → notify owner + manager.
- Key form submitted (demo request) → notify owner immediately.

### Step 2: Build the workflows
For each: enrollment trigger = the moment; action = **send internal notification** (in-app/email) and/or **create task**, and/or Slack/Teams message if integrated. Include the record link + why it's flagged.

### Step 3: Route by urgency
Immediate revenue moments → Slack/real-time; follow-ups → task; FYIs → email digest. Don't send everything real-time.

## After State

**Verification checklist:**

1. Each notification maps to a clear action, not just an event.
2. Channels match urgency (task vs email vs Slack).
3. Owners actually receive alerts for their records (test one).
4. Alert volume is sane — spot-check that a rep isn't getting dozens/day.
5. Notifications include the record link + reason.

## Key Technical Learnings

- **Notify on action-required moments only** — event-spam kills all alerts' credibility.
- **Channel = urgency** — Slack for now, task for later, email for FYI.
- **Context in the alert** — link + reason, so the person can act without digging.
- **Pairs with routing, `deal-rotting-alerts`, and SLA dashboards** — notifications are how those become action.
- **Fewer, better alerts** beat comprehensive noise.

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
