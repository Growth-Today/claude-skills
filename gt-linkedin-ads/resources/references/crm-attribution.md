# CRM Attribution — HubSpot & Salesforce (LinkedIn Ads)

How to close the loop between LinkedIn Ads and revenue in the two CRMs GT runs. This is where LinkedIn stops being a "cost per lead" channel and becomes a "cost per pipeline / closed-won" channel. Load alongside `measurement-attribution.md` (CAPI + Revenue Attribution Report deep dive).

> GT cross-refs: for the CRM-side build (lifecycle stages, workflows, deal pipelines, list/audience objects, dedupe) use **gt-hubspot-admin** and **gt-salesforce-admin**. This file covers the LinkedIn-ads side of the connection.

---

## The principle

LinkedIn's in-platform reporting sees clicks and form-fills, not deals. To optimize toward revenue you must feed **offline conversions** (CRM stage changes) back to LinkedIn, and read **company-level, long-window** attribution — because B2B deals close over months, across a buying committee, mostly without a click (view-through). Optimizing on CPL alone produces cheap leads sales ignore.

---

## HubSpot — the 3-layer connection

1. **Native HubSpot ↔ LinkedIn integration** — connect the ad account under *Marketing → Ads*. Syncs Lead Gen Form submissions to contacts automatically and shows ad spend/leads on the HubSpot ads dashboard. New leads sync within ~2 hours.
2. **Conversions API (CAPI)** — server-to-server. Push **pipeline events back to LinkedIn** (SQL, Opportunity, Closed-Won) so LinkedIn's bidding optimizes toward revenue, not form-fills. Survives ad blockers and cookie loss.
3. **Insight Tag** — website behavior + retargeting + web conversions.

**Offline-conversion loop (the money step):** build a HubSpot workflow that fires a LinkedIn offline-conversion event on **lifecycle-stage change** for contacts/companies sourced from LinkedIn — with a deal value where available. Map: `MQL → SQL → Opportunity → Closed-Won` to distinct LinkedIn conversion events. Reported effect of sending pipeline-stage offline conversions: **+30–50% SQL volume at the same spend**, because the algorithm learns which clicks become real pipeline.

**Reporting:** use HubSpot's attribution reporting (multi-touch / W-shaped) to see LinkedIn's assist role, and reconcile against LinkedIn's own Revenue Attribution Report.

**Audience sync (bonus):** sync HubSpot lists as LinkedIn Matched Audiences (Settings → Marketing → Ads → Audience Sync); refreshes ~every 24h. Great for ABM COLD/WARM movement and suppression (exclude current customers / open opportunities).

---

## Salesforce — offline conversions + Campaign Influence

Salesforce has **no native LinkedIn ad-engagement integration**, so you wire it up deliberately:

- **Offline conversions** — push closed-loop conversions to LinkedIn via the **CAPI Salesforce connector**, a data connector (Zapier/CDP), or scheduled offline-conversion file upload keyed on the LinkedIn click/first-party identifiers.
- **Campaign Influence** — model **account-level** attribution: aggregate every touchpoint across contacts at one account and attribute pipeline/revenue at the account, not the lead. Configure Campaign Influence (and, if used, Salesforce Campaigns for LinkedIn) so multi-contact buying committees are credited correctly.
- **Opportunity stage → LinkedIn event** — mirror the HubSpot loop: when an Opportunity from a LinkedIn-sourced account advances or closes-won, send the corresponding offline conversion + amount back to LinkedIn.

For the Salesforce build itself (Campaign Influence setup, stages, flows, dedupe), route to **gt-salesforce-admin**.

---

## Attribution model — B2B default

Start with **position-based / U-shaped**: 40% first touch (demand creation — often LinkedIn), 40% last touch before SQL (demand capture — often Search), 20% across the middle. Move to full **multi-touch** for long cycles. Avoid last-click for LinkedIn — it systematically under-credits an upper-funnel channel whose impact is mostly view-through.

---

## Implementation reality (set client expectations)

- **~7–14 days** to wire the CAPI layer (developer support for the server-to-server piece).
- **~4–8 weeks** for LinkedIn's algorithm to learn from the new pipeline signals before optimization shifts.
- **Evidence discipline:** the "+30–50% SQL", CAPI "−20% CPA / +31% conversions", and similar figures are **vendor-/study-reported** — validate against your own before/after, don't promise them as guarantees.

---

*Sources: LinkedIn Marketing Solutions Help (Conversions API, Revenue Attribution Report) and HubSpot Knowledge Base (ads setup, audience sync, offline conversions) — official docs — plus public B2B attribution best-practice guidance, accessed 2026-07-21.*

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
