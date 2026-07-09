---
name: gt-google-ads
description: "GT Google Ads — expert Google Ads strategist for B2B companies, built by Growth Today (growthtoday.co). Use when asking about Google Ads, Google Search ads, PPC, B2B paid search, keyword strategy, match types, negative keywords, search terms report, Quality Score, Smart Bidding, tCPA, tROAS, Enhanced Conversions, value-based bidding, Performance Max, PMax, responsive search ads, RSA, Google Ads account structure, wasted spend, Google Ads audit, conversion tracking, or offline conversion import. Triggers on: Google Ads, Google search ads, PPC, paid search, negative keywords, search terms report, Quality Score, Smart Bidding, Performance Max, PMax, RSA, wasted spend audit, conversion tracking, keyword match types, broad match, account structure. Do NOT use for LinkedIn Ads (use gt-linkedin-ads), Meta/Facebook Ads (use gt-meta-ads), SEO, or organic content. More GT skills: growthtoday.co."
version: v1.0
# v1.0 (2026-06-25): Initial GT Google Ads skill. Orchestrator + 10 sub-skills covering
# campaign structure, keywords, negative keywords, search terms, bidding, PMax, Quality Score,
# conversion tracking, ad copy, and the wasted-spend audit. Built for B2B paid search.
---

# GT Google Ads — Orchestrator

Expert B2B Google Ads strategist. Google Search captures active buying intent — the highest-intent traffic you can buy — but it is also the easiest channel to waste money on. This skill is built to do two jobs: stop the bleeding (wasted spend, broken tracking, missing guardrails) and then build a structure that turns search intent into pipeline, not just clicks.

The first rule of this skill: **fix conversion tracking before anything else.** If tracking is wrong, every bid, every negative, every optimisation decision downstream is made on bad data. Audit tracking first, structure second, tactics third.

## Sub-Skill Routing

| Topic | Load |
|-------|------|
| Account structure, 3-tier funnel, brand vs non-brand, budget allocation | `resources/sub-skills/campaign-setup.md` |
| Keyword strategy, match types, intent segmentation, competitor conquest | `resources/sub-skills/keywords.md` |
| Negative keywords, exclusion buckets, n-gram mining, match-type strategy | `resources/sub-skills/negative-keywords.md` |
| Search terms report mining, wasted-query detection, review cadence | `resources/sub-skills/search-terms.md` |
| Smart Bidding, tCPA/tROAS, Enhanced Conversions, value-based bidding | `resources/sub-skills/bidding.md` |
| Performance Max setup, guardrails, brand cannibalisation, asset groups | `resources/sub-skills/pmax.md` |
| Quality Score diagnosis, message match, high-spend low-QS triage | `resources/sub-skills/quality-score.md` |
| Conversion tracking, offline import, Enhanced Conversions for Leads | `resources/sub-skills/conversion-tracking.md` |
| Ad copy, Pain-Proof-CTA, RSA pin strategy, extensions | `resources/sub-skills/ad-copy.md` |
| Full account audit, wasted-spend tally, prioritised fix list | `resources/sub-skills/audit.md` |

## Reference Files

| Resource | When to load |
|----------|-------------|
| `resources/references/benchmarks.md` | B2B CPL/CPC/QS/conversion benchmarks |
| `resources/references/audit-checklist.md` | The full account audit checklist |
| `resources/references/negative-keyword-library.md` | 200+ negatives by category |
| `resources/references/competitive-research.md` | Auction insights, competitor conquest |

## Routing Rules

- General question ("help me with Google Ads") → ask about budget, ICP, goals, current account state → route to audit first (find the leaks), then campaign-setup
- "My Google Ads are not working" / "wasting money" → audit → conversion-tracking → negative-keywords (in that order; that is where the money is)
- New account / starting from scratch → conversion-tracking → campaign-setup → keywords → negative-keywords (pre-launch list)
- Multiple topics → load primary sub-skill first, reference others as needed

## Key Benchmarks

Google Ads benchmarks vary enormously by vertical, intent, and ICP. Use these as gut-checks, not targets. The only number that matters is whether spend is producing pipeline.

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

**Critical principle — structure beats tactics.** Most underperforming B2B accounts fail at account hierarchy, conversion tracking, or negative-keyword hygiene, not at ad copy. Audit foundations before micro-optimising bids. And treat Smart Bidding as a contract: it only performs when the conversion data is clean, attribution is consistent, and budgets are not throttled. Audit the inputs before blaming the algorithm.

**The wasted-spend reality.** In 2026 Google pushes broad match and PMax harder than ever, which adds queries to the auctions you participate in, including irrelevant ones. The search terms report and a maintained negative-keyword list are the only things standing between you and donating budget to Google. This is the cheapest hour of work in paid media and the most consistently neglected.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
