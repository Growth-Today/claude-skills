---
description: B2B Google Ads conversion tracking — the highest priority audit, offline conversion import, Enhanced Conversions for Leads, and tracking the right action. Use for conversion tracking, offline conversion import, Enhanced Conversions, tracking setup, tracking the wrong action, page-load vs form-submit, attribution. Triggers on "conversion tracking", "offline conversion import", "Enhanced Conversions", "tracking setup", "tracking broken", "attribution model", "data-driven attribution", "track revenue not leads". Do NOT use for bid strategy mechanics (use bidding).
---

# Google Ads Conversion Tracking

This is the first thing to check in any account and the highest-priority fix. If tracking is wrong, every bid, every negative, every optimisation decision downstream is made on garbage data. Most B2B companies track the wrong thing.

## Instructions

1. Verify the conversion action is the real outcome, not a proxy
2. Confirm data-driven attribution is active
3. Set up Enhanced Conversions for Leads (hashed first-party data)
4. Import offline conversions so the algorithm optimises to pipeline, not form-fills
5. Only after tracking is clean, trust any automated bidding

## Why Most B2B Tracking Is Wrong

- **Tracking a proxy, not the outcome.** Counting all form-fills (including spam, students, job seekers) optimises toward volume, not pipeline. Worse: accounts that fire the conversion on **page load** instead of form submit are optimising toward "someone landed on the thank-you URL", which is meaningless.
- **No offline data.** The real conversion in B2B happens off-platform: SQL, opportunity, closed-won. If Google only sees the form-fill, it optimises for cheap leads, not revenue.
- **Inconsistent attribution.** Comparing last-click history to data-driven present creates false reads.

## The Fix (in order)

1. **Audit the conversion action.** Confirm it fires on the real action (form submit / demo booked), not page load. If tracking is broken, fix this before touching anything else — it is the highest-priority item in any audit.
2. **Enhanced Conversions for Leads.** Pass hashed first-party data (email) so Google matches ad clicks to lead records even after cookie loss. Essential for broad match and AI Max.
3. **Offline Conversion Import.** Push CRM stage changes back to Google: lead → MQL → SQL → opportunity → closed-won, ideally with value. Now the algorithm sees which clicks became revenue, not just which became form-fills. This is the single biggest lever for B2B lead-gen accounts.
4. **Value-based bidding** on top, so different conversions carry different value (see bidding).
5. **Data-driven attribution** as the default; be careful comparing to last-click history. Review assisted conversions before cutting "low-performing" upper-funnel campaigns that actually assist.

## The Payoff

Once offline conversions flow, you can finally answer the only question that matters: which keywords, queries, and campaigns produce **pipeline and revenue**, not just leads. Platform-reported ROAS stops drifting away from P&L ROAS, and Smart Bidding optimises toward deals.

## Examples

Example 1: "Where do I start auditing a B2B Google Ads account?"
→ Conversion tracking, always. Verify the action is real (not page-load), confirm attribution, then layer Enhanced Conversions for Leads and offline import before trusting any bid strategy.

Example 2: "Google says my CPL is great but sales says the leads are junk."
→ Classic proxy-tracking problem. You are optimising to form-fills, not pipeline. Set up offline conversion import (lead → SQL → closed-won with value) so the algorithm chases revenue-shaped outcomes, and add value-based bidding.


## CRM attribution

For the full HubSpot + Salesforce loop — Enhanced Conversions for Leads, GCLID capture, the June-2026 Data Manager API migration, Dreamdata, and value-based bidding on offline pipeline value → Read `resources/references/crm-attribution.md` (CRM build itself: gt-hubspot-admin / gt-salesforce-admin).
---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
