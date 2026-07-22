# Changelog - gt-meta-ads

All notable changes to this skill. Newest first.

---

## v2.0.1 — 2026-07-22

**Summary:** Housekeeping — removed named third-party agencies from the v1.0 baseline "Sources" line (QA sweep), leaving official + neutral references only. Consistent with the competitor policy (name only SaaS products / official docs, never outside agencies; never link to competitor sites). No strategy content changed.

---

## v2.0.0 — 2026-07-22

**Summary:** MAJOR restructure into a master router + 9 sub-skills (multi-sub-skill layout), matching gt-linkedin-ads and the CRM admin skills. Progressive disclosure; no strategy content removed. Triad parity.

**Changed:**
- `SKILL.md` is now a **master router**: dynamic `SKILL_BASE` Setup block (Glob for `**/gt-meta-ads/SKILL.md`), intent → sub-skill routing table, shared-reference table, Key Benchmarks, and the B2B guardrail up top.
- The 9 sub-skills moved from `resources/sub-skills/*.md` to `.claude/skills/<name>/gt-SKILL.md`: tracking, campaign-setup, audiences, creative, creative-fatigue, learning-phase, lead-forms, measurement, audit. Each now carries a `name:` (meta-ads-*) it previously lacked.
- Normalized all sub-skill resource references to `{SKILL_BASE}/resources/references/...`.
- Removed the stray "(vs $8-20 B2C)" comparison from the CPM benchmark — benchmarks are B2B-only.

**Validation:** 9 sub-skills referenced exactly once; every `{SKILL_BASE}` reference resolves; all names lowercase-hyphen ≤64; descriptions ≤1024; footers on every file; `.claude/` present in git; 0 competitor references.

---

## v1.3.0 — 2026-07-22

**Summary:** Phase 2 — the B2B guardrail. Codifies that generic/DTC Meta advice, tactics, and benchmarks do not transfer to B2B, so the skill (and anyone reading it) filters them out. Pure positioning + guardrail; no DTC content added.

**Added:**
- `resources/references/b2b-vs-b2c-guardrail.md` — "What does NOT transfer from generic (DTC) Meta advice": judge on pipeline/SQL not ROAS; cheap leads are the trap; no catalog/Advantage+ Shopping/commerce; B2B frequency & creative economics differ; first-party + offline mandatory; interest-stacking/day-parting/lookalike-refresh are DTC hypotheses not rules; benchmarks are not shared. Plus the rule of thumb: if the success metric is ROAS/AOV/purchases, it's DTC — adapt to pipeline/SQL or drop.
- Names B2B SaaS tooling (HubSpot, Dreamdata, Metadata.io); notes ZenABM is LinkedIn-only.

**Wired:** referenced from the orchestrator's "B2B reality" note and from campaign-setup, audiences, creative, measurement.

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

**Sources:** Meta / HubSpot official documentation + public Meta best-practice and B2B guidance (industry-reported ranges, not GT-measured), accessed 2026-06-25.

---


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
