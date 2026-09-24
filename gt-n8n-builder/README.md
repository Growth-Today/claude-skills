# n8n Builder

n8n workflow-automation skill for B2B sales and GTM teams: an orchestrator that routes each build to the right sub-skill.

| | |
|---|---|
| **What it does** | Designs and hardens n8n workflows - triggers and webhooks, node configuration, expressions, code nodes, error handling, sub-workflows and loops, AI-agent nodes, Clay + n8n integration, CRM automation, and self-hosting. |
| **Use it when** | The request is about n8n workflows, nodes, triggers or webhooks, self-hosting (Docker, PostgreSQL, queue mode), Clay + n8n, CRM automation, or n8n vs Zapier/Make. Not for Clay-only questions without n8n context. |
| **Outputs** | Workflow designs, node configurations, integration patterns, and self-hosting/scaling guidance. |
| **Entry point** | [`SKILL.md`](SKILL.md) - orchestrator with sub-skill routing, routing rules, and key principles. |

## Resource groups

| Location | Holds |
|---|---|
| `resources/sub-skills/` | The routed plays: workflow-design, triggers-webhooks, error-handling, clay-integration, crm-automation, self-hosting, ai-agents, expressions, node-configuration, code-nodes, mcp-build-loop, binary-data, subworkflows-loops |
| `resources/` (core guides) | Core concepts & pricing (`n8n-core-guide.md`), HTTP/API patterns, Clay + n8n integration |
