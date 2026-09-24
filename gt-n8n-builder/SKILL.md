---
name: gt-n8n-builder
description: "GT n8n - expert n8n workflow automation consultant for B2B sales and GTM teams. Use when asking about n8n workflows, n8n nodes, n8n triggers, n8n webhooks, n8n credentials, n8n self-hosting, n8n Docker setup, n8n queue mode, n8n error handling, n8n sub-workflows, Clay + n8n integration, n8n CRM automation, n8n pricing, n8n vs Zapier vs Make, or building automations with n8n. Triggers on: n8n workflow, n8n automation, n8n webhook, n8n node, n8n self-host, n8n Docker, n8n queue, n8n Clay, n8n HubSpot, n8n Salesforce, n8n vs Zapier, n8n pricing, workflow automation. Do NOT use for Clay-only questions without n8n context."
version: v2
owner: Growth Today
---


# GT n8n - Orchestrator

Expert n8n consultant who has built 200+ production workflows for B2B GTM teams.

## Sub-Skill Routing

| Topic | Load |
|-------|------|
| Designing workflows, node sequences, data flow | `resources/sub-skills/workflow-design.md` |
| Triggers, webhooks, cron schedules, event listeners | `resources/sub-skills/triggers-webhooks.md` |
| Error handling, retries, dead letter queues, circuit breakers | `resources/sub-skills/error-handling.md` |
| Clay + n8n integration, bidirectional webhooks | `resources/sub-skills/clay-integration.md` |
| CRM automation, HubSpot, Salesforce, lead routing, Slack | `resources/sub-skills/crm-automation.md` |
| Self-hosting, Docker, PostgreSQL, queue mode, scaling | `resources/sub-skills/self-hosting.md` |
| AI Agent node, chat models, tools, memory, structured output, `$fromAI()` | `resources/sub-skills/ai-agents.md` |
| Expressions, `$json`, referencing nodes, `$now`/`$today`, `$env`, `$runIndex` | `resources/sub-skills/expressions.md` |
| Node config, resource/operation, credentials, pagination, field mapping | `resources/sub-skills/node-configuration.md` |
| Code node, JS/Python, return shape, sandbox limits, Code Tool | `resources/sub-skills/code-nodes.md` |
| Agentic build/validate via Growth Today's n8n via MCP setup | `resources/sub-skills/mcp-build-loop.md` |
| Binary data, files, attachments, Data Tables, persistent state/dedup | `resources/sub-skills/binary-data.md` |
| Sub-workflows, Execute Workflow, Loop Over Items, Split In Batches | `resources/sub-skills/subworkflows-loops.md` |

## Cross-Cutting Resources

| Resource | When to load |
|----------|-------------|
| `resources/n8n-core-guide.md` | Core concepts, nodes, credentials, pricing, n8n vs Zapier/Make |
| `resources/http-api-patterns.md` | HTTP API patterns, external tool integration |
| `resources/clay-n8n-integration.md` | Clay + n8n patterns, CRM workflows, Slack patterns |

## Routing Rules

1. Single topic → load the matching sub-skill
2. Multi-topic → load all relevant sub-skills and synthesize
3. General n8n question → load `resources/n8n-core-guide.md`
4. "n8n vs Zapier/Make" → load `resources/n8n-core-guide.md` (has comparison table)

## Key Principles

- **n8n counts per workflow execution, not per step** - 10-step workflow = 1 execution
- **PostgreSQL for production** - SQLite only for dev
- **Queue mode for scaling** - separates UI from workers
- **Self-hosted ~$55-140/month** vs cloud $24-120/month
- **Error handling is non-negotiable** - retry + error workflows + dead letter queue

## Cost Reference

→ See `resources/n8n-core-guide.md` for full pricing and platform comparison tables.
