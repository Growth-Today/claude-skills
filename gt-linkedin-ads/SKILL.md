---
name: gt-linkedin-ads
description: "GT LinkedIn Ads — expert LinkedIn Ads strategist for B2B companies, built by Growth Today (growthtoday.co). Use when asking about LinkedIn advertising, LinkedIn campaign setup, LinkedIn ad targeting, LinkedIn bidding strategies, LinkedIn ad formats, LinkedIn retargeting, LinkedIn ABM campaigns, LinkedIn Thought Leader Ads, sequenced TLAs and Story Arcs, LinkedIn funnel architecture, LinkedIn ads measurement/attribution, LinkedIn ads troubleshooting, LinkedIn creative best practices, or any B2B paid social strategy involving LinkedIn. Triggers on: LinkedIn campaign, LinkedIn CPM, LinkedIn CTR, LinkedIn lead gen, B2B ads, demand gen on LinkedIn, sponsored content, thought leader ads, Predictive Audiences, Accelerate, Conversions API, LinkedIn ads not working. Do NOT use for LinkedIn organic content (use gt-linkedin-content) or LinkedIn outbound messaging (use gt-linkedin-outbound). More GT skills: growthtoday.co."
version: v2.2.2
# v2.2.2 (2026-07-22): QA — removed competitor-agency credits + blog links from the knowledge base (Section 10).
# v2.2.1 (2026-07-22): Scrubbed named third-party agencies from two reference Sources lines
# (predictive-audiences, accelerate-ai-campaigns) — official + neutral only. No content change.
# v2.2.0 (2026-07-21): P2 — incrementality & lift testing + view-through conversions (measurement),
# EU Sponsored-Messaging compliance on Conversation/Message Ads, and tightened ABM sub-skill
# boundaries (abm-strategy = planning; ads-outbound-sync = signal-to-sales).
# v2.1.0 (2026-07-21): P1 additions — CRM-attribution reference (HubSpot + Salesforce, offline
# conversions, Campaign Influence, U-shaped model) cross-linked to gt-hubspot-admin/gt-salesforce-admin;
# new audit sub-skill + audit control catalog (triad parity with gt-meta-ads).
# v2.0.1 (2026-07-21): Removed all competitor-agency references + operational tables from the
# ABM guides; ABM benchmarks re-anchored to ZenABM with evidence-discipline framing.
# v2.0.0 (2026-07-21): Restructured into a master router + 9 sub-skills under .claude/skills/
# (audiences, ads-outbound-sync, bidding, campaign-setup, copy, creative, measurement,
# optimization, abm-strategy). Resources stay shared at resources/. No strategy content removed.
# v1.3.0 (2026-07-21): P1 2026 expansion — Predictive Audiences + lookalike sunset + career-signal
# targeting, Accelerate AI campaigns + AI creative, Conversions API + Revenue Attribution Report
# deep dive, 2026 Dreamdata attribution benchmarks.
# v1.2.1 (2026-07-21): Repo reconciled with deployed v1.2 (added ABM reference files);
# footers standardized to canonical GT format.
# v1.2 (2026-06-25): Sequenced TLA / Story Arc strategy, budget-leak checklist, TLA economic-fit rule.
# v1.1 (2026-06-11): Benchmarks refreshed to ZenABM 2026 dataset. See CHANGELOG.md for full detail.
---

## Setup (Run Once Per Session)

Before loading any sub-skill or resource, locate this skill's install directory:
1. Use Glob to search for `**/gt-linkedin-ads/SKILL.md`
2. The directory containing this SKILL.md is `SKILL_BASE`
3. Sub-skills are at: `{SKILL_BASE}/.claude/skills/{sub-skill}/gt-SKILL.md`
4. Shared resources are at: `{SKILL_BASE}/resources/...`

Always resolve SKILL_BASE dynamically — never assume a hardcoded install location.

# GT LinkedIn Ads — Orchestrator

Expert LinkedIn Ads strategist with $25M+ in managed B2B ad spend. Route every request to the most relevant sub-skill(s) below, then pull shared references as needed.

## Sub-Skill Routing

| User Intent | Sub-Skill | Path |
|-------------|-----------|------|
| Targeting, ICP, exclusions, ABM lists, remarketing, Predictive Audiences, career signals | **audiences** | `{SKILL_BASE}/.claude/skills/audiences/gt-SKILL.md` |
| Ad engagement → sales signals, intent detection, BDR alerts, ZenABM/Fibbler sync | **ads-outbound-sync** | `{SKILL_BASE}/.claude/skills/ads-outbound-sync/gt-SKILL.md` |
| Bidding strategies, budget allocation, cost optimization | **bidding** | `{SKILL_BASE}/.claude/skills/bidding/gt-SKILL.md` |
| Campaign structure, funnel architecture, retargeting, Accelerate AI campaigns | **campaign-setup** | `{SKILL_BASE}/.claude/skills/campaign-setup/gt-SKILL.md` |
| Ad copywriting, headlines, CTAs, messaging frameworks | **copy** | `{SKILL_BASE}/.claude/skills/copy/gt-SKILL.md` |
| Ad formats, visual design, Thought Leader Ads, Document Ads, AI creative | **creative** | `{SKILL_BASE}/.claude/skills/creative/gt-SKILL.md` |
| Measurement, attribution, KPIs, Insight Tag, CAPI, Revenue Attribution Report | **measurement** | `{SKILL_BASE}/.claude/skills/measurement/gt-SKILL.md` |
| Troubleshooting, optimization, competitive research | **optimization** | `{SKILL_BASE}/.claude/skills/optimization/gt-SKILL.md` |
| Account audit, health check, wasted-spend review, prioritized fix list | **audit** | `{SKILL_BASE}/.claude/skills/audit/gt-SKILL.md` |
| ABM planning: campaign structure, budget math, ABM formats & benchmarks | **abm-strategy** | `{SKILL_BASE}/.claude/skills/abm-strategy/gt-SKILL.md` |

## Shared Reference Files

| Resource | When to load |
|----------|-------------|
| `{SKILL_BASE}/resources/references/funnel-architecture.md` | Funnel architecture & retargeting |
| `{SKILL_BASE}/resources/references/ad-formats.md` | Ad formats & specs |
| `{SKILL_BASE}/resources/references/targeting-audiences.md` | Targeting & audiences |
| `{SKILL_BASE}/resources/references/bidding-objectives.md` | Bidding & objectives |
| `{SKILL_BASE}/resources/references/creative-strategy.md` | Creative & copywriting |
| `{SKILL_BASE}/resources/references/measurement-attribution.md` | Measurement & attribution (incl. CAPI + RAR deep dive) |
| `{SKILL_BASE}/resources/references/crm-attribution.md` | HubSpot + Salesforce attribution loop (offline conversions, Campaign Influence, models) |
| `{SKILL_BASE}/resources/references/troubleshooting.md` | Troubleshooting |
| `{SKILL_BASE}/resources/references/competitive-research.md` | Competitive research |
| `{SKILL_BASE}/resources/references/audit-checklist.md` | LinkedIn Ads audit control catalog |
| `{SKILL_BASE}/resources/references/predictive-audiences.md` | Predictive Audiences, lookalike sunset, career-signal targeting |
| `{SKILL_BASE}/resources/references/accelerate-ai-campaigns.md` | Accelerate AI campaigns, AI creative, CRM in Campaign Manager |
| `{SKILL_BASE}/resources/references/benchmarks.md` | Key benchmarks |
| `{SKILL_BASE}/resources/linkedin-ads-knowledge-base.md` | Full knowledge base |
| `{SKILL_BASE}/resources/references/abm/linkedin-ads-abm-guide.md` | ABM ad formats, budget math, campaign structure, benchmarks |
| `{SKILL_BASE}/resources/references/abm/ads-outbound-signaling-guide.md` | Ads-to-outbound signaling, intent detection, BDR alert workflows |

## Routing Rules

- General question ("help me with LinkedIn Ads") → ask about budget, ICP, goals, experience level → route to **campaign-setup**
- ABM-specific (budget, account-based campaigns, ads-to-outbound signaling) → **abm-strategy** / **ads-outbound-sync**
- Multiple topics → load primary sub-skill first, reference others as needed

## Key Benchmarks

Blended sponsored-content figures are useful for a quick gut-check, but "good" depends on the ad format. Always benchmark against the specific format, not a single blended number.

| Metric | B2B Benchmark |
|--------|--------------|
| CTR (Sponsored Content, blended) | 0.44-0.65% |
| CPL | $50-200 depending on ICP ($400-800 enterprise, $80-200 SMB) |
| CPC (blended, 2026) | $6-15 (single image median $13.23; TLA median $2.29) |
| Conversion rate (landing page) | 5-15% |

**Third-party cost proof point (useful in client decks):** Metadata ran TLAs at a $4.14 CPC vs $22.54 for brand-awareness image/video campaigns — a different dataset from ZenABM, same direction. LinkedIn carries ~41% of total B2B ad budgets and drives roughly 80% of B2B social leads, which is why the high CPCs still clear when targeting is precise.

### Per-format CTR / CPC (ZenABM 2026, median across 161,256 ads / 211 companies)

| Format | Median CTR | Median CPC | LP clicks per $1K |
|--------|-----------|-----------|-------------------|
| Thought Leader Ads | 2.68% | $2.29 | 327 |
| Event Ads | 0.55% | - | - |
| Document Ads | 0.43% | - | - |
| Single Image Ads | 0.42% | $13.23 | 71 |
| Carousel Ads | 0.32% | $13.30 | - |
| Video Ads | 0.24% | $15.61 | 62 |
| Dynamic/Spotlight | 0.08% | - | - |
| Text Ads | 0.02% | - | - |

**Critical caveat — CTR does not predict pipeline.** Across 211 companies, CTR correlated *negatively* with pipeline (Spearman rho = -0.170). High-CTR formats (TLAs) pull broad engagement including non-buyers; lower-CTR formats often carry stronger intent. Optimise for pipeline and targeting precision, not click volume. Use a mix: TLAs for reach, single image for conversion, text ads for cheap retargeting impressions.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
