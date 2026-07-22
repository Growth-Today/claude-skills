---
name: google-ads-search-terms
description: B2B Google Ads search terms report process — mining wasted queries, promoting winners, and review cadence. Use for search terms report, query mining, finding wasted spend, zero-conversion queries, promoting search terms to keywords. Triggers on "search terms report", "search query report", "mine queries", "zero conversion queries", "wasted queries", "promote search terms". Do NOT use for building the negative list buckets (use negative-keywords).
---

# Google Ads Search Terms Report

The search terms report is where the reality of your account lives. It shows the actual queries that triggered your ads. If you are not reviewing it on cadence, you are donating money to Google — and in 2026, with broad match and PMax pushed harder than ever, it matters more, not less.

## Instructions

1. Pull the search terms report, last 90 days, sorted by spend descending
2. Flag every term with meaningful spend and zero conversions
3. Add waste as negatives at the narrowest effective level (see negative-keywords)
4. Promote high-performing queries to exact-match keywords
5. Repeat weekly on active accounts

## The Core Process

1. **Pull** the last 90 days (90 is the balanced window for B2B sales cycles; use 30 only for short-cycle, 365 for very long consideration).
2. **Sort by cost descending.** The waste hides at the top of the spend list.
3. **Flag waste:** any query with $50+ spend and zero conversions, or a CPA more than 2x your account average. These are the bleed points.
4. **Cross-check intent:** is the query actually relevant? Broad match drags in conceptually-adjacent and irrelevant queries.
5. **Act:**
   - Irrelevant / wasteful → add as a negative at the narrowest level that stops it without blocking relatives.
   - Relevant and converting → promote to an exact-match keyword in the right ad group so you can bid and message-match it deliberately.

## What to look for

- High-spend / zero-conversion queries → immediate negatives.
- Patterns of waste (same junk word across many queries) → an n-gram negative (see negative-keywords).
- Converting queries not yet keywords → promote to exact, write a tighter ad + LP.
- Brand terms leaking into non-brand campaigns → add brand as a negative there.
- Note: Google hides a share of search terms under "other" — you will not see 100%, so pair this with conversion-level checks.

## Cadence

| Account spend | Cadence |
|---------------|---------|
| $10k+/mo | Weekly |
| Under $10k/mo | Biweekly |
| Any | Never less than monthly — waste compounds |

For new campaigns: lock a pre-launch negative list before the campaign enters the learning phase. Early spend leaking into junk queries during the learning window anchors Smart Bidding to bad signal, and cleaning that up later costs more than preventing it.

## Examples

Example 1: "How do I find wasted spend in Google Ads?"
→ Pull 90-day search terms sorted by cost, flag $50+ spend / zero-conversion queries, add as narrow negatives, promote converters to exact match, repeat weekly.

Example 2: "I found a query that converts well — what do I do?"
→ Promote it to an exact-match keyword in the matching ad group, write a tight ad + message-matched LP, and bid it deliberately instead of letting broad match catch it loosely.


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
