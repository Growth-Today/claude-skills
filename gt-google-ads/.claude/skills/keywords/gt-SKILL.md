---
name: google-ads-keywords
description: B2B Google Ads keyword strategy, match types, intent segmentation, the qualifier mechanic, and competitor conquest. Use for keyword selection, match types, broad/phrase/exact, keyword research, intent mapping, competitor keywords. Triggers on "keyword strategy", "match types", "broad match", "phrase match", "exact match", "keyword research", "competitor conquest", "qualifier keywords". Do NOT use for negative keywords (use negative-keywords) or search terms (use search-terms).
---

# Google Ads Keyword Strategy

You pick keywords by intent and control match types so Smart Bidding learns from clean signal.

## Instructions

1. Map keywords to funnel tier by intent, not by search volume
2. Choose match types deliberately — broad only with strong tracking and negatives
3. Use the qualifier mechanic to filter for commercial intent
4. Run competitor conquest in its own campaign
5. Promote winning search terms to exact-match keywords (see search-terms)

## Match Type Strategy (2026)

Google pushes broad match hard. Broad can find new converting queries, but only with the guardrails in place.

| Match type | When to use |
|-----------|-------------|
| Exact `[keyword]` | High-intent BOFU terms you know convert. Tightest control. |
| Phrase `"keyword"` | Mid-intent, controlled expansion around a known theme. |
| Broad `keyword` | Only with Enhanced Conversions + value-based bidding + a maintained negative list. Without those, broad overvalues junk and the algorithm anchors to bad signal. |

**Rule:** do not enable broad match (or AI Max) in an existing campaign without testing. Use the experiment tool to A/B test broad/AI Max against your current setup before rolling out. Broad without clean conversion tracking is how accounts quietly bleed.

## The Qualifier Mechanic

Attach commercial-intent qualifiers to category terms so you filter for buyers, not researchers:
- "software for X", "X platform", "X tool", "X vendor", "X agency", "best X", "X pricing", "X for [industry]"
- These pull people who are evaluating and buying, not students writing a paper. Pair with negatives that strip "free", "how to", "tutorial".

## Intent Segmentation

Segment campaigns by intent so each bid strategy gets homogeneous data:
- High-intent commercial → BOFU campaign, tightest match types
- Comparison / category → MOFU
- Informational → TOFU (only when funded)

If you are not yet on value-based bidding, separate campaigns by intent and manually push budget to the high-intent terms closest to converting.

## Competitor Conquest

- Bid on competitor brand terms in a **dedicated campaign** with its own budget and negatives.
- Expect lower Quality Score and higher CPC (you are not the brand they searched). Justify it on pipeline, not CPC.
- Keep your own brand terms as negatives here so signals stay clean.

## Quality Score Note

Keyword relevance feeds Quality Score, which feeds CPC. Tightly themed ad groups + message-matched ads + a relevant landing page is the lever. Sort by Quality Score, focus on high-spend keywords below 5 (see quality-score).

## Examples

Example 1: "What match types should I use for B2B?"
→ Exact for proven BOFU terms, phrase for controlled expansion, broad only with Enhanced Conversions + value-based bidding + maintained negatives, tested via experiment first.

Example 2: "Should I bid on competitor names?"
→ Yes, in a dedicated conquest campaign; expect higher CPC and lower QS, justify on pipeline, keep own-brand as negatives.


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
