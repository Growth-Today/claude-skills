---
name: n8n-mcp-build-loop
description: Hand off from n8n advice to actually building and validating workflows via Growth Today's n8n via MCP setup. Use when the user wants an agent to create, edit, validate, or test real n8n workflows programmatically rather than get written guidance. Triggers on "build the workflow for me", "actually create it", "validate my workflow", "n8n MCP", "agent build n8n", "programmatically", "close the loop", "instance MCP server". Do NOT use for advisory-only questions (use workflow-design or the relevant sub-skill).
---

# n8n MCP Build Loop

You decide when to stop advising and hand off to Growth Today's n8n via MCP setup so an agent builds and validates the real workflow.

## Instructions

1. Confirm the user wants a built artifact, not written guidance
2. Check the target n8n instance is recent and has the instance-level MCP server enabled
3. Hand off to Growth Today's n8n via MCP skill / setup to create, edit, validate, and test
4. Return the validated workflow ID and the test-run result, not just a description

## Reference

For workflow architecture before handoff → Read `{SKILL_BASE}/resources/sub-skills/workflow-design.md`
For node concepts and credentials → Read `{SKILL_BASE}/resources/n8n-core-guide.md`

## Advisory vs Agentic

| Mode | What happens | When |
|------|-------------|------|
| **Advisory** | You describe the nodes, flow, and settings | Scoping, teaching, review |
| **Agentic (MCP)** | A coding agent builds/edits/validates/tests on the instance | User wants a working workflow |

## Key Principles

- **Advice ends where a build begins** - once the user wants it live, hand off to the MCP setup
- **The agent connects to the instance's built-in MCP server** - it creates and edits workflows directly
- **Validation closes the loop** - the setup validates node config and runs a test before you report success
- **Needs a recent n8n with instance MCP enabled** - older versions cannot expose the server
- **Report the artifact** - return the workflow ID and test result, not a paragraph of intent

## Examples

Example 1: "Stop explaining and just build the enrichment workflow"
→ Confirm instance MCP is enabled → hand off to Growth Today's n8n via MCP setup → return the validated, test-run workflow

Example 2: "Can you check my workflow actually works?"
→ Agentic mode: the MCP setup validates node configuration and runs a test execution, then reports pass/fail
