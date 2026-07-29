---
name: email-infra-provisioning
description: "Provision cold-email mailboxes and configure DNS and authentication. Use for Google Workspace, Microsoft 365, and custom-SMTP mailbox setup, MX/SPF/DKIM/DMARC records, masking versus redirect, custom tracking domains, and DNS-drift monitoring. Triggers on mailbox setup, DNS setup, MX, SPF, DKIM, DMARC, provisioning, masking, redirect, tracking domain, Google Workspace, Microsoft 365. Do NOT use for buying domains (use the domain-research sub-skill), Instantly inbox connection (use the instantly-setup sub-skill), or warmup (use the warmup-golive sub-skill)."
---

# Provisioning, DNS & Authentication  ·  [Sales Ops]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §4, §6 · `{SKILL_BASE}/resources/approved-vendors.md`  ·  **Related:** domain-research, warmup-golive, instantly-setup.

Turn purchased domains (the domain-research sub-skill) into sending-ready mailboxes with correct authentication. This is where two of our biggest historical mistakes live — **bare redirects** and **default tracking domains** — so read the "never" boxes. Numbers in `{SKILL_BASE}/resources/reference.md` §6; vendors in `{SKILL_BASE}/resources/approved-vendors.md`.

---

## Part 1 — Mailboxes

- **Max 2 mailboxes per domain** (hard rule — verify it never drifts above 2 during scale-ups).
- **One domain = one workspace.**
- **Real first-name addresses:** `alex@`, `sarah@`, `james@` — keep names consistent across domains. **Never** `sales@`, `info@`, `noreply@`, `hello@`, `outreach@`.
- **Profile picture** (professional headshot) on every mailbox — improves deliverability and reply rate; don't skip.
- **Provider split 60% Google / 40% Microsoft** (`reference.md` §4).

**Google Workspace (Business Starter):** add the secondary domain → verify via TXT → create the 2 users → configure DNS (Part 3).

**Microsoft 365 (Business Basic):** add domain → verify via TXT → create users → **enable Authenticated SMTP + IMAP** (Admin Center → Users → Mail → Manage email apps) → **wait ~1 hour** before connecting to the sequencer. Microsoft connects **one-by-one** (no bulk import).

**Custom SMTP vendors** (Winnr, MissionInbox, ScaledMail, InboxedUp, Lunatro/Azure, Maildoso — see approved-vendors): the vendor provisions mailboxes + SMTP/IMAP; you still verify DNS/auth (Part 3) and the destination rule (Part 2).

---

## Part 2 — Destination: masking or a real landing page, NEVER a bare redirect

> **🔴 NEVER point a secondary domain at the main site with a bare 301/302 redirect.** Blocklists (SURBL) follow the redirect to the final site; many secondaries → one site is the exact spam fingerprint, and it gets domains listed *before any send*. It is the single most common pre-send blocklisting cause.

**Do instead:**
- **Masking** through an approved service (e.g. EmailGuard), **or**
- a **real, distinct landing page** with clean content.

**Vet the masking service** so it does not mark client content as duplicate to Google (an SEO hit for the client). No shared redirect IPs from the registrar/DNS provider — dedicated masking proxy or dedicated landing pages only.

> **🔴 No custom tracking domain and no links in cold email by default.** Tracking domains and click-wrapped links are strong spam/SEG triggers. Share via LinkedIn or an unlinked URL. Only a client who *strongly insists* gets a dedicated, never-shared tracking domain, phased in.

---

## Part 3 — DNS & authentication (all 4 records)

Every domain needs **MX, SPF, DKIM, DMARC**. Missing one can bin your mail. Details in `reference.md` §6.

**SPF** (only ONE record per domain; keep total DNS lookups ≤ 10):
- Google: `v=spf1 include:_spf.google.com ~all`
- Microsoft: `v=spf1 include:spf.protection.outlook.com ~all`
- If a registrar auto-created a second SPF (common), delete the extra.

**DKIM:**
- Google: generate in Admin → Apps → Gmail → Authenticate Email, add the TXT, then Start Authentication.
- Microsoft: two CNAMEs (`selector1._domainkey`, `selector2._domainkey`).
- Copy the exact key — no stray spaces or truncation.

**DMARC** (add manually — never auto-created). Start in monitor mode and tighten later:
```
Host: _dmarc
Value: v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com
```

**Verify:** `dig TXT yourdomain.com` (SPF), email headers show `dkim=pass`, `dig TXT _dmarc.yourdomain.com` (DMARC); or the sequencer's built-in domain test + a placement/mail test.

---

## Part 4 — Guard against silent DNS drift

Correct-at-setup is not enough — the real risk is a provider **quietly breaking a record later**, which silently kills deliverability. Re-check MX/SPF/DKIM/DMARC on a schedule (the DNS/auth-health panel in the dashboard-reading sub-skill surfaces broken/never-checked records and should alert on a break). Treat a broken auth record as **P0**.

---

## Part 5 — Connect to the sequencer

Platform-aware (`approved-vendors.md`): EmailBison today, migrating to Instantly, Smartlead benchmarked.

- **Google:** OAuth (recommended) or app password; bulk import supported for 10+.
- **Microsoft:** one-by-one only; confirm SMTP enabled and the 1-hour window elapsed; consent on behalf of the org.
- After connecting: set send limits by state (`reference.md` §1), tag by client/domain/provider/region, and **leave open tracking OFF**.

> **On Instantly?** For the full Instantly connect + warmup + advanced-deliverability setup (vendor-managed or in-house), use **the instantly-setup sub-skill**.

---

## Troubleshooting (folded in)

| Symptom | Likely cause → fix |
|---|---|
| "DNS records not found" | Not propagated / not saved → wait (15 min–48 h), verify saved in the correct domain, lower TTL to 300, flush cache |
| "Multiple SPF records" | Two `v=spf1` TXT records → delete the extra, keep one (common with some registrars) |
| "DKIM authentication failed" | Wrong/absent key or host → regenerate, paste exact value, correct host (`google._domainkey` / `selector1._domainkey`), wait up to 24 h |
| "DMARC missing" | Never auto-created → add the `_dmarc` TXT above |
| Microsoft won't connect | SMTP+IMAP not both enabled, or 1-hour window not elapsed → enable both, wait, retry (incognito) |
| Warmup red / disabled | Usually a DNS/bounce problem → run the domain test, fix DNS, check blacklist (the bounce-audit sub-skill), re-enable warmup |

---

## ✅ PROVISIONING CHECKLIST (copy-paste per domain)

```
MAILBOXES
[ ] ≤ 2 mailboxes on the domain
[ ] Real first-name addresses (no sales@/info@/noreply@)
[ ] Consistent names across domains
[ ] Professional profile picture on each mailbox
[ ] (Microsoft) Authenticated SMTP + IMAP enabled, waited ~1 hour

DESTINATION
[ ] Masking or a real landing page set up — NOT a bare 301/302 redirect
[ ] Masking service vetted (no duplicate-content SEO hit; no shared redirect IPs)
[ ] No custom tracking domain, no links in cold email (unless client insists → dedicated)

DNS / AUTH
[ ] MX set
[ ] Exactly ONE SPF record (≤ 10 lookups)
[ ] DKIM added, exact key, authentication started
[ ] DMARC added manually (p=none to start)
[ ] Verified (dig / headers / sequencer domain test)

ONGOING
[ ] Domain enrolled in the DNS/auth-drift re-check (the dashboard-reading sub-skill)
[ ] Connected to the sequencer; open tracking OFF; tags set
[ ] Handed to the warmup-golive sub-skill
```

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
