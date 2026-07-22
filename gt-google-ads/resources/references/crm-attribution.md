# CRM Attribution — HubSpot & Salesforce (Google Ads, B2B)

How to make Google optimize toward pipeline instead of cheap form-fills. If Google is optimizing to form submissions, it is not optimizing to pipeline — offline conversions close that gap. Load alongside `conversion-tracking.md` and `bidding.md`.

> GT cross-refs: for the CRM-side build (lifecycle stages, workflows, dedupe, fields) use **gt-hubspot-admin** and **gt-salesforce-admin**. This file is the Google-ads side.

---

## The 2026 setup order (important — this changed)
1. **Enhanced Conversions for Leads (ECL) is the recommended path.** GCLID-only Offline Conversion Import (OCI) is now Google's **legacy** route. ECL sends **hashed first-party form data** (email/phone) privately, matched to signed-in Google accounts. When the GCLID survives the journey Google uses it; when it doesn't, the hashed email can still match. If starting from scratch, start with ECL.
2. **Still capture GCLID.** Google appends **GCLID** to the landing URL; capture it on the form and store it on the CRM record. It **expires after 90 days** — push the conversion within the window. GCLID + hashed data together give the best match.
3. **API migration (must-flag):** from **June 15 2026**, OCI and ECL uploads migrate to the **Google Ads Data Manager API** and are **blocked in the classic Google Ads API**. Any custom upload pipeline must move to Data Manager; native CRM integrations handle this for you.

## HubSpot → Google
- **Native integration** with **Enhanced Conversions for Leads** support. Fire a conversion on **lifecycle-stage change** (Lead → MQL → SQL → Opportunity → Closed-Won) with a **value**, so bidding learns which clicks become pipeline.
- Capture GCLID on the form (hidden field) → contact property; pass it (plus hashed email) back to Google.

## Salesforce → Google
- Direct Google Ads connectivity / OCI, or via Data Manager / a connector. Fire on **Opportunity stage change** with amount. For account-level B2B attribution, model influence in Salesforce (Campaign Influence). Build details → **gt-salesforce-admin**.
- **Dreamdata** (B2B account-based attribution) has a documented Google offline-conversion path — useful when you want multi-touch, account-level credit rather than last-click.

## The bidding unlock (this is the point)
Feed offline conversions, then run **value-based bidding (tROAS / Maximize Conversion Value)** on the **pipeline value**, not on form-fills. This is the **B2B gold standard**, and it's **essential** for Broad Match and **AI Max for Search** — without clean offline signal they optimize to junk leads. Reported effect of offline-conversion tracking: **+30–50% SQL at the same spend.**

## Reality & discipline
- ~7–14 days to wire (native integrations faster); ~2–4 weeks for bidding to re-learn on pipeline signals.
- Vendor/study figures (+30–50% SQL, "16% CPC per QS point," etc.) are **claims to validate**, not guarantees.
- **B2B SaaS tooling (named):** HubSpot, Salesforce, Dreamdata. (No competitor agencies.)

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
