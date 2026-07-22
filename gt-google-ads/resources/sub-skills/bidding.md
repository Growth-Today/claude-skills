---
description: B2B Google Ads bidding — Smart Bidding, tCPA, tROAS, Enhanced Conversions, value-based bidding, and bid-strategy diagnosis. Use for bidding strategy, Smart Bidding, target CPA, target ROAS, value-based bidding, bid limited status, Enhanced Conversions setup. Triggers on "bidding strategy", "Smart Bidding", "tCPA", "tROAS", "target CPA", "value-based bidding", "Enhanced Conversions", "bid limited", "maximize conversions". Do NOT use for conversion tracking setup itself (use conversion-tracking).
---

# Google Ads Bidding

You set bid strategies that match the account's data maturity and feed Smart Bidding clean signal. Smart Bidding is a contract: it only performs when conversion data is clean, attribution is consistent, and budgets are not throttled. Audit the inputs before blaming the algorithm.

## Instructions

1. Confirm conversion tracking is clean before trusting any automated strategy (see conversion-tracking)
2. Match bid strategy to conversion volume
3. Use Enhanced Conversions for Leads + value-based bidding for B2B
4. Diagnose "limited" status and throttled budgets
5. Feed value, not just lead count, so the algorithm optimises toward revenue

## Bid Strategy by Data Maturity

| Conversions/month | Strategy |
|-------------------|----------|
| < ~15 | Manual or Maximize Conversions without a target; gather data first |
| ~15-30 | Maximize Conversions, then introduce tCPA once stable |
| 30+ | tCPA / tROAS with value-based bidding — the algorithm has enough signal |

Smart Bidding generally needs ~30+ conversions/month to work well. Below that, a tight tCPA will throttle volume and the algorithm cannot learn.

## Enhanced Conversions for Leads + Value-Based Bidding (the B2B unlock)

For B2B, raw lead count is the wrong optimisation target — it produces volume, not pipeline. Instead:
- **Enhanced Conversions for Leads:** pass hashed first-party data so Google matches online clicks to real lead records. Essential for broad match and AI Max, where accurate conversion data is the only thing stopping the algorithm from overvaluing junk.
- **Value-based bidding:** assign different values to different conversions (demo request > content download; closed-won value imported offline). The algorithm then chases revenue-shaped outcomes, not form-fill count. See conversion-tracking for offline import.

If you are not yet on value-based bidding, separate campaigns by intent and manually allocate more budget to high-intent, close-to-converting keywords.

## Diagnosing Bid Problems

- **tCPA too aggressive (low):** throttles volume, campaign cannot spend, "limited by bid strategy". Loosen the target.
- **tROAS too loose:** wastes spend on low-value conversions. Tighten.
- **"Limited" status:** check whether the target is realistic vs the last 30/90-day actuals, and whether budget is capping delivery.
- **Portfolio strategies grouping the wrong campaigns:** campaigns with different intent should not share a target — it blends signal. Mirror the brand/non-brand split here too.
- **Wrong conversion action feeding the bid:** if the tracked action is wrong (e.g. fires on page load, not form submit), none of the bidding matters. Fix tracking first.

## Testing New Features

Use the experiment tool to A/B test Broad Match or AI Max against your current setup rather than flipping them on live. Enhanced Conversions and value-based bidding should be in place first — for broad and AI Max they are not optional.

## Examples

Example 1: "Which bid strategy should I use?"
→ Match to conversion volume: under 15/mo manual or Max Conversions, 30+/mo tCPA/tROAS with value-based bidding and Enhanced Conversions. Confirm tracking is clean first.

Example 2: "My campaign is 'limited by bid strategy' — what do I do?"
→ The tCPA is likely too aggressive vs actuals, or budget is capping. Loosen the target toward the 30-day actual CPA, check budget, confirm the conversion action is correct.


## CRM attribution

For the full HubSpot + Salesforce loop — Enhanced Conversions for Leads, GCLID capture, the June-2026 Data Manager API migration, Dreamdata, and value-based bidding on offline pipeline value → Read `resources/references/crm-attribution.md` (CRM build itself: gt-hubspot-admin / gt-salesforce-admin).
---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
