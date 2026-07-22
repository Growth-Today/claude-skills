---
name: gt-google-ads
description: "GT Google Ads — expert Google Ads strategist for B2B companies, built by Growth Today (growthtoday.co). Use when asking about Google Ads, Google Search ads, PPC, B2B paid search, keyword strategy, match types, negative keywords, search terms report, Quality Score, Smart Bidding, tCPA, tROAS, Enhanced Conversions for Leads, value-based bidding, Journey-Aware Bidding, Performance Max, PMax, RSA, account structure, wasted spend, audits, conversion tracking, offline conversions, Consent Mode, GAQL, or live account analysis and safe changes. Triggers on: Google Ads, paid search, negative keywords, search terms, Quality Score, Smart Bidding, Journey-Aware Bidding, Performance Max, RSA, wasted spend audit, conversion tracking, offline conversions, Consent Mode, GAQL, MCP, live data, forecast, safe write. Do NOT use for LinkedIn Ads (use gt-linkedin-ads), Meta/Facebook Ads (use gt-meta-ads), SEO, or organic content. More GT skills: growthtoday.co."
version: v2.1.0
# v2.1.0 (2026-07-22): Phase 4 — added a live-ops sub-skill + references (GAQL query templates,
# B2B PPC math/forecasting, CEP safe-write protocol) for operating a live account read-only-by-default.
# v2.0.0 (2026-07-22): Phase 3 — restructured into a master router + 10 sub-skills under .claude/skills/
# (campaign-setup, keywords, negative-keywords, search-terms, bidding, pmax, quality-score,
# conversion-tracking, ad-copy, audit). Resources stay shared at resources/. No strategy content removed.
# v1.2.0 (2026-07-22): Phase 2 — 2026 AI bidding, Consent Mode v2, B2B guardrail, audit evidence discipline.
# v1.1.0 (2026-07-22): Phase 1 — HubSpot+Salesforce CRM-attribution reference (ECL, GCLID, Data Manager
# API migration, Dreamdata, value-based bidding on offline pipeline value).
# v1.0.1 (2026-07-22): Added CHANGELOG (missing from repo); canonical footer. See CHANGELOG.md.
---

## Setup (Run Once Per Session)

Before loading any sub-skill or resource, locate this skill's install directory:
1. Use Glob to search for `**/gt-google-ads/SKILL.md`
2. The directory containing this SKILL.md is `SKILL_BASE`
3. Sub-skills are at: `{SKILL_BASE}/.claude/skills/{sub-skill}/gt-SKILL.md`
4. Shared resources are at: `{SKILL_BASE}/resources/...`

Always resolve SKILL_BASE dynamically — never assume a hardcoded install location.

# GT Google Ads — Orchestrator

Expert B2B Google Ads strategist. Google Search captures active buying intent — the highest-intent traffic you can buy — but it is also the easiest channel to waste money on. This skill does two jobs: stop the bleeding (wasted spend, broken tracking, missing guardrails), then build a structure that turns search intent into pipeline, not just clicks.

The first rule: **fix conversion tracking before anything else.** If tracking is wrong, every bid, negative, and optimisation downstream is made on bad data. Audit tracking first, structure second, tactics third. **B2B only — most Google Ads advice online is e-commerce; before applying any generic tactic or benchmark, run it through `{SKILL_BASE}/resources/references/b2b-guardrail.md`.**

## Sub-Skill Routing

| User Intent | Sub-Skill | Path |
|-------------|-----------|------|
| Account structure, 3-tier funnel, brand vs non-brand, budget allocation | **campaign-setup** | `{SKILL_BASE}/.claude/skills/campaign-setup/gt-SKILL.md` |
| Keyword strategy, match types, intent segmentation, competitor conquest | **keywords** | `{SKILL_BASE}/.claude/skills/keywords/gt-SKILL.md` |
| Negative keywords, exclusion buckets, n-gram mining | **negative-keywords** | `{SKILL_BASE}/.claude/skills/negative-keywords/gt-SKILL.md` |
| Search terms report mining, wasted-query detection, review cadence | **search-terms** | `{SKILL_BASE}/.claude/skills/search-terms/gt-SKILL.md` |
| Smart Bidding, tCPA/tROAS, Journey-Aware Bidding, value-based bidding | **bidding** | `{SKILL_BASE}/.claude/skills/bidding/gt-SKILL.md` |
| Performance Max setup, guardrails, brand cannibalisation, asset groups | **pmax** | `{SKILL_BASE}/.claude/skills/pmax/gt-SKILL.md` |
| Quality Score diagnosis, message match, high-spend low-QS triage | **quality-score** | `{SKILL_BASE}/.claude/skills/quality-score/gt-SKILL.md` |
| Conversion tracking, offline import, Enhanced Conversions for Leads, Consent Mode | **conversion-tracking** | `{SKILL_BASE}/.claude/skills/conversion-tracking/gt-SKILL.md` |
| Ad copy, Pain-Proof-CTA, RSA pin strategy, extensions | **ad-copy** | `{SKILL_BASE}/.claude/skills/ad-copy/gt-SKILL.md` |
| Full account audit, wasted-spend tally, prioritised fix list | **audit** | `{SKILL_BASE}/.claude/skills/audit/gt-SKILL.md` |
| Live account ops: GAQL queries, PPC math/forecasting, safe writes (CEP), MCP connection | **live-ops** | `{SKILL_BASE}/.claude/skills/live-ops/gt-SKILL.md` |

## Shared Reference Files

| Resource | When to load |
|----------|-------------|
| `{SKILL_BASE}/resources/references/b2b-guardrail.md` | What does NOT transfer from e-commerce Google Ads advice — read first |
| `{SKILL_BASE}/resources/references/crm-attribution.md` | HubSpot + Salesforce offline-conversion loop (ECL, GCLID, Data Manager API, value-based bidding) |
| `{SKILL_BASE}/resources/references/ai-bidding-2026.md` | Journey-Aware Bidding, Smart Bidding Exploration, AI Max (B2B) |
| `{SKILL_BASE}/resources/references/consent-mode-v2.md` | EU/EEA Consent Mode v2 compliance |
| `{SKILL_BASE}/resources/references/benchmarks.md` | B2B CPL/CPC/QS/conversion benchmarks |
| `{SKILL_BASE}/resources/references/audit-checklist.md` | The full account audit checklist |
| `{SKILL_BASE}/resources/references/negative-keyword-library.md` | 200+ negatives by category |
| `{SKILL_BASE}/resources/references/competitive-research.md` | Auction insights, competitor conquest |
| `{SKILL_BASE}/resources/references/gaql-queries.md` | GAQL query templates for live analysis (B2B) |
| `{SKILL_BASE}/resources/references/ppc-math.md` | PPC math & forecasting — break-even CPL/CPC, cost-per-SQL, budgets (B2B) |
| `{SKILL_BASE}/resources/references/safe-write-cep.md` | Safe write operations — Confirm→Execute→Post-check |

## Routing Rules

- General question ("help me with Google Ads") → ask about budget, ICP, goals, current account state → route to **audit** first (find the leaks), then campaign-setup
- "My Google Ads are not working" / "wasting money" → **audit** → conversion-tracking → negative-keywords (that is where the money is)
- New account / from scratch → **conversion-tracking** → campaign-setup → keywords → negative-keywords (pre-launch list)
- EU/EEA account → confirm **Consent Mode v2** early (conversion-tracking)
- Multiple topics → load primary sub-skill first, reference others as needed

## Key Benchmarks

B2B only. Benchmarks vary enormously by vertical, intent, and ICP — use as gut-checks, not targets; check intent tier/industry/geo/deal size/maturity before applying any figure. The only number that matters is whether spend produces pipeline.

| Metric | B2B Benchmark (2026) |
|--------|---------------------|
| CPC (B2B Search, non-brand) | $4-15+ depending on vertical (legal, SaaS, finance run higher) |
| CPL (Search) | $50-200+ for B2B SaaS; higher for enterprise / high-ACV |
| Quality Score (focus area) | High-spend keywords below 5 = overpaying; fix or restructure |
| Wasted spend found on audit | Most B2B accounts waste 20-40% of budget on unqualified clicks |
| Negative keyword reclaim | A 90-day search-terms sweep routinely finds $1,000-10,000/mo recoverable |
| PMax budget allocation | 15-25% of total Google Ads spend, with guardrails |
| Smart Bidding data floor | ~30+ conversions/month for the algorithm to work well |
| Search terms review cadence | Weekly on active accounts ($10k+/mo); biweekly below that |

**Critical principle — structure beats tactics.** Most underperforming B2B accounts fail at account hierarchy, conversion tracking, or negative-keyword hygiene, not at ad copy. Audit foundations before micro-optimising bids. Treat Smart Bidding as a contract: it only performs when conversion data is clean, attribution is consistent, and budgets aren't throttled. Audit the inputs before blaming the algorithm.

**The wasted-spend reality.** In 2026 Google pushes broad match and PMax harder than ever, adding queries — including irrelevant ones — to your auctions. The search terms report and a maintained negative-keyword list are the only things standing between you and donating budget to Google. Cheapest hour of work in paid media, most consistently neglected.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
