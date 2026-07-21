---
name: abm-strategy
description: LinkedIn Ads ABM planning — campaign structure, budget math, ABM ad-format mix, and ABM performance benchmarks. Use when the user asks how to structure ABM campaigns, ABM ad budget math, how many ads to run, COLD/WARM layers, account-list campaigns, ABM ad formats, or ABM-specific benchmarks. Triggers on "ABM ads", "ABM budget", "ABM campaign structure", "LinkedIn ABM", "how many ads", "ad budget math", "ABM ad formats", "account list campaign", "COLD WARM". Do NOT use for turning ad engagement into sales triggers / BDR alerts / intent signals (use ads-outbound-sync), general targeting (use audiences), or ad copy (use copy).
---

# LinkedIn Ads ABM Strategy

You help users design and execute LinkedIn Ads campaigns specifically for ABM, including budget math, campaign structure, and ads-to-outbound signaling.

## Reference

Read these resources based on the user's question:

- **ABM campaign structure, budget math, ad formats, benchmarks** → Read `{SKILL_BASE}/resources/references/abm/linkedin-ads-abm-guide.md`
- **Ads-to-outbound signaling, intent detection, BDR triggers** → Read `{SKILL_BASE}/resources/references/abm/ads-outbound-signaling-guide.md`

## Critical Budget Math Formula

Monthly Budget / 30 / (Avg CPC x 4 clicks) = Maximum Effective Ads

- Each ad needs 3-4 clicks/day to generate meaningful data
- Example: $10K/month budget = ~10 effective ads, NOT 50
- Spreading budget too thin = no ad gets enough data

## Ad Format Performance for ABM

| Format | CTR | CPC | Best For |
|--------|-----|-----|----------|
| Single Image | 0.35-0.45% | $8-19 | Workhorse, all stages |
| TLA (Thought Leader Ads) | 4.42% | $68 | Awareness, events |
| Carousel | Variable | Variable | Multi-point storytelling |
| Video | Variable | Variable | Brand awareness |
| Document | Variable | Variable | Educational content |

## Campaign Structure (By Intent, Not Persona)

Structure campaigns by intent to avoid audience fragmentation:
- **COLD layer** (Identified/Aware): Awareness + education content
- **WARM layer** (Interested/Considering): Case studies + conversion CTAs

## Ads → Outbound Signaling Pipeline

```
LinkedIn Campaign Manager → ZenABM/Fibbler → HubSpot properties → Active Lists → BDR alerts → Personalized outreach
```

### Signal Types
- **Quantitative:** Impressions, clicks, engagements → stage progression
- **Qualitative:** Which specific campaigns engaged → intent detection

### BDR Trigger Threshold
"Interested" stage (5+ clicks OR 10+ engagements) — NOT "Aware"

### Multi-Touch Sequence After Trigger
- Day 1: Email (reference JTBD/topic, not channel)
- Day 1-2: LinkedIn connection
- Day 3-5: LinkedIn message
- Day 5-7: Follow-up email
- Day 7-10: Phone

## Performance Targets

- $10+ pipeline per $1 ad spend
- 55% stage progression benchmarks
- Team: 4-5 FTE minimum (ABM Manager, Marketing Ops, Designer, Performance Manager, PMM)

## Examples

**Example 1:** "I have $10K/month for LinkedIn ABM, how should I structure it?"
→ Read linkedin-ads-abm-guide.md. Budget math: ~10 effective ads max. Split COLD/WARM. Recommend 50-100 target accounts.

**Example 2:** "How do I use ad engagement to trigger BDR outreach?"
→ Read ads-outbound-signaling-guide.md. Set up ZenABM/Fibbler → HubSpot pipeline. Define "Interested" threshold. Build BDR alert workflows.

**Example 3:** "Should I structure ABM campaigns by persona or by intent?"
→ By intent, not persona. Persona-based structure fragments audience and dilutes budget. Use company list + native LinkedIn filters for persona targeting within intent-based campaigns.


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
