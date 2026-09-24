# Meta Ads

B2B Meta (Facebook + Instagram) Ads strategy skill: a master router that resolves its install directory, then routes each request to one of its sub-skills. Two anchors - **fix tracking first** (Pixel + CAPI), and **treat creative as the strategy**, not a design task.

| | |
|---|---|
| **What it does** | Covers B2B Meta ads - tracking hygiene, campaign and funnel structure, custom/lookalike audiences, creative strategy and fatigue, the learning phase, Instant Forms, measurement, and full audits. B2B only: optimise and measure to pipeline, not raw CPL, and run generic DTC tactics through the B2B-vs-B2C guardrail. |
| **Use it when** | The request is about Meta / Facebook / Instagram ads, Advantage+, custom or lookalike audiences, creative fatigue, Pixel / Conversions API, the learning phase, or Instant Forms. Not for LinkedIn or Google ads, or organic social. |
| **Outputs** | Funnel structures, audience and creative strategy, tracking setups, and a full audit with a prioritised fix list. |
| **Entry point** | [`SKILL.md`](SKILL.md) - orchestrator with the Setup (resolve `SKILL_BASE`) step and sub-skill routing table. |

## Resource groups

| Location | Holds |
|---|---|
| `.claude/skills/` | The sub-skill routers: tracking, campaign-setup, audiences, creative, creative-fatigue, learning-phase, lead-forms, measurement, audit |
| `resources/references/` | Shared references: 2026 AI updates, audit checklist, B2B-vs-B2C guardrail, benchmarks, creative formats, CRM attribution, tracking hygiene |
