---
name: email-infra-provisioning
description: "Provision cold-email mailboxes and configure DNS and authentication. Use for Google Workspace, Microsoft 365 and custom-SMTP mailbox setup, MX/SPF/DKIM/DMARC records, masking versus redirect, custom tracking domains, and DNS-drift monitoring via the dns-auth-audit playbook. Triggers on mailbox setup, DNS setup, MX, SPF, DKIM, DMARC, check my DNS, verify SPF, DMARC policy, p=reject, DNS drift, provisioning, masking, redirect, tracking domain, Google Workspace, Microsoft 365. Do NOT use for buying domains (use the domain-research sub-skill), Instantly inbox connection (use the instantly-setup sub-skill), or warmup (use the warmup-golive sub-skill)."
---

# Provisioning, DNS & Authentication · [Sales Ops]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §4, §6 · `{SKILL_BASE}/resources/approved-vendors.md` · **Related:** domain-research, warmup-golive, instantly-setup.

Turn purchased domains (the domain-research sub-skill) into sending-ready mailboxes with correct authentication. This is where two of our biggest historical mistakes live, **bare redirects** and **default tracking domains**, so read the "never" boxes. Numbers in `{SKILL_BASE}/resources/reference.md` §6; vendors in `{SKILL_BASE}/resources/approved-vendors.md`.

---

## Part 1, Mailboxes

- **Mailboxes per domain (average): Google 2–3, Microsoft up to ~25.** Google stays lean for deliverability; Microsoft can host many per domain. Verify the per-provider density on scale-ups.
- **One domain = one workspace.**
- **Real first-name addresses:** `alex@`, `sarah@`, `james@`, keep names consistent across domains. **Never** `sales@`, `info@`, `noreply@`, `hello@`, `outreach@`.
- **Profile picture** (professional headshot) on every mailbox, improves deliverability and reply rate; don't skip.
- **Provider split: ask, don't assume.** There is no house mix — it's a per-client decision, and it moves the mailbox count more than the monthly goal does (`reference.md` §4). Get it in writing before you size the build.

**Google Workspace (Business Starter):** add the secondary domain → verify via TXT → create the 2 users → configure DNS (Part 3).

**Microsoft 365 (Business Basic):** add domain → verify via TXT → create users → **enable Authenticated SMTP + IMAP** (Admin Center → Users → Mail → Manage email apps) → **wait ~1 hour** before connecting to the sequencer. Microsoft connects **one-by-one** (no bulk import).

**Custom SMTP vendors** (Winnr, MissionInbox, ScaledMail, InboxedUp, Lunatro/Azure, Maildoso, see approved-vendors): the vendor provisions mailboxes + SMTP/IMAP; you still verify DNS/auth (Part 3) and the destination rule (Part 2).

---

## Part 2, Destination: masking or a real landing page, NEVER a bare redirect

> **🔴 NEVER point a secondary domain at the main site with a bare 301/302 redirect.** Blocklists follow the redirect to the final site; many secondaries → one site is the exact bulk-sender fingerprint, and it can get domains listed *before any send*.
>
> **Current state (Aug 2026): GT runs no redirects for clients**, so this is a standard we are already holding — treat the check below as a confirmation, not a live defect hunt. What *is* open is masking: Instantly has no built-in masking, so moving off EmailBison removes what we had. Owner: Fezekile (`approved-vendors.md`).

**Do instead:**
- **Masking** through an approved service (e.g. EmailGuard), **or**
- a **real, distinct landing page** with clean content. Scaledmail currently does this for all client domains.

**Vet the masking service** so it does not mark client content as duplicate to Google (an SEO hit for the client). No shared redirect IPs from the registrar/DNS provider, dedicated masking proxy or dedicated landing pages only.

> **🔴 No custom tracking domain and no links in cold email by default.** Tracking domains and click-wrapped links are strong spam/SEG triggers. Share via LinkedIn or an unlinked URL. Only a client who *strongly insists* gets a dedicated, never-shared tracking domain, phased in.

---

## Part 3, DNS & authentication (all 4 records)

Every domain needs **MX, SPF, DKIM, DMARC**. Missing one can bin your mail. Details in `reference.md` §6.

**SPF** (only ONE record per domain; keep total DNS lookups ≤ 10):
- Google: `v=spf1 include:_spf.google.com ~all`
- Microsoft: `v=spf1 include:spf.protection.outlook.com ~all`
- If a registrar auto-created a second SPF (common), delete the extra.

**DKIM:**
- Google: generate in Admin → Apps → Gmail → Authenticate Email, add the TXT, then Start Authentication.
- Microsoft: two CNAMEs (`selector1._domainkey`, `selector2._domainkey`).
- Copy the exact key, no stray spaces or truncation.

**DMARC** (add manually, never auto-created). **`p=reject` is the GT standard** — these are
dedicated cold-sending domains we fully control, so there is no legitimate mail to break and no
reason to sit in monitor mode:
```
Host: _dmarc
Value: v=DMARC1; p=reject; rua=mailto:dmarc@yourdomain.com
```
Use `p=none` only as a short verification phase during first setup, then move to `p=reject`.
(Google, Yahoo and Microsoft still only *require* `p=none`; enforcement is best practice and is
what GT already runs in production.)

**Verify — run the playbook, don't click through a web tool:**

```bash
cd {SKILL_BASE}/playbooks/dns-auth-audit/scripts
uv run execute.py newdomain.com anotherdomain.com --csv <client>_baseline.csv
```

It checks all four records plus two things a manual pass reliably misses: a **second SPF record**
(both get ignored, while every UI tool still shows a green tick) and an **over-budget include chain**
(more than 10 lookups is a permerror under RFC 7208). It also flags stray Lync/Skype SRV records
copy-pasted from the Microsoft 365 guide.

Keep the CSV. It is the baseline Part 4 diffs against.

By hand, if you must: `dig TXT yourdomain.com` (SPF), headers show `dkim=pass`,
`dig TXT _dmarc.yourdomain.com` (DMARC). Inside a sequencer? Use its built-in domain check.

---

## Part 4, Guard against silent DNS drift

Getting it right at setup isn't enough (§6). Treat a broken auth record as **P0** — dead auth means mail goes in the bin.

**The email infra management system owns the scheduled weekly re-check** — read its result in the DNS/auth-health panel (the dashboard-reading sub-skill), and do not build a competing scheduler.

What you *can* run on demand, on any domain, without credentials:

```bash
cd {SKILL_BASE}/playbooks/dns-auth-audit/scripts
uv run after.py --csv <client>_baseline.csv
```

This re-queries every domain in the baseline and reports each record as FIXED, STILL FAIL,
REGRESSED or CHANGED. **REGRESSED is the alarm** — a record that was healthy and is now broken
means the provider changed something underneath you, and nothing in the sequencer will tell you.

---

## Part 5, Connect to the sequencer

Use the matching setup sub-skill for the full connect + warmup flow per platform: emailbison-setup, instantly-setup, smartlead-setup, or lemlist-setup (see `{SKILL_BASE}/resources/approved-vendors.md`).

- **Google:** OAuth (recommended) or app password; bulk import supported for 10+.
- **Microsoft:** one-by-one only; confirm SMTP enabled and the 1-hour window elapsed; consent on behalf of the org.
- After connecting, **at first setup only**: set the starting send limits by state (`reference.md` §1), tag by client/domain/provider/region, and **leave open tracking OFF**. Once the inbox is live and the email infra management system is classifying it, limits and tags are **owned by the email infra management system** — see the read-only boundary in the root skill.

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
[ ] Mailboxes/domain within provider density (Google ~2–3, Microsoft ~25)
[ ] Real first-name addresses (no sales@/info@/noreply@)
[ ] Consistent names across domains
[ ] Professional profile picture on each mailbox
[ ] (Microsoft) Authenticated SMTP + IMAP enabled, waited ~1 hour

DESTINATION
[ ] Masking or a real landing page set up, NOT a bare 301/302 redirect
[ ] Masking service vetted (no duplicate-content SEO hit; no shared redirect IPs)
[ ] No custom tracking domain, no links in cold email (unless client insists → dedicated)

DNS / AUTH
[ ] MX set
[ ] Exactly ONE SPF record (≤ 10 lookups)
[ ] DKIM added, exact key, authentication started
[ ] DMARC added manually, p=reject (p=none only as a short verification phase)
[ ] Verified (dig / headers / sequencer domain test)

ONGOING
[ ] Domain enrolled in the DNS/auth-drift re-check (the dashboard-reading sub-skill)
[ ] Connected to the sequencer; open tracking OFF; tags set
[ ] Handed to the warmup-golive sub-skill
```

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
