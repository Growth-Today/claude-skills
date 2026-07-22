# Changelog - gt-google-ads

All notable changes to this skill. Newest first.

---

## v2.1.1 — 2026-07-22

**Summary:** Housekeeping — removed named third-party agencies from the v1.0 baseline "Sources" line (QA sweep), leaving official + neutral references only. Consistent with the competitor policy (name only SaaS products / official docs, never outside agencies; never link to competitor sites). No strategy content changed.

---

## v2.1.0 — 2026-07-22

**Summary:** Phase 4 — a live-ops (operational) tier, so the skill can operate a live account, not just advise. Read-only by default; writes are gated. All B2B.

**Added:**
- `.claude/skills/live-ops/gt-SKILL.md` — the operational sub-skill: read-only live analysis via the Google Ads API/MCP, PPC math/forecasting, and guarded writes. Read-only is the default; connectors need explicit write scope.
- `resources/references/gaql-queries.md` — B2B GAQL query templates (campaign performance, wasted-spend search terms, keyword+Quality Score, pipeline value, impression share, device/geo; values in micros).
- `resources/references/ppc-math.md` — B2B math/forecasting: cost-per-SQL, break-even CPL/CPC from close rate + ACV, value-based-bidding values, budget projections, impression-share opportunity, Smart Bidding data floor.
- `resources/references/safe-write-cep.md` — the **Confirm → Execute → Post-check** protocol for any account mutation; read-only/draft by default, one scoped change per confirmation, rollback stated.

**Positioning:** analysis reads to CRM outcome (SQL/pipeline); forecasts are estimates, not promises; default posture is read-only.

**Attribution:** live-ops patterns acknowledged from itallstartedwithaidea/google-ads-skills (Apache-2.0), reimplemented GT-native. Sub-skills: 10 → 11.

---

## v2.0.0 — 2026-07-22

**Summary:** MAJOR restructure into a master router + 10 sub-skills (multi-sub-skill layout), matching gt-linkedin-ads and gt-meta-ads. Progressive disclosure; no strategy content removed. Triad parity.

**Changed:**
- `SKILL.md` is now a **master router**: dynamic `SKILL_BASE` Setup block (Glob for `**/gt-google-ads/SKILL.md`), intent → sub-skill routing table, shared-reference table, Key Benchmarks, and the B2B guardrail up top.
- The 10 sub-skills moved from `resources/sub-skills/*.md` to `.claude/skills/<name>/gt-SKILL.md`: campaign-setup, keywords, negative-keywords, search-terms, bidding, pmax, quality-score, conversion-tracking, ad-copy, audit. Each now carries a `name:` (google-ads-*) it previously lacked.
- Normalized all sub-skill resource references to `{SKILL_BASE}/resources/references/...`.

**Validation:** 10 sub-skills referenced exactly once; every `{SKILL_BASE}` reference resolves; all names lowercase-hyphen ≤64; descriptions ≤1024; footers on every file; `.claude/` present in git; 0 competitor references.

---

## v1.2.0 — 2026-07-22

**Summary:** Phase 2 — 2026 AI bidding, EU compliance, and the B2B guardrail. All B2B; no e-commerce/DTC.

**Added:**
- `resources/references/ai-bidding-2026.md` — **Journey-Aware Bidding** (Search + tCPA learns from the full CRM lead-to-sale journey; needs offline conversions pushed tighter than weekly), **Smart Bidding Exploration** (+27% unique converting users on Search; demand-led pacing), and **AI Max** guidance (only safe on clean offline signal + value-based bidding). Wired into `bidding`.
- `resources/references/consent-mode-v2.md` — required in the EU/EEA since Mar 2024 (Google-certified CMP); Basic vs Advanced (run Advanced in Europe or forfeit paid conversions); without it conversions unreported + audiences unusable. Wired into `conversion-tracking`.
- `resources/references/b2b-guardrail.md` — what does NOT transfer from e-commerce Google Ads advice: judge on pipeline/cost-per-SQL not ROAS; no Shopping/retail-PMax/feed; respect the intent ladder; Broad Match/AI Max require offline conversions; protect low B2B conversion volume; benchmarks aren't shared. Referenced from the orchestrator up top.

**Changed:**
- `resources/references/audit-checklist.md` — evidence-discipline preamble + new controls: GCLID capture, Data Manager API migration, Consent Mode v2, value-based bidding on offline data, Journey-Aware Bidding readiness, Broad Match/AI Max gating, Auction Insights + device/geo breakdowns.

**Sources:** Google Ads Help / Google blog (Journey-Aware Bidding, Smart Bidding Exploration, Consent Mode v2), certified-CMP docs — accessed 2026-07-22.

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

**Sources:** Google Ads Help + public Google Ads best-practice and PPC-tooling documentation (industry-reported ranges, not GT-measured), accessed 2026-06-25.

---


---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
