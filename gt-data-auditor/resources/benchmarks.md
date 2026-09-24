# Benchmarks Reference

Central database of all stat-receipts used by this skill. Refresh every 6 months. Last updated: June 2026.

Every benchmark in any output must trace to a source in this file. Do not invent or interpolate numbers. When a number is more than 12 months old and the user is making a high-stakes decision on it, name the date and offer to web-search for an update.

## Email Accuracy

| Metric | Benchmark | Source |
|---|---|---|
| Good email validity rate (ICP list) | 90%+ | UnifyGTM Provider Comparison 2026 |
| Acceptable email validity rate | 80% to 89% | UnifyGTM 2026 |
| Disqualify provider below | 80% | UnifyGTM 2026 |
| Real-world bounce rate target | Under 1% | Validity 2025 Deliverability Benchmark |
| Hard bounce threshold (spam filter trigger) | 2% | Validity 2025 |
| Hard bounce that drops inbox placement 20pp | 5% | Validity 2025 |
| Global avg inbox placement | 83.5% | Validity 2025 |
| "Verified" list first-send bounce (worst case) | 38% | SparkDBI 2026 |

Tested provider accuracy ranking (Cleanlist 1,000-contact benchmark 2026):
- Cleanlist: 98%
- Cognism: 90%
- ZoomInfo: 85%
- Clearbit / Breeze: 85%
- Apollo: 80%
- Independent average across 15 providers: 50%

Waterfall vs single source:
- Waterfall enrichment find rate: 85% to 95%
- Single-source find rate: 50% to 60%
- Difference: 8 to 18 percentage points improvement in deliverability
- Source: DealSignal Sales Performance Report 2026

## Email Decay and Freshness

| Metric | Benchmark | Source |
|---|---|---|
| Monthly contact data decay | 2.1% | Dun & Bradstreet Data Advisory |
| Annual contact data decay | 22% to 30% | Dun & Bradstreet |
| Annual email obsolescence | 23% to 30% | Dun & Bradstreet |
| Annual phone number change | 18% | Dun & Bradstreet |
| Annual employer change (professionals) | 15% to 20% | Dun & Bradstreet |
| 12-month-old "95% accurate" list current accuracy | 65% to 70% | SparkDBI 2026 |
| Recommended refresh cadence (top tier) | Weekly | Amplemarket 2026 |
| Recommended refresh cadence (minimum) | Monthly | Salesmotion 2026 |

## Phone and Cold Call Connect Rates

| Metric | Benchmark | Source |
|---|---|---|
| US avg cold connect rate | 3% to 10% (5% to 8% realistic) | SalesHive 2026 |
| Top performer cold connect rate (verified mobile) | 18% to 22% | Cognism State of Cold Calling 2026 |
| Mobile vs non-mobile connect rate lift | 45% higher | Prospeo 2026 |
| Mobile direct dial coverage (strong, US list) | 60%+ | Cognism 2026 |
| Mobile direct dial coverage (acceptable) | 30% to 59% | Cognism 2026 |
| Generic connect rate target | 8% to 12% | Cognism 2026 |
| Avg dials per connect | 18+ | Gartner |
| Avg dials per booked meeting | 40 to 45 | The Bridge Group 2026 |
| Top performer dials per meeting | 25 to 30 | Cognism 2026 |
| Avg B2B cold call dial-to-meeting | 2.3% | Cognism (down from 4.82% prior year) |
| Top performer dial-to-meeting | 5% to 8% | Cognism 2026 |
| Connect rate collapse (STIR/SHAKEN era) | 60% to 15% over 18 months | r/b2bmarketing case |
| SDR day lost to manual dial and dead ring | 35% | Bridge Group 2026 |
| Best call days | Tuesday and Wednesday (44% of demos) | ZoomInfo 1.4M call analysis |
| Worst call day | Friday | ZoomInfo |
| Best call time | 4 to 5 PM (71% more effective) | ZoomInfo |
| Avg call duration | 93 seconds | Prospeo 2026 |
| Conversation rate (within answered calls) | 65.6% | Prospeo 2026 |
| Callback reach rate | 26.85% | Prospeo 2026 |
| Calls analyzed (Cognism dataset) | 200,000 | Cognism State of Cold Calling 2026 |

## Spam and Compliance Thresholds

| Metric | Benchmark | Source |
|---|---|---|
| Spam complaint rate 2025 B2B avg | 0.04% to 0.06% | Verified.email 2026 |
| Industry best practice | Under 0.1% | Verified.email 2026 |
| Critical threshold (Gmail/Outlook filter trigger) | Over 0.3% | Verified.email 2026 |
| Healthy unsubscribe range | 0.1% to 0.2% | Verified.email 2026 |
| CAN-SPAM opt-out honor window | 10 business days | CAN-SPAM Act |
| GDPR opt-out honor window | Immediate | GDPR Article 21 |

## Cost and ROI

| Metric | Benchmark | Source |
|---|---|---|
| Poor data quality cost per business | $12.9M annually | Gartner |
| US business loss from data quality | $3.1T annually | Gartner |
| SDR hours lost validating contacts | 500 hours/year (62 working days) | DealSignal 2026 |
| Selling capacity lost to data hygiene | 25% | DealSignal 2026 |
| Teams reporting 10%+ revenue impact from CRM decay | 44% | Landbase 2026 |
| Clean list ROI | $36 per $1 spent | Litmus 2024 |
| Email verification service ROI | 10x to 20x | Verified.email 2026 |

Provider pricing range (per record):
- Low end: $0.01
- High end: $2.50
- Credit-based vs seat-based savings: 40% to 60% on equivalent volume
- Source: Cleanlist 15-provider benchmark 2026

Cost per usable contact benchmarks:
- Strong: Under $0.30 (high-volume waterfall)
- Acceptable: $0.30 to $0.80 (mid-volume)
- Fail: Above $0.80

## Coverage and Match Rates

| Metric | Benchmark | Source |
|---|---|---|
| Strong match rate on tight ICP slice | 70%+ | Internal GT testing + UnifyGTM 2026 |
| Acceptable match rate | 50% to 69% | UnifyGTM 2026 |
| Fail match rate | Under 50% | UnifyGTM 2026 |
| Average single-provider match rate | ~50% | Landbase 2026 |
| Single-source usable matches per 1,000 queried | 400 to 600 | Landbase 2026 |
| CRM systems with outdated/incomplete/inaccurate info | 70% | Landbase 2026 |

## CRM Hygiene

| Metric | Benchmark | Source |
|---|---|---|
| Strong duplicate rate (companies) | Under 2% | GT internal standard |
| Title taxonomy unique-to-total ratio (standardized) | Under 0.3 | GT internal standard |
| Title taxonomy unique-to-total ratio (free-text problem) | Over 0.6 | GT internal standard |

## Enrichment Method

| Metric | Benchmark | Source |
|---|---|---|
| Single-source find rate | 50% to 60% | DealSignal 2026 |
| Multi-source waterfall find rate | 85% to 95% | DealSignal 2026 |
| AI-routed uplift over static waterfall | 5% to 15% | DealSignal 2026 |

## SDR Performance and Pipeline

| Metric | Benchmark | Source |
|---|---|---|
| SDR pipeline generation share | 46% to 73% | TOPO |
| Median SDR-generated pipeline | $3M annually | Bridge Group |
| Outbound SDR meetings per month | 15 (Operatix) / 21 (Bridge Group) | Multiple sources |
| Meeting show rate | 70% to 80% | SalesHive 2026 |
| Cold email reply rate avg | 3% to 5.1% (down from ~7% prior year) | Prospeo 2026 |

## Notes on usage

1. Always cite source. When using a benchmark in client-facing output, name the source briefly ("Validity 2025", "Cognism 2026", "Dun & Bradstreet")
2. Use ranges, not point estimates. B2B data is noisy. "18% to 22% on verified mobile" is more credible than "20% mobile connect rate"
3. Refresh quarterly. Industry shifts fast. Check the source list in sources.md for refresh links every 90 days
4. Flag stale benchmarks. If a number is more than 12 months old and the user is making a high-stakes decision on it, mention the date and offer to web-search for an update


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
