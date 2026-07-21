---
name: property-validation-rules
description: "Prevent bad data at the point of entry. Audits format anomalies, then configures HubSpot property validation rules (email/phone/number formats, required fields, dropdowns over free-text) so junk data can't enter the CRM in the first place."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: data-model
---

# Property Validation Rules

Stop bad data before it enters, instead of cleaning it up forever. This playbook audits current format problems and configures HubSpot's property validation rules and field-type choices so new records come in clean.

## Why This Matters

The cheapest bad record is the one that never gets created. Most hygiene work (dedup, standardization, geo cleanup) exists because there was no gate at the entry point. Validation rules — required formats, number ranges, dropdowns instead of free-text — turn "we'll clean it later" into "it can't come in wrong." This is the prevention layer that makes the hygiene playbooks a one-time fix rather than an endless chore.

## Prerequisites

- HubSpot API token as `HUBSPOT_ACCESS_TOKEN` in a `.env` file (see `requirements.txt` at the skill root)
- Python 3.10+ with `requests`, `python-dotenv`, and `hubspot-api-client` (`uv add requests python-dotenv hubspot-api-client`, or `pip install -r ../../requirements.txt`)
- Access to Settings > Properties (Super Admin or "Edit property settings" permission)
- `property-architecture-governance` ideally done first (correct field types are half the battle)

## Critical Concept: Where Validation Applies (and Where It Doesn't)

HubSpot validation rules (min/max length, numeric range, disallow special characters, required) enforce on **form submissions and manual UI entry**. Like stage-gating, they can be **bypassed by imports, workflows, and the API**. So the strategy is two-layer: validation rules on the front door, plus periodic audit (`scripts/before.py`) to catch anything that slipped through the back.

## Plan

1. Audit current format anomalies per key property (before state — `scripts/before.py`)
2. Convert high-variance free-text fields to dropdowns (with value mapping)
3. Configure validation rules on the properties that matter
4. Add required-field rules where appropriate
5. Verify + schedule periodic re-audit (after state)

## Before State

Run the audit to quantify existing format problems:

```bash
cd scripts
python before.py
```

`scripts/before.py` samples records and flags common anomalies: malformed emails, phone numbers without country codes, non-numeric values in number fields, and free-text fields with high value cardinality (dropdown candidates).

## Execute

### Step 1: Free-text → dropdown

For high-cardinality free-text fields the audit flags (e.g. Industry with 200 variants), create a dropdown with a controlled value set, map the existing variants, migrate, and retire the free-text field. This is the single biggest prevention win.

### Step 2: Configure validation rules

Settings > Properties > select property > **Rules / validation**:

- **Number** properties: set min/max where sensible (e.g. Employees ≥ 0).
- **Text** properties that must follow a format (e.g. postal code): set min/max length and disallow special characters where supported.
- **Phone**: enforce a format expectation (country code) via rule + helper text.
- **Email**: HubSpot validates email format on the default email property; for secondary email fields, add guidance and monitoring.

### Step 3: Required fields

Make properties required on the surfaces where they're captured — on **forms** (required form fields) and on **record creation** (required properties for creating a record) for the fields your process depends on. Don't over-require; require only what's truly needed at capture.

### Step 4: Close the import/API back door

Because imports and API writes bypass validation, add a scheduled re-run of `before.py` (fold into `weekly-cleanup-routine`), and where critical, a workflow that flags or corrects malformed values after creation (see `data-formatting-automation` in the automation group).

## After State

**Verification checklist:**

1. High-variance free-text fields have been converted to dropdowns (audit shows low/controlled cardinality).
2. Validation rules are live on the key number/text/phone properties.
3. Required fields are set on the relevant forms and on record creation.
4. A test entry that violates a rule is blocked in the UI/form. (Try it, confirm, clean up.)
5. `before.py` re-run shows fewer anomalies; a periodic re-audit is scheduled.

## Key Technical Learnings

- **Prevention beats cleanup.** Every validation rule is hygiene work you never have to do again.
- **Dropdowns are the highest-leverage change.** Free-text is where variants (and dedup pain) are born.
- **Front door + back door.** Rules stop manual/form entry; only monitoring catches import/API/workflow writes — do both.
- **Require sparingly.** Over-requiring at capture pushes users to enter junk to get past the gate.
- **Pairs with `property-architecture-governance`** (right types) and `import-data-onboarding` (the biggest bypass source).

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
