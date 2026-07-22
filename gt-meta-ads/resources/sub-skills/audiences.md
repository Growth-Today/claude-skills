---
description: Meta Ads audiences for B2B — custom audiences, lookalikes, Advantage+ audience, broad targeting, exclusions, and overlap. Use for custom audiences, lookalike audiences, Advantage+ audience, broad targeting, detailed targeting, audience overlap, CRM list audiences, retargeting audiences. Triggers on "custom audience", "lookalike", "Advantage+ audience", "broad targeting", "detailed targeting", "audience overlap", "CRM list", "1% lookalike", "minimum audience size". Do NOT use for campaign budget structure (use campaign-setup).
---

# Meta Ads Audiences (B2B)

In 2026 targeting is less about finding one perfect audience and more about giving Meta clean first-party signal and trusting the system. Strong creative now does much of the "targeting" by filtering who responds. Still, the audience architecture matters for B2B, where firmographic precision is weaker than LinkedIn.

## Instructions

1. Feed first-party data: build custom audiences from CRM lists and site/engagement data
2. Build lookalikes off your best converters, not all leads
3. Lean broader than instinct says; let creative and the algorithm filter
4. Manage overlap and exclusions deliberately
5. Respect minimum sizes and 2026 sensitive-category restrictions

## Custom Audiences (your highest-intent targeting)

- **CRM lists:** upload customer / closed-won / SQL lists (hashed) → these are your best lookalike seeds and your exclusion lists.
- **Website visitors** (via Pixel/CAPI): segment by recency and page. For B2B, extend retargeting windows to **60-90 days** since the cycle is long.
- **Engagement audiences:** video viewers (e.g. 25%+ watched), page/IG engagers, lead-form openers. These build the consideration layer.
- Minimum ~1,000 people in a custom audience to run ads to it.

## Lookalikes

- Seed from **high-value actions** (closed-won, SQL, demo-booked), not "all leads". A lookalike of junk leads finds more junk.
- Start **1%** for conversions (closest match, best CPA), test 3% and 5% for awareness/scale.
- Lookalike source minimum is 100, but 1,000+ seeds perform better.
- In 2026, Meta expands first-party audiences implicitly once you feed it good signal, so lookalikes help less than they used to — but a 1-3% lookalike + broad creative testing is still a reliable combination.

## Broad + Advantage+ Audience

- Meta's Andromeda update means **broad targeting with strong creative often beats narrow interest stacking.** Give Advantage+ Audience a few relevant interests/behaviours as *suggestions*, not hard filters, and let it learn.
- Avoid the ten-ad-sets-one-interest-each pattern — overlap kills validity and spreads learning thin.

## Exclusions & Overlap

- Exclude current customers and active CRM leads from prospecting.
- Exclude recent converters (30-60 days) from conversion retargeting.
- Watch audience overlap between ad sets; high overlap means you bid against yourself and corrupt test reads. Consolidate overlapping ad sets.

## 2026 Restrictions

- Meta blocks custom audiences that imply sensitive attributes (health, financial status). Do not build segments like "high income" or condition-based audiences — they are auto-rejected.

## Examples

Example 1: "What audiences should I run for B2B on Meta?"
→ Custom audiences from CRM (seeds + exclusions), 1% lookalikes off closed-won/SQL, broad + Advantage+ Audience with light interest hints, and 60-90 day retargeting windows. Exclude current customers from prospecting.

Example 2: "Should I build lots of tightly targeted interest ad sets?"
→ No. In 2026 broad + strong creative beats narrow interest stacking, and many overlapping ad sets corrupt learning. Consolidate, feed first-party signal, and let creative filter.


## B2B guardrail

Before applying any generic Meta tactic or benchmark here, check `resources/references/b2b-vs-b2c-guardrail.md` — most public Meta advice is DTC/e-commerce and does not transfer to B2B.
---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
