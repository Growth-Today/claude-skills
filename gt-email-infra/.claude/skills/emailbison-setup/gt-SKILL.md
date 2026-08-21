---
name: email-infra-emailbison-setup
description: "Set up and connect sending inboxes in EmailBison (infrastructure side). Use for connecting Google, Microsoft, and custom-SMTP inboxes to EmailBison, warmup configuration, advanced deliverability settings, custom tracking domains, and vendor-managed versus in-house setup. Triggers on EmailBison setup, Bison connect inboxes, Bison warmup, bisonsphere, EmailGuard placement test, ScaledMail Bison, add sender emails. Do NOT use for writing sequences or copy (use gt-cold-email), buying domains (use the domain-research sub-skill), or another sequencer (use instantly-setup / smartlead-setup / lemlist-setup)."
---

# EmailBison Inbox Setup · [Sales Ops]

> **⚠️ EmailBison is being retired.** Growth Today is moving to Instantly. The migration is
> approved and under way, and all EmailBison campaigns finish by **end of August 2026**, after
> which Bison is switched off. Keep using this sub-skill for campaigns still running on Bison;
> **start anything new in Instantly** (the instantly-setup sub-skill). Do not invest further
> effort in Bison-specific process.


> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §5 · `{SKILL_BASE}/resources/approved-vendors.md` · **Related:** provisioning, warmup-golive, campaign-building.

Set up sending inboxes in **EmailBison** (one of the sequencers Growth Today runs). Infrastructure/inbox side only, sequences and copy live in `gt-cold-email`. Numbers in `{SKILL_BASE}/resources/reference.md` §1, §5. Steps below reflect the EmailBison / Bisonsphere help center; where a value is set only in the app UI, that is flagged.

---

## Part 0, Who does the setup (two paths)

**Default: a vendor does it.** An approved vendor (e.g. ScaledMail, see `{SKILL_BASE}/resources/approved-vendors.md`) buys the domains, creates and configures the mailboxes, sets DNS, and does first QA. Growth Today hands off the domain-research output (the domain-research sub-skill) plus a brief, then verifies on delivery.

**Fallback: in-house.** Connect and configure manually (Parts 2–4).

**Growth Today always owns:** QA, warmup config, placement tests, and the handoff to the GTM Engineer.

---

## Part 1, Connecting inboxes

Email Accounts → **Connect email account** → pick the provider.

**Google Workspace**: **OAuth only** (no app-password path). Connect → Google Workspace → **Google OAuth** → copy the Client ID → Google Admin Console → Add app → OAuth App Name/Client ID → select **EmailBison** → mark **Trusted** → back in Bison **Sign in with Google**. **No bulk Google** connection (Google captchas block it), one-by-one.

**Microsoft / Outlook 365**: OAuth, with prerequisites:
- **First** enable SMTP AUTH: Exchange Admin Centre → Settings → Mail flow → ensure *"Turn off SMTP AUTH protocol for your organization"* is **NOT** checked.
- **Admin approval (since Dec 2025):** assign the **Cloud Application Administrator** role to the mailbox (admin.cloud.microsoft → Users → Manage roles → Identity → Cloud Application Administrator). No tenant-wide bulk path.
- **90-day token expiry:** Microsoft tokens must be refreshed every 90 days, reconnect on a schedule (Bison can export accounts with expired tokens; a bulk reconnect uploader exists).
- **Bulk Microsoft:** supported via Bison's native bulk-uploader tool (CSV `name,email,password`; for tenant consent add one account with the Cloud App Admin role and `use_as_admin=true`).

**Custom SMTP**: Connect email account → **Custom Provider** → enter your provider's SMTP + IMAP host/port/credentials (host/port table in `{SKILL_BASE}/resources/reference.md`; Bison enters both together). Bulk via **Bulk Upload Custom Provider** (sample CSV). **Amazon SES is not recommended** (violates AWS ToS for cold; Bison can't use different SMTP/IMAP usernames on one inbox).

> A sender email can exist in **one workspace at a time**. Provider tags (Google/Microsoft) are auto-applied.

---

## Part 2, Warmup

**You set only the max daily warmup limit, Bison automates the rest** (ramp, reply rate, timing). Set the max to the Growth Today target in `{SKILL_BASE}/resources/reference.md` §1 (Google warmup ~30, Microsoft ~15 for a fully-warmed sending inbox; during warming cold is 0–1).

- **Ramp (automatic):** starts ~2/day, increases ~50%/day to your max, then flexes ~±20%/day to mimic human variation.
- **Ratio:** Google **1.5:1** warmup-to-cold; Microsoft stricter (Bison's own guidance: 2–4 warmup/day, max 3 warmup replies), keep aligned with `reference.md` §1.
- **Reply rate** is under Advanced Settings but Bison strongly advises leaving it at default.
- **Duration:** warm **≥ 21 days / 3 weeks** before any cold send (`reference.md` §5); monitor scores over 3 / 7 / 10–14-day windows; if low, cut cold temporarily and raise volume only as scores recover.
- **Pool + filter phrase:** the warmup pool is private/self-healing; the filter phrase is a fixed per-workspace random string (not editable), no deliverability impact.

> **EmailBison cold-limit floor = 1 (not 0).** An unhealthy inbox is throttled to 1, not silenced, a lead on it keeps getting sent from it (the failover gap; see the dashboard-reading and campaign-building sub-skills). Confirm the current app behavior, as this is a Growth Today operational finding, not a documented help-center value.

---

## Part 3, Advanced deliverability

- **Open tracking:** OFF. Bison strongly advises against it, enabling it forces emails to **HTML-only** and requires a custom tracking domain, both of which hurt placement. Use **reply rate** as the primary metric.
- **Unsubscribe links:** OFF by default, they force HTML and require a tracking domain. Use a **plain-text opt-out line** instead ("not interested? just reply 'no'").
- **No links / no custom tracking domain** in cold email by default (the provisioning sub-skill).
- **First email plain text** (the warmup-golive sub-skill launch gate).
- **ESP routing:** decide from the dashboard matrix (the campaign-building sub-skill), not a hard ESP-matching rule.
- **Campaign schedule** defaults to weekdays 8am–5pm EST, set the correct timezone + a randomized send interval for the segment.

---

## Part 4, Custom tracking domain (only if a client insists)

**Growth Today default = none.** Only if required: Settings → **Custom Tracking Domains** → **Create Tracking Domain** → follow the in-app CNAME + verification flow (the exact CNAME host/target is shown in the app). Dedicated, never-shared.

---

## Part 5, Placement tests

Run **through the EmailGuard integration** (requires an active paid EmailGuard plan + EmailGuard connected to the Bison workspace + a launched campaign): open the campaign → **Inbox Placement Tests** → **New Inbox Placement Test** → run → View Results. Complements Growth Today's own dashboard placement tests (the dashboard-reading sub-skill).

---

## ✅ EMAILBISON SETUP CHECKLIST (copy-paste)

```
CONNECT
[ ] Google via OAuth (one-by-one; no bulk); app marked Trusted in Google Admin
[ ] Microsoft: SMTP AUTH enabled, Cloud App Admin role assigned, connected via OAuth
[ ] Microsoft 90-day token refresh scheduled
[ ] Custom SMTP: host/port + IMAP entered; no Amazon SES
[ ] Inboxes tagged; correct single workspace

WARMUP
[ ] Max daily warmup limit set to GT target (reference §1); Bison automates ramp/reply/timing
[ ] Warmed >= 21 days; scores healthy on 3/7/10-14d windows
[ ] Cold limit correct per state (Active Google 20 / Outlook 5; unhealthy throttled to 1)

DELIVERABILITY
[ ] Open tracking OFF; no unsubscribe link (plain-text opt-out); first email plain text
[ ] No custom tracking domain (unless client insists -> dedicated)
[ ] Correct timezone + randomized send interval
[ ] ESP routing from the dashboard matrix, not hard-coded

VERIFY
[ ] MX/SPF/DKIM/DMARC verified (the provisioning sub-skill)
[ ] EmailGuard placement tests set up
[ ] Cross-sequencer: if an inbox is also used in Lemlist, set Bison cold to 1 and tag "Lemlist"
[ ] GTM Engineer + AM notified inboxes are ready
```

---

> **Internal reference (Growth Today team).** In-house step-by-step SOP (access-gated; do not delete, referenced by this skill): [MASTER Setting Up Domains and Inboxes with ScaledMail + Bison](https://app.notion.com/p/growth-today/MASTER-Setting-Up-Domains-and-Inboxes-with-ScaledMail-Bison-14899b4b261980d2b941ee3c39918ef9) and [How to Connect Email Inboxes, Start Warmup & Configure Account Settings (Bison)](https://app.notion.com/p/growth-today/How-to-Connect-the-Email-Inboxes-Start-the-Email-Warmup-and-Configure-Account-Settings-Bison-2c699b4b26198027b308d4a5750a4c9e). This sub-skill is the primary source going forward.

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
