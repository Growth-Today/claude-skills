---
name: gt-email-infra
version: v5
description: "Email Infrastructure & Deliverability by Growth Today (growthtoday.co). Expert cold-email infrastructure and deliverability strategist. Use for infrastructure sizing, domain research and purchasing, DNS and auth (MX/SPF/DKIM/DMARC), masking versus redirect, mailbox provisioning (Google Workspace / Microsoft 365 / custom SMTP), Instantly inbox setup and warmup, going live, campaign building and ESP/SEG routing, inbox-health dashboards, and blacklist/bounce auditing. Runs on EmailBison, migrating to Instantly. Triggers on: email infra, buy or setup domains, DNS, MX, SPF, DKIM, DMARC, warmup, mailbox setup, EmailBison, Instantly, Smartlead, deliverability, inbox placement, scaling email, how many domains or mailboxes, ESP matching, SEG, Mimecast, Proofpoint, blacklist, SURBL, Spamhaus, bounce rate, bounce audit, why are my emails bouncing. Do NOT use for cold email copywriting or sequences (use gt-cold-email); the lead list (use gt-list-building); or marketing emails/newsletters."
---

## Setup (Run Once Per Session)

Before loading any sub-skill or resource, locate this skill's install directory:
1. Use Glob to search for `**/gt-email-infra/SKILL.md`.
2. The directory containing this SKILL.md is `SKILL_BASE`.
3. Sub-skills are at: `{SKILL_BASE}/.claude/skills/{sub-skill}/gt-SKILL.md`.
4. Resources are at: `{SKILL_BASE}/resources/...`.

Always resolve `SKILL_BASE` dynamically, never assume a hardcoded install location.

# Email Infrastructure & Deliverability — Orchestrator

Expert cold-email **infrastructure and deliverability** strategist. This skill is the *plumbing that gets cold email delivered* — not the message itself. Route by **who you are** and **what you're doing** to the one sub-skill that matches. Each sub-skill is self-contained and ends in a copy-pasteable checklist.

Platform: Growth Today sends on **EmailBison today** and is **migrating to Instantly** (Smartlead is benchmarked as the third option). Concepts are ESP-agnostic; platform-specific steps are called out inline.

## When NOT to use this skill

- Writing the email — subject lines, body, sequences, personalization → `gt-cold-email`.
- Building or verifying the lead list → `gt-list-building`.
- Marketing emails / newsletters — this is cold-outreach infrastructure only.
- CRM setup or data hygiene → `gt-hubspot-admin` / `gt-salesforce-admin`.

---

## Sub-Skill Routing

| You are… | You want to… | Sub-skill | Path |
|---|---|---|---|
| **Sales Ops** | Research and buy sending domains | **domain-research** | `{SKILL_BASE}/.claude/skills/domain-research/gt-SKILL.md` |
| **Sales Ops** | Provision mailboxes + DNS/auth (masking, not redirect) | **provisioning** | `{SKILL_BASE}/.claude/skills/provisioning/gt-SKILL.md` |
| **Sales Ops** | Set up / connect inboxes in Instantly | **instantly-setup** | `{SKILL_BASE}/.claude/skills/instantly-setup/gt-SKILL.md` |
| **Sales Ops → GTM** | Warm up and take domains live | **warmup-golive** | `{SKILL_BASE}/.claude/skills/warmup-golive/gt-SKILL.md` |
| **GTM Engineer** | Build campaigns, route by ESP/SEG | **campaign-building** | `{SKILL_BASE}/.claude/skills/campaign-building/gt-SKILL.md` |
| **GTM Engineer** | Read the inbox-health dashboard, act on it | **dashboard-reading** | `{SKILL_BASE}/.claude/skills/dashboard-reading/gt-SKILL.md` |
| **GTM Engineer** | Audit a bounce / blacklist to root cause | **blacklist-bounce-audit** | `{SKILL_BASE}/.claude/skills/blacklist-bounce-audit/gt-SKILL.md` |

---

## Cross-Cutting Resources

- **All numbers, limits, timelines, thresholds, and the ESP/SEG taxonomy** (the single source of truth every sub-skill derives from) → Read `{SKILL_BASE}/resources/reference.md`.
- **Approved SMTP / sequencer / masking vendors** → Read `{SKILL_BASE}/resources/approved-vendors.md`.
- **2026 market performance benchmarks** (results-side: is a bounce/reply rate good or bad vs the market) → Read `{SKILL_BASE}/resources/benchmarks.md`.

---

## Critical Rules (Never Break)

1. **Never** cold-send from the primary/brand domain — only dedicated secondary domains.
2. **Max 2 mailboxes per domain.**
3. **One domain = one workspace.**
4. **Buy across multiple registrars**, spread over ~24h, **< 5 per registrar per day** — no single point of failure, no bulk-buy fingerprint.
5. **Warm up ≥ 14 days / 2 weeks** (hard floor; recommended 3–4 weeks) before sending; **link only from domains > 30 days old**.
6. **Never disable warmup** once campaigns are running.
7. **Masking or a real landing page — never a bare 301/302 redirect** to the main site.
8. **No links and no custom tracking domain** in cold email by default (share via LinkedIn or an unlinked URL).
9. **ESP matching is not a rule** — decide keep/drop from our own dashboard data.
10. Start conservative, scale gradually (**≤ 20%/week**).

## Sizing formula (detail in `{SKILL_BASE}/resources/reference.md` §4)

Monthly goal ÷ 20 workdays = daily volume → ÷ 20–25 per mailbox = mailboxes → × 1.5 buffer → ÷ 2 = domains. Split **60% Google / 40% Microsoft**.

## What we can and cannot see

- **We can see and control:** each domain's public footprint (WHOIS, registrar, creation date, DNS, nameservers, masking host) and our own per-inbox/per-domain sending metrics (bounce, reply, placement, warmup).
- **We cannot inspect or split:** the vendor's shared warmup/seed pool (EmailBison + EmailGuard under one shared Growth Today account). Risk is low; escalation path if ever needed: DNS-footprint check across clients → written per-tenant isolation from the vendor → worst case a separate workspace + placement-test account per client.

## Growth Today's point of view (our answers)

- **SURBL:** de-scoped as a primary threat — Google and Microsoft barely weight it. The real fix is **domain sourcing**, not chasing delistings.
- **Microsoft / Outlook:** expect weaker Outlook placement; check sudden drops against **Microsoft BCL recalibration** dates before blaming infra; conservative limits; short copy.
- **SEG (Mimecast/Proofpoint/Barracuda):** a block is the recipient's policy working as designed. **Isolate SEG leads onto dedicated, never-reused domains**, low concurrency into one org, no links/tracking, go multi-channel, and **recycle burnt SEG domains** onto easy Google/Outlook segments before retiring.
- **Bounces:** **strip OOO/auto-replies first** — Bison inflates bounce counts by counting them (~54% in one audit). Read the real number, then diagnose.
- **Failover gap:** Bison can't set cold limit 0, so it strands leads on unhealthy inboxes — a real bounce driver and the key reason for the Instantly migration.

---

## Routing Rules (composite requests)

Most real requests chain sub-skills. Common ones:

1. **"Set up cold email infra for X/month"** → domain-research → provisioning → instantly-setup → warmup-golive (in order).
2. **"Audit our deliverability / why are we bouncing?"** → blacklist-bounce-audit (root cause) + dashboard-reading (health context).
3. **"Build / launch a campaign"** → campaign-building (route from the matrix), then the launch gate in warmup-golive.
4. **"How many domains and mailboxes do I need?"** → `{SKILL_BASE}/resources/reference.md` §4 (sizing).
5. **"Is this bounce/reply rate good?"** → `{SKILL_BASE}/resources/benchmarks.md`.
6. **Single-topic question** → the one matching sub-skill above.

---

## Decision Tree

```
Who / what?
├─ Sales Ops: ideate or buy domains?          → domain-research
├─ Sales Ops: mailboxes / DNS / auth?         → provisioning
├─ Set up / connect inboxes in Instantly?      → instantly-setup
├─ Warm up / go live?                          → warmup-golive
├─ GTM: build or route a campaign (ESP/SEG)?   → campaign-building
├─ GTM: read the dashboard / act on health?    → dashboard-reading
├─ GTM: something bouncing / blacklisted?      → blacklist-bounce-audit
├─ Just need a number / limit / threshold?     → resources/reference.md
└─ Is this metric good or bad vs the market?   → resources/benchmarks.md
```

---

*Created by [Growth Today](https://www.growthtoday.co), an AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
