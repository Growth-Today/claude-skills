# Google Ads

B2B Google Ads strategy skill: a master router that resolves its install directory, then routes each request to one of its sub-skills. First rule - **fix conversion tracking before anything else**; audit tracking first, structure second, tactics third.

| | |
|---|---|
| **What it does** | Covers B2B paid search end to end - account structure, keywords and match types, negative keywords, search-terms mining, Smart Bidding, Performance Max, Quality Score, conversion tracking, ad copy, full audits, and live account ops. B2B only: generic e-commerce tactics run through the B2B guardrail first. |
| **Use it when** | The request is about paid search, negative keywords, search terms, Quality Score, Smart Bidding, Performance Max, RSAs, wasted-spend audits, conversion tracking / offline conversions, Consent Mode, GAQL, or safe live-account changes. Not for LinkedIn or Meta ads, SEO, or organic. |
| **Outputs** | Account structures, keyword and negative-keyword plans, bidding and tracking setups, and a full audit with a prioritised wasted-spend fix list. |
| **Entry point** | [`SKILL.md`](SKILL.md) - orchestrator with the Setup (resolve `SKILL_BASE`) step and sub-skill routing table. |

## Resource groups

| Location | Holds |
|---|---|
| `.claude/skills/` | The sub-skill routers: campaign-setup, keywords, negative-keywords, search-terms, bidding, pmax, quality-score, conversion-tracking, ad-copy, audit, live-ops |
| `resources/references/` | Shared references: 2026 AI bidding, audit checklist, B2B guardrail, benchmarks, Consent Mode v2, CRM attribution, GAQL queries, negative-keyword library, PPC math, safe-write (CEP) |
