# GT Salesforce Admin

A comprehensive Salesforce CRM administration skill for Claude, built by [Growth Today](https://www.growthtoday.co). A single orchestrator routes to 32 specialised playbooks covering audit, database hygiene, enrichment, segmentation, scoring, automation (Flow), and ongoing maintenance. The Salesforce twin of gt-hubspot-admin.

## Install

Add it to your project with the [skills CLI](https://www.growthtoday.co/claude-skills):

```bash
npx skills add Growth-Today/claude-skills gt-salesforce-admin
```

Or copy the `gt-salesforce-admin/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Not sure how to install or use Claude Skills? Full walkthrough here: **https://www.growthtoday.co/claude-skills/gt-salesforce-admin**

## What it does

Trigger it with any Salesforce org administration request — cleanup, audit, enrichment, suppression, deduplication, Flow building, list view segmentation, lead scoring, owner management, lead status or opportunity stage fixes, or routine maintenance. Start with `playbooks/salesforce-audit` to score the org, then `playbooks/salesforce-implementation-plan` for a phased cleanup.

## Object model

Lead (pre-conversion) and Contact (post-conversion) are separate. Account = company, Opportunity = deal, OwnerId points to a User. Data quality is enforced with Validation, Matching, and Duplicate Rules. Salesforce has no native enrichment, so enrichment playbooks require a third-party source (Apollo, Clearbit, Clay).

## Structure

```
gt-salesforce-admin/
├── SKILL.md                 ← orchestrator (auto-loaded by Claude)
├── README.md                ← this file
├── LICENSE                  ← MIT
└── playbooks/               ← 32 playbooks, loaded on-demand
    ├── <playbook-name>/
    │   └── playbook.md      ← step-by-step instructions
    └── salesforce-audit/
        └── scripts/
            └── audit_org.py ← runnable org audit (simple-salesforce)
```

## Coverage — 32 playbooks across 6 categories

| Category | Playbooks |
|---|---|
| Audit & planning | salesforce-audit, salesforce-implementation-plan |
| Database hygiene | delete-no-email-leads-contacts, merge-duplicate-accounts, reassign-inactive-owners, suppress-hard-bounced, suppress-opted-out, suppress-unengaged-leads |
| Data enrichment | assign-unowned-records, enrich-account-name, enrich-industry, fix-lead-status-and-stages, standardize-geo-values |
| Segmentation & scoring | build-lead-scoring, build-list-views-and-reports, create-icp-tiers |
| Automation (Flow) | bounce-monitoring-flow, engagement-suppression-flow, lead-lifecycle-flow, new-record-hygiene-flow |
| Ongoing maintenance | backfill-geo-data, cleanup-dashboards, cleanup-fields, cleanup-flows-and-workflows, cleanup-inactive-users, cleanup-list-views, cleanup-opportunities, cleanup-web-to-lead-forms, create-segment-list-views, quarterly-org-cleanup, review-bounced-records, weekly-cleanup-routine |

## Safety

The audit script reads Salesforce credentials from environment variables (`SF_USERNAME`, `SF_PASSWORD`, `SF_SECURITY_TOKEN`, `SF_DOMAIN`) — no credentials are stored in the skill. Requires Python and `simple-salesforce`. Always back up with Data Loader before any bulk delete or update; the Recycle Bin holds deleted records for 15 days only. Review each playbook's stated automation level before running it against a live org.

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
