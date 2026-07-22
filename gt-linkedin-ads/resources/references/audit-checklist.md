# LinkedIn Ads Audit — Control Catalog (GT)

A structured, B2B-opinionated audit for a LinkedIn Ads account. Work top to bottom; for each control record **observation → diagnosis → recommendation**, and mark **`n/a`** or **`unknown`** honestly when the surface doesn't apply or you lack evidence.

**Evidence discipline (read first):** don't apply a benchmark or "rule" without checking objective, geography, methodology, sample size, conversion lag, and account maturity. Betas, vendor claims, and new features are **discovery, not failures** — never score an account down for not adopting an optional feature. Pull all benchmark numbers from `benchmarks.md` (ZenABM 2026), not from memory.

---

## 1. Tracking & measurement (the floor)
1. **Insight Tag** installed, firing, deduped against CAPI.
2. **Conversions API** live; offline/pipeline events (SQL/Opp/Closed-Won) sent back — see `crm-attribution.md`.
3. **Conversion actions** defined and mapped to real business outcomes (not just "page view").
4. **Attribution window** appropriate for the sales cycle (consider 28–90d click for long B2B; view-through understood).
5. **CRM connected** for revenue attribution (HubSpot/Salesforce) — Revenue Attribution Report reviewed.
6. **Self-reported attribution** ("how did you hear about us?") on high-intent forms.

## 2. Targeting & audiences
7. **Targeting precision** — job title vs function+seniority chosen deliberately; not over-broad.
8. **Company-size / industry** filters aligned to ICP.
9. **Seniority** logic (500+ employees: exclude managers; <500: include).
10. **Exclusions** set — competitors, current customers, open opportunities, wrong seniority, login-page visitors.
11. **Audience Expansion OFF** unless intentionally broadening; **LinkedIn Audience Network** reviewed.
12. **Predictive Audiences** used correctly for scaling (not as a substitute for ICP precision); lookalikes are sunset.
13. **ABM company lists** used where relevant (≥300 matched members); persona filters layered.
14. **Frequency / impression capping** in place (e.g. cap per company/7 days).

## 3. Creative & formats
15. **Format diversity** matched to funnel stage; single-image workhorse present.
16. **Thought Leader Ads** used where the executive voice + economics fit.
17. **Video / Document** ads present where appropriate.
18. **Creative refresh cadence** healthy (watch CTR decay + frequency thresholds).
19. **A/B testing** active with proper variable isolation.
20. **Message/Conversation Ads** — used sparingly; **EU audiences excluded** (regulatory restriction).

## 4. Bidding, budget & structure
21. **Bid strategy** appropriate (manual/target-cost over uncapped max delivery where control matters).
22. **Budget sufficiency** — each ad gets enough daily spend to learn (3–4 clicks/day); no dilution.
23. **Objective alignment** — campaign objective matches the actual goal and conversion event.
24. **Account structure** — grouped sensibly (by intent for ABM), not sprawling.

## 5. Outcomes & governance
25. **Lead-quality tracking** — leads scored/qualified in CRM; optimizing to SQL/pipeline, not raw CPL.
26. **CTR / CPC vs benchmark** — compared to the *format-specific* ZenABM range, not a blended number.
27. **Demographics report** reviewed — who's actually being served vs the ICP.
28. **Wasted spend** — audience overlap, underperforming placements, stale creatives.

---

## Output format
Group findings by section. For each flagged control: what you saw, why it matters, the fix, and priority (P1 wasted-spend/tracking-broken → P3 nice-to-have). End with a prioritized fix list and any missing inputs. Keep vendor-claimed performance figures labeled as claims.

*Audit structure is GT-native; the control-catalog pattern is common across paid-media audits (incl. the MIT-licensed AgriciDaniel/claude-ads).*

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
