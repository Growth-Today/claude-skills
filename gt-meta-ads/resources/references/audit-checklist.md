# Meta Ads Account Audit Checklist (B2B)

Score each finding by impact x effort and ship the top items first. The two anchors: is tracking sound, and is creative treated as the strategy. Fix in the priority order at the bottom.

**Evidence discipline:** don't apply a benchmark without checking objective, geography, methodology, sample size, and account maturity; mark **n/a**/**unknown** where you can't see it; treat betas/new features and vendor performance claims as **discovery, not a failure**. All benchmarks here are B2B — never import DTC/e-commerce figures.

## 1. Tracking (highest priority)
- [ ] Pixel installed and firing on the right events
- [ ] Conversions API (CAPI) live, server-side
- [ ] Pixel + CAPI deduplicated with a shared event ID
- [ ] Event match quality healthy (hashed first-party data passed)
- [ ] Conversion event is the real outcome (lead submit / demo), not page-load or landing-view
- [ ] Attribution window consistent across campaigns (28-day click for long cycles)
- [ ] Domain verified in Business Manager
- [ ] Aggregated Event Measurement configured; the true B2B conversion prioritized (not page view)
- [ ] Standard events used where possible (custom only for bespoke steps)
- [ ] CAPI Gateway considered where no dev resource for full CAPI
- [ ] `fbclid` captured + persisted on the contact for match quality (see crm-attribution)

## 2. Measurement loop
- [ ] CRM outcomes synced back as offline conversions (lead to MQL to SQL to closed-won)
- [ ] Account judged on pipeline / cost per SQL, not raw CPL
- [ ] Platform numbers reconciled against CRM reality
- [ ] Creative read by spend allocation, not ad-level CPA alone
- [ ] Judged over a full B2B cycle, not first two weeks
- [ ] UTM taxonomy consistent + validated (source/medium/campaign/content) so CRM reads it
- [ ] Breakdown reporting run (placement / demographic / time) and read to SQL, not CPL
- [ ] Incrementality checked before scaling (Conversion Lift / holdout) at meaningful spend

## 3. Creative
- [ ] Modular creative library exists (hooks, bodies, CTAs)
- [ ] 2-4 new concepts/week, one variable per test
- [ ] 3-5 new variants/week at $300+/day
- [ ] Mobile-first, captioned (85% watch sound-off)
- [ ] Hook in the first 3 seconds
- [ ] Native / authentic over polished-corporate
- [ ] Format matched to funnel stage
- [ ] Static vs video tested per account (do not assume motion wins)

## 4. Creative fatigue
- [ ] Frequency 1.5-2.5/7 days on cold audiences
- [ ] Refresh triggered at CTR -20% from baseline or frequency >3-3.5
- [ ] Rolling refresh: pause lowest performer, add fresh one every ~2 weeks
- [ ] Fatigue vs saturation diagnosed (small audience + high freq = saturation)

## 5. Account structure
- [ ] Full-funnel: prospecting / consideration / retargeting
- [ ] Budget split sane (40-50 / 30-40 / 20-25)
- [ ] CBO for prospecting, ABO for retargeting
- [ ] 4-5 ads per ad set
- [ ] Current customers excluded from prospecting
- [ ] Active CRM leads excluded from prospecting
- [ ] Recent converters (30-60 days) excluded from conversion retargeting
- [ ] Not blanket-excluding all past purchasers everywhere

## 6. Audiences
- [ ] Custom audiences from CRM lists (hashed)
- [ ] Lookalikes seeded off closed-won / SQL, not all leads
- [ ] 1% lookalike for conversions; 3-5% for scale
- [ ] Broad + Advantage+ Audience tested with light interest hints
- [ ] Not over-segmented into tiny overlapping ad sets
- [ ] Audience overlap checked between ad sets
- [ ] Retargeting windows 60-90 days for B2B
- [ ] No sensitive-category custom audiences

## 7. Learning phase
- [ ] Ad sets clearing ~50 events/week
- [ ] None stuck "Learning Limited"
- [ ] Budget floors met (CPA x 50 / 7 per day)
- [ ] Optimisation event frequent enough to hit 50/week
- [ ] Not making mid-test edits that reset learning

## 8. Lead quality (Instant Forms)
- [ ] Form length matched to ACV (4-5 fields for high-ACV)
- [ ] Qualifying questions filtering non-buyers
- [ ] Higher-intent form option where quality matters
- [ ] CRM real-time sync (no leads stranded in Meta)
- [ ] Fast speed-to-follow-up
- [ ] Lead outcomes fed back to optimisation

## 9. Placements & settings
- [ ] Facebook Feed / Stories prioritised for B2B; Audience Network off for lead gen
- [ ] Reels creative in 9:16 where used
- [ ] Objective matches funnel stage

## Output
- [ ] Wasted-spend tally (stale creative, junk leads, saturated audiences, Learning-Limited ad sets)
- [ ] Findings scored by impact x effort
- [ ] Top fixes shipped first

## Priority order of fixes
1. Tracking errors (everything downstream depends on them)
2. Measurement loop (so you optimise to pipeline, not cheap leads)
3. Creative + fatigue (the biggest B2B Meta levers)
4. Structure / audiences / learning phase
5. Lead-form quality


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
