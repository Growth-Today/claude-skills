# GT Data Audit

A B2B contact data quality audit framework for Claude, built by [Growth Today](https://www.growthtoday.co). Scores a CRM's contact data layer from 0 to 10 across 10 dimensions (coverage, accuracy, freshness, cost, governance, and more) and returns a single score plus a prioritized fix list.

## Install

Add it to your project with the [skills CLI](https://www.growthtoday.co/claude-skills):

```bash
npx skills add Growth-Today/claude-skills/gt-data-audit
```

Or copy the `gt-data-audit/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Not sure how to install or use Claude Skills? Full walkthrough here: **https://www.growthtoday.co/claude-skills/gt-data-audit**

## What it does

Trigger it with any data-quality intent — "audit our data", "is our data the bottleneck", "email accuracy benchmark", "what is a good bounce rate", "cost per usable contact", "ZoomInfo vs Cognism", "CRM hygiene", or "data layer for AI agents". The skill walks all 10 dimensions in order, scores each against a pass benchmark, and returns a single number with the highest-priority fix. A full audit is 3 to 5 hands-on hours for the person running it. Works on any CRM (HubSpot, Salesforce, Pipedrive, Close, Attio). Best run before a Clay build or a GTM playbook.

## Structure

```
gt-data-audit/
├── SKILL.md                    ← orchestrator (auto-loaded by Claude)
├── README.md                   ← this file
├── LICENSE                     ← MIT
└── resources/                  ← loaded on-demand
    ├── scoring.md              ← the 10-dimension scoring bands and fixes
    ├── benchmarks.md           ← email accuracy, bounce, mobile connect, decay benchmarks
    ├── providers.md            ← provider comparison (Apollo, ZoomInfo, Cognism, Clay, and more)
    ├── sources.md              ← the research sources behind the benchmarks
    ├── crm-routing.md          ← how to pull the data per CRM
    └── audit-template.md       ← the deliverable template (Notion / PDF / scorecard)
```

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
