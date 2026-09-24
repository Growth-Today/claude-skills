---
name: n8n-binary-data
description: Handle binary data and persistent state in n8n - files, attachments, and Data Tables. Use when the user asks about $binary vs $json, binary property keys, downloading files into binary, Read/Write Binary File, email attachments, or using n8n Data Tables for dedup and state across executions. Triggers on "$binary", "binary data", "download file", "read binary file", "email attachment", "n8n Data Tables", "persistent state", "dedup across runs", "CSV in n8n", "export file". Do NOT use for in-memory JSON transforms (use code-nodes).
---

# n8n Binary Data

You move files through n8n as binary and keep state across executions with Data Tables.

## Instructions

1. Distinguish JSON fields (`$json`) from file payloads (`$binary`)
2. Bring files in as binary (HTTP download, Read Binary File, trigger attachment)
3. Reference the binary property by its key when passing it downstream
4. Use Data Tables for persistent state (dedup keys, run history) between executions

## Reference

For node concepts and HTTP setup → Read `{SKILL_BASE}/resources/n8n-core-guide.md`
For HTTP download and response handling → Read `{SKILL_BASE}/resources/http-api-patterns.md`

## Binary & State Reference

| Task | How |
|------|-----|
| Download a file | HTTP Request → Response Format: File → binary property |
| Read from disk | Read Binary File node → binary property key |
| Attach to email | Gmail/SMTP node → Attachments → binary property name |
| Persist state | Data Table node → upsert by key (dedup, seen-list) |
| Export data | Convert to File (CSV/JSON) → Write Binary File / upload |

## Key Principles

- **`$binary` ≠ `$json`** - files live under a named binary property, not in the JSON body
- **Reference binary by its key** - the default is `data`; keep the name consistent across nodes
- **Set Response Format to File** - HTTP returns binary only when told to
- **Data Tables for cross-run state** - dedup and idempotency need storage the execution outlives
- **Stream large files** - don't base64 big payloads through Code nodes; use binary nodes

## Examples

Example 1: "Enrich a CSV of accounts and export the result"
→ Read Binary File (CSV) → parse to items → enrich via HTTP → Convert to File (CSV) → Write Binary File / email

Example 2: "Don't process the same lead twice across daily runs"
→ Data Table keyed on email → upsert on ingest → IF key exists, skip; else process and record
