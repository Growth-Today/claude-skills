---
name: subscription-types-consent
description: "Design communication subscription types and manage consent properly. Sets up granular subscription types, a preference center, and consent tracking so contacts control what they get — improving deliverability and compliance."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: governance
---

# Subscription Types & Consent

Set up communication subscription types (newsletter, product updates, events, etc.) and a preference center so contacts opt into specific communications — instead of a single all-or-nothing unsubscribe. Improves deliverability, engagement, and compliance.

## Why This Matters

With one blunt "unsubscribe from everything," a contact who's tired of the newsletter also loses product and billing emails — and you lose the contact entirely. Granular subscription types let people tune what they receive, which reduces full unsubscribes, improves engagement (people get what they want), and is the backbone of consent compliance (GDPR/CAN-SPAM).

## Prerequisites

- Access to Settings > Marketing > Email > Subscription Types
- Marketing email tool in use
- Alignment on which communication categories the business actually sends

## Critical Concept: Subscription Types Are the Unit of Consent

Each **subscription type** is a communication category a contact can opt in/out of independently, and each marketing email is sent under one. The **preference center** is where contacts manage these. HubSpot logs subscription/consent changes (visible in the custom report builder) so you can prove and analyze consent over time. Design the types deliberately — too few = blunt unsubscribes; too many = confusing.

## Plan

1. Audit current subscription types + how emails map to them
2. Design a clean, small set of types matching real communication categories
3. Configure types + the preference center; map emails to types
4. Verify contacts can self-manage; consent is tracked (after state)

## Execute

### Step 1: Design the types
Keep it to the real categories, e.g. **Newsletter, Product Updates, Events/Webinars, Sales Outreach, Billing/Account**. Mark operational ones appropriately. Avoid one-type-per-campaign sprawl.

### Step 2: Configure + preference center
Settings > Marketing > Email > Subscription Types: create the types. Build/enable the **preference center** so contacts can opt into specific types instead of unsubscribing entirely. Add region-specific handling if you operate under GDPR (see `gdpr-data-privacy`).

### Step 3: Map emails + migrate
Assign each marketing email to the correct subscription type. Ensure existing consent is respected when introducing new types (don't opt people in without basis).

## After State

**Verification checklist:**

1. A small, clear set of subscription types matches real communication categories.
2. The preference center lets contacts opt into/out of specific types.
3. Every marketing email is mapped to a subscription type.
4. Consent changes are tracked (spot-check the subscription events report).
5. New types didn't silently opt existing contacts in without basis.

## Key Technical Learnings

- **Granular types reduce full unsubscribes** — people leave one list, not your whole database.
- **The preference center is the retention tool** — offer "get less," not just "leave."
- **Subscription type = the consent unit** — every email maps to one; consent changes are logged.
- **Small, real categories** — sprawl confuses contacts and dilutes the point.
- **Pairs with `gdpr-data-privacy` and `suppress-global-unsubscribes`.**

---

*Part of [gt-hubspot-admin](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
