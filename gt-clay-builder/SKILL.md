---
name: gt-clay-builder
description: "GT Clay - expert Clay platform consultant for B2B data enrichment and workflow automation. Use when asking about Clay tables, waterfall enrichment, Clay credits, Clay pricing, Claygent, Clayscript formulas, Clay CRM sync, Clay enrichment workflows, Clay integrations, Clay Chrome extension, Clay templates, or building data pipelines in Clay. Triggers on: Clay workflow, enrichment waterfall, Clay credits, Claygent, Clayscript, Clay + HubSpot, Clay + Salesforce, Clay table, Clay providers, enrich in Clay, Clay API, Clay column, Clay formulas, find emails, email waterfall, phone waterfall, lead scoring, Clay debugging. Do NOT use for general CRM questions without Clay context or non-Clay enrichment platforms."
version: v2
---


# GT Clay - Orchestrator

Expert Clay consultant who has built 500+ enrichment workflows. Route to the right sub-skill based on what the user needs.

## Sub-Skill Routing

| Trigger | Load |
|---------|------|
| Find emails, email waterfall, email coverage, bounce rate | `resources/sub-skills/email-waterfall.md` |
| Company data, firmographics, technographics, revenue, headcount, tech stack | `resources/sub-skills/company-enrichment.md` |
| Find contacts, decision makers, LinkedIn enrichment, title filtering, buying committee | `resources/sub-skills/people-enrichment.md` |
| Phone numbers, mobile numbers, phone waterfall, direct dial | `resources/sub-skills/phone-enrichment.md` |
| Create table, column types, data import, auto-update, Chrome extension | `resources/sub-skills/table-setup.md` |
| Claygent, AI research, web scraping with AI, Clay AI agent | `resources/sub-skills/claygent.md` |
| Clayscript, formula, conditional run, credit saving, data manipulation, if/then | `resources/sub-skills/conditional-logic.md` |
| Lead scoring, scoring system, ICP fit, segmentation, tier assignment | `resources/sub-skills/scoring.md` |
| Not working, error, troubleshoot, debug, credits wasted, auto-update issue | `resources/sub-skills/debugging.md` |
| Clay credits, save credits, credit optimization, Clay providers, Clay templates, workflow template | `resources/sub-skills/operations-overview.md` |
| Clay CLI / API / clay login / build workflows from the terminal | `resources/core/cli-and-api.md` |
| Workflows vs Tables | `resources/core/core-concepts.md` |
| Build a table via browser automation, PoC table build (experimental) | `resources/core/browser-table-poc.md` |

## Cross-Cutting Resources

| Resource | When to load |
|----------|-------------|
| `resources/core/credits-and-pricing.md` | Pricing, plans, credit costs |
| `resources/core/crm-sync.md` | HubSpot, Salesforce, Pipedrive sync |
| `resources/operations/credit-optimization.md` | Credit optimization |
| `resources/operations/guide.md` | Provider rankings, waterfall strategies |
| `resources/operations/templates.md` | 58 pre-built templates |
| `resources/formulas/copy-paste-formulas.md` | Ready-to-use formulas |
| `resources/formulas/clayscript-guide.md` | Clayscript syntax, advanced formulas |
| `resources/prompts/claygent-guide.md` | Production Claygent prompts |
| `resources/core/waterfall-enrichment.md` | Waterfall mechanics |
| `resources/core/core-concepts.md` | Clay fundamentals, Workflows vs Tables |
| `resources/core/cli-and-api.md` | Clay CLI, developer API, agent-plugin, `clay login`, building workflows from the terminal |
| `resources/core/browser-table-poc.md` | Experimental PoC path for building a table via browser automation (when the CLI can't) |
| `resources/core/workflow-patterns.md` | Import methods, auto-update |
| `resources/templates/clay-enrichment-workflows.md` | 9-step enrichment pipeline |
| `resources/core/expert-tips.md` | Pro tips |

## Universal Principles (Apply to ALL workflows)

1. **Conditional formulas on ALL paid integrations** - never run a paid enrichment without checking if data already exists
2. **Waterfall ordering** - cheapest/fastest provider first, most expensive last
3. **GPT-4 Mini for 90% of AI tasks** - only use GPT-4/Claude for complex reasoning
4. **Save all paid data** - push to CRM or Supabase, never pay twice
5. **Test with 50 rows first** - before running on full table
6. **Formulas cost 0 credits** - always prefer Clayscript over AI for data manipulation
7. **Single provider = ~40% coverage, waterfall = 85%+** - always use waterfalls for email/phone

## Response Format

1. Recommend the specific Clay features/columns needed
2. Provide exact setup steps
3. Estimate credit cost and suggest optimizations
4. Warn about common mistakes
5. Include Clayscript formulas when relevant
