# Meta Tracking Hygiene & Reporting (B2B)

The difference between "CAPI installed" and "CAPI actually attributing." Load alongside `tracking.md` and the `audit`. All B2B — no DTC/commerce assumptions. **Evidence discipline:** verify each item against the live account; mark unknown/n/a where you can't see it.

---

## Signal-quality controls (fix these before trusting any number)
- **Domain verification** — verify the sending domain in Business Manager, or events/attribution get restricted.
- **Aggregated Event Measurement (AEM)** — configure and **prioritize your conversion events** (the post-iOS event set); put your true B2B conversion (lead/MQL/SQL) at the top, not "page view."
- **CAPI + Pixel with deduplication** — run both, dedupe on event ID; server-side alone loses browser context, browser-side alone loses ~15% to blockers/iOS.
- **Event Match Quality (EMQ)** — check the EMQ score per event; raise it by passing `fbclid` + hashed email/phone (see `crm-attribution.md`). Low EMQ = weak matching = bad optimization.
- **CAPI Gateway** — a lower-code server-side option when a full dev CAPI build isn't feasible; evaluate for accounts without engineering support.
- **Standard vs custom events** — map to **standard events** where possible so Meta's models understand them; reserve custom events for genuinely bespoke steps.

## UTM & naming standardization
Broken UTMs = broken CRM attribution. Enforce one taxonomy across every campaign so HubSpot/Salesforce can read source/medium/campaign consistently:
- Template: `utm_source=meta` · `utm_medium=paid_social` · `utm_campaign={funnel-stage}_{offer}` · `utm_content={ad-id}` · `utm_term={audience}`.
- Validate new URLs against the template before launch; a single misspelled campaign name pollutes a month of reporting.
- Keep it consistent with the LinkedIn/Google conventions so cross-channel reports reconcile.

## Breakdown reporting (where B2B budget leaks)
Advantage+/Andromeda hide where money goes. Pull breakdowns regularly and judge on **pipeline/lead-quality**, not CTR/CPM:
- **Placement** (Feed/Reels/Stories/Audience Network) — Audience Network is the usual money pit; exclude if it produces junk leads.
- **Demographic** (age/seniority proxy) and **time** (day/hour) — trim segments that never produce SQLs.
- Report **spend share vs conversion share**; anything spending 2x its conversion share is a leak.
- Always read breakdowns to **CRM outcome** (SQL/pipeline), never to raw Instant-Form CPL.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
