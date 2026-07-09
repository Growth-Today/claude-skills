---
description: B2B Google Ads account audit — the systematic wasted-spend review, priority order of fixes, and the recoverable-spend tally. Use for Google Ads audit, account audit, wasted spend review, account health check, what to fix first, inherited account review. Triggers on "Google Ads audit", "account audit", "audit my account", "wasted spend", "account health check", "what to fix first", "inherited a Google Ads account". Routes into the other sub-skills for each fix.
---

# Google Ads Account Audit

You run a systematic audit that finds the leaks, scores them, and produces a ranked fix list — not a 40-page PDF that gets shelved. Most B2B accounts waste 20-40% of budget on unqualified clicks, and the problems are rarely obvious: everything runs, it just runs badly.

## Instructions

1. Audit conversion tracking first — if it is broken, every other read is wrong
2. Work top-down: tracking → structure → negatives → bidding → copy/LP
3. Score each finding by impact x effort
4. End with a dollar figure of recoverable wasted spend
5. Ship the top fixes in the first two weeks

## Audit Order (highest-leverage first)

1. **Conversion tracking** (see conversion-tracking). Is the action real (not page-load)? Is attribution consistent? Is offline import in place? Fix this before anything else — broken tracking invalidates the rest of the audit.
2. **Account structure** (see campaign-setup). Brand vs non-brand split? Tight ad groups? One LP per intent? PMax cannibalising brand?
3. **Negative keywords + search terms** (see negative-keywords, search-terms). Pull 90-day search terms by spend; flag $50+/zero-conversion. This routinely finds $1,000-10,000/mo recoverable. Check for over-negation too.
4. **Bidding** (see bidding). Targets realistic vs actuals? Anything "limited"? Portfolio strategies blending intent? Wrong conversion action feeding bids?
5. **Quality Score** (see quality-score). High-spend keywords below 5 inflating CPC?
6. **Ad copy + landing pages** (see ad-copy, conversion-tracking). RSA strength, message match, dedicated LPs, page live and fast?
7. **PMax guardrails** (see pmax). Account-level negatives, brand exclusions, asset-group discipline?

## Quick Diagnostic Checklist

- [ ] Conversion action fires on real action (form submit / demo), not page load
- [ ] Data-driven attribution active; not comparing to last-click history blindly
- [ ] Enhanced Conversions for Leads + offline import in place
- [ ] Brand and non-brand in separate campaigns
- [ ] Brand terms added as negatives to non-brand campaigns
- [ ] Account-level negative lists exist (jobs, free, DIY, competitor) and applied to new campaigns + PMax
- [ ] 90-day search terms reviewed; $50+/zero-conversion flagged
- [ ] No over-negation blocking converting queries
- [ ] Ad groups tightly themed (5-15 keywords, single intent)
- [ ] 2-3+ RSAs per ad group at Good/Excellent strength
- [ ] Dedicated landing pages, not the homepage; live, fast, message-matched
- [ ] High-spend keywords not stuck below QS 5
- [ ] Bid targets realistic vs 30/90-day actuals; nothing wrongly "limited"
- [ ] PMax capped at 15-25% with brand exclusions + negatives
- [ ] Ad scheduling sane for a B2B offer (not burning budget at 2am if no one converts)

## The Output

Every audit ends with a **wasted-spend tally** — an actual dollar figure of spend that went to traffic with no conversion path, no relevance, or no business value. Then a fix list **scored by impact x effort**, so the team ships the top 10 in two weeks. A ranked backlog beats a long report.

Priority of fixes when in doubt: conversion tracking errors first (everything depends on them), then negative-keyword gaps (stops active bleeding immediately), then structure, then bidding, then copy/LP.

## Examples

Example 1: "Audit my Google Ads account."
→ Start with conversion tracking, then structure, negatives/search terms, bidding, QS, copy/LP, PMax. Score findings by impact x effort, end with a recoverable-spend dollar figure and a top-10 fix list.

Example 2: "I inherited a Google Ads account — where do I start?"
→ Audit negative lists and conversion tracking before running anything. Pull 90-day search terms, check the action fires correctly, confirm brand/non-brand split, then prioritise fixes by impact x effort.


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
