# Clay CLI / API / Agent-Plugin

Clay ships a developer surface that runs from the terminal: a CLI, a developer API, and an
agent-plugin that bundles both. This lets you build and run enrichment **workflows**
programmatically instead of clicking through the UI.

> **CAVEAT (read first):** The CLI / agent-plugin builds and runs **WORKFLOWS**, but **CANNOT
> create or manage TABLES** - table reads are enterprise-gated. To build a table you need the UI or
> the browser-automation PoC path (see `browser-table-poc.md`), not the CLI.

## Install

1. Add the plugin marketplace:
   ```
   /plugin marketplace add clay-run/agent-plugins
   ```
2. Install the Clay plugin:
   ```
   /plugin install clay@clay-plugins
   ```
3. Run the bundled setup, then authenticate:
   ```
   clay login
   ```
   `clay login` runs an OAuth flow - approve in the browser, and the terminal session is linked to
   your Clay workspace.

## Primitives

| Primitive | What it does | Read/Write |
|-----------|--------------|-----------|
| **Search** | Find people or companies from natural language | Read |
| **Routines** | Run enrichment functions on records | Run |
| **Tables** | Query / read table data only | Read only (enterprise-gated) |
| **Workflows** | Build, edit, trigger, test, and version workflows from the terminal | Full |

- **Search** - describe the audience in plain language and Clay returns matching people or
  companies (the same discovery layer as Find People, driven from the CLI).
- **Routines** - invoke enrichment functions directly, useful for scripted one-off enrichment.
- **Tables** - query and read existing table data; you cannot create, restructure, or add columns
  to a table from here, and reads require an enterprise plan.
- **Workflows** - the full lifecycle: build a workflow, edit its nodes, trigger it, test a single
  record, and manage versions - all from the terminal.

## GT Positioning

Clay's own agent-plugin ships its own MCP tools and setup skills, so we do **not** re-document
Clay's tool list here - GT's skill is the **strategy layer** on top: which workflow to build, how
to order a waterfall, when to reach for the CLI vs the UI vs the PoC path, and how to keep credit
spend honest. When in doubt, GT's assessment is that workflows built and versioned through the CLI
are the reliable path; table work stays in the UI.

## When to use the CLI

- Reuse and version a workflow across clients instead of rebuilding it in the UI each time.
- Trigger enrichment from a script, cron, or another system (webhook / CSV upload triggers).
- Test a workflow against a single record before running it at volume.

For anything that needs a **table** built - columns, imports, auto-run - stay in the UI or use the
PoC path in `browser-table-poc.md`.
