---
name: linkedin-ads-audit
description: Run a structured audit of a LinkedIn Ads account for B2B advertisers. Use when the user asks to audit LinkedIn Ads, review an account, find wasted spend, do a health check, inherited an account, or wants a prioritized fix list across tracking, targeting, creative, bidding, and lead quality. Triggers on "LinkedIn ads audit", "audit my account", "account review", "health check", "wasted spend", "what's wrong with my LinkedIn ads", "inherited this account", "pre-launch check". Do NOT use for live troubleshooting of a single broken metric (use optimization) or for setup from scratch (use campaign-setup).
---

# LinkedIn Ads Audit (B2B)

You audit a LinkedIn Ads account like a senior media buyer inheriting it: structured, evidence-based, and honest about what you can't see.

## Instructions

1. Collect context first: objective, conversion definition, account/campaign age, geography, date window, currency, spend, targets, and available data (exports, screenshots, CRM access).
2. Read `{SKILL_BASE}/resources/references/audit-checklist.md` and work the control catalog top to bottom.
3. Pull benchmark numbers from `{SKILL_BASE}/resources/references/benchmarks.md` (ZenABM 2026) — never from memory; check objective/geo/methodology/maturity before applying any figure.
4. For measurement/attribution depth read `{SKILL_BASE}/resources/references/measurement-attribution.md` and `{SKILL_BASE}/resources/references/crm-attribution.md`.
5. Separate observations, diagnoses, and recommendations. Mark `n/a`/`unknown` where evidence is missing. Never score an account down for not adopting an optional/beta feature.

## Output

Findings grouped by section (tracking, targeting, creative, bidding/budget/structure, outcomes/governance), each with observation → diagnosis → fix → priority (P1 broken-tracking / wasted-spend → P3 nice-to-have), then a prioritized fix list and a list of missing inputs. Label any vendor-claimed performance figure as a claim.

## Routing
- Wants to *fix* one live symptom (CPL spike, delivery drop) → **optimization**.
- Wants to *build* from scratch → **campaign-setup**.
- Attribution is the core problem → **measurement**.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
