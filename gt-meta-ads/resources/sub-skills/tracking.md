---
description: Meta Ads tracking — Pixel, Conversions API (CAPI), conversion events, attribution windows, and iOS privacy impact. Use for Pixel setup, CAPI, Conversions API, conversion events, attribution windows, iOS 14 tracking, event match quality, deduplication. Triggers on "Pixel", "CAPI", "Conversions API", "conversion event", "attribution window", "iOS tracking", "event match quality", "server-side tracking". Do NOT use for lead form setup (use lead-forms) or measurement reporting (use measurement).
---

# Meta Ads Tracking (Pixel + CAPI)

This is the foundation. Browser-only Pixel tracking under-reports badly after iOS privacy changes, and the algorithm optimises on whatever signal it receives — feed it partial data and it optimises toward the wrong people. Fix tracking before touching creative, audiences, or bidding.

## Instructions

1. Install the Pixel and the Conversions API (CAPI), with deduplication between them
2. Define the right conversion event (the real outcome, not page-load)
3. Set a consistent attribution window across campaigns
4. Sync offline / CRM conversions back for B2B lead quality
5. Only trust optimisation once event match quality is healthy

## Pixel + CAPI (both, not either)

- **Pixel** = browser-side events. Necessary but increasingly lossy (iOS, ad blockers, cookie restrictions).
- **CAPI (Conversions API)** = server-side events sent directly from your server to Meta, bypassing browser limitations. In 2026 this is not optional — it is how Meta recovers the events the browser loses.
- **Deduplication:** send the same event from both with a shared event ID so Meta does not double-count. Misconfigured dedup is a common, silent error.
- **Event match quality:** Meta scores how well your events match to users (email, phone, name passed as hashed parameters). Higher match quality = better optimisation and attribution. Pass as much hashed first-party data as you cleanly can.

## The Conversion Event Must Be Real

- Optimise toward the actual outcome (lead submitted, demo booked), not a proxy like landing-page view or "thank-you page load".
- For B2B, the form-fill is still only a proxy for pipeline. Layer offline/CRM conversions on top so Meta learns which leads became real opportunities (see measurement).

## Attribution Windows

- Default is **7-day click / 1-day view.** Fine for fast cycles.
- For longer B2B consideration, test the **28-day click** window to capture delayed conversions — but keep the window consistent across campaigns so comparisons are valid.
- iOS limits view-through data for off-platform conversions; lean on click attribution and CAPI-backed signal.

## Examples

Example 1: "Where do I start with a new Meta account?"
→ Tracking. Install Pixel + CAPI with deduplication, define the real conversion event, set a consistent attribution window, then build campaigns. Optimisation on broken tracking is wasted spend.

Example 2: "My Meta CPL looks great but the leads are junk."
→ You are optimising to a proxy (form-fill). Sync CRM outcomes back via offline conversions so Meta optimises toward qualified leads, and check event match quality is high enough for the signal to be reliable.


## CRM attribution

For sending CRM outcomes back to Meta as offline conversions (HubSpot/Salesforce, Meta CAPI, fbclid matching) → Read `resources/references/crm-attribution.md`.
## Tracking hygiene & reporting

For domain verification, Aggregated Event Measurement, CAPI Gateway, standard-vs-custom events, Event Match Quality, UTM standardization, and breakdown reporting (all B2B) → Read `resources/references/tracking-hygiene.md`.
---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
