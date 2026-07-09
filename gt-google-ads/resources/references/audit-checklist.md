# Google Ads Account Audit Checklist (B2B)

A structured review to find wasted spend and structural problems. Score each finding by impact x effort and ship the top 10 in two weeks. Fix in the priority order at the bottom.

## 1. Conversion tracking (highest priority)
- [ ] Conversion action fires on the real action (form submit / demo booked), not page load
- [ ] No duplicate or double-counted conversions
- [ ] Data-driven attribution active
- [ ] Enhanced Conversions for Leads enabled (hashed first-party data)
- [ ] Offline conversion import live (lead to MQL to SQL to opportunity to closed-won, with value)
- [ ] Conversion values reflect real business value, not flat per-lead
- [ ] The action feeding Smart Bidding is the correct one

## 2. Account structure
- [ ] Brand and non-brand in separate campaigns
- [ ] Brand terms added as negatives to non-brand campaigns
- [ ] Competitor conquest in its own campaign
- [ ] Ad groups tightly themed (5-15 keywords, single intent)
- [ ] One landing page intent per ad group
- [ ] 3-tier funnel with budget by intent (BOFU 50-60 / MOFU 25-35 / TOFU 10-15)
- [ ] No single campaign serving radically different geos without location segmentation

## 3. Keywords and match types
- [ ] Match types deliberate (exact for proven BOFU, phrase for controlled, broad only with tracking + negatives)
- [ ] Broad / AI Max tested via experiment, not flipped on live
- [ ] Qualifier mechanic applied to category terms
- [ ] Winning search terms promoted to exact-match keywords

## 4. Negative keywords and search terms
- [ ] Account-level shared lists exist: jobs, free/cheap/DIY, competitor
- [ ] Industry-layer negatives added
- [ ] Shared lists applied to all relevant campaigns AND new launches
- [ ] PMax has account-level negatives applied
- [ ] 90-day search terms pulled, sorted by cost; $50+/zero-conversion flagged
- [ ] Negatives added at the narrowest effective match level
- [ ] No over-negation blocking converting queries (quarterly match-type sweep)

## 5. Bidding
- [ ] Bid strategy matches conversion volume (~30+/mo for tCPA/tROAS)
- [ ] Targets realistic vs 30/90-day actuals
- [ ] Nothing wrongly stuck in "limited by bid strategy"
- [ ] Value-based bidding where conversion values differ
- [ ] Portfolio strategies not blending different-intent campaigns
- [ ] Budgets not throttling delivery on profitable campaigns

## 6. Quality Score
- [ ] High-spend keywords not stuck below QS 5
- [ ] Low QS diagnosed to component (expected CTR / ad relevance / LP experience)
- [ ] Not chasing QS on low-volume long-tail

## 7. Ad copy and landing pages
- [ ] 2-3+ RSAs per ad group at Good/Excellent strength
- [ ] Pain to Proof to CTA structure; strongest pain headline pinned to position 1
- [ ] Not over-pinned (variation preserved)
- [ ] Sitelinks, callouts, structured snippets in place
- [ ] Dedicated landing pages (not homepage); live, fast on mobile, message-matched
- [ ] Most-clicked URLs checked: page live, aligned, has a conversion element

## 8. PMax
- [ ] Capped at 15-25% of total spend
- [ ] Brand exclusions applied (no brand cannibalisation)
- [ ] Account-level negatives applied
- [ ] Asset groups themed, not one catch-all
- [ ] Judged on incremental pipeline, not self-reported ROAS

## 9. Scheduling and settings
- [ ] Ad scheduling sane for a B2B offer (not 24/7 if no one converts at 2am)
- [ ] Device performance reviewed (bid adjustments where warranted)
- [ ] MCC / account alerts configured for spend spikes, tracking drops, disapprovals

## Output
- [ ] Wasted-spend tally (actual dollar figure)
- [ ] Findings scored by impact x effort
- [ ] Top-10 ranked fix list shipped in first two weeks

## Priority order of fixes
1. Conversion tracking errors (everything downstream depends on them)
2. Negative-keyword gaps (stops active bleeding immediately)
3. Account structure (clean signal for bidding)
4. Bidding targets and strategy
5. Quality Score / ad copy / landing pages


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
