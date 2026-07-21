---
name: reengagement-reenrollment
description: "Design re-engagement and workflow re-enrollment correctly. Builds a dormant-contact re-engagement track and sets re-enrollment rules so workflows re-fire when they should — without infinite loops or spam."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation
---

# Re-engagement & Re-enrollment

Two related things: a **re-engagement** track that tries to wake dormant contacts before you suppress them, and correct **re-enrollment** settings so workflows re-fire for contacts who re-qualify — without creating loops or over-sending.

## Why This Matters

Contacts go quiet; some are recoverable, some are dead weight. A re-engagement track gives dormant contacts a last, well-timed nudge before suppression (protecting deliverability and the marketable-contact bill). Separately, re-enrollment is one of the most misunderstood workflow settings — off when it should be on (contacts who re-qualify never get re-processed) or on when it shouldn't be (contacts loop and get spammed).

## Prerequisites

- Access to Automation > Workflows and lists
- `engagement-suppression-workflow` in place (re-engagement feeds the sunset flow)
- Understanding of your engagement signals (opens/clicks/visits/replies)

## Critical Concept: Re-enrollment Re-fires on the Trigger

A workflow only re-enrolls a contact if **re-enrollment is enabled** AND the contact **re-meets the enrollment trigger** (having previously left it). Enable it for state-based automations that should repeat (e.g. "became unengaged again"); keep it off for one-time actions (e.g. "send welcome email once"). Guard against loops: never let a workflow's own action re-trigger its enrollment.

## Plan

1. Define dormant vs active (the re-engagement threshold)
2. Build the re-engagement track (last-nudge sequence) feeding the sunset flow
3. Audit existing workflows' re-enrollment settings; fix wrong ones
4. Verify no loops, no spam (after state)

## Execute

### Step 1: Re-engagement track
Build a workflow: enroll contacts newly-dormant (e.g. no engagement 90 days but not yet 180). Send a short, distinct re-engagement sequence (2-3 emails, different angle/subject). Branch: re-engaged (opened/clicked) → return to normal; still silent → hand to `engagement-suppression-workflow` for sunset/suppression.

### Step 2: Fix re-enrollment settings
Review key workflows:
- **Enable** re-enrollment on repeatable state automations (unengaged, missing field, stage-based) so contacts get re-processed when they re-qualify.
- **Disable** on one-time actions (welcome, first-touch).
- **Loop check:** ensure a workflow's action can't re-satisfy its own trigger (e.g. don't set a property that re-enrolls the same workflow).

## After State

**Verification checklist:**

1. Dormant threshold defined; re-engagement track live and feeding the sunset flow.
2. Re-engaged contacts return to normal; still-silent ones are routed to suppression.
3. Repeatable workflows have re-enrollment ON; one-time ones have it OFF.
4. No workflow loops (an action re-triggering its own enrollment).
5. Send volume per contact is sane (no re-engagement spam).

## Key Technical Learnings

- **Re-enrollment = re-fire on re-qualifying** — off by default; enable deliberately for state-based repeats.
- **Loops come from self-triggering actions** — never let a workflow's write re-satisfy its own enrollment.
- **Re-engage before you suppress** — a last nudge recovers some contacts and cleans the rest.
- **One-time vs repeatable** is the core distinction for the re-enrollment toggle.
- **Feeds `engagement-suppression-workflow` and `contact-data-decay-review`.**

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
