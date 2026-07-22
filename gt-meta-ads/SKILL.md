---
name: gt-meta-ads
description: "GT Meta Ads — expert Meta (Facebook and Instagram) Ads strategist for B2B companies, built by Growth Today (growthtoday.co). Use when asking about Meta ads, Facebook ads, Instagram ads, Advantage+, custom audiences, lookalike audiences, creative fatigue, Pixel and Conversions API (CAPI), learning phase, Meta funnel structure, retargeting, Instant Forms, Meta lead gen, ad creative strategy, frequency capping, or B2B paid social on Meta. Triggers on: Meta ads, Facebook ads, Instagram ads, Advantage+, ASC, custom audience, lookalike, creative fatigue, CAPI, Conversions API, Pixel, learning phase, Instant Forms, Meta retargeting, frequency cap, Reels ads. Do NOT use for LinkedIn Ads (use gt-linkedin-ads), Google Ads (use gt-google-ads), or organic social content. More GT skills: growthtoday.co."
version: v1.3.0
# v1.3.0 (2026-07-22): Phase 2 — added the B2B-vs-B2C guardrail reference (what does NOT transfer
# from generic/DTC Meta advice) wired across the orchestrator + sub-skills; named B2B SaaS (HubSpot,
# Dreamdata, Metadata.io). Reinforces B2B-only positioning.
# v1.2.0 (2026-07-21): Phase 1 — tracking hygiene (domain verification, AEM, CAPI Gateway, EMQ,
# standard-vs-custom events), UTM standardization, breakdown reporting; concrete HubSpot property
# mapping (fbclid/email/phone, lifecycle-stage trigger) + Dreamdata path in CRM-attribution;
# audit-checklist upgraded with evidence discipline. All B2B.
# v1.1.0 (2026-07-21): P1 2026 expansion — Opportunity Score, Advantage+ 2026 updates + Predictive
# Budget Allocation, gen-AI Creative Enhancements, Advantage+ Leads, Threads; HubSpot+Salesforce
# CRM-attribution reference (Meta CAPI offline conversions); Conversion Lift incrementality.
# v1.0.1 (2026-07-21): Added CHANGELOG (was missing from repo); canonical footer. No content change.
# v1.0 (2026-06-25): Initial GT Meta Ads skill. Orchestrator + 9 sub-skills covering
# tracking (Pixel/CAPI), funnel structure, audiences, creative, creative fatigue, learning
# phase, Instant Forms lead quality, measurement, and the account audit. Built for B2B.
---

# GT Meta Ads — Orchestrator

Expert B2B Meta Ads strategist (Facebook + Instagram). Meta is not LinkedIn: people are not there to think about work, the targeting is weaker for firmographics, and the algorithm now does most of the audience work. That flips the job. On Meta in 2026, **creative is the primary lever you control** and **tracking is the foundation everything else stands on**. Media-buying mechanics matter far less than they did three years ago.

Two rules anchor this skill:
1. **Fix tracking first.** Pixel + Conversions API (CAPI), correct conversion event, clean attribution. iOS privacy changes mean browser-only tracking under-reports badly; without CAPI the algorithm optimises on partial data.
2. **Treat creative as the strategy, not a design task.** The algorithm finds the right people only if the creative gives it something worth showing them. Volume, hooks, and fatigue management are where B2B Meta is won or lost.

B2B caveat throughout: Meta CPLs look cheap next to LinkedIn, but lead quality is the risk. Optimise and measure to pipeline, not raw CPL, or you will celebrate leads sales ignores.

## Sub-Skill Routing

| Topic | Load |
|-------|------|
| Pixel, Conversions API, conversion events, attribution windows, iOS | `resources/sub-skills/tracking.md` |
| Full-funnel structure, CBO/ABO, budget split, prospecting vs retargeting | `resources/sub-skills/campaign-setup.md` |
| Custom audiences, lookalikes, Advantage+ audience, exclusions, overlap | `resources/sub-skills/audiences.md` |
| Creative strategy, formats, hooks, UGC, video specs, creative library | `resources/sub-skills/creative.md` |
| Creative fatigue detection, refresh cadence, frequency thresholds | `resources/sub-skills/creative-fatigue.md` |
| Learning phase, 50-events rule, budget floors, exiting learning | `resources/sub-skills/learning-phase.md` |
| Instant Forms, lead quality, form length, CRM sync, lead nurture | `resources/sub-skills/lead-forms.md` |
| Measurement, CAPI-backed reporting, pipeline attribution, KPIs by stage | `resources/sub-skills/measurement.md` |
| Full account audit, wasted-spend review, prioritised fix list | `resources/sub-skills/audit.md` |

## Reference Files

| Resource | When to load |
|----------|-------------|
| `resources/references/benchmarks.md` | B2B CPM/CPL/frequency/creative-volume benchmarks |
| `resources/references/audit-checklist.md` | The full account audit checklist |
| `resources/references/creative-formats.md` | Format specs, funnel-stage format matching |
| `resources/references/2026-ai-updates.md` | Opportunity Score, Advantage+ 2026, gen-AI creative, Advantage+ Leads, Threads |
| `resources/references/crm-attribution.md` | HubSpot + Salesforce offline-conversion loop (Meta CAPI, fbclid matching, models) |
| `resources/references/tracking-hygiene.md` | Signal-quality controls, UTM standardization, breakdown reporting (B2B) |
| `resources/references/b2b-vs-b2c-guardrail.md` | What does NOT transfer from generic (DTC) Meta advice — read first |

## Routing Rules

- General question ("help me with Meta ads") → ask about budget, ICP, offer, current account state → route to audit first (find the leaks), then tracking, then campaign-setup
- "My Meta ads stopped working" / "CPL spiked" → creative-fatigue first (most common cause), then tracking, then audiences
- New account → tracking (Pixel + CAPI) → campaign-setup → creative → learning-phase
- B2B lead gen specifically → lead-forms + tracking + measurement (lead quality is the whole game)
- Multiple topics → load primary sub-skill first, reference others as needed

## Key Benchmarks

Meta benchmarks swing hard by vertical, offer, and audience temperature. Use as gut-checks, never targets. Focus on cost-per-result trend over time, not absolute numbers.

| Metric | B2B Benchmark (2026) |
|--------|---------------------|
| CPM (cold) | $20-60 for B2B (vs $8-20 B2C) |
| CPL (Instant Form / lower-friction) | $15-80 typical; landing-page leads cost more but often qualify better |
| Cost per SQL / pipeline | The number that matters; only visible with CRM-synced offline data |
| Creative refresh trigger | CTR drops ~20%+ from baseline, or frequency > 3-4 in 7 days |
| Creative volume (at $300+/day) | 3-5 new variants per week to outrun fatigue |
| Learning phase | 50 optimisation events per ad set per week to exit |
| Frequency (cold prospecting) | 1.5-2.5 per 7 days healthy; 3-4 is the warning zone |
| Ads per ad set | 4-5 (enough for the algorithm to optimise, not so many budget spreads thin) |
| Video completion (awareness) | 25%+ is strong for B2B |
| Attribution window | 7-day click / 1-day view default; consider 28-day click for long B2B cycles |

**Critical principle — creative is the lever, tracking is the floor.** In 2026 Meta's Advantage+ and AI delivery (Andromeda/GEM) handle most audience and placement work. That means manual audience micro-segmentation yields less than it used to, and creative quality plus clean conversion signal drive results. Note one consequence: with sequenced delivery, ad-level CPA is no longer a reliable read of creative quality — spend allocation across creatives is the better signal of what the algorithm trusts.

**B2B reality — cheap leads are not the goal.** Meta will happily produce a flood of low-cost Instant Form leads. Without CRM feedback and pipeline measurement you optimise toward volume sales cannot use. Sync leads to the CRM, pass back quality, and judge Meta on pipeline. **Before applying any generic Meta tactic or benchmark, run it through `resources/references/b2b-vs-b2c-guardrail.md` — most web/Meta advice is DTC and does not transfer.**

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
