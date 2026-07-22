# CRM Attribution — HubSpot & Salesforce (Meta Ads)

How to make Meta optimize toward pipeline instead of cheap Instant-Form leads. On B2B, Meta will happily flood you with low-cost leads sales ignore; the fix is feeding **CRM outcomes back to Meta as offline conversions** and judging on pipeline. Load alongside `tracking.md` and `measurement.md`.

> GT cross-refs: for the CRM-side build (lifecycle stages, workflows, dedupe, list objects) use **gt-hubspot-admin** and **gt-salesforce-admin**. This file is the Meta-ads side.

---

## The principle
The Pixel sees form-fills; it doesn't see deals. To optimize toward revenue, send **offline conversion events** (CRM lifecycle/stage changes) back to Meta via the Conversions API, and match them to the original ad click. Meta's Advantage+ responds especially well to offline conversion signals.

## HubSpot → Meta
1. **Pixel** for initial click tracking + **Conversions API (CAPI)** server-side for resilience (iOS/cookie loss).
2. **Send HubSpot lifecycle events to Meta as offline conversions** — MQL → SQL → Opportunity → Closed-Won, with value where available. Options: HubSpot Marketing Hub **Pro/Enterprise native** Facebook integration, a **workflow → webhook → CAPI** endpoint, or a connector (e.g. Zapier) on lifecycle-stage change.
3. **Matching:** hashed email/phone **plus `fbclid`** (Facebook Click ID) — passing fbclid materially improves match rates over email alone. Capture fbclid on the form/landing page and store it on the contact.
4. **Volume reality:** Meta wants ~**100 conversions/week/campaign** for stable learning — for low-volume B2B, send an **upper-funnel** offline event (e.g. MQL/qualified-lead) to feed the algorithm, and track SQL/Closed-Won for reporting.

## Salesforce → Meta
No turnkey native path — use the **CAPI** via a connector/CDP or scheduled offline-event upload keyed on fbclid/email; fire the event on Opportunity stage change with amount. Model account-level influence in Salesforce (Campaign Influence) for reporting. Build details → **gt-salesforce-admin**.

## Attribution model — B2B default
Meta's default 7-day-click / 1-day-view under-credits long B2B cycles. Report **view-through separately**, consider longer windows, and treat Meta as an **assist** channel in a multi-touch / position-based model rather than judging it on last-click Instant-Form CPL.

## Concrete HubSpot property mapping (native integration)
When you use HubSpot's native Meta integration (create/sync ad conversion events via Meta CAPI):
- **Event trigger = lifecycle-stage change.** Tick the HubSpot lifecycle stages that should fire a Meta event; you can also sync **custom lifecycle stages**.
- **Data shared with Meta (for matching):** **Click ID (`fbclid`)** — auto-captured on the contact when they click a Meta ad — plus **email** and **phone**. Capture and persist `fbclid` on the form/contact; it lifts match rates far above email alone.
- **Constraint:** Meta accepts offline events **≤7 days old** — send the conversion promptly on stage change, don't batch weekly.

## Doing it via Dreamdata (B2B attribution SaaS)
Dreamdata uses **account-based** attribution. Setup: Meta Events Manager → **Connect Data → Offline**; then in Dreamdata **Activation Hub → Syncs → Meta Conversions**, connect the account, pick the **CRM stage** to treat as the conversion + the Ad Account/Dataset. Don't directly compare Dreamdata vs Meta numbers (different attribution models).

## B2B expectation-setting (important)
Independent B2B attribution data (Dreamdata) puts Meta's attributed ROAS well below LinkedIn's for B2B — Meta is a **volume / modest-share** channel, not the primary last-click revenue engine. Set that expectation with stakeholders: run Meta for reach + retargeting + cheap mid-funnel, judge it on **assisted pipeline**, and don't hold it to LinkedIn's last-touch revenue.

## Tooling (SaaS, B2B)
- **HubSpot** native Meta integration — lifecycle → offline conversions (above).
- **Metadata.io** — B2B paid-social automation (MetaMatch identity graph for B2B targeting on Meta) + pipeline attribution.
- **Dreamdata** — account-based multi-touch attribution + Meta offline sync.
- **Note:** ZenABM is **LinkedIn-focused (no Meta ad tracking)** — don't reach for it here; it's the LinkedIn-ads tool.

## Reality check
- **~7–14 days** to wire CAPI + offline events; **~2–4 weeks** for the algorithm to re-optimize on pipeline signals.
- **Evidence discipline:** offline-conversion lift figures are vendor-/study-reported — validate against your own.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
