---
name: n8n-ai-agents
description: Build AI Agent workflows in n8n with chat models, tools, memory, and structured output. Use when the user asks about the n8n AI Agent node, connecting a chat model, giving an agent tools, agent memory, structured output parsing, $fromAI, system prompts, or choosing an agent vs a fixed chain. Triggers on "AI Agent node", "n8n agent", "agent tools", "chat model", "window buffer memory", "structured output parser", "$fromAI", "agent vs chain", "research agent", "reply triage". Do NOT use for non-AI workflow design (use workflow-design).
---

# n8n AI Agents

You build AI Agent workflows in n8n that reason over tools, memory, and structured output for GTM automation.

## Instructions

1. Decide agent vs fixed chain (dynamic tool choice → agent; deterministic single call → chain)
2. Attach a chat model sub-node and write a tight system prompt
3. Wire tools as sub-nodes and expose their parameters with `$fromAI()`
4. Add memory and a structured output parser when the result feeds downstream nodes

## Reference

For core node concepts, credentials, and workflow patterns → Read `{SKILL_BASE}/resources/n8n-core-guide.md`

## AI Agent Building Blocks

| Sub-node | Role | GTM use |
|----------|------|---------|
| **Chat Model** | The reasoning LLM | Score a lead, draft a reply |
| **Tool** | An action the agent can call | HTTP enrich, HubSpot lookup, Slack post |
| **Memory** | Window buffer of recent turns | Multi-turn reply-triage threads |
| **Output Parser** | Forces JSON shape | `{ tier, reason, next_step }` |

## Key Principles

- **Agent when the path is dynamic** - it picks which tool to call; a chain runs a fixed sequence
- **`$fromAI('domain')` in tool parameters** - lets the model fill a tool's inputs at runtime
- **System prompt is the guardrail** - state the role, the tools, and the exact output contract
- **Window buffer memory** - keep only the last N turns; unbounded context gets expensive and drifts
- **Structured output parser for anything downstream** - never regex an LLM's free text

## Examples

Example 1: "Build a research agent for target accounts"
→ AI Agent + chat model → tools: HTTP (company site), HTTP (news), HubSpot lookup → output parser returns `{ summary, buying_signals, fit_score }`

Example 2: "Triage inbound replies"
→ Gmail Trigger → AI Agent (window buffer memory) → classify `{ intent, sentiment }` → Switch → route Positive to Slack, OOO to Wait
