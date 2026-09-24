# LinkedIn Ads

B2B LinkedIn Ads strategy skill: a master router that resolves its install directory, then routes each request to one of its sub-skills and pulls shared references as needed.

| | |
|---|---|
| **What it does** | Covers the full B2B LinkedIn Ads motion - targeting and ABM audiences, bidding, campaign and funnel architecture, ad copy, creative and Thought Leader Ads, measurement and attribution, optimization, audits, ad-to-outbound signal sync, and recurring reporting. |
| **Use it when** | The request is about LinkedIn campaigns, CPM/CTR, lead gen, Thought Leader Ads, Predictive Audiences, Accelerate, Conversions API, ABM, or LinkedIn ads reporting/QBRs. Not for LinkedIn organic content or outbound DMs. |
| **Outputs** | Campaign and funnel structures, targeting and bidding plans, creative and copy direction, audit findings, and weekly/monthly/quarterly reports. |
| **Entry point** | [`SKILL.md`](SKILL.md) - orchestrator with the Setup (resolve `SKILL_BASE`) step and sub-skill routing table. |

## Resource groups

| Location | Holds |
|---|---|
| `.claude/skills/` | The sub-skill routers: audiences, ads-outbound-sync, bidding, campaign-setup, copy, creative, measurement, optimization, reporting, audit, abm-strategy |
| `resources/references/` | Shared references: benchmarks, ad formats, bidding objectives, funnel architecture, targeting, creative strategy, measurement/attribution, CRM attribution, predictive audiences, reporting playbook, troubleshooting |
| `resources/linkedin-ads-knowledge-base.md` | The consolidated knowledge base |
