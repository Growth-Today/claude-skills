---
name: gt-email-infra
description: "GT Email Infrastructure & Deliverability by Growth Today (growthtoday.co). Use for cold email infrastructure setup, domain research and purchasing, DNS configuration (MX/SPF/DKIM/DMARC), email warmup, mailbox provisioning, Google Workspace or Microsoft 365 for cold email, EmailBison/Instantly setup, going live, deliverability monitoring, automated inbox management at scale (dashboard, inbox classification/tagging, campaign routing, blacklist monitoring), and bounce/blacklist auditing and root-cause diagnosis. Triggers on: email infra, setup domains, buy domains, domain research, DNS setup, MX records, SPF, DKIM, DMARC, warmup, mailbox setup, Google Workspace cold email, Microsoft 365 cold email, EmailBison, Instantly, deliverability issue, inbox placement, scaling email, how many domains, how many mailboxes, inbox management automation, inbox tagging, blacklist, bounce rate, soft bounce, hard bounce, bounce audit, why are my emails bouncing. Do NOT use for email copywriting (use gt-cold-email)."
version: v4
---

# GT Email Infrastructure — Orchestrator

Expert cold email infrastructure strategist. Route to the right resource based on the user's question.

## When to use this skill

Use this skill whenever the question is about the *plumbing* that gets cold email delivered — not the message itself. That includes:

- **Planning & sizing** — "how many domains/mailboxes do I need for X emails a month", infrastructure architecture, provider split.
- **Domains** — ideating and researching new sending domains, naming patterns, registrars, buying strategy.
- **Setup** — Google Workspace / Microsoft 365 provisioning, DNS records (MX, SPF, DKIM, DMARC), forwarding, custom tracking domains.
- **Warmup & going live** — warmup timelines, ramp schedules, send limits per provider.
- **Deliverability** — inbox placement, spam diagnosis, authentication, CAN-SPAM / GDPR compliance.
- **Automation at scale** — inbox classification/tagging, deliverability dashboards, campaign routing, blacklist monitoring, reporting across many inboxes and workspaces.
- **Bounce & blacklist auditing** — finding where a bounce actually comes from, categorizing bounces, reading soft vs hard SMTP codes, tracing root cause to infra / list / copy.

## When NOT to use this skill

- **Writing the email itself** — subject lines, body copy, sequences, personalization → use `gt-cold-email`.
- **Building the lead list** — sourcing, filtering, verification of contacts → use `gt-list-building`.
- **Marketing emails or newsletters** — this skill is cold-outreach infrastructure only, not broadcast/marketing email.
- **CRM setup or data hygiene** → use `gt-hubspot-admin` / `gt-salesforce-admin`.

If the question is "what should the email say", it's the wrong skill. If it's "why isn't the email arriving / how do I set up the sending system / why is it bouncing", it's the right one.

## How to use this skill

1. Read the routing table below and load the **one** resource that matches the question. Don't load everything — each resource is self-contained.
2. For numbers, limits, and benchmarks, `email-infra-reference.md` is the single source of truth — never invent values.
3. When diagnosing a live problem, start from the symptom (spam / bounce / blacklist / not sending) and follow the decision tree.
4. GT runs this on **EmailBison** as the sending platform; the automation and audit workflows use EmailBison specifics as a worked example. The concepts, thresholds, and diagnostics apply to any ESP — adapt tool-specific steps to your own stack.

## Routing Table

| Question | Load |
|----------|------|
| Complete setup guide, domains, DNS, warmup, monitoring | Read `resources/email-infra-guide.md` |
| Ideating or researching new domain names, naming patterns, what to avoid in a domain | Read `resources/domain-research.md` |
| Step-by-step walkthroughs, video tutorial references | Read `resources/email-infra-step-by-step.md` |
| Diagnosis, DNS issues, warmup problems, blacklist recovery | Read `resources/email-infra-troubleshooting.md` |
| Auditing bounces or blacklists, finding where a bounce comes from, categorizing bounces, soft vs hard bounce codes, root-cause diagnosis | Read `resources/blacklist-bounce-audit.md` |
| General deliverability concepts, bounce management, compliance | Read `resources/deliverability-guide.md` |
| Send limits, metrics, warmup timeline, DNS records, ramp schedule | Read `resources/email-infra-reference.md` |
| Automating inbox management, deliverability dashboard, inbox tagging/classification, scaling monitoring across many inboxes | Read `resources/email-infra-automation.md` |

## Decision Tree

```
User Request
├─ Ideating / researching new domain names? → domain-research.md
├─ Domain setup / DNS / mailbox provisioning? → email-infra-guide.md
├─ Step-by-step walkthrough needed? → email-infra-step-by-step.md
├─ Something not working / going to spam / blacklisted? → email-infra-troubleshooting.md
├─ Auditing a bounce/blacklist problem, finding the root cause? → blacklist-bounce-audit.md
├─ General deliverability concepts / bounce / compliance? → deliverability-guide.md
├─ Automating inbox management across many inboxes / dashboard / auto-tagging? → email-infra-automation.md
└─ Numbers, limits, metrics, timelines? → email-infra-reference.md
```

## Critical Rules (Never Break)

1. Never use primary domain for cold outreach
2. Max 2 mailboxes per domain
3. One domain = one workspace
4. Use multiple registrars (no single point of failure)
5. Warm up minimum 14 days before sending — ideally 3 weeks
6. Never disable warm-up once campaigns are running
7. Start conservative, scale gradually

## Infrastructure Sizing Formula

- Monthly goal ÷ 20 working days = daily volume needed
- Daily volume ÷ 20–25 per mailbox = mailboxes needed
- Mailboxes × 1.5 (buffer) ÷ 2 = domains needed
- Provider split: 60% Google Workspace, 40% Microsoft 365

> For all send limits, healthy metrics, warmup timelines, ramp schedules, and reference numbers → see `resources/email-infra-reference.md`
