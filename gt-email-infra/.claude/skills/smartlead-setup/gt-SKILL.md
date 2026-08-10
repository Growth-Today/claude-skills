---
name: email-infra-smartlead-setup
description: "Set up and connect sending inboxes in Smartlead (infrastructure side). Use for connecting Google, Microsoft, and custom-SMTP inboxes to Smartlead, warmup configuration, advanced deliverability settings, custom tracking domains, SmartDelivery placement tests, and vendor-managed versus in-house setup. Triggers on Smartlead setup, Smartlead connect inboxes, Smartlead warmup, SmartDelivery, Smartlead custom tracking domain. Do NOT use for writing sequences or copy (use gt-cold-email), buying domains (use the domain-research sub-skill), or another sequencer (use instantly-setup / emailbison-setup / lemlist-setup)."
---

# Smartlead Inbox Setup · [Sales Ops]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §5 · `{SKILL_BASE}/resources/approved-vendors.md` · **Related:** provisioning, warmup-golive, campaign-building.

Set up sending inboxes in **Smartlead** (one of the sequencers Growth Today runs). Infrastructure/inbox side only, sequences and copy live in `gt-cold-email`. Numbers in `{SKILL_BASE}/resources/reference.md` §1, §5. Steps reflect the Smartlead help center; app-only values are flagged.

---

## Part 0, Who does the setup

**Default: a vendor** (e.g. ScaledMail) buys domains, creates/configures mailboxes, sets DNS, first QA; Growth Today hands off the domain-research output plus a brief and verifies. **Fallback: in-house** (Parts 1–4). Growth Today always owns QA, warmup config, placement tests, and the GTM handoff.

---

## Part 1, Connecting inboxes

Email Accounts → **Add Account(s) / + Connect Mailbox** → pick the provider.

**Google Workspace**: **OAuth (recommended)**, or app-password (enable 2-Step Verification first, generate an app password for **Mail** / **Other**). Gmail values if using SMTP: SMTP `smtp.gmail.com:465` (SSL), IMAP `imap.gmail.com:993` (SSL); **both required**. **Bulk CSV** supported for Google (upload with validation preview).

**Microsoft / Outlook 365**: **one-by-one, OAuth only** (no bulk CSV for Outlook):
- **First** enable Authenticated SMTP + IMAP: admin.microsoft.com → Users → Active Users → user → Mail → Manage email apps → check **Authenticated SMTP** + **IMAP** → Save. **Wait 20–30 minutes.**
- Connect → **Smartlead's Infrastructure** → Outlook → sign in → **Accept** permissions → green **Connected**.
- Org-level: Smartlead also supports **Private Infrastructure OAuth** with your own Azure app (register app, redirect `https://server.intellioauth.com/api/email-account/microsoft/callback`, grant admin consent, paste Client ID + secret under Settings → OAuth Configuration).

**Custom SMTP**: enter your provider's host/port (SMTP 587 STARTTLS or 465 SSL; IMAP 993 SSL); both SMTP + IMAP required (`{SKILL_BASE}/resources/reference.md` host table).

---

## Part 2, Warmup

Email Accounts → select account → **Warm-up** tab → configure → **Enable Warmup**.

- **Total Daily Emails:** 10–20 while campaigns run (raise after a campaign completes). Keep aligned with `{SKILL_BASE}/resources/reference.md` §1 targets.
- **Daily Ramp Up:** enable for fresh domains (must be turned on **at the same time** as warmup); disable if already warmed/migrating.
- **Reply Rate:** **70-75%** (don't set up less than 70%).
- **Randomise Warmup Numbers:** on (human-like variation).
- **Auto-Adjust Warmup/Sending Ratio:** optional smart-adjust, when on an active campaign the AI trims warmup (~7–10) and manages the ratio automatically.
- **Weekdays-only** toggle available.
- **Warmup identifier:** unique 2-word phrase used as an inbox filter/rule (no visible subject tag).
- **Duration:** warm **≥ 2 weeks** (Growth Today recommends 3–4, `reference.md` §5), Smartlead doesn't publish a minimum, so use the GT gate.

---

## Part 3, Advanced deliverability (campaign options)

- **Plain text (no HTML)**: toggle in **draft only** (can't change after start). Enabling it **auto-disables open tracking, click tracking, and unsubscribe links.** GT default: first email plain text.
- **Disable open tracking / click tracking**: available separately.
- **Enhanced Email Sending (ESP matching)**: provider matching exists, but decide from the dashboard matrix (the campaign-building sub-skill), not as a fixed rule.
- **Company-level auto-pause**: stop messaging other people at a company once one replies.
- **Stop conditions**: halt on reply / click / open.
- **High Bounce Rate Auto-Protection**: auto-pauses a campaign over a bounce threshold (industry standard <5%; GT acts earlier, `reference.md` §3).
- **Unsubscribe Header**: one-click list-unsubscribe header; note it needs HTML, so it conflicts with full plain-text/"Optimize Email Delivery."
- **Send interval:** the campaign's "email sent every X" must be **≥ 2 minutes greater** than the mailbox-level minimum gap (≈5-min minimum) or sends get skipped; set a randomized interval + correct timezone.

---

## Part 4, Custom tracking domain (only if a client insists)

**Growth Today default = none.** If required: CNAME **Host `emailtracking`** → **Target `open.sleadtrack.com`** (TTL auto). In Smartlead: account settings → **Custom tracking domain** → enter `http://emailtracking.yourdomain` → **Verify CNAME**. One aged domain's `emailtracking.` subdomain can be reused across mailboxes. Dedicated, never-shared.

---

## Part 5, Placement tests (SmartDelivery)

Smartlead's built-in **SmartDelivery** runs manual + automated inbox-placement tests (inbox vs promotions vs spam), a content spam score, and infra insights (IP/domain reputation, auth health, blacklists). **7 free manual tests**, then a paid plan. Complements Growth Today's own dashboard placement tests (the dashboard-reading sub-skill).

---

## ✅ SMARTLEAD SETUP CHECKLIST (copy-paste)

```
CONNECT
[ ] Google via OAuth (or app-password with 2FA); bulk CSV if many
[ ] Microsoft: SMTP+IMAP enabled, waited 20-30 min, connected one-by-one via OAuth
[ ] Custom SMTP: host/port + IMAP entered (both required)
[ ] Inboxes tagged; correct workspace

WARMUP
[ ] Warmup enabled; Daily Ramp Up on (with warmup) for fresh domains; reply rate 20-30%
[ ] Total daily volume aligned with GT targets (reference §1); randomise on
[ ] Warmed >= 2 weeks (3-4 recommended)
[ ] Cold limit correct per state (Active Google 20 / Outlook 5)

DELIVERABILITY
[ ] First email plain text (set in draft); open + link tracking OFF
[ ] Company auto-pause on; stop-on-reply on; high-bounce auto-protection on
[ ] Send interval randomized (campaign interval >= mailbox min + 2 min); correct timezone
[ ] ESP routing from the dashboard matrix, not hard-coded
[ ] No custom tracking domain (unless client insists -> dedicated)

VERIFY
[ ] MX/SPF/DKIM/DMARC verified (the provisioning sub-skill)
[ ] SmartDelivery placement test run
[ ] GTM Engineer + AM notified inboxes are ready
```

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
