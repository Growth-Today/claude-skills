---
name: n8n-expressions
description: Write and debug n8n expressions for referencing and transforming data between nodes. Use when the user asks about n8n expression syntax, {{ }}, $json, referencing another node, $node, $now/$today, $env, $items, $runIndex, or why webhook data is empty. Triggers on "n8n expression", "$json", "$('Node Name')", "reference node", "$now", "$today", "$env", "$runIndex", "webhook body", "expression not working", "empty item". Do NOT use for Code node JavaScript (use code-nodes).
---

# n8n Expressions

You write and debug n8n expressions so data flows correctly between nodes.

## Instructions

1. Identify which node holds the data you need (previous node vs a named earlier node)
2. Choose the right accessor (`$json`, `$('Node').item.json`, `$now`, `$env`)
3. Wrap it in `{{ }}` in any field, or use it raw inside a Code node
4. Test the expression in the field preview before running the full workflow

## Reference

For node concepts, data flow, and credential setup → Read `{SKILL_BASE}/resources/n8n-core-guide.md`

## Expression Cheatsheet

| Expression | Returns |
|-----------|---------|
| `{{ $json.email }}` | Field from the current item (previous node) |
| `{{ $('Get Contacts').item.json.id }}` | Field from a specific earlier node's matching item |
| `{{ $node['HTTP Request'].json.status }}` | Field from a named node by index |
| `{{ $now }}` / `{{ $today }}` | Luxon datetime for now / start of today |
| `{{ $now.minus({ days: 7 }).toISODate() }}` | Luxon math and formatting |
| `{{ $env.API_BASE_URL }}` | Environment variable value |
| `{{ $items('Split In Batches') }}` | All items from a named node |
| `{{ $runIndex }}` | Current loop iteration index |

## Key Principles

- **Webhook payloads live under `.body`** - use `{{ $json.body.email }}`, not `{{ $json.email }}`
- **`$json` = previous node only** - to reach further back, name the node with `$('Node Name')`
- **`.item` matches by pairing** - use `.first()` / `.all()[0]` when items don't pair 1:1
- **Guard empty items** - `{{ $json.name || 'Unknown' }}` stops blank rows breaking downstream calls
- **`$env` needs it enabled** - self-hosted must allow env access for `$env` to resolve

## Examples

Example 1: "My webhook field is always empty"
→ The payload is nested: reference `{{ $json.body.<field> }}`, not `{{ $json.<field> }}`

Example 2: "Pull the deal ID from three nodes back"
→ Use `{{ $('Get Deal').item.json.id }}` - `$json` only sees the immediately previous node
