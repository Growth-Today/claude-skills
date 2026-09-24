# List Builder

B2B list-building skill for outbound campaigns: a master orchestrator that takes a target definition and walks it through to a scored, verified, deduped prospect list.

| | |
|---|---|
| **What it does** | Defines the ICP, sources companies, discovers contacts, scores and qualifies accounts (including ABM tiers), verifies emails/phones, and deduplicates. Handles single steps or a full "build me a list" chain. |
| **Use it when** | The request is about a lead list, Sales Navigator, boolean search, ICP definition or scoring, lead sources, email/phone verification, list hygiene, deduplication, account qualification, or ABM lists. Not for enrichment workflows (use `clay-builder`) or email copy (use `cold-email-writer`). |
| **Outputs** | A scored, verified, deduplicated prospect list, plus the ICP and qualification framework behind it. |
| **Entry point** | [`SKILL.md`](SKILL.md) - orchestrator with sub-skill routing, decision flow, and key numbers. |

## Resource groups

| Folder | Holds |
|---|---|
| `resources/sub-skills/` | The routed plays: icp-definition, company-sourcing, contact-discovery, account-qualification/-selection, email-validation, deduplication, persona-mapping |
| `resources/reference/` | Sales Navigator guide, data-quality reference, scoring framework, data sources, directories, deep dives |
| `resources/templates/` | Beginner and qualification (GT tier system) workflows |
