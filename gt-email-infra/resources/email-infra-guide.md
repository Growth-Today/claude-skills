---
name: email-infra
description: Plan, build, and maintain cold email sending infrastructure. Covers infrastructure sizing logic, domain acquisition strategy, workspace/mailbox creation (Google Workspace + Microsoft 365), DNS configuration, connecting to Instantly, warm-up, going live, and ongoing monitoring. Use when setting up cold outreach infrastructure or onboarding a new client's email infra.
---

# Cold Email Infrastructure — Guide

Complete guide to setting up and maintaining cold email sending infrastructure — from zero to live campaigns.

For all send limits, metrics, timelines, and reference numbers → see [email-infra-reference.md](email-infra-reference.md).
For detailed walkthroughs of each step → see [email-infra-step-by-step.md](email-infra-step-by-step.md).
For DNS issues and deliverability problems → see [email-infra-troubleshooting.md](email-infra-troubleshooting.md).

---

## The Redline (Follow In Order)

1. **Calculate** infrastructure needs
2. **Acquire** secondary domains
3. **Create** workspaces & mailboxes
4. **Configure** DNS (SPF, DKIM, DMARC)
5. **Connect** to sending platform (Instantly)
6. **Warm up** mailboxes (minimum 14 days, ideally 3 weeks)
7. **Go live** with conservative limits
8. **Monitor** and maintain ongoing

---

## Infrastructure Sizing

Work backwards: **Monthly goal → Daily volume → Mailboxes → Domains**

### Sizing Steps

1. Define monthly email goal
2. Divide by 20 working days = daily volume
3. Divide daily volume by 20 (conservative) or 25 (aggressive) = mailboxes
4. Multiply by 1.5 = mailboxes with buffer
5. Divide mailboxes by 2 = domains needed
6. Split 60% Google Workspace, 40% Microsoft 365

For sizing calculator and provider split rationale → see [email-infra-reference.md](email-infra-reference.md).

---

## Domain Acquisition

### Naming Patterns (Good)

For primary domain `acme.com`:
- Prefix: getacme.com, tryacme.com, goacme.com, hiacme.com, meetacme.com
- Suffix: acmehq.com, acmeco.com, acmegroup.com
- Team: teamacme.com, acme-team.com

### Naming Patterns (Bad)

- Random strings, misspellings, spammy words (deals, offers)
- Numbers, excessive hyphens

### TLD Rules

- **.com is king** — best deliverability and trust
- **.org** acceptable as secondary
- **Avoid** .io, .ai, .co for cold email

### Recommended Registrars

Spread purchases across multiple registrars — no single point of failure:
- **Cloudflare** — no markup, great DNS management
- **Namecheap** — affordable, good for bulk
- **GoDaddy** — widely used
- **Squarespace** (ex–Google Domains) — reliable
- **Porkbun** — cheap, good reputation

### Per-Domain Checklist

- [ ] Domain registered
- [ ] Auto-renew enabled
- [ ] Whois privacy enabled
- [ ] Logged in tracking spreadsheet

---

## Workspace & Mailbox Setup

### Google Workspace (~$6/user/month, Business Starter)

1. Create new workspace at workspace.google.com
2. Add secondary domain → verify ownership via TXT record
3. Create mailboxes (max 2 per domain, real names)
4. Configure DNS records (see DNS section)

### Microsoft 365 (~$6/user/month, Business Basic)

1. Purchase plan at microsoft.com/microsoft-365/business
2. Add secondary domain → verify ownership via TXT record
3. Create mailboxes (max 2 per domain, real names)
4. **Critical: Enable SMTP & IMAP** in Admin Center → Users → Active Users → Mail → Manage email apps
5. **Wait 1 hour** after enabling SMTP before connecting to Instantly

### Mailbox Naming

**Good:** Real first names — alex@, sarah@, michael@, james@, emma@, david@
**Bad:** sales@, info@, noreply@, hello@, outreach@

**Pro tip:** Keep names consistent across domains (alex@ on all your domains).

### Profile Pictures

Add a professional headshot to every mailbox. Improves deliverability and reply rates. Do not skip.

---

## DNS Configuration

Every domain needs **all four records**. Missing one can tank deliverability.

### SPF Records

- Google: `v=spf1 include:_spf.google.com ~all`
- Microsoft: `v=spf1 include:spf.protection.outlook.com ~all`
- **Only ONE SPF record per domain** — most common mistake

### DMARC Record

| Field | Value |
|---|---|
| Type | TXT |
| Host | _dmarc |
| Value | `v=DMARC1;p=none;sp=none;pct=100;rua=mailto:you@domain.com;ri=86400;aspf=r;adkim=r;fo=1` |

### Domain Forwarding

Redirect secondary domains → main website (301 permanent redirect). Makes domains look legitimate when prospects check.

### Custom Tracking Domain

CNAME record: `inst` → `prox.itrackly.com` (TTL 300)
Configure in Instantly → Settings → Custom Tracking Domain.
**Cloudflare users:** proxy must be OFF (grey cloud).

### Testing DNS

1. **Instantly:** Email Accounts → Test domain setup (easiest)
2. **MXToolbox:** mxtoolbox.com — MX, SPF, DMARC, blacklist
3. **Mail-Tester:** mail-tester.com — deliverability score (aim 8+/10)
4. **Google Postmaster Tools:** postmaster.google.com — Gmail reputation

---

## Connecting to Instantly

### Google Accounts (OAuth — Recommended)

1. Email Accounts → Add New → Google → OAuth
2. Copy Client ID → Google Workspace Admin → Security → API Controls → Manage App Access
3. Configure new app → paste Client ID → select "Instantly OAuth Email v1"
4. Scope: All users, Access: Trusted
5. Return to Instantly → Login to complete

### Microsoft Accounts (One-by-One Only)

1. Email Accounts → Add New → Microsoft
2. Confirm SMTP is enabled → sign in
3. **Check "Consent on behalf of your organization"**
4. Accept permissions

**Microsoft cannot be bulk imported.** Plan time accordingly.

### Post-Connection Settings

- **Daily send limits:** see [email-infra-reference.md](email-infra-reference.md)
- **Custom tracking domain:** Enable per account
- **Account tags:** Organize by client / domain / provider
- **Slow ramp:** Enable — starts at 2/day, increases by 2/day

---

## Going Live

### Deliverability Settings in Instantly

- **Text-only first email** — reduces spam filter triggers
- **Disable open tracking** — improves inbox placement
- **ESP matching** — Google sends to Gmail, Microsoft sends to Outlook
- **Limit emails per company** — 2–3 per company per day (workspace-wide)
- **Slow ramp** — enable for new accounts only

### First Campaign

- Start with **50–100 leads**
- Monitor 2–3 days before scaling
- Scale by adding mailboxes, not pushing limits higher

For ramp schedule and healthy metrics → see [email-infra-reference.md](email-infra-reference.md).

---

## Ongoing Monitoring

### Daily (5 min)

- Check bounce rates, reply rates, spam complaints
- Spot-check 2–3 warm-up emails
- Watch for blacklist alerts

### Weekly (15 min)

- Google Postmaster Tools + Microsoft SNDS
- MXToolbox blacklist check
- Compare week-over-week trends

### Monthly (30 min)

- Update suppression list, audit bounces
- Review domain reputation, clean old leads
- Rotate warm-up email content

### Quarterly (1 hour)

- Full DNS audit across all domains
- Infrastructure cost review
- Strategic capacity planning

For scaling rules and seasonal expectations → see [email-infra-reference.md](email-infra-reference.md).

---

## Infrastructure Tracking Spreadsheet

Maintain a spreadsheet with:

| Domain | Registrar | Provider | Mailbox 1 | Mailbox 2 | Admin Email | Status |
|---|---|---|---|---|---|---|
| acmehq.com | Cloudflare | Google | alex@acmehq.com | sarah@acmehq.com | admin@you.com | Active |
| getacme.com | Namecheap | Microsoft | alex@getacme.com | sarah@getacme.com | admin@you.com | Warming |

Track: domain, registrar, provider, mailboxes, admin email, warm-up status, health score.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
