# Measurement & Attribution

## Core Equation
**Reach x Relevance x Engagement = Pipeline Uplift**

## Three Forces Framework

### Force 1: Reach Quality
Not raw impressions — visibility among buying committees.

**Metrics**:
- Ad impressions filtered by target audience
- CPM within segments
- Named account penetration
- Profile views from relevant titles/industries
- Newsletter subscriber quality

Key: "50,000 impressions from your ideal customers > 500,000 from people who'll never buy."

### Force 2: Relevance Signals
Whether audiences engage rather than scroll past.

**Metrics**:
- Dwell time
- Video completion rates
- Message ad open rates
- Click-through rates
- Follower growth among targets
- Engagement quality (meaningful comments vs generic reactions)

### Force 3: Engagement Depth
Meaningful interactions moving attention into action.

**Metrics**:
- Qualified CTR
- Cost-per-click within segments
- Landing page conversion rates
- Messaging response rates
- Attributed website visits

## Business Outcome Metrics
- **Pipeline attribution**: Deals traced to LinkedIn touchpoints
- **Influenced revenue**: Total opportunity value involving LinkedIn
- **Deal velocity**: Speed of LinkedIn-influenced deal closure
- **Customer acquisition cost**: LinkedIn's impact on CAC
- **Brand search uplift**: Direct company name search increases
- **Sales conversation quality**: Lead-to-conversion rates

## Attribution Challenges
- Only **20-30%** of LinkedIn-driven conversions are captured
- **90%+** impact occurs without clickthrough (invisible engagement)
- **83%** impressions on mobile, **72%** conversions on desktop (cross-device gap)
- **6-10** decision-makers per deal across channels
- Cookie deprecation eliminates third-party tracking
- Email mismatch (personal LinkedIn vs work conversion emails)

## Attribution Stack (Recommended Setup)

### Technical Foundation
1. **LinkedIn Insight Tag** — demographics, retargeting, conversion tracking
2. **LinkedIn Conversion API** — server-side, bypasses ad blockers
3. **CRM integration** (HubSpot, Salesforce) for revenue attribution
4. **UTM parameters** with LinkedIn dynamic UTM feature

### Self-Reported Attribution
- Add **"How did you hear about us?"** field on high-intent forms
- Track responses in CRM
- Compare with platform-reported data

### Advanced Tools
- Multi-touch attribution tools (e.g., Fibbler)
- View-through windows: 7-60 day lookback for B2B
- Companies Tab monitoring for account engagement
- Conversion lift analysis correlating campaign periods with pipeline increases

### Duplicate Conversion Events
Set up 90-day click/view windows to capture:
- Direct last-touch conversions
- Blended pipeline impact
- Compare multiple data sources for complete picture

## 2026 Deep Dive — Conversions API (CAPI) & Revenue Attribution Report

The two updates that most change LinkedIn measurement in 2025–2026. If you set up nothing else new, set up these two.

### Conversions API (CAPI) — server-side conversions

CAPI securely connects **first-party online AND offline data** to LinkedIn — website actions, **phone sales, and in-person/event conversions** — server-side, so it survives ad blockers and cookie loss. It integrates with **Salesforce, Google Tag Manager, Tealium, and Adobe**, and complements (does not replace) the Insight Tag — run both for overlap and resilience.

**Why it matters (reported results):** CAPI users see roughly **20% lower CPA and ~31% more attributed conversions** vs non-integrated accounts; some report **~39% lower cost per qualified lead**. Dreamdata's 2026 benchmark finds **~75% of LinkedIn advertisers now use CAPI** — it is becoming table stakes, not an edge.

**Setup priority:** Insight Tag → CAPI (via GTM or a CRM/CDP connector) → map offline conversions (closed-won, SQLs) back to LinkedIn so bidding optimizes toward revenue, not form-fills.

### Revenue Attribution Report (RAR) — CRM revenue, not clicks

RAR **connects your CRM to LinkedIn campaigns** and reports **revenue impact at the company level**, with review periods extended up to **365 days** — matching real B2B sales cycles instead of a 30-day click window. Combined with **real-time CRM data now shown inside Campaign Manager (since June 2025)**, you can optimize on pipeline and revenue directly.

**The engagement insight:** Dreamdata 2026 found that **including paid engagement data (not just clicks/conversions) attributes ~7.7x more revenue** — i.e. LinkedIn's brand/engagement effect is real but invisible to click-only tracking. This is the data-backed version of the long-standing "CTR does not predict pipeline" caveat. LinkedIn's own team reported a **150x increase in attribution credit for upper/mid-funnel** campaigns after adopting these tools.

**Implication for optimization:** stop killing upper-funnel campaigns on CTR/CPL alone. Judge them on company-level pipeline over a 90–365 day window via RAR.

## Measurement Timeline
- Allow **2-4 weeks** minimum for meaningful data
- Track long-term pipeline influence over **3-6 months**
- **Measure quarterly, not weekly** — cumulative effects matter
- Compare pipe-to-spend ratio trends over time

## Critical Mistakes
1. Treating all engagement equally (ICP comments >> generic reactions)
2. Ignoring cumulative effects
3. Measuring LinkedIn in isolation
4. Focusing on short-term results in a long-cycle B2B environment


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
