---
name: n8n-code-nodes
description: Write Code nodes in n8n with JavaScript or Python, correct return shape, and sandbox limits. Use when the user asks about the n8n Code node, Run Once for All Items vs Once for Each Item, the return format, $input.all, items, Python beta, allowed built-ins, npm on cloud, or the Code Tool for agents. Triggers on "Code node", "n8n JavaScript", "run once for all items", "run once for each item", "return json", "$input.all", "n8n Python", "code tool", "npm in n8n", "sandbox". Do NOT use for expression fields (use expressions).
---

# n8n Code Nodes

You write Code nodes that transform items safely within n8n's sandbox and return the correct shape.

## Instructions

1. Choose the run mode (all items at once for aggregation; per item for row-by-row transforms)
2. Read inputs via `$input.all()` / `items` (JS) or `_input` (Python)
3. Return the required shape: an array of `{ json: {...} }` objects
4. Keep to allowed built-ins; move heavy external calls to HTTP or dedicated nodes

## Reference

For node concepts and where Code fits the flow → Read `{SKILL_BASE}/resources/n8n-core-guide.md`

## Mode & Language Reference

| Setting | Behavior |
|---------|----------|
| **Run Once for All Items** | Code runs once; `items` is the full array (aggregation, dedup) |
| **Run Once for Each Item** | Code runs per item; use `$json` for the current row |
| **JavaScript** | Full JS; `$input.all()`, `$('Node').all()`, helpers available |
| **Python (beta)** | Access items via `_input`; return list of `{ "json": {...} }` |

## Key Principles

- **Return `[{ json: {...} }]`** - every item must be wrapped in a `json` key or the node errors
- **All Items for aggregation, Each Item for mapping** - pick the mode to match the job
- **No arbitrary npm on cloud** - use allowed built-ins; self-host for custom modules
- **Code Tool variant for agents** - exposes a Code node as a callable tool inside an AI Agent
- **Keep it pure** - transform data; leave API calls and side effects to proper nodes

## Examples

JavaScript (Run Once for All Items) - dedup by email:
```js
const seen = new Set();
return $input.all().filter(i => {
  const e = i.json.email?.toLowerCase();
  if (!e || seen.has(e)) return false;
  seen.add(e); return true;
});
```

Python (Run Once for Each Item) - normalize a domain:
```python
raw = _input.item.json["website"]
d = raw.split("://")[-1].strip("/")
return [{ "json": { "domain": d } }]
```
