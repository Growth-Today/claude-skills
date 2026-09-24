---
name: gt-buying-signal-sourcer
description: "GT Signal Sourcer — expert signal-based selling for B2B outbound. Use when asking about buying signals, intent data, signal scoring, signal-based selling, website visitor tracking, job change signals, hiring signals, funding signals, competitor signals, tech stack changes, content engagement signals, multi-signal stacking, RB2B setup, Trigify setup, Common Room, Bombora, Koala, Warmly, 6sense, signal-to-action playbooks, or building signal-driven outbound campaigns. Triggers on: buying signals, intent data, signal scoring, signal-based, website visitors, job change, hiring signal, funding signal, competitor signal, tech change, content engagement, RB2B, Trigify, Common Room, Bombora, intent signals, warm outbound, signal stacking, visitor tracking, signal tools, GTM plays. Do NOT use for general list building (use gt-list-builder) or email writing (use gt-copywriting)."
version: v2
---

# GT Signal Sourcer — Orchestrator

Expert in signal-based selling achieving 35-40% reply rates through multi-signal stacking.

## Folder Structure

```
resources/
├── core/                        ← Core reference docs (load first)
│   ├── buying-signals.md        ← 6 core signals, benchmarks, Clay workflows
│   ├── signal-scoring.md        ← Full scoring framework, weights, SLAs, plays
│   └── signal-taxonomy.md       ← 137 buying triggers taxonomy
├── detection/                   ← Tools and detection logic
│   ├── signal-detection-tools.md ← 30-trigger quick ref, Clay credit costs, freshness rules
│   └── tool-setup-guides.md     ← RB2B, Trigify, Common Room, Bombora setup
├── plays/                       ← Execution playbooks
│   ├── gtm-plays.md             ← 11 executable GTM plays
│   └── job-change-tracking.md   ← Clay job change tracking (historical vs future)
└── signals/                     ← Per-signal deep dives
    ├── job-changes.md
    ├── funding.md
    ├── hiring.md
    ├── website-visitors.md
    ├── company-events.md
    ├── tech-changes.md
    ├── competitor-signals.md
    ├── content-engagement.md
    └── multi-signal.md
```

## Signal Routing

| User asks about... | Load |
|---|---|
| Job changes, new roles, champion tracking, vendor amnesty period, days 14-45 | `resources/signals/job-changes.md` |
| Funding rounds, Series A/B/C, new budget, post-raise outreach | `resources/signals/funding.md` |
| Hiring signals, job postings, missing roles, leaving employees, skills targeting | `resources/signals/hiring.md` |
| Website visitors, RB2B, pixel tracking, IP identification, visitor alerts | `resources/signals/website-visitors.md` |
| Company events, M&A, expansion, IPO, product launches, leadership changes | `resources/signals/company-events.md` |
| Tech stack changes, vendor switches, new tool adoption, BuiltWith | `resources/signals/tech-changes.md` |
| Competitor engagement, bad reviews, LinkedIn scraping, battle cards | `resources/signals/competitor-signals.md` |
| Content engagement, post likes/comments, webinar attendance, Trigify | `resources/signals/content-engagement.md` |
| Signal stacking, scoring framework, action thresholds, multi-signal | `resources/signals/multi-signal.md` |
| Tool setup, comparison, pricing | `resources/detection/tool-setup-guides.md` |
| 30-trigger list, Clay credits, signal freshness, detection logic | `resources/detection/signal-detection-tools.md` |
| GTM plays, outreach playbooks, execution templates | `resources/plays/gtm-plays.md` |
| Job change tracking in Clay, historical vs future monitoring | `resources/plays/job-change-tracking.md` |

## Core Reference Files

| Resource | When to load |
|----------|-------------|
| `resources/core/buying-signals.md` | 6 core buying signals, benchmarks |
| `resources/core/signal-scoring.md` | Scoring framework, weights, thresholds, SLAs |
| `resources/core/signal-taxonomy.md` | 137 buying triggers taxonomy |
| `resources/detection/signal-detection-tools.md` | 30-trigger quick ref, Clay credit costs, reliability tiers |
| `resources/detection/tool-setup-guides.md` | RB2B, Trigify, Common Room, Bombora setup |
| `resources/plays/gtm-plays.md` | 11 executable GTM plays |
| `resources/plays/job-change-tracking.md` | Job change tracking in Clay |

## Key Benchmarks

| Metric | Value |
|--------|-------|
| Cold outreach reply rate | 6-8% |
| Single signal reply rate | 18-22% |
| Multi-signal (3+) reply rate | 35-40% |
| Job change response lift | 3x vs cold |
| Job change peak window | Days 14-45 |
| Website visitor reply rate | 25-30% |
| Signal-based contract value | 3-4x baseline |

## Signal Scoring Quick Reference

| Score | Heat Level | Action | SLA |
|-------|-----------|--------|-----|
| 150+ | Red Hot | Immediate manual outreach by AE | < 1 hour |
| 100-149 | Hot | SDR personalized sequence | < 24 hours |
| 50-99 | Warm | Automated nurture + SDR monitoring | < 72 hours |
| 20-49 | Cool | Marketing nurture campaigns | This week |
| 0-19 | Cold | Monitor for signal changes | Ongoing |

## Response Format

1. Identify which signals are relevant
2. Load the correct signal sub-skill(s) from `resources/signals/`
3. Recommend a scoring framework with specific weights
4. Map signals to actions (who does what, when, on which channel)
5. Recommend tools based on budget, geography, and use case
6. Provide ready-to-use outreach templates tied to each signal
