---
name: agentforce-ai-readiness
description: "Get a Salesforce org data-ready for Agentforce / Einstein: clean, complete, deduped, well-permissioned data and clear field semantics so AI agents give reliable answers and actions. Part of gt-salesforce-admin."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: integrations
---

# Agentforce / Einstein AI Readiness

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills

AI in Salesforce (Agentforce, Einstein) is only as good as the org's data and permissions. Bad data → wrong answers; loose permissions → an agent that surfaces or edits things it shouldn't. This playbook is the readiness checklist before switching AI on.

## Prerequisites
- The relevant hygiene, data-model, and security playbooks available
- Agentforce/Einstein licensing (check edition)
- Clear scope: which objects/fields the agent should read/act on

## Critical concept
An AI agent reads your data and your field **semantics** (names, descriptions, help text) and acts within the running user's **permissions**. So readiness = (1) clean/complete/deduped data, (2) meaningful field metadata, (3) tight permissions/FLS so the agent can't over-reach, (4) grounding scope. Duplicates and blanks are the #1 cause of wrong AI output.

## Automation level
Guided — a readiness audit that routes to the underlying playbooks.

## Steps
1. **Data quality:** run dedupe + suppression + fix-status/stages + validation rules (`matching-and-duplicate-rules`, `fix-lead-status-and-stages`, `validation-rules-setup`) — resolve duplicates and blanks the agent would trip on.
2. **Field semantics:** ensure key fields have clear labels, descriptions, and help text (the agent uses these to reason). Remove/relabel ambiguous fields (`cleanup-fields`).
3. **Permissions/FLS:** confirm the agent's running context can only see/act on what it should (`audit-profiles-permission-sets`, `field-level-security-audit`, `setup-roles-and-record-access`).
4. **Scope/grounding:** define which objects/records the agent uses; exclude sensitive fields.
5. **Pilot + verify:** test on real prompts; check answers are correct and actions stay in scope; iterate.

## Notes
- AI amplifies data quality — duplicates/blanks become confident wrong answers. Clean first.
- The agent inherits permissions/FLS — tighten access before enabling, not after.
- This is an orchestrator: it routes to the hygiene, data-model, and security playbooks.

---
Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
