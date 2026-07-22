---
name: google-ads-negative-keywords
description: B2B Google Ads negative keyword strategy, the four exclusion buckets, match-type strategy for negatives, n-gram mining, and over-negation risk. Use for negative keywords, exclusion lists, wasted spend from bad queries, negative match types, shared negative lists. Triggers on "negative keywords", "exclusion list", "block keywords", "negative match type", "shared negatives", "n-gram", "over-negation". Do NOT use for the search terms report process itself (use search-terms).
---

# Google Ads Negative Keywords

Negative keyword hygiene is the single most underrated lever in paid search and the fastest reclaim a B2B account has. It is the cheapest hour of work in paid media and the most consistently neglected.

## Instructions

1. Build a pre-launch negative list before any new campaign spends a dollar
2. Maintain account-level shared lists + campaign-level negatives
3. Choose negative match types deliberately
4. Mine the search terms report on a weekly cadence (see search-terms)
5. Audit for over-negation quarterly — stale negatives block good traffic

## The Four Buckets (account-level shared lists)

1. **Employment** — jobs, careers, salary, hiring, internship. The largest single source of wasted B2B spend. Add as phrase-match negatives at the account level unless you are actively recruiting.
2. **Price / low-intent** — free, cheap, DIY, discount (for premium brands). Be careful with broad-match negatives here.
3. **DIY / education** — how to, tutorial, examples, PDF, template, course, "what is".
4. **Competitor brand terms** — exclude from non-brand campaigns unless you are running a deliberate conquest campaign.

**Industry layer on top:** add vertical-specific exclusions. A B2B SaaS should negate "review" and "vs" until brand-search campaigns warrant them; a services firm should negate "student", "pro bono", etc. See `negative-keyword-library.md` for the 200+ categorised list.

## Negative Match Types (use all three intentionally)

| Negative match | Use for |
|----------------|---------|
| Negative exact `[term]` | Strict removal of one long-tail variation without nuking similar queries. |
| Negative phrase `"term"` | Groups of related queries: competitor names, question phrases, intent modifiers like "tutorial", "review". Phrase-match brand exclusions catch variations better than exact. |
| Negative broad `term` | Words to eliminate entirely regardless of query construction: "cheap", "free", "jobs". |

**Critical caution — over-negation kills volume.** Adding "free" as a broad negative also blocks "free trial", "free consultation", "free demo". Adding "services" when you sell services is catastrophic. Add negatives at the narrowest level that prevents the waste without blocking relevant traffic.

## Structure: shared vs campaign-level

- **Universal negatives** (jobs, free-intent modifiers) → account-level shared lists applied across all Search campaigns and the Search inventory in PMax.
- **Campaign / ad-group negatives** → tailored per campaign. A term irrelevant in the brand campaign may be the whole point of a conquest campaign.
- Apply shared lists to **new launches** — easy to forget, and a fresh campaign with no negatives bleeds during the learning phase.

## N-Gram Mining (the advanced move)

Pull the search terms report and break queries into n-grams (single words and word pairs). Cross-check each n-gram's spend against conversions to find waste patterns a query-by-query scan misses, and to catch negatives that are accidentally blocking converting queries. Always require human review before adding — automated negative suggestions over-negate.

## Maintenance Cadence

- Active accounts ($10k+/mo): mine search terms weekly.
- Lower spend: biweekly. Less than monthly and waste compounds before anyone catches it.
- Quarterly: a match-type sweep on the negatives serving against the most queries, to catch stale exclusions throttling volume.

## Examples

Example 1: "How do I cut wasted spend on Google Ads?"
→ Build the four buckets as account-level shared lists, mine the search terms report weekly for $50+ spend / zero-conversion queries, add at the narrowest match level, audit for over-negation quarterly.

Example 2: "Should 'free' be a broad negative?"
→ Careful — broad "free" blocks "free trial", "free demo", "free consultation". Use phrase/exact for the specific junk queries instead.


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
