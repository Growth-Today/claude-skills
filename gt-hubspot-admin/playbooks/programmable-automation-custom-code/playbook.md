---
name: programmable-automation-custom-code
description: "Use custom-code and webhook actions in workflows (Operations/Data Hub) for logic beyond the standard actions: complex calculations, data transformations, external API calls, and advanced routing — safely."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation
---

# Programmable Automation (Custom Code)

When standard workflow actions can't do it, custom-code actions can: run JavaScript (or Python) in a workflow to do complex calculations, transform data, call external APIs, or implement advanced routing. This playbook covers when to reach for it and how to do it safely.

## Why This Matters

Most automation should use standard actions (they're reliable and need no maintenance). But some logic genuinely requires code — randomized/weighted lead distribution, multi-field calculations, calling an external system mid-workflow, or transformations HubSpot can't express. Custom-code actions (Operations/Data Hub) unlock these, at the cost of added complexity and maintenance — so use them deliberately.

## Prerequisites

- **Operations Hub / Data Hub Professional or Enterprise** (custom-code + webhook workflow actions)
- Access to Automation > Workflows
- For external calls: API keys/secrets stored in HubSpot **workflow secrets** (never hard-coded)
- Basic JS/Python; understanding of the workflow's input/output contract

## Critical Concept: Prefer Standard Actions; Code Is a Last Resort

Every custom-code action is code someone must maintain and debug. Before writing code, confirm no standard action (set property, format data, rotate owner, webhook) does the job. When you do use code: keep it small, store secrets in workflow secrets, handle errors, and document what it does and why.

## Plan

1. Confirm the need is real (no standard action fits)
2. Design the input fields → logic → output fields contract
3. Write + test the custom-code action (use the test panel)
4. Add error handling + documentation; monitor (after state)

## Execute

### Step 1: Justify it
List the logic; confirm standard actions can't do it. Common legitimate cases: weighted/randomized routing, multi-field/date math beyond calculation properties, calling an external API, or complex string parsing.

### Step 2: Build the action
In a workflow, add a **Custom code** action:
- Define **input fields** (the properties the code reads).
- Write the function; return **output fields** to use in later workflow steps.
- Store any API keys in **Secrets** (never inline).
- Use the built-in **test** to run against a sample record before activating.

### Step 3: Webhook alternative
If you only need to send data out (no in-workflow logic), use the simpler **webhook action** instead of code.

### Step 4: Error handling + docs
Wrap external calls in try/catch, handle timeouts, and log meaningfully. Document the action's purpose, inputs, and outputs (ties to `workflow-naming-governance`).

## After State

**Verification checklist:**

1. The custom code does something no standard action could.
2. Secrets are in workflow Secrets, never hard-coded.
3. The action was tested on sample records before activation.
4. Errors/timeouts are handled; failures don't silently corrupt data.
5. Purpose + I/O are documented; the workflow follows naming governance.

## Key Technical Learnings

- **Code is a last resort** — every custom action is maintenance debt; exhaust standard actions first.
- **Secrets in Secrets** — never hard-code API keys in a workflow action.
- **Test before activating** — the test panel prevents shipping broken logic to live records.
- **Webhook for send-only** — don't write code when a webhook action suffices.
- **Operations/Data Hub gated** — confirm the tier before designing around it.
