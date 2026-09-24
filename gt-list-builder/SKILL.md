---
name: gt-list-builder
description: "GT List Building — expert B2B list building for outbound sales campaigns. Use when asking about building lead lists, Sales Navigator search, boolean filters, ICP definition, ICP scoring, lead sources, data validation, email verification, list segmentation, Apollo prospecting, Clay Find People, list hygiene, deduplication, account qualification, ABM lists, or assembling prospect lists for cold outreach. Triggers on: lead list, list building, Sales Navigator, boolean search, ICP, ideal customer profile, find leads, prospect list, lead source, email verification, data validation, list hygiene, Evaboot, PhantomBuster, export leads, build a list, find prospects, deduplicate, qualify accounts, ABM. Do NOT use for enrichment workflows (use gt-clay-builder) or email writing (use gt-copywriting)."
version: v6
---

# GT List Building — Master Orchestrator

Expert B2B list builder for campaigns sending 100K+ cold emails per month.

## Sub-Skill Routing

| User Intent | Load |
|-------------|------|
| Define target audience, scoring criteria, ICP, firmographic | `resources/sub-skills/icp-definition.md` |
| Find target companies from data sources | `resources/sub-skills/company-sourcing.md` |
| Find contacts/people at companies, boolean search, Sales Navigator | `resources/sub-skills/contact-discovery.md` |
| Score and qualify accounts, ABM tiers, intent data, lookalikes | `resources/sub-skills/account-qualification.md` |
| Verify emails/phones, bounce rates, list hygiene | `resources/sub-skills/email-validation.md` |
| Remove duplicates, merge data sources | `resources/sub-skills/deduplication.md` |
| ABM account selection, revenue reverse-engineering, how many accounts | `resources/sub-skills/account-selection.md` |
| Buying committee mapping, persona-based messaging, champion vs buyer | `resources/sub-skills/persona-mapping.md` |

## Decision Flow

```
User Request
    ├─ Defining WHO to target? ---------> icp-definition
    ├─ Finding COMPANIES? --------------> company-sourcing
    ├─ Finding PEOPLE/CONTACTS? --------> contact-discovery
    ├─ Scoring/qualifying ACCOUNTS? ----> account-qualification
    ├─ Verifying/cleaning DATA? --------> email-validation
    ├─ Removing DUPLICATES? ------------> deduplicate
    ├─ ABM account selection/sizing? ---> account-selection
    ├─ Buying committee/personas? ------> persona-mapping
    └─ Full workflow / "build me a list"?
        ├─ Beginner? → resources/templates/beginner-workflow.md
        ├─ Advanced? → chain: icp-definition → company-sourcing → contact-discovery → account-qualification → email-validation → deduplication
        └─ ABM? → chain: account-selection → persona-mapping → company-sourcing → contact-discovery → account-qualification → email-validation
```

## Reference Files

| Resource | When to load |
|----------|-------------|
| `resources/reference/sales-navigator-guide.md` | ICP, scoring, boolean search, Sales Nav filters, ABM |
| `resources/reference/data-quality-reference.md` | Email/phone verification, bounce management, data decay |
| `resources/reference/scoring-decision-framework.md` | Which scoring layer to apply, decision flow, outreach motion by tier |
| `resources/templates/beginner-workflow.md` | 7-step Clay pipeline (beginner) |
| `resources/templates/qualification-workflow.md` | Growth Today tier system, weighted scoring |
| `resources/reference/list-building-data-sources.md` | 62+ underused data sources |
| `resources/reference/list-building-deep-dives.md` | Multi-source workflows, deep dives |
| `resources/reference/list-building-directories.md` | 100+ industry-specific directories |
| `resources/reference/list-building-framework.md` | 8-phase quality framework |

## Key Numbers

- **2,500** — Sales Navigator max results per search (bypass by segmenting)
- **22-30%** — Annual email decay rate
- **<1%** — Target bounce rate for campaigns
- **95%+** — Target email deliverability
- **100 points** — ICP scoring system (Tier A: 90-100, B: 70-89, C: 50-69, D: <50)
- **10-50 accounts** — Tier 1 ABM (1:1 custom)
- **30 days** — Re-verify lists older than this

## Response Format

1. Identify which sub-skill(s) the user needs
2. For full workflow requests, present beginner template first
3. Always clarify ICP if not provided (industry, company size, titles, geo, tech stack)
4. Provide specific, actionable steps with tool recommendations
5. Include relevant numbers (list size estimates, cost, timeline)
