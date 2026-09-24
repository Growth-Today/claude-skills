---
name: mcp-handoff
description: How the GT Lemlist skill connects to and hands off to the official Lemlist MCP. Read when the MCP isn't connected, when you need to know which tool group does what, or before firing a batch of Lemlist calls. This is a POINTER, not a full tool catalog.
---

# Lemlist MCP hand-off

This skill is advisory. Execution runs through the **official Lemlist MCP**, which Lemlist builds and maintains. This file is how you connect to it and where to reach for each kind of action. It is a map, not a manual — the MCP's own tool schemas and Lemlist's `load_skill` advisories are the source of truth for mechanics.

## Connecting

- **Endpoint:** `app.lemlist.com/mcp`
- **Auth:** OAuth 2.1 or an API key, both at the endpoint above.
- **Org install:** the connector is added at the org level by an admin (Brigi or Nikola). It is not something this session can self-authorize.
- **If it's not connected:** tell the user it's an admin connector-approval step, keep advising, and stage the plan. Do not try to route around it.

## Tool groups (what to reach for, not every tool)

| Group | Use it for | Representative tools |
|---|---|---|
| Campaigns | create, read, duplicate, report | `get_campaigns`, `create_campaign_with_sequence`, `get_campaigns_stats`, `duplicate_campaign` |
| Sequences | build and edit the multichannel steps | `add_sequence_step`, `update_sequence_step`, `delete_sequence_step`, `set_ab_variant`, `propose_sequence` |
| Leads | import, enrich, update, personalize | `import_leads_to_campaign`, `update_lead`, `personalize_step_for_lead` |
| Replies / inbox / calls | conversations, call activity and status | `get_inbox_conversations`, `get_call_activities`, `update_call_status` |
| Unsubscribes | suppression handling | `get_unsubscribes`, `add_unsubscribe` |
| CRM | contacts, companies, lists | `create_or_update_contact`, `create_contact_list`, `search_contacts` |
| People Database | prospect sourcing | `people_database_search_count`, `push_contacts_from_people_database` |
| Enrichment | providers and waterfalls | `enrich_lead`, `list_enrichment_waterfalls`, `bulk_enrich_leads` |
| Signals / watch lists | intent triggers → campaigns | `list_watch_lists`, `create_watch_list`, `generate_campaign_for_watch_list` |
| Email infra / deliverability | domains, mailboxes, warmup, audits | `list_domains`, `list_mailboxes`, `run_deliverability_audit`, `run_inbox_placement_test` |
| Senders | rotation and strategy | `set_campaign_senders`, `set_campaign_sender_strategy` |
| Templates | reusable message blocks | `list_message_templates`, `get_message_template` |
| Webhooks | event push to other systems | `get_webhooks`, `create_webhook` |

## Rate limit

The MCP is roughly **10 requests per second**. Batch reads, avoid tight loops, and space out bulk writes.

## Lemlist ships its own advisories

Lemlist exposes `load_skill` with its own guides (campaign-builder, copywriting, and others). **Call those for product mechanics** — how a field works, exact step configuration, product-specific copy tips. Do not re-document them here. This skill holds the GT layer those advisories don't cover: channel choice, cadence judgment, the pre-launch gate, and signal routing.

## The gate

Reads and diagnostics (`get_*`, `list_*`, `run_deliverability_audit`, `validate_campaign_readiness`) run freely. Any write, send, or launch (`add_sequence_step`, `import_leads_to_campaign`, `launch_campaign`, `set_campaign_state`) waits for an explicit human yes.
