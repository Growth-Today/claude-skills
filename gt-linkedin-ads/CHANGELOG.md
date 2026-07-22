# Changelog — gt-linkedin-ads

All notable changes to this skill. Newest first.

---

## v2.2.2 — 2026-07-22

**Summary:** QA sweep — removed competitor-agency references and traffic-driving blog links from the knowledge base. No strategy content changed.

**Changed:**
- `resources/linkedin-ads-knowledge-base.md`: removed a header that credited competitor agencies + their blog URLs, and deleted the "Section 10 — Sources & References" list of competitor-agency blog articles and courses. Replaced the header with a neutral GT + official-LinkedIn-docs provenance line.
- `CHANGELOG.md`: trimmed a bare vendor blog URL to the report name (ZenABM kept as a named SaaS source, no link).

**Policy:** name only SaaS products / official docs, never competitor agencies; never link out to competitor sites. Now 0 agency references and 0 external non-GT/official links.

---

## v2.2.1 — 2026-07-22

**Summary:** Housekeeping — removed named third-party agencies from two reference "Sources" lines (`predictive-audiences.md`, `accelerate-ai-campaigns.md`), leaving official docs + neutral "public best-practice guidance." Consistent with the competitor policy (name only SaaS products, never outside agencies). No strategy content changed.

---

## v2.2.0 — 2026-07-21

**Summary:** P2 coverage additions from the review — rigorous measurement, EU messaging compliance, and sharper ABM routing. No restructure.

**Added / expanded:**
- `measurement-attribution.md`: **Incrementality & Lift Testing** (native Brand Lift with its budget minimums + settle window; DIY conversion incrementality via holdout / geo-lift — LinkedIn has no robust self-serve conversion-lift) and **View-Through Conversions** (window guidance, report VTC separately from CTC, weight below clicks, sanity-check with incrementality). This is the causal answer to "CTR ≠ pipeline."
- `ad-formats.md`: **EU Sponsored-Messaging compliance** on Conversation Ads and Message Ads — blocked for EU members from Dec 2021 (ECJ/ePrivacy), consent-gated for opted-in EU members since ~Oct 2024; don't build an EU motion on these formats.

**Changed:**
- Tightened `abm-strategy` vs `ads-outbound-sync` descriptions + master routing to remove overlap: **abm-strategy = ABM planning** (structure, budget, formats, benchmarks); **ads-outbound-sync = ad-engagement → sales signals** (intent, BDR alerts, ZenABM/Fibbler sync). Clear "Do NOT use … (use the other)" boundaries.

**Note:** Conversation/Message Ads were already documented in `ad-formats.md` — v2.2.0 only adds the EU-compliance nuance (no duplicate format section).

**Sources:** LinkedIn Marketing Solutions Help (Brand Lift, Sponsored Messaging EU targeting), plus public incrementality-testing best-practice guidance — accessed 2026-07-21.

---

## v2.1.0 — 2026-07-21

**Summary:** P1 coverage additions from the critical review — the CRM-attribution loop and a structured account audit. Sub-skills now number 10.

**Added:**
- `resources/references/crm-attribution.md` — HubSpot 3-layer connection (native + CAPI + Insight Tag) with the offline-conversion loop on lifecycle-stage changes (~+30–50% SQL at same spend), Salesforce offline conversions + Campaign Influence for account-level attribution, the B2B U-shaped model default, and a 7–14d setup / 4–8wk learning timeline. Cross-linked to **gt-hubspot-admin** and **gt-salesforce-admin** for the CRM-side build. Wired into the `measurement` sub-skill.
- `.claude/skills/audit/gt-SKILL.md` + `resources/references/audit-checklist.md` — a GT-native LinkedIn Ads **audit** sub-skill with a 28-control catalog across tracking, targeting, creative, bidding/budget/structure, and outcomes/governance, built on evidence discipline (mark n/a/unknown; benchmarks are conditional; betas aren't failures). Brings triad parity with `gt-meta-ads` (which already had an audit). Audit-catalog pattern is common in paid-media audits (incl. MIT-licensed AgriciDaniel/claude-ads); implemented GT-native.

**Sources:** LinkedIn Marketing Solutions Help and HubSpot Knowledge Base (official docs), plus public B2B attribution best-practice guidance — accessed 2026-07-21.

---

## v2.0.1 — 2026-07-21

**Summary:** Removed all references to competitor services and re-anchored ABM benchmarks to the authoritative source. No GT strategy lost — the ABM guides were rewritten GT-native.

**Changed:**
- Rewrote `resources/references/abm/linkedin-ads-abm-guide.md` GT-native: dropped every reference to a competitor agency, its credit block, and its operational tables (team-requirements/FTE plan, tool-stack cost table). Benchmarks now point to `benchmarks.md` (ZenABM 2026) with an evidence-discipline caveat (check objective/geo/methodology/sample/maturity before applying any figure).
- Cleaned `resources/references/abm/ads-outbound-signaling-guide.md`: removed the "Source:" lines and the competitor credit block; content kept.
- Added a note on EU restrictions for Conversation/Message Ads.

**Policy:** competitor agencies/services are never referenced in GT skills; SaaS tools (ZenABM, HubSpot, Clay, Fibbler, etc.) remain named as products.

---

## v2.0.0 — 2026-07-21

**Summary:** MAJOR restructure into a master router + 9 sub-skills (multi-sub-skill layout), matching the pattern used by gt-linkedin-content and the CRM admin skills. Progressive disclosure — Claude loads only the relevant domain. No strategy content removed.

**Changed:**
- `SKILL.md` is now a **master router**: dynamic `SKILL_BASE` Setup block (Glob for `**/gt-linkedin-ads/SKILL.md`), an intent → sub-skill routing table, a shared-reference table, and the cross-cutting Key Benchmarks block.
- The 9 sub-skills moved from `resources/sub-skills/*.md` to `.claude/skills/<name>/gt-SKILL.md`: audiences, ads-outbound-sync, bidding, campaign-setup, copy, creative, measurement, optimization, abm-strategy.
- **Fixed a latent path bug:** sub-skills referenced `{SKILL_BASE}/references/...` but the files live under `resources/`; all references normalized to `{SKILL_BASE}/resources/references/...`.
- Enriched routing descriptions with the v1.3.0 topics (Predictive Audiences / career signals → audiences; Accelerate → campaign-setup; CAPI + Revenue Attribution Report → measurement).
- Corrected the master "Do NOT use" cross-links to `gt-linkedin-content` and `gt-linkedin-outbound`.

**Shared resources** (`resources/references/`, `resources/references/abm/`, knowledge base) stay at the top level — script/relative paths and requirements unaffected.

**Validation:** all 9 sub-skills referenced exactly once; every `{SKILL_BASE}` reference resolves; all descriptions ≤1024; footers on every file; `.claude/` present in git; no stray files.

---

## v1.3.0 — 2026-07-21

**Summary:** P1 expansion from a July 2026 platform-research pass. Added the AI-era LinkedIn Ads capabilities the skill was missing (audiences, campaign automation, and attribution), grounded in current LinkedIn Marketing Solutions changes and 2026 benchmark data. Additive only — no existing strategy removed.

**Added:**
- `resources/references/predictive-audiences.md` — the Feb-2024 lookalike sunset, Predictive Audiences (30/account cap, 4-day processing, seed-quality rules), Audience Expansion vs predictive, and Career Journey / career-signal targeting.
- `resources/references/accelerate-ai-campaigns.md` — Accelerate AI campaign mode (GA for lead gen + website visits; video/document support; +42% CPA vendor claim), when to keep manual control (ABM, tight ICP), AI Ad Variants / Shutterstock creative with human-review guardrails, and real-time CRM data in Campaign Manager (June 2025).

**Expanded:**
- `resources/references/measurement-attribution.md` — new "2026 Deep Dive" section on the Conversions API (server-side, offline conversions, Salesforce/GTM/Tealium/Adobe; ~20% lower CPA / ~31% more attributed conversions; ~75% adoption) and the Revenue Attribution Report (CRM-connected, company-level, up to 365-day windows; engagement attributes ~7.7x more revenue).
- `resources/references/benchmarks.md` — 2026 Dreamdata attribution benchmark block.
- Sub-skills `audiences`, `campaign-setup`, `creative` now route to the new references.

**Sources:** LinkedIn Marketing Solutions Help (official docs), Dreamdata 2026 LinkedIn Ads B2B Benchmarks, and B2B marketing press (AdExchanger, Search Engine Land, Social Media Today) — accessed 2026-07-21.

---

## v1.2.1 — 2026-07-21

**Summary:** Repo reconciliation + attribution normalization. Brought the public repo copy in line with the org-deployed v1.2 and standardized every footer to the canonical Growth Today format. No strategy content changed.

**Changed:**
- Added the two ABM reference files that existed in the deployed build but were missing from the repo: `resources/references/abm/linkedin-ads-abm-guide.md` and `resources/references/abm/ads-outbound-signaling-guide.md` (external ABM source material; later rewritten GT-native in v2.0.1).
- `resources/sub-skills/abm-strategy.md`: added the ABM reference-routing block and fixed the resource path to `{SKILL_BASE}/resources/references/abm/...`.
- `SKILL.md`: added the two ABM reference files to the Reference Files table.
- All files: footer standardized to the canonical `Created by [Growth Today] … More open Claude Skills …` format (replacing the older "Visit and download more skills" line).

---

## v1.2 — 2026-06-25

**Summary:** Added new tactical content from a 2026 research pass (thought leadership ad guides, Metadata, and leading LinkedIn-ads agencies) and added a Growth Today attribution footer to every file. No content removed — only additions, plus the description and footer changes.

**Why:** The v1.1 refresh fixed the TLA *benchmarks* but the skill still treated TLAs as single-post tests, had no consolidated "default settings waste money" checklist, and gave no economic-fit rule for when TLAs are worth running. The research surfaced three repeatable, non-obvious tactics worth encoding, plus a stronger third-party cost proof point (Metadata) and updated 2026 cost figures.

**Changed:**

1. **SKILL.md**
   - Description: added "built by Growth Today (growthtoday.co)", "sequenced TLAs and Story Arcs", and a closing "More GT skills: growthtoday.co" for AI-search/SEO surface. No header attribution block (kept clean by design). Length 864 chars (under the 1024 org limit).
   - Version v1.1 → v1.2 with inline note.
   - Key Benchmarks: updated blended CPC to the 2026 $6-15 spread with format medians, added the Metadata $4.14-vs-$22.54 proof point and the 41%-of-B2B-budget / 80%-of-social-leads macro stats.
   - Added attribution footer.

2. **resources/sub-skills/creative.md**
   - New "Sequenced TLAs / Story Arcs" subsection: 5-7 post arcs, 4-6 variant minimum, deliberate ordering, tight fixed audience, 14+ day minimum.
   - New "Who TLAs are economically right for" subsection: ~$1M+ ARR + enterprise/ABM + active executive voice; smaller teams start with sponsored content.
   - New "TLA Anti-Patterns" section: hard-sell, over-broad targeting, single-post campaigns, killing too early, ignoring comments, click-only tracking.

3. **resources/references/troubleshooting.md**
   - New "0. Default Settings Audit" as the first troubleshooting step: Audience Expansion OFF, LinkedIn Audience Network OFF, ABM budget concentration check, frequency capping, manual/target-cost bidding over uncapped Maximum delivery.
   - Quick Diagnostic Checklist expanded with LAN, bid strategy, and ABM spread items.

4. **resources/references/benchmarks.md**
   - Cost Benchmarks table updated with 2026 CPC spread.
   - New "Cost proof points" block: Metadata experiment, channel-weight stats, and the $3-5K/month spend floor + learning-phase timing.

5. **resources/references/ad-formats.md**
   - Added a Story-Arc + economic-fit pointer after the 14 TLA strategies, cross-referencing creative.md.

6. **resources/linkedin-ads-knowledge-base.md**
   - TLA block: added Story-Arc and economic-fit lines so the KB matches the sub-skills.

7. **All files**
   - Added a footer: "Built and updated by Brigitta Ruha (LinkedIn link). Visit and download more skills on growthtoday.co."

**Not changed (intentionally):** the GT-internal finding that single static images outperform animations/GIFs on Brigi and Jani's profiles is a GT-specific learning and was left as-is; the generic "moving elements increase clicks" line in creative.md is kept as a general-market note, not a GT recommendation. All audience, bidding, campaign-setup, copy, measurement, optimization, abm-strategy, and ABM guide content unchanged beyond the footer.

**Sources:** ZenABM and Metadata.io (published LinkedIn-ads benchmark/cost data) plus public LinkedIn-ads best-practice sources, accessed 2026-06-25.

---

## v1.1 — 2026-06-11

**Summary:** Benchmark refresh to the ZenABM 2026 dataset (161,256 ads across 211 companies) and expanded Thought Leader Ads creative guidance. No content was removed — only outdated benchmark figures were updated and new data was added alongside the existing structure.

**Why:** The skill carried the old LinkedIn-reported "63% higher CTR" figure for Thought Leader Ads. The ZenABM 2026 report gives far more specific, format-level data and surfaces an important counter-insight (CTR does not predict pipeline). Keeping the skill on the old number risked steering ad strategy by click volume instead of pipeline.

**Changed:**

1. **SKILL.md → Key Benchmarks**
   - Added a per-format CTR/CPC table (TLA 2.68% / $2.29, Single Image 0.42% / $13.23, Video 0.24% / $15.61, Carousel 0.32% / $13.30, plus Event, Document, Dynamic, Text).
   - Added the "CTR does not predict pipeline" caveat (Spearman rho = -0.170) and the use-a-mix rule.
   - Refined the blended CTR line from "0.4-0.6%" to "0.44-0.65%" and added enterprise/SMB CPL spread.
   - Bumped version v1 → v1.1 with an inline note.

2. **resources/sub-skills/creative.md**
   - Format Selection table: TLA metric changed from "63% higher CTR (mid-funnel)" to "2.68% median CTR, $2.29 CPC (ZenABM 2026)".
   - Thought Leader Ads section: added the ZenABM performance figures, dwell time (6.63s), and the two top-performer creative rules (65% first-person "I" voice; 75% place the link in the bottom 25% of the post), plus the open-with-a-concrete-statement / ~800-1,200 char guidance and the CTR-vs-pipeline caveat.
   - Example 2: updated the benchmark quoted in the answer.

3. **resources/references/benchmarks.md**
   - Replaced the CTR table with per-format ZenABM 2026 medians.
   - Added CTR-by-geography (NL 0.72% / UK 0.55% / US 0.52%), dwell-time-by-format, and a "good CTR by campaign purpose" table.
   - Added the CTR-vs-pipeline negative-correlation note.
   - Added a CPL-by-ICP-tier table (SMB $80-200 / mid $150-450 / enterprise $400-800).

4. **resources/references/ad-formats.md**
   - Thought Leader Ads "Stats" line updated from "63% higher CTR on mid-funnel content" to the ZenABM 2026 figures + CTR-vs-pipeline caveat. (Caught in QA — kept consistent with the rest of the skill.)

5. **resources/linkedin-ads-knowledge-base.md**
   - Same TLA "Stats" update as above, so the knowledge base doesn't contradict the sub-skills. (Caught in QA.)

**Not changed (intentionally):** all sub-skills other than creative, all other reference files (ad-formats, creative-strategy, funnel-architecture, targeting-audiences, bidding-objectives, measurement-attribution, troubleshooting, competitive-research, both ABM guides), and the full knowledge base. Structure and strategy were already current; only benchmark numbers and TLA creative rules needed the 2026 refresh.

**Source:** ZenABM 2026 LinkedIn ABM Benchmarks Report (ZenABM is a SaaS tool), accessed 2026-06-11.

---

## v1 — baseline

Initial GT LinkedIn Ads skill: orchestrator + 9 sub-skills (audiences, ads-outbound-sync, bidding, campaign-setup, copy, creative, measurement, optimization, abm-strategy), reference files, ABM guides, and full knowledge base. Built on $25M+ in managed B2B ad spend.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
