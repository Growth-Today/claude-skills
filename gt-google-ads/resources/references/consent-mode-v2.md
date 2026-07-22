# Consent Mode v2 (EU/EEA compliance) — Google Ads

If a client runs ads in the EU/EEA, this is not optional. Load when the account targets Europe.

---

## What it is / why it's required
Since **March 2024**, Google requires advertisers serving ads in the **EEA** to implement **Consent Mode v2** via a **Google-certified CMP** (consent management platform). It's required for **Google Ads and GA4** in the EU/EEA. Without it: **conversions stop being reported and Google Ads audiences become unusable** — you keep paying but lose measurement and remarketing.

## Basic vs Advanced
- **Basic** — Google tags don't load at all until consent; on refusal, **total signal loss**.
- **Advanced** — tags load on page open with default-denied state, send **cookieless pings**, then adjust on the user's choice; Google can **model** some of the un-consented conversions.

**GT recommendation:** if you spend on Google Ads in Europe, run **Advanced** — Basic quietly forfeits conversions you're already paying for. Advanced recovers partial signal via modeling.

## Checklist
- Google-certified CMP installed and passing consent signals.
- Consent Mode v2 in **Advanced** for EU/EEA ad spend.
- Verify in Google Ads/GA4 that consented + modeled conversions are flowing.
- Coordinate with the CRM/offline-conversion setup (`crm-attribution.md`) so consented offline events still upload.

Non-EU accounts: not mandated, but first-party consent hygiene still helps measurement durability.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
