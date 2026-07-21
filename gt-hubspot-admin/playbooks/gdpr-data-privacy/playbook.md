---
name: gdpr-data-privacy
description: "Configure HubSpot for GDPR/privacy compliance: enable data privacy features, lawful-basis tracking, consent capture on forms, data subject requests (access/delete), and sensitive-data handling."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: governance
---

# GDPR & Data Privacy

Set up the privacy controls a compliant portal needs: GDPR functionality enabled, lawful basis tracked, consent captured on forms, a process for data subject requests (access/erase), and sensitive-data handled correctly.

## Why This Matters

If you market to or store data on EU/UK (and increasingly other) residents, privacy compliance isn't optional — mishandling consent or a deletion request carries legal and financial risk. HubSpot has built-in GDPR features, but they must be turned on and operationalized. This playbook covers the setup and the recurring process. (This is operational configuration, not legal advice — confirm requirements with counsel.)

## Prerequisites

- Super Admin access to Settings > Privacy & Consent (data privacy options)
- Alignment with legal/DPO on lawful bases and retention policy
- Forms in use (for consent capture)

## Critical Concept: Consent Must Be Captured, Tracked, and Honorable

Compliance is a loop: **capture** consent + lawful basis at collection (forms), **track** it (subscription types + lawful-basis properties — see `subscription-types-consent`), and **honor** requests (access + erasure) and suppressions. HubSpot's GDPR features enable the consent checkboxes and the permanent-delete/anonymize actions; the process around them is what makes it real.

## Plan

1. Enable GDPR/data-privacy features and set lawful bases
2. Add consent + lawful-basis capture to forms
3. Establish the data-subject-request process (access + erase)
4. Handle sensitive data + retention; verify (after state)

## Execute

### Step 1: Enable privacy features
Settings > Privacy & Consent: turn on GDPR functionality. This enables lawful-basis tracking and consent options on forms and contact records.

### Step 2: Consent capture on forms
Add consent checkboxes and lawful-basis capture to forms (explicit opt-in where required). Map consent to the right subscription types (`subscription-types-consent`).

### Step 3: Data subject requests
Define the process for **access** (export a contact's data) and **erasure** (HubSpot's permanently-delete / GDPR-delete, which is irreversible and also prevents re-import of that email). Document who handles requests and the SLA.

### Step 4: Sensitive data + retention
Use sensitive-data controls / field-level permissions for regulated fields (`permission-sets-roles`). Apply a retention policy — suppress/delete per policy (ties to the suppression playbooks).

## After State

**Verification checklist:**

1. GDPR features are enabled; lawful basis is tracked on contacts.
2. Forms capture consent + lawful basis where required.
3. A documented data-subject-request process exists (access + erasure, with owner + SLA).
4. GDPR-delete is understood as permanent (and blocks re-import of that email).
5. Sensitive fields are access-controlled; a retention policy is applied.

## Key Technical Learnings

- **Compliance is capture → track → honor** — all three, not just an unsubscribe link.
- **GDPR-delete is permanent and blocks re-import** — use it deliberately; it's not a normal delete.
- **Consent maps to subscription types** — the two systems work together.
- **This is configuration, not legal advice** — confirm lawful bases + retention with counsel.
- **Pairs with `subscription-types-consent`, `permission-sets-roles`, suppression playbooks.**
