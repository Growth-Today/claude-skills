---
name: apollo-workflows
description: Automate Apollo actions with Workflows (formerly called "Plays") and configure CRM enrichment automation. Use when user asks about "Apollo Workflows", "Apollo Plays", "automate Apollo", "Apollo automation", "CRM enrichment", "auto-enrich CRM", "real-time enrichment", "scheduled enrichment", "job change alerts". Do NOT use for Clay-based enrichment (use gt-clay-builder) or for building the underlying contact list (use company-sourcing, contact-discovery).
---

# Apollo Workflows & Enrichment Automation — Sub-Skill

You help users automate repeatable Apollo actions with Workflows and set up CRM enrichment automation. Always read the reference links before responding, and re-check them if Apollo's product has changed since this was written.

## Reference

- [Workflows Overview](https://knowledge.apollo.io/hc/en-us/articles/14296116597901-Workflows-Overview) — what workflows are, the trigger/condition/action model
- [Create a Workflow](https://knowledge.apollo.io/hc/en-us/articles/4413804036109-Create-a-Workflow) — permissions, enrollment, FAQs on trigger behaviour
- [Workflow Integrations and Actions](https://knowledge.apollo.io/hc/en-us/articles/46233304897933-Workflow-Integrations-and-Actions) — the full list of native and third-party actions
- [Use CRM Enrichment](https://knowledge.apollo.io/hc/en-us/articles/4413921630989-Use-CRM-Enrichment) — auto-fill/overwrite, real-time vs scheduled jobs
- [Enrich Contacts with Job Changes](https://knowledge.apollo.io/hc/en-us/articles/5130064363661-Enrich-Contacts-with-Job-Changes) — job-change-specific enrichment, separate from general CRM enrichment

## What Apollo Workflows Are

Apollo renamed "Plays" to "Workflows" — this is now a full rename, not just an alternate name. The help centre article used to be titled "Plays Overview"; it's now titled "Workflows Overview" at the same article ID, so if you see "Plays" in older material or a client's own notes, treat it as the same feature.

A workflow has three parts:

- **Trigger** — determines when a contact or account enters the workflow. Documented triggers: added to a list, matches specific filters, record created, or experiences a job change.
- **Conditions** (optional) — further criteria a record must meet to continue.
- **Actions** — what Apollo does with qualifying records: add to a list or sequence, remove from a sequence, create a task, update a field, send a notification (e.g. to Slack), or call out to a third-party integration (200+ supported, via Pipedream).

Workflows can be built from scratch, from an Apollo template, or described in plain language to Apollo's AI assistant.

## Example Use Cases

Documented, native uses:

- Add contacts to a sequence or list, or remove them
- Create tasks for reps (calls, LinkedIn touches)
- Update contact records and act on job changes (e.g. notify the rep and re-route when a champion moves to a new company)
- Send a notification (Slack, email) when a rep needs to take a manual action

**Illustrative example, not an Apollo-documented trigger:** a Flatline Agency agency guide describes a workflow where a lead opens an email and then visits the pricing page, enrolling them in a matching sequence or notifying the rep in Slack. Apollo's own docs do not list "website visit" as a trigger — this example is third-party framing (the agency guide still calls the feature "Plays"), not a confirmed Apollo capability. If a client wants this, check the live trigger list in their Apollo account first, or ask Apollo support, before promising it.

## Automating Enrichment (a separate feature from Workflows)

Enrichment automation for your CRM runs through **CRM Enrichment**, not through building a Workflow. It only works with **Salesforce and HubSpot** integrations.

Setup:

1. Integrate your CRM with Apollo and map your default fields.
2. Set **auto-fill or overwrite** permissions per field:
   - **Auto-fill** — enriches a field only when it's empty.
   - **Overwrite** — replaces the field with Apollo data whether or not it's already populated.
3. Choose how it runs:
   - **Real-time** — new and existing records enrich automatically as they sync (every 15-30 minutes, depending on the CRM).
   - **Scheduled** — enrich existing records on a set cadence (weekly/monthly) from the Data Health Center, with a per-run record limit.

**Credit warning:** for scheduled jobs, set filters to control which records get enriched on each run. With no filters, Apollo enriches every record of the selected object type — this can burn through credits fast.

Job changes have their own enrichment path (People/Lists "Job Change" filter, or a dedicated schedule in the Data Health Center) separate from general CRM enrichment, and from the job-change *trigger* inside a Workflow above — the two aren't the same thing, though they use the same underlying data.

## Known Gap: Enrichment Inside a Workflow

This is narrower than "enrichment isn't available in Workflows" — it partly is, just not the way most people assume:

- **Confirmed:** "Enrichment" is one of the listed action categories for *third-party integrations* inside a Workflow (e.g. Hunter, FullContact, NeverBounce, ZeroBounce can run as workflow actions).
- **Not confirmed:** Apollo's own native CRM Enrichment engine (the auto-fill/overwrite one described above) does not appear anywhere in Apollo's documented list of native workflow actions. There's no official doc showing "run CRM Enrichment" as a step you can drop into a Workflow.

**Not confirmed: check with Apollo support before promising a client that native CRM Enrichment can run as a Workflow action.** What you can promise today: CRM Enrichment on its own schedule, and third-party enrichment vendors as workflow actions.

## Upstream List Source (Optional)

Before any of this runs, companies need to reach Apollo in the first place. The original SOP for this area describes a two-step upstream source, kept here as optional context, not a full workflow:

1. Integrate HubSpot with Store Leads.
2. Build HubSpot lists of TAM-fit companies — either a one-off upload or a recurring sync — which then feeds into Apollo.

The source SOP doesn't document anything beyond these two steps, so nothing further is assumed here.
