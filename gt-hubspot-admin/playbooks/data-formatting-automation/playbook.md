---
name: data-formatting-automation
description: "Auto-normalize data as it enters: casing, whitespace, phone format, country/state values. Builds format-fix workflows so the Data Quality Command Center stops flagging the same issues and hygiene becomes self-healing."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: automation
---

# Data Formatting Automation

Turn recurring formatting fixes into automation. Instead of repeatedly cleaning casing, whitespace, phone formats, and geo values by hand, build workflows that normalize data on create/update — so the database stays clean without manual passes.

## Why This Matters

Formatting issues (name in ALL CAPS, " john@x.com " with spaces, phone without country code, "usa" vs "United States") recur endlessly from forms, imports, and integrations. Fixing them once via a hygiene pass doesn't hold — new records reintroduce them. Format-fix workflows make hygiene self-healing and keep the Data Quality Command Center quiet.

## Prerequisites

- Access to Automation > Workflows (format actions like "format property" / set-value with functions)
- Baseline of recurring issues from `data-quality-command-center` and `property-validation-rules`
- Standardized target values defined (`standardize-geo-values`)

## Critical Concept: Fix Format at Write, Validate at Entry

Two complementary layers: **validation rules** (`property-validation-rules`) block bad manual/form entry; **format workflows** normalize whatever still gets in (imports, API, integrations). Together they close the loop the Command Center monitors. HubSpot's workflow "Format data" action handles common cases (capitalize, trim, fix number/phone) without code; complex cases use a custom-code action (`programmable-automation-custom-code`).

## Plan

1. Pull the recurring formatting issues from the Command Center
2. Build format workflows for each common case
3. Handle complex normalizations with custom code where needed
4. Verify the Command Center flags drop (after state)

## Execute

### Step 1: Prioritize by frequency
From `data-quality-command-center`, list the most common recurring format issues (typically: name casing, email/text whitespace, phone country code, country/state variants).

### Step 2: Build format workflows
Automation > Workflows (contact/company-based), enrolled on create + property update:
- **Name casing:** Format data action → capitalize first/last name.
- **Whitespace:** trim email/text fields.
- **Phone:** normalize to E.164-style (country code) where feasible.
- **Geo values:** map variants → standardized values (`standardize-geo-values`).
Enable re-enrollment so updates get re-normalized (mind the loop rule from `reengagement-reenrollment`).

### Step 3: Complex cases → custom code
For normalizations beyond the built-in action (e.g. parsing/reformatting), use a custom-code action (`programmable-automation-custom-code`).

## After State

**Verification checklist:**

1. Format workflows exist for the top recurring issues.
2. New records get normalized on create/update (test one).
3. Command Center formatting flags trend down over time.
4. No workflow loops from the normalization writes.
5. Validation rules cover the front door; format workflows cover imports/API.

## Key Technical Learnings

- **Validate at entry + format at write** = self-healing hygiene; you need both layers.
- **Built-in "Format data" action covers most cases** — reserve custom code for the hard ones.
- **Watch re-enrollment loops** — normalization writes can re-trigger; guard against it.
- **Command Center is the feedback loop** — declining flags prove the automation works.
- **Pairs with `property-validation-rules`, `standardize-geo-values`, `data-quality-command-center`.**

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
