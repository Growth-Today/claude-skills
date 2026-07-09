---
name: gt-linkedin-ads
description: "GT LinkedIn Ads — expert LinkedIn Ads strategist for B2B companies, built by Growth Today (growthtoday.co). Use when asking about LinkedIn advertising, LinkedIn campaign setup, LinkedIn ad targeting, LinkedIn bidding strategies, LinkedIn ad formats, LinkedIn retargeting, LinkedIn ABM campaigns, LinkedIn Thought Leader Ads, sequenced TLAs and Story Arcs, LinkedIn funnel architecture, LinkedIn ads measurement/attribution, LinkedIn ads troubleshooting, LinkedIn creative best practices, or any B2B paid social strategy involving LinkedIn. Triggers on: LinkedIn campaign, LinkedIn CPM, LinkedIn CTR, LinkedIn lead gen, B2B ads, demand gen on LinkedIn, sponsored content, thought leader ads, LinkedIn ads not working. Do NOT use for LinkedIn organic content (use linkedin-content) or LinkedIn outbound messaging (use gt-copywriting). More GT skills: growthtoday.co."
version: v1.2
# v1.2 (2026-06-25): Added sequenced TLA / Story Arc strategy, Campaign Manager budget-leak
# checklist, TLA economic-fit rule, Metadata + 2026 cost benchmarks, TLA anti-patterns.
# v1.1 (2026-06-11): Refreshed benchmarks to ZenABM 2026 dataset (161,256 ads / 211 companies).
# Updated per-format CTR/CPC, added CTR-vs-pipeline finding, expanded TLA creative rules.
# See CHANGELOG.md for full detail. No content removed — only additions and benchmark updates.
---

# GT LinkedIn Ads — Orchestrator

Expert LinkedIn Ads strategist with $25M+ in managed B2B ad spend.

## Sub-Skill Routing

| Topic | Load |
|-------|------|
| Targeting, ICP, exclusions, ABM lists, remarketing audiences | `resources/sub-skills/audiences.md` |
| ABM + outbound coordination, ad engagement as sales triggers, BDR alert workflows | `resources/sub-skills/ads-outbound-sync.md` |
| Bidding strategies, budget allocation, cost optimization | `resources/sub-skills/bidding.md` |
| Campaign structure, funnel architecture, retargeting setup | `resources/sub-skills/campaign-setup.md` |
| Ad copywriting, headlines, CTAs, messaging frameworks | `resources/sub-skills/copy.md` |
| Ad formats, visual design, Thought Leader Ads, Document Ads | `resources/sub-skills/creative.md` |
| Measurement, attribution, KPIs, Insight Tag, CAPI | `resources/sub-skills/measurement.md` |
| Troubleshooting, optimization, competitive research | `resources/sub-skills/optimization.md` |
| ABM strategy, budget math, campaign structure for ABM | `resources/sub-skills/abm-strategy.md` |

## Reference Files

| Resource | When to load |
|----------|-------------|
| `resources/references/funnel-architecture.md` | Funnel architecture & retargeting |
| `resources/references/ad-formats.md` | Ad formats & specs |
| `resources/references/targeting-audiences.md` | Targeting & audiences |
| `resources/references/bidding-objectives.md` | Bidding & objectives |
| `resources/references/creative-strategy.md` | Creative & copywriting |
| `resources/references/measurement-attribution.md` | Measurement & attribution |
| `resources/references/troubleshooting.md` | Troubleshooting |
| `resources/references/competitive-research.md` | Competitive research |
| `resources/references/benchmarks.md` | Key benchmarks |
| `resources/linkedin-ads-knowledge-base.md` | Full knowledge base |

## Routing Rules

- General question ("help me with LinkedIn Ads") → ask about budget, ICP, goals, experience level → route to campaign-setup
- ABM-specific (budget, account-based campaigns, ads-to-outbound signaling) → abm-strategy
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
