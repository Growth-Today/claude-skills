# PPC Math & Forecasting (B2B)

Pure-math helpers — no API needed, works with numbers the user provides. Frame everything to **B2B economics** (close rate, ACV, pipeline), not e-commerce ROAS.

---

## Core B2B formulas
- **CPL** = Cost ÷ Leads
- **Cost per SQL** = Cost ÷ SQLs  (the real efficiency metric)
- **Cost per Opp / per Closed-Won** = Cost ÷ (Opps | Won)
- **Lead→SQL rate**, **SQL→Won rate** — pull from the CRM; these drive everything below.

## Break-even math (what you can afford to pay)
```
Max cost per SQL      = Gross-margin-per-deal × (target CAC payback fraction)
Break-even CPL        = Max cost per SQL × (Lead→SQL rate)
Max CPC               = Break-even CPL × (Click→Lead conversion rate)
```
Example: ACV $12,000, 70% gross margin, allow 30% of GP to acquisition → max cost/deal ≈ $2,520. If SQL→Won = 25% → max cost/SQL ≈ $630. If Lead→SQL = 20% → break-even CPL ≈ $126. If landing CVR = 5% → max CPC ≈ $6.30.

## Value for value-based bidding
Assign each CRM stage a value = **expected pipeline value** (deal value × stage→won probability). Feed these as conversion values (see `crm-attribution.md`) so tROAS/Max-Conv-Value bids to pipeline, not form-fills.

## Forecasting & opportunity
- **Budget → conversions:** Budget ÷ CPA = expected conversions (hold CVR/CPC constant; state assumptions).
- **Impression-share opportunity:** extra clicks ≈ (impressions ÷ current IS) × (target IS − current IS) × CTR. Split lost-IS into budget vs rank before promising lift.
- **Smart Bidding data-floor:** ~30+ conversions / 30 days per campaign (or portfolio) for stable learning — below that, consolidate or use a higher-volume signal (micro-conversion / Journey-Aware Bidding).

**Discipline:** every projection states its assumptions and flags they're estimates, not guarantees. Never present a forecast as a promise.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
