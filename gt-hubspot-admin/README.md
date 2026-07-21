# GT HubSpot Admin

A comprehensive HubSpot CRM administration skill for Claude, built by [Growth Today](https://www.growthtoday.co). A master router orchestrates **68 playbooks across 7 sub-skills** covering audit, data hygiene, data model, segmentation, pipelines & deals, automation, reporting, and governance.

## Install

Add it to your project with the [skills CLI](https://www.growthtoday.co/claude-skills):

```bash
npx skills add Growth-Today/claude-skills gt-hubspot-admin
```

Or copy the `gt-hubspot-admin/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Not sure how to install or use Claude Skills? Full walkthrough here: **https://www.growthtoday.co/claude-skills/gt-hubspot-admin**

## What it does

Trigger it with any HubSpot portal administration request — cleanup, audit, enrichment, suppression, deduplication, data modelling, pipeline design, workflow and routing automation, reporting, lead scoring, owner and permission management, or routine maintenance. The master router matches the request to one or more sub-skills, each of which routes to the right playbook.

## Structure

```
gt-hubspot-admin/
├── SKILL.md                 ← master router (auto-loaded by Claude)
├── .claude/skills/          ← 7 sub-skills, each a gt-SKILL.md router for its domain
│   ├── hubspot-data-hygiene/gt-SKILL.md
│   ├── hubspot-data-model/gt-SKILL.md
│   ├── hubspot-segmentation/gt-SKILL.md
│   ├── hubspot-pipelines-deals/gt-SKILL.md
│   ├── hubspot-automation/gt-SKILL.md
│   ├── hubspot-reporting/gt-SKILL.md
│   └── hubspot-governance/gt-SKILL.md
├── playbooks/               ← 68 playbooks (shared; sub-skills route to them)
│   └── <playbook-name>/
│       ├── playbook.md      ← step-by-step instructions
│       └── scripts/         ← optional Python scripts (requests + python-dotenv)
├── requirements.txt         ← requests, python-dotenv, hubspot-api-client
├── .env.example
├── README.md                ← this file
└── LICENSE                  ← MIT
```

## Coverage — 68 playbooks across 7 sub-skills

| Sub-skill | Playbooks |
|---|---|
| hubspot-data-hygiene | 17 |
| hubspot-data-model | 7 |
| hubspot-segmentation | 6 |
| hubspot-pipelines-deals | 7 |
| hubspot-automation | 11 |
| hubspot-reporting | 6 |
| hubspot-governance | 10 |
| Cross-cutting (audit, implementation plan, weekly & quarterly routines) | 4 |

## Safety

The scripts read your HubSpot access token from the `HUBSPOT_ACCESS_TOKEN` environment variable (via a `.env` in each playbook folder) — no credentials are stored in the skill. Playbooks that modify or delete data follow a `before → execute → after` pattern with pre-flight counts and post-run validation. Review each playbook's stated automation level before running it against a live portal.

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
