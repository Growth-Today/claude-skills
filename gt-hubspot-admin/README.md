# GT HubSpot Admin

A comprehensive HubSpot CRM administration skill for Claude, built by [Growth Today](https://www.growthtoday.co). A single orchestrator routes to 32 specialised playbooks covering audit, database hygiene, enrichment, segmentation, scoring, automation, and ongoing maintenance.

## Install

Add it to your project with the [skills CLI](https://www.growthtoday.co/claude-skills):

```bash
npx skills add Growth-Today/claude-skills gt-hubspot-admin
```

Or copy the `gt-hubspot-admin/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Not sure how to install or use Claude Skills? Full walkthrough here: **https://www.growthtoday.co/claude-skills/gt-hubspot-admin**

## What it does

Trigger it with any HubSpot portal administration request — cleanup, audit, enrichment, suppression, deduplication, workflow building, list segmentation, lead scoring, owner management, lifecycle stage fixes, or routine maintenance. Claude reads the routing index, picks the matching playbook, and follows it step by step.

## Structure

```
gt-hubspot-admin/
├── SKILL.md                 ← orchestrator (auto-loaded by Claude)
├── README.md                ← this file
├── LICENSE                  ← MIT
└── playbooks/               ← 32 playbooks, loaded on-demand
    ├── <playbook-name>/
    │   ├── playbook.md      ← step-by-step instructions
    │   └── scripts/         ← optional Python scripts (requests + python-dotenv)
    └── ...
```

## Coverage — 32 playbooks across 6 categories

| Category | Playbooks |
|---|---|
| Audit & planning | hubspot-audit, hubspot-implementation-plan |
| Database hygiene | delete-no-email-contacts, merge-duplicate-companies, reassign-deactivated-owners, suppress-ghost-contacts, suppress-global-unsubscribes, suppress-hard-bounced |
| Data enrichment | assign-unowned-contacts, enrich-company-name, enrich-industry, fix-lifecycle-stages, standardize-geo-values |
| Segmentation & scoring | build-lead-scoring, build-smart-lists, create-icp-tiers |
| Automation workflows | bounce-monitoring-workflow, engagement-suppression-workflow, lifecycle-progression-workflow, new-contact-hygiene-workflow |
| Ongoing maintenance | backfill-geo-data, cleanup-dashboards, cleanup-deals, cleanup-forms, cleanup-lead-owners, cleanup-lists, cleanup-properties, cleanup-workflows, create-segment-lists, quarterly-database-cleanup, review-bounced-contacts, weekly-cleanup-routine |

## Safety

The scripts read your HubSpot access token from the `HUBSPOT_ACCESS_TOKEN` environment variable — no credentials are stored in the skill. Playbooks that modify or delete data follow a `before → execute → after` pattern with pre-flight counts and post-run validation. Review each playbook's stated automation level before running it against a live portal.

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
