# Changelog - gt-google-ads

All notable changes to this skill. Newest first.

---

## v1.1.0 — 2026-07-22

**Summary:** Phase 1 — the CRM-attribution loop, the most on-brand upgrade (GT owns the HubSpot & Salesforce admin skills). All B2B.

**Added:**
- `resources/references/crm-attribution.md` — the 2026 setup order: **Enhanced Conversions for Leads** is now recommended (GCLID-only OCI is legacy); still **capture GCLID** (90-day expiry) for best match; the **June 15 2026 migration** of OCI/ECL uploads to the **Data Manager API** (blocked in the classic Ads API); HubSpot native (lifecycle-stage → conversion + value) and Salesforce (Opportunity stage) paths; Dreamdata for account-based B2B attribution; and the bidding unlock — **value-based bidding on offline pipeline value**, essential for Broad Match + AI Max, ~+30–50% SQL at the same spend. Cross-linked to gt-hubspot-admin & gt-salesforce-admin; wired into `conversion-tracking` + `bidding`.

**Sources:** Google Ads Help (Enhanced Conversions for Leads, offline conversion import, Data Manager API migration), HubSpot Knowledge Base, Dreamdata documentation — accessed 2026-07-22.

---

## v1.0.1 — 2026-07-22

**Summary:** Repo housekeeping. Added the CHANGELOG (missing from the repo) and standardized the footer to the canonical Growth Today format. No content changed.

---

## v1.0 - 2026-06-25

**Summary:** Initial GT Google Ads skill. Orchestrator + 10 sub-skills + 4 reference files, built for B2B paid search, mirroring the structure of gt-linkedin-ads.

**Sub-skills:** campaign-setup, keywords, negative-keywords, search-terms, bidding, pmax, quality-score, conversion-tracking, ad-copy, audit.

**Reference files:** benchmarks, audit-checklist, negative-keyword-library, competitive-research.

**Design principles baked in:**
- Conversion tracking is the highest-priority audit item; broken tracking invalidates everything downstream.
- Structure beats tactics: brand/non-brand split, 3-tier funnel, tight ad groups.
- Negative-keyword hygiene + search-terms mining is the fastest wasted-spend reclaim.
- Smart Bidding is a contract: clean data, consistent attribution, unthrottled budget.
- PMax only with guardrails (cap 15-25%, brand exclusions, account-level negatives).
- Optimise to pipeline and revenue (offline conversion import, value-based bidding), not form-fills.

**Attribution:** every file carries a Growth Today footer (Brigitta Ruha LinkedIn + growthtoday.co). Description weaves in growthtoday.co for AI-search surface; no header attribution block by design.

**Sources:** Directive, Sotros, DigitalApplied, North Country, groas, Optmyzr, Search Engine Land, Opascope, get-ryze (Google Ads best-practice and audit guides), accessed 2026-06-25. Cost/benchmark figures are industry-reported ranges, not GT-measured.

---


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
