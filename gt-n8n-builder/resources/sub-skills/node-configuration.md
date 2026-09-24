---
name: n8n-node-configuration
description: Configure n8n nodes correctly using the resource/operation model, parameters, credentials, and pagination. Use when the user asks about n8n node settings, resource and operation fields, fixed value vs expression, selecting credentials, pagination, field mapping, or validating a node before running. Triggers on "node configuration", "resource operation", "n8n parameters", "fixed vs expression", "select credential", "pagination", "field mapping", "test the node", "node not returning data". Do NOT use for expression syntax (use expressions) or Code node logic (use code-nodes).
---

# n8n Node Configuration

You configure n8n nodes precisely so they return the right data on the first run.

## Instructions

1. Pick the **Resource** first (e.g. Contact), then the **Operation** (e.g. Create/Get/Search)
2. Fill required parameters; toggle fixed value vs expression per field
3. Select or create the credential for that node
4. Test the single step (Execute Node) before wiring it into the full workflow

## Reference

For node types, credentials, and authentication → Read `{SKILL_BASE}/resources/n8n-core-guide.md`
For HTTP node parameters and pagination → Read `{SKILL_BASE}/resources/http-api-patterns.md`

## Common Misconfigurations

| Symptom | Cause | Fix |
|---------|-------|-----|
| Field options empty | Resource/Operation not set | Set both before mapping fields |
| Literal `{{ $json.x }}` sent | Fixed value mode on | Switch the field to expression |
| 401 / auth error | Wrong or unselected credential | Re-select credential, re-test |
| Only 100 records | Pagination off | Enable "Return All" / pagination |
| Wrong field updated | Parameter dependency ignored | Set parent field so child options load |

## Key Principles

- **Resource → Operation → parameters** - options are dependent; later fields load from earlier choices
- **Fixed value vs expression is per-field** - the toggle decides literal text vs computed value
- **Validate before you run** - Execute Node on one item beats debugging a 20-node run
- **Return All vs Limit** - default limits hide records; enable pagination for full pulls
- **Map fields explicitly** - don't rely on auto-mapping when field names differ across systems

## Examples

Example 1: "My HubSpot node only returns 100 contacts"
→ Enable Return All (or set pagination + limit); default operations cap at one page

Example 2: "The API rejects my auth"
→ Confirm the credential is selected on the node, re-test the single step, then scale
