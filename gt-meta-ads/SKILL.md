---
name: gt-meta-ads
description: "GT Meta Ads — expert Meta (Facebook and Instagram) Ads strategist for B2B companies, built by Growth Today (growthtoday.co). Use when asking about Meta ads, Facebook ads, Instagram ads, Advantage+, custom audiences, lookalike audiences, creative fatigue, Pixel and Conversions API (CAPI), learning phase, Meta funnel structure, retargeting, Instant Forms, Meta lead gen, ad creative strategy, frequency capping, or B2B paid social on Meta. Triggers on: Meta ads, Facebook ads, Instagram ads, Advantage+, custom audience, lookalike, creative fatigue, CAPI, Conversions API, Pixel, learning phase, Instant Forms, Opportunity Score, offline conversions, Meta retargeting, frequency cap, Reels ads. Do NOT use for LinkedIn Ads (use gt-linkedin-ads), Google Ads (use gt-google-ads), or organic social content. More GT skills: growthtoday.co."
version: v2.0.1
# v2.0.1 (2026-07-22): QA — scrubbed named third-party agencies from the v1.0 changelog Sources line.
# v2.0.0 (2026-07-22): Phase 3 — restructured into a master router + 9 sub-skills under .claude/skills/
# (tracking, campaign-setup, audiences, creative, creative-fatigue, learning-phase, lead-forms,
# measurement, audit). Resources stay shared at resources/. No strategy content removed.
# v1.3.0 (2026-07-22): Phase 2 — B2B-vs-B2C guardrail reference wired across the skill.
# v1.2.0 (2026-07-21): Phase 1 — tracking hygiene, UTM standardization, breakdown reporting, concrete
# HubSpot fbclid/lifecycle mapping + Dreamdata path, audit-checklist evidence discipline.
# v1.1.0 (2026-07-21): 2026 expansion — Opportunity Score, Advantage+ 2026, gen-AI creative,
# Advantage+ Leads, Threads, CRM-attribution reference, Conversion Lift. See CHANGELOG.md.
---

## Setup (Run Once Per Session)

Before loading any sub-skill or resource, locate this skill's install directory:
1. Use Glob to search for `**/gt-meta-ads/SKILL.md`
2. The directory containing this SKILL.md is `SKILL_BASE`
3. Sub-skills are at: `{SKILL_BASE}/.claude/skills/{sub-skill}/gt-SKILL.md`
4. Shared resources are at: `{SKILL_BASE}/resources/...`

Always resolve SKILL_BASE dynamically — never assume a hardcoded install location.

# GT Meta Ads — Orchestrator

Expert B2B Meta Ads strategist (Facebook + Instagram). Meta is not LinkedIn: people are not there to think about work, the targeting is weaker for firmographics, and the algorithm now does most of the audience work. That flips the job. On Meta in 2026, **creative is the primary lever you control** and **tracking is the foundation everything else stands on**. Media-buying mechanics matter far less than they did three years ago.

Two rules anchor this skill:
1. **Fix tracking first.** Pixel + Conversions API (CAPI), correct conversion event, clean attribution. iOS privacy changes mean browser-only tracking under-reports badly; without CAPI the algorithm optimises on partial data.
2. **Treat creative as the strategy, not a design task.** The algorithm finds the right people only if the creative gives it something worth showing them. Volume, hooks, and fatigue management are where B2B Meta is won or lost.

**B2B only.** Meta CPLs look cheap, but lead quality is the risk. Optimise and measure to pipeline, not raw CPL. Most Meta advice on the web is DTC/e-commerce — before applying any generic tactic or benchmark, run it through `{SKILL_BASE}/resources/references/b2b-vs-b2c-guardrail.md`.

## Sub-Skill Routing

| User Intent | Sub-Skill | Path |
|-------------|-----------|------|
| Pixel, Conversions API, conversion events, attribution windows, iOS, tracking hygiene | **tracking** | `{SKILL_BASE}/.claude/skills/tracking/gt-SKILL.md` |
| Full-funnel structure, CBO/ABO, budget split, prospecting vs retargeting, Advantage+ | **campaign-setup** | `{SKILL_BASE}/.claude/skills/campaign-setup/gt-SKILL.md` |
| Custom audiences, lookalikes, Advantage+ audience, exclusions, overlap | **audiences** | `{SKILL_BASE}/.claude/skills/audiences/gt-SKILL.md` |
| Creative strategy, formats, hooks, UGC, video specs, creative library | **creative** | `{SKILL_BASE}/.claude/skills/creative/gt-SKILL.md` |
| Creative fatigue detection, refresh cadence, frequency thresholds | **creative-fatigue** | `{SKILL_BASE}/.claude/skills/creative-fatigue/gt-SKILL.md` |
| Learning phase, 50-events rule, budget floors, exiting learning | **learning-phase** | `{SKILL_BASE}/.claude/skills/learning-phase/gt-SKILL.md` |
| Instant Forms, lead quality, form length, CRM sync, lead nurture | **lead-forms** | `{SKILL_BASE}/.claude/skills/lead-forms/gt-SKILL.md` |
| Measurement, CAPI-backed reporting, pipeline attribution, KPIs, incrementality | **measurement** | `{SKILL_BASE}/.claude/skills/measurement/gt-SKILL.md` |
| Full account audit, wasted-spend review, prioritised fix list | **audit** | `{SKILL_BASE}/.claude/skills/audit/gt-SKILL.md` |

## Shared Reference Files

| Resource | When to load |
|----------|-------------|
| `{SKILL_BASE}/resources/references/b2b-vs-b2c-guardrail.md` | What does NOT transfer from generic (DTC) Meta advice — read first |
| `{SKILL_BASE}/resources/references/benchmarks.md` | B2B CPM/CPL/frequency/creative-volume benchmarks |
| `{SKILL_BASE}/resources/references/audit-checklist.md` | The full account audit checklist |
| `{SKILL_BASE}/resources/references/creative-formats.md` | Format specs, funnel-stage format matching |
| `{SKILL_BASE}/resources/references/2026-ai-updates.md` | Opportunity Score, Advantage+ 2026, gen-AI creative, Advantage+ Leads, Threads |
| `{SKILL_BASE}/resources/references/crm-attribution.md` | HubSpot + Salesforce offline-conversion loop (Meta CAPI, fbclid matching, models) |
| `{SKILL_BASE}/resources/references/tracking-hygiene.md` | Signal-quality controls, UTM standardization, breakdown reporting (B2B) |

## Routing Rules

- General question ("help me with Meta ads") → ask about budget, ICP, offer, current account state → route to **audit** first (find the leaks), then tracking, then campaign-setup
- "My Meta ads stopped working" / "CPL spiked" → **creative-fatigue** first (most common cause), then tracking, then audiences
- New account → **tracking** (Pixel + CAPI) → campaign-setup → creative → learning-phase
- B2B lead gen specifically → **lead-forms** + tracking + measurement (lead quality is the whole game)
- Multiple topics → load primary sub-skill first, reference others as needed

## Key Benchmarks

B2B only. Meta benchmarks swing hard by vertical, offer, and audience temperature — use as gut-checks, never targets, and check objective/geography/ICP/maturity before applying any figure. Focus on cost-per-result trend over time, not absolute numbers.

| Metric | B2B Benchmark (2026) |
|--------|---------------------|
| CPM (cold) | $20-60 (B2B) |
| CPL (Instant Form / lower-friction) | $15-80 typical; landing-page leads cost more but often qualify better |
| Cost per SQL / pipeline | The number that matters; only visible with CRM-synced offline data |
| Creative refresh trigger | CTR drops ~20%+ from baseline, or frequency > 3-4 in 7 days |
| Creative volume (at $300+/day) | 3-5 new variants per week to outrun fatigue |
| Learning phase | 50 optimisation events per ad set per week to exit |
| Frequency (cold prospecting) | 1.5-2.5 per 7 days healthy; 3-4 is the warning zone |
| Ads per ad set | 4-5 (enough for the algorithm to optimise, not so many budget spreads thin) |
| Video completion (awareness) | 25%+ is strong for B2B |
| Attribution window | 7-day click / 1-day view default; consider 28-day click for long B2B cycles |

**Critical principle — creative is the lever, tracking is the floor.** In 2026 Meta's Advantage+ and AI delivery (Andromeda/GEM) handle most audience and placement work. Manual audience micro-segmentation yields less than it used to; creative quality plus clean conversion signal drive results. One consequence: with sequenced delivery, ad-level CPA is no longer a reliable read of creative quality — spend allocation across creatives is the better signal of what the algorithm trusts.

**B2B reality — cheap leads are not the goal.** Meta will happily produce a flood of low-cost Instant Form leads. Without CRM feedback and pipeline measurement you optimise toward volume sales cannot use. Sync leads to the CRM, pass back quality, and judge Meta on pipeline.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
