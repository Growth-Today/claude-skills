# Cold Email Deliverability & Compliance Guide

Deep reference for authentication setup, compliance requirements, bounce management, and blacklist monitoring. For send limits and healthy metrics → see [email-infra-reference.md](email-infra-reference.md).

---

## 1. Email Authentication

### SPF (Sender Policy Framework)

**What it does:** Tells receiving servers which IP addresses/servers are authorized to send email for your domain.

**Setup:**
1. Go to your DNS provider
2. Add a TXT record:
```
Host: @
Type: TXT
Value: v=spf1 include:_spf.google.com ~all
```

**For multiple providers:**
```
v=spf1 include:_spf.google.com include:spf.protection.outlook.com -all
```

**Common mistakes:**
- Multiple SPF records (only ONE allowed per domain — merge them)
- Using `+all` instead of `~all` or `-all`
- Exceeding 10 DNS lookups (each `include:` counts as one)

---

### DKIM (DomainKeys Identified Mail)

**What it does:** Adds a digital signature to outgoing emails proving they haven't been tampered with.

**Setup (Google Workspace):**
1. Google Admin Console → Apps → Gmail → Authenticate Email
2. Generate DKIM key (2048-bit recommended)
3. Add TXT record to DNS:
```
Host: google._domainkey
Type: TXT
Value: v=DKIM1; k=rsa; p=[your-public-key]
```
4. Back in Google Admin, click "Start Authentication"

**Verification:** Send test email, check headers for `dkim=pass`.

---

### DMARC (Domain-based Message Authentication)

**What it does:** Tells receiving servers what to do when SPF or DKIM fails, and where to send reports.

**Progressive setup:**
```
# Week 1-2: Monitor only (no blocking)
v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com

# Week 3-4: Quarantine failures
v=DMARC1; p=quarantine; pct=50; rua=mailto:dmarc@yourdomain.com

# Week 5+: Reject failures (full protection)
v=DMARC1; p=reject; rua=mailto:dmarc@yourdomain.com
```

Add as TXT record:
```
Host: _dmarc
Type: TXT
Value: v=DMARC1; p=reject; rua=mailto:dmarc@yourdomain.com
```

### Authentication Verification Checklist

- [ ] SPF: `dig TXT yourdomain.com` shows `v=spf1`
- [ ] DKIM: Email headers show `dkim=pass`
- [ ] DMARC: `dig TXT _dmarc.yourdomain.com` shows policy
- [ ] Use mail-tester.com or MXToolbox for full check

---

## 2. Inbox Placement

### Plain Text vs HTML

| Factor | Plain Text | HTML |
|---|---|---|
| Deliverability | Better | Worse (more spam signals) |
| Trust signal | Feels personal | Feels like marketing |
| Tracking | Limited (no pixel) | Open tracking possible |
| Rendering | Universal | Can break across clients |
| Cold email best practice | **Preferred** | Avoid for cold |

**Rule: Use plain text for cold email. Always.**

### Sending Time Optimization

- Send during **business hours in recipient's timezone** (9 AM – 5 PM)
- Peak windows: **8–10 AM** and **1–3 PM** (Tuesday–Thursday)
- Random delays between emails: 30–120 seconds
- Vary sending times slightly day-to-day (not always at 9:00 AM)

### Reply Rate Impact on Deliverability

Reply rate is the **single most powerful positive signal**:

| Reply Rate | Status |
|---|---|
| >15% | Excellent — strong positive reputation |
| >10% | Good — inbox placement stable |
| >5% | Minimum acceptable for sustained sending |
| <3% | Danger zone — deliverability will degrade |

**How replies help:** Creates a conversation (trust signal), recipients who reply rarely mark as spam, high replies offset occasional complaints.

---

## 3. Compliance

### CAN-SPAM (United States)

**Requirements:**
1. Accurate "From" and "Reply-To" headers
2. Non-deceptive subject lines
3. Identify as advertisement (flexibility on this)
4. Include valid physical postal address
5. Clear opt-out explanation
6. Honor opt-outs within 10 business days
7. Monitor compliance of third parties

**Penalties:** Up to $51,744 per email in violation.

**Key:** CAN-SPAM does NOT require prior consent. B2B cold email is compliant with unsubscribe + physical address.

---

### GDPR (EU/EEA/UK)

**Legal bases for B2B cold email:**

1. **Legitimate Interest (Article 6(1)(f))** — most common:
   - Conduct Legitimate Interest Assessment (LIA)
   - Email must be relevant to professional role
   - Easy opt-out required
   - Data sourced lawfully

2. **Consent (Article 6(1)(a))** — required in some countries (notably Germany)

**Country-specific:**

| Country | B2B Cold Email |
|---|---|
| UK | Generally permitted (legitimate interest) |
| France | Permitted if relevant to professional role |
| Germany | Very restrictive — consent generally required |
| Netherlands | Permitted with legitimate interest |
| Nordic | Generally permit with legitimate interest |

**Requirements:** Lawful basis, transparency, right to object, data minimization, right to erasure, record keeping, privacy notice, data source disclosure.

**Compliant footer:**
```
You're receiving this because of your role as [Role] at [Company].
To opt out, reply "unsubscribe" or click here: [link]
Privacy policy: [link]
```

**Penalties:** Up to 4% of global annual revenue or EUR 20M.

---

### RFC 8058: One-Click Unsubscribe

**Required since February 2024** for bulk senders (5,000+/day to Gmail/Yahoo).

```
List-Unsubscribe: <https://yourdomain.com/unsubscribe?id=token>, <mailto:unsubscribe@yourdomain.com>
List-Unsubscribe-Post: List-Unsubscribe=One-Click
```

Most cold email tools (Instantly, Smartlead, Lemlist) add these automatically.

---

## 4. Blacklist Monitoring

### Major Blacklists

| Blacklist | Severity | Impact |
|---|---|---|
| **Spamhaus ZEN** | Critical | Used by ~80% of ISPs |
| **Spamhaus DBL** | Critical | Domain-based |
| **Barracuda BRBL** | High | Corporate email gateways |
| **SpamCop** | Medium-High | Auto-expires 24–48 hrs |
| **SORBS** | Medium | Multiple lists |
| **URIBL / SURBL** | High | Checks domains in email body |

### How to Check

1. **MXToolbox**: mxtoolbox.com/blacklists.aspx (100+ blacklists)
2. **MultiRBL**: multirbl.valli.org (300+ blacklists)
3. **Google Postmaster Tools**: domain/IP reputation with Gmail
4. **Microsoft SNDS**: reputation with Outlook/Hotmail

**Frequency:** Daily during warmup, weekly during campaigns.

---

## 5. Bounce Management

### Hard vs Soft Bounces

| Type | Definition | Action |
|---|---|---|
| **Hard Bounce** (5xx) | Permanent failure — address invalid | Remove immediately, never retry |
| **Soft Bounce** (4xx) | Temporary failure — server issue | Retry 2–3 times over 24–72 hrs |

### Email Verification Tools

| Tool | Cost | Accuracy | Best For |
|---|---|---|---|
| **ZeroBounce** | $0.008/email | 98%+ | Comprehensive verification |
| **NeverBounce** | $0.008/email | 97%+ | Platform integrations |
| **Findymail** | ~$0.01/email | 99%+ B2B | Find + verify combined |
| **MillionVerifier** | $0.0005/email | 95%+ | Budget large lists |
| **Bouncer** | $0.008/email | 97%+ | EU-based (GDPR) |

### Verification Best Practices

1. **Verify 100% of emails before any campaign.** No exceptions.
2. **Re-verify lists older than 30 days.**
3. **Remove "unknown" and "catch-all" results** or treat with extreme caution.
4. **Remove role-based emails** (info@, admin@, sales@).
5. **Remove free email providers** for B2B outreach.

---

## Pre-Launch Checklist

- [ ] 3–5 outreach domains purchased (not primary domain)
- [ ] Domains aged 2+ weeks
- [ ] Google Workspace or Microsoft 365 on each domain
- [ ] 2 mailboxes per domain
- [ ] SPF, DKIM, DMARC configured for each domain
- [ ] Custom tracking domain (CNAME) per domain
- [ ] Warmup running on every mailbox (minimum 14 days, ideally 3 weeks)
- [ ] 100% email verification before loading campaigns
- [ ] Blacklist monitoring alerts set up
- [ ] Compliant templates (physical address, unsubscribe)
- [ ] Legitimate interest assessment (if emailing EU)

---

## Active Campaign Monitoring

- [ ] Sending volume within daily limits (see [email-infra-reference.md](email-infra-reference.md))
- [ ] Warmup tool running on all mailboxes
- [ ] Bounce rate below 3%
- [ ] Spam complaint rate below 0.1%
- [ ] Reply rate above 5%
- [ ] Blacklists checked weekly
- [ ] Google Postmaster + Microsoft SNDS reviewed weekly
- [ ] Plain text emails (no HTML/images)
- [ ] Sending during business hours in recipient's timezone
- [ ] Unsubscribes processed within 24 hours
- [ ] Mailbox rotation across campaigns
- [ ] Re-verify lists older than 30 days

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
