---
name: lead-routing-assignment
description: "Route and assign leads automatically in Salesforce: assignment rules, queues, and Flow-based round-robin / territory routing, with a fallback owner and SLA task. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation
---

# Lead Routing & Assignment

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

Get every qualified lead to the right rep instantly. Salesforce routes via **Lead Assignment Rules** (+ queues) and/or **Flow** for round-robin/territory logic. Unassigned leads (or leads stuck in a queue) get no follow-up and no SLA.

## Prerequisites
- "Manage Leads", "Customize Application", Flow access
- `setup-roles-and-record-access` + active users/queues to route to
- `fix-lead-status-and-stages` (route on qualification, not raw creation)

## Critical concept
- **Assignment rules** — criteria-based owner/queue assignment on create/edit (one active rule with ordered entries). Good for territory/segment routing.
- **Queues** — hold unassigned leads for a team to pull from.
- **Round-robin / complex logic** — needs a Flow (or apex/package): pick the next rep from a rotation. Always define a **fallback owner** for records matching no rule.
- Route on **qualification** (lead status/score), not the instant any lead is created (else you distribute junk).

## Automation level
Hybrid — assignment rules + Flow config; API to audit unassigned/uneven ownership.

## Steps
1. **Audit** unassigned/queued leads and owner distribution (overloaded reps?).
2. **Define routing rules:** segments → teams/queues; the qualification trigger; the fallback owner.
3. **Build:** assignment rule entries for territory/segment; a Flow for round-robin within a team where needed.
4. **Add SLA:** on assignment, create a first task + notify the owner ("follow up within X hours").
5. **Exclude** already-owned / customer records from re-routing.
6. **Verify:** a qualified test lead assigns correctly + fires the task; even distribution; nothing left unassigned.

## Notes
- Route on qualification, always with a fallback owner — the top routing gap is leads matching no rule.
- Round-robin needs Flow (assignment rules alone can't rotate). Build on `flow-builder-patterns`.
- Pairs with `setup-roles-and-record-access`, `build-lead-scoring`, `fix-lead-status-and-stages`.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
