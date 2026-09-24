---
name: scoring-decision-framework
description: Canonical reference for the three-layer GTM scoring framework. Use when the user asks which scoring system to apply, how to prioritize accounts, how company tier and contact tier combine, or what outreach motion to use. Covers ICP Fit Score, ABM Account Prioritization, and Outreach Prioritization Matrix.
---

# GTM Scoring Decision Framework

Three distinct scoring layers. Each answers a different question. Never conflate them.

---

## The Three Layers

### Layer 1 - ICP Fit Score (static)

**Question it answers:** Does this company fit our ideal customer profile?

**Inputs:** Firmographics, technographics, geography, industry, revenue, company size.

**Output:** 0-100 score → A/B/C/D tier.

**Key characteristic:** Static. Does not change based on whether the prospect is actively buying or has engaged with us. Every company is treated as cold.

**Tiers:**
| Tier | Score | Action |
|------|-------|--------|
| A | 90-100 | Perfect fit - prioritize for all motions |
| B | 70-89 | Strong fit - pursue |
| C | 50-69 | Moderate fit - nurture only |
| D | <50 | Poor fit - exclude |

For the full scoring matrix (7 criteria, weights), see `resources/sub-skills/icp-definition.md`.

---

### Layer 2 - ABM Account Prioritization (dynamic)

**Question it answers:** Among our ICP-fit accounts, which ones deserve attention RIGHT NOW based on where they are in the buying journey?

**Inputs:** ICP Fit Score + intent data (first/second/third party) + LinkedIn engagement + stage progression.

**Output:** ABM Tier 1 / 2 / 3 → outreach intensity.

**Key characteristic:** Dynamic. A Tier C ICP fit company showing strong first-party intent can be elevated. A Tier A ICP fit company with zero engagement stays deprioritized until signals appear.

**⚠️ This layer only exists if ABM motion is live** (LinkedIn ads + intent data feed + CRM stage tracking). Without it, skip directly to Layer 3.

**Stage Progression:**
```
Identified → Aware → Interested → Considering → Selecting
```

| ABM Tier | Stage | Outreach |
|----------|-------|----------|
| Tier 1 (1:1) | Interested → Considering | Fully custom, multi-threaded, executive alignment |
| Tier 2 (1:Few) | Aware → Interested | Segment-based, personalized sequences |
| Tier 3 (1:Many) | Identified → Aware | Programmatic, automated |

---

### Layer 3 - Outreach Prioritization Matrix (operational)

**Question it answers:** Given this company's tier and this contact's tier, what is the exact outreach motion?

**Inputs:** Company tier (1/2/3) × Contact tier (1/2/3).

**Output:** Channel mix + personalization depth + effort level.

**Key characteristic:** Operational. Tells the GTM engineer or BDR exactly what to execute.

| Company tier | Contact tier | Outreach motion |
|-------------|-------------|----------------|
| T1 | T1 | Omni-channel · white-glove (email + LinkedIn + ads + direct mail + phone + exec alignment) |
| T1 | T2 | Multi-channel · personalized (email + LinkedIn, custom messaging) |
| T2 | T1 | Multi-channel · solid sequence (email + LinkedIn, strong value prop) |
| T2 | T2 | Email + LinkedIn · segmented (segment-level personalization) |
| T3 | Any | Programmatic · templated (automated sequences, minimal manual effort) |

**⚠️ Omni-channel requires LinkedIn ads budget.** Without it, T1+T1 defaults to multi-channel manual - still strong, but a different motion.

---

## Decision Flow

```
START
  │
  ▼
Do we have ABM motion?
  │
  ├── YES
  │     │
  │     ▼
  │   Layer 1: ICP Fit Score (A/B/C/D)
  │     │
  │     ▼ (exclude D)
  │   Layer 2: ABM Account Prioritization
  │   (ICP score + intent + engagement stage)
  │     │
  │     ▼
  │   Layer 3: Outreach Prioritization Matrix
  │   (Company tier × Contact tier → motion)
  │
  └── NO
        │
        ▼
      Layer 1: ICP Fit Score (A/B/C/D)
        │
        ▼ (exclude D)
      Layer 3: Outreach Prioritization Matrix
      (Layer 2 does not exist without ABM motion)
```

---

## Contact Tier Definition

| Tier | Titles | Role |
|------|--------|------|
| T1 | CEO, CFO, CTO, Founder, VP, Head of | Decision-maker with budget authority |
| T2 | Manager, Senior, Director (mid) | Influencer, internal champion |
| T3 | Associate, Coordinator, Specialist, Analyst | End user, not a decision-maker |

---

## Key Caveat for GTM Engineers

The most common mistake: applying ABM Account Prioritization logic when there is no ABM motion. If there are no LinkedIn ads running, no intent data feed, and no stage tracking in the CRM - Layer 2 is empty. Trying to score accounts by "engagement" without a structured signal source produces noise, not signal.

Build Layer 2 only after:
1. LinkedIn Campaign Manager is live with company list targeting
2. A connector tool (ZenABM or Fibbler) is pushing engagement data to HubSpot
3. ABM Stage properties are configured in CRM
4. At least 300 matched LinkedIn members per campaign audience
