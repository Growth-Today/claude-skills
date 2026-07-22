---
name: meta-ads-audit
description: Meta Ads account audit for B2B — systematic review across tracking, structure, audiences, creative, learning phase, and lead quality, with a prioritised fix list. Use for Meta ads audit, account audit, account health check, wasted spend review, what to fix first, inherited Meta account. Triggers on "Meta audit", "Facebook ads audit", "account audit", "audit my Meta", "account health check", "what to fix first", "inherited a Meta account". Routes into the other sub-skills for each fix.
---

# Meta Ads Account Audit (B2B)

You run a systematic audit, score findings by impact x effort, and produce a ranked fix list. On Meta the two anchors are always the same: is tracking sound, and is creative being treated as the strategy. Most weak B2B accounts fail on one of those, not on bid mechanics.

## Instructions

1. Audit tracking first — Pixel + CAPI, correct event, attribution
2. Then structure, audiences, creative, learning phase, lead quality
3. Score each finding by impact x effort
4. End with a wasted-spend figure and a top-fix list
5. Judge the account on pipeline, not reported CPL

## Audit Order (highest-leverage first)

1. **Tracking** (see tracking). Pixel + CAPI both live with deduplication? Conversion event = real outcome, not page-load? Event match quality healthy? Attribution window consistent? If tracking is broken, every other read is wrong — fix first.
2. **Measurement loop** (see measurement). Are CRM outcomes synced back? Is the account judged on pipeline or just CPL? An open loop means the algorithm is optimising to cheap junk.
3. **Creative** (see creative, creative-fatigue). Is there a creative library and a weekly testing cadence, or stale ads? Check frequency + CTR trend for fatigue. Mobile-first, hook in 3 seconds?
4. **Account structure** (see campaign-setup). Full-funnel layers with sane budget split? CBO/ABO used correctly? Exclusions keeping prospecting honest (current customers, active leads)?
5. **Audiences** (see audiences). First-party custom audiences + lookalikes off best converters? Over-segmented into tiny overlapping ad sets? Broad + Advantage+ tested? Sensitive-category audiences avoided?
6. **Learning phase** (see learning-phase). Ad sets clearing 50 events/week or stuck Learning Limited? Budget floors met? Edits resetting learning?
7. **Lead quality** (see lead-forms). Instant Forms qualified? CRM synced in real time? Fast follow-up? Quality fed back to optimisation?

## Quick Diagnostic Checklist

- [ ] Pixel + CAPI both firing, deduplicated, high event match quality
- [ ] Conversion event is the real outcome (not page-load / landing-view)
- [ ] Attribution window consistent across campaigns (28-day click for long cycles)
- [ ] CRM outcomes synced back as offline conversions; account judged on pipeline
- [ ] Full-funnel structure: prospecting / consideration / retargeting with sane split
- [ ] CBO for prospecting, ABO for retargeting; 4-5 ads per ad set
- [ ] Current customers + active leads excluded from prospecting
- [ ] Custom audiences from CRM; lookalikes seeded off closed-won/SQL, not all leads
- [ ] Not over-segmented into tiny overlapping ad sets; broad + Advantage+ in play
- [ ] No sensitive-category custom audiences (auto-rejected)
- [ ] Creative library exists; 2-4 new concepts/week, one variable per test
- [ ] Mobile-first, captioned, hook in first 3 seconds, native not over-polished
- [ ] Frequency 1.5-2.5/7 days on cold; refresh trigger at CTR -20% or freq >3-3.5
- [ ] 3-5 new variants/week at $300+/day to outrun fatigue
- [ ] Ad sets clearing ~50 events/week; none stuck Learning Limited
- [ ] Instant Forms qualified (questions, length for ACV); CRM real-time sync; fast follow-up
- [ ] Creative read by spend allocation, not ad-level CPA alone

## The Output

End with a **wasted-spend tally** (budget on stale creative, junk leads, oversaturated audiences, Learning-Limited ad sets) and a fix list **scored by impact x effort** — ship the top items first. Priority when in doubt: tracking errors first (everything depends on them), then the measurement loop and creative (the two biggest B2B levers), then structure / audiences / learning phase, then lead-form quality.

## Examples

Example 1: "Audit my Meta account."
→ Start with tracking (Pixel + CAPI, real event), then the measurement loop, creative + fatigue, structure, audiences, learning phase, lead quality. Score by impact x effort, end with a wasted-spend figure and top fixes.

Example 2: "I inherited a Facebook ads account — where do I start?"
→ Verify Pixel + CAPI and the conversion event before trusting any number. Then check whether CRM outcomes are synced (is it optimising to pipeline or cheap leads), review creative freshness and frequency, and consolidate over-segmented ad sets.


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
