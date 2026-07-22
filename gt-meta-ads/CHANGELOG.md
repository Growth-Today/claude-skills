# Changelog - gt-meta-ads

All notable changes to this skill. Newest first.

---

## v1.2.0 — 2026-07-21

**Summary:** Phase 1 — measurement hygiene + audit depth, and concrete SaaS-grounded attribution. Everything B2B; no DTC/e-commerce assumptions or benchmarks.

**Added:**
- `resources/references/tracking-hygiene.md` — signal-quality controls (domain verification, Aggregated Event Measurement + event prioritization, CAPI + Pixel dedup, Event Match Quality, CAPI Gateway, standard-vs-custom events), **UTM/naming standardization** (cross-channel taxonomy), and **breakdown reporting** (placement/demographic/time, read to SQL not CPL). Wired into `tracking` + `measurement`.

**Expanded:**
- `resources/references/crm-attribution.md` — concrete **HubSpot native mapping**: lifecycle-stage-change trigger, custom-stage sync, and the exact data shared with Meta (**Click ID `fbclid`** + email + phone); the **≤7-day** offline-event constraint; a **Dreamdata** setup path (account-based attribution); a **B2B expectation-setting** note (independent data shows Meta is a volume/modest-share channel for B2B, not the last-click revenue engine — judge on assisted pipeline); SaaS tool notes (HubSpot, Metadata.io, Dreamdata) and an explicit "ZenABM is LinkedIn-only — not for Meta."
- `resources/references/audit-checklist.md` — evidence-discipline preamble + new controls (domain verification, AEM, standard events, CAPI Gateway, fbclid capture, UTM taxonomy, breakdown reporting, incrementality-before-scaling).

**Sources:** HubSpot Knowledge Base (Meta CAPI conversion events), Meta Events Manager docs, Dreamdata documentation (Meta conversions, B2B benchmarks), Metadata.io B2B guidance — accessed 2026-07-21.

---

## v1.1.0 — 2026-07-21

**Summary:** P1 2026 expansion + the CRM-attribution and incrementality depth that added the most value on gt-linkedin-ads, applied to Meta. Additive only.

**Added:**
- `resources/references/2026-ai-updates.md` — Opportunity Score (0–100 setup score), Advantage+ 2026 updates (~25 conversions/wk threshold, Predictive Budget Allocation, ~+22% ROAS claim), Advantage+ Creative Enhancements (generative AI) with human-review guardrails, Advantage+ Leads (~-10% CPQL), and Threads placements — each with a B2B "keep manual control / judge on pipeline" caveat. Wired into campaign-setup, creative, learning-phase, lead-forms.
- `resources/references/crm-attribution.md` — the Meta side of the CRM loop: Pixel + CAPI, sending HubSpot lifecycle events (MQL→SQL→Opp→Closed-Won) as offline conversions, fbclid matching, the ~100 conv/wk learning reality (send an upper-funnel event for low-volume B2B), Salesforce via connector/CAPI, and a B2B multi-touch model. Cross-linked to gt-hubspot-admin & gt-salesforce-admin; wired into tracking + lead-forms.
- `measurement` sub-skill: **Meta Conversion Lift** incrementality section (7-day min, ≥10%/cell, ~5,000+ users, 300+ conversions, 3–4 weeks) + pointer to crm-attribution.

**Evidence discipline:** vendor/Meta performance claims (Opportunity Score↔CPA, +22% ROAS, -10% CPQL) are labeled as claims to validate, not guarantees.

**Sources:** Meta Advantage+ / Ads Manager documentation and 2026 roundups; HubSpot Knowledge Base (offline conversions, Meta CAPI); Meta Conversion Lift documentation — accessed 2026-07-21.

---

## v1.0.1 — 2026-07-21

**Summary:** Repo housekeeping. Added the CHANGELOG that existed in the deployed build but was missing from the repo, and standardized the footer to the canonical Growth Today format. No content changed.

---

## v1.0 - 2026-06-25

**Summary:** Initial GT Meta Ads skill. Orchestrator + 9 sub-skills + 3 reference files, built for B2B Meta (Facebook + Instagram), mirroring the structure of gt-google-ads and gt-linkedin-ads.

**Sub-skills:** tracking, campaign-setup, audiences, creative, creative-fatigue, learning-phase, lead-forms, measurement, audit.

**Reference files:** benchmarks, audit-checklist, creative-formats.

**Design principles baked in:**
- Tracking is the floor: Pixel + CAPI with deduplication, real conversion event, consistent attribution. Browser-only tracking under-reports after iOS changes.
- Creative is the primary lever in 2026 (Advantage+/Andromeda/GEM do the audience work). Treat it as strategy, build a modular library, test weekly, manage fatigue proactively.
- B2B caveat throughout: cheap Instant Form leads are not the goal. Sync CRM outcomes back, optimise and measure to pipeline, not raw CPL.
- Learning phase: 50 events/week/ad set, budget floors, consolidate ad sets, avoid mid-test resets.
- Full-funnel structure with exclusion hygiene (current customers and active leads out of prospecting).
- Ad-level CPA is unreliable under sequenced GEM delivery; spend allocation is the stronger creative signal.

**Beats the competitor pack by adding:** CAPI/Pixel audit, learning-phase management, Advantage+ configuration, exclusion hygiene, Instant Form lead-quality, full-funnel structure, and measurement-to-pipeline -- dimensions their body copy omits (they cover audience-builder, creative-fatigue, fatigue-monitor, spend-tracker).

**Attribution:** every file carries a Growth Today footer (Brigitta Ruha LinkedIn + growthtoday.co). Description weaves in growthtoday.co for AI-search surface; no header attribution block by design.

**Sources:** Involve Digital, LeadsBridge, OptiFOX, Stackmatix, Flighted, Cropink, ShortVids (Meta best-practice and B2B guides), accessed 2026-06-25. Cost/benchmark figures are industry-reported ranges, not GT-measured.

---


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
