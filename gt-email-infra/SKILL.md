---
name: gt-email-infra
description: Email Infrastructure & Deliverability by Growth Today (growthtoday.co). Use for cold email infrastructure and deliverability: infrastructure sizing, domain research and purchasing, DNS/auth (MX/SPF/DKIM/DMARC), masking vs redirect, mailbox provisioning (Google Workspace / Microsoft 365), warmup and going live, campaign building and ESP/SEG routing, reading an inbox-health dashboard, and blacklist/bounce auditing and root-cause diagnosis. Runs on EmailBison today, migrating to Instantly (Smartlead benchmarked). Triggers on: email infra, setup domains, buy domains, domain research, DNS setup, MX/SPF/DKIM/DMARC, warmup, mailbox setup, Google Workspace or Microsoft 365 cold email, EmailBison, Instantly, Smartlead, deliverability issue, inbox placement, scaling email, how many domains/mailboxes, campaign routing, ESP matching, SEG, Mimecast/Proofpoint/Barracuda, inbox classification, blacklist, SURBL, Spamhaus, bounce rate, soft/hard bounce, bounce audit, why are my emails bouncing. Do NOT use for cold email copywriting, subject lines, or sequences (use gt-cold-email); for building/verifying the lead list (use gt-list-building); or for marketing emails and newsletters (this is cold-outreach infrastructure only).
metadata:
  version: 2.0.0
---

# Growth Today Email Infrastructure & Deliverability — Router

Expert cold-email **infrastructure and deliverability** strategist. This skill is about the *plumbing that gets cold email delivered* — not the message itself. Route by **who you are** and **what you're doing**, then open the one playbook that matches.

Platform: Growth Today sends on **EmailBison today** and is **migrating to Instantly** (Smartlead is benchmarked as the third option). Concepts here are ESP-agnostic; platform-specific steps are called out in boxes.

## When NOT to use this skill

- Writing the email — subject lines, body, sequences, personalization → `gt-cold-email`.
- Building or verifying the lead list → `gt-list-building`.
- Marketing emails / newsletters — this is cold-outreach infrastructure only.
- CRM setup or data hygiene → `gt-hubspot-admin` / `gt-salesforce-admin`.

If the question is "what should the email say", it's the wrong skill. If it's "how do I set up the sending system / why isn't it arriving / why is it bouncing", it's the right one.

---

## Route by role

| You are… | You do… | Open |
|---|---|---|
| **Sales Ops** | Research and buy sending domains | `playbooks/01-domain-research-and-purchasing.md` |
| **Sales Ops** | Provision mailboxes + DNS/auth (masking, not redirect) | `playbooks/02-provisioning-dns-auth.md` |
| **Sales Ops → GTM** | Warm up and take domains live | `playbooks/03-warmup-and-go-live.md` |
| **GTM Engineer** | Build campaigns, route by ESP/SEG | `playbooks/04-campaign-building.md` |
| **GTM Engineer** | Read the inbox-health dashboard, act on it | `playbooks/05-dashboard-reading.md` |
| **GTM Engineer** | Audit a bounce / blacklist problem to root cause | `playbooks/06-blacklist-bounce-audit.md` |
| Anyone | Look up a number, limit, threshold, taxonomy | `references/reference.md` |
| Anyone | Benchmark a metric — is this bounce/reply rate good or bad? | `references/benchmarks.md` |
| Anyone | Which sending/SMTP vendors are approved? | `references/approved-vendors.md` |

Every playbook is self-contained and ends in a copy-pasteable checklist. For any number, defer to `references/reference.md` — never invent values.

---

## Critical rules (never break)

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

---

## Sizing formula (detail in `references/reference.md`)

Monthly goal ÷ 20 workdays = daily volume → ÷ 20–25 per mailbox = mailboxes → × 1.5 buffer → ÷ 2 = domains. Split **60% Google / 40% Microsoft**.

---

## What we can and cannot see

- **We can see and control:** each domain's public footprint — WHOIS, registrar, creation date, DNS (MX/SPF/DKIM/DMARC), nameservers, masking host — and our own sending metrics (bounce, reply, placement, warmup) per inbox and domain.
- **We cannot inspect or split:** the vendor's shared warmup/seed pool (EmailBison + EmailGuard run under one shared Growth Today account). Risk is low given our discipline; if isolation is ever needed, the escalation path is a DNS-footprint check across clients → written per-tenant isolation from the vendor → worst case a separate workspace + placement-test account per client.

---

## Growth Today's point of view (our answers)

- **SURBL:** de-scoped as a primary threat — Google and Microsoft barely weight it. The real fix is **domain sourcing** (registrar/date/DNS spread, clean naming, masking), not chasing delistings.
- **Microsoft / Outlook:** expect weaker Outlook placement; check sudden drops against **Microsoft BCL recalibration** dates before blaming our infra; conservative Outlook limits; short copy.
- **SEG (Mimecast/Proofpoint/Barracuda):** a block is the recipient's policy working as designed. **Isolate SEG leads onto dedicated, never-reused domains**, low concurrency into one org, no links/tracking, go multi-channel, and **recycle burnt SEG domains** onto easy Google/Outlook segments before retiring them.
- **Bounces:** **strip OOO/auto-replies first** — Bison inflates bounce counts by counting them (~54% in one audit). Read the real number, then diagnose.
- **Failover gap:** Bison can't set cold limit 0, so it strands leads on unhealthy inboxes — a real bounce driver and the key reason we are moving to Instantly.

---

## Decision tree

```
Who / what?
├─ Sales Ops: ideate or buy domains?          → playbooks/01-domain-research-and-purchasing.md
├─ Sales Ops: mailboxes / DNS / auth?         → playbooks/02-provisioning-dns-auth.md
├─ Warm up / go live?                          → playbooks/03-warmup-and-go-live.md
├─ GTM: build or route a campaign (ESP/SEG)?   → playbooks/04-campaign-building.md
├─ GTM: read the dashboard / act on health?    → playbooks/05-dashboard-reading.md
├─ GTM: something bouncing / blacklisted?      → playbooks/06-blacklist-bounce-audit.md
├─ Just need a number / limit / threshold?     → references/reference.md
└─ Is this metric good or bad vs the market?    → references/benchmarks.md
```

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
