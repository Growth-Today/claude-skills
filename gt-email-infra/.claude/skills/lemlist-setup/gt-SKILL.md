---
name: email-infra-lemlist-setup
description: "Set up and connect sending inboxes in Lemlist (infrastructure side), including its multichannel email + LinkedIn setup. Use for connecting Google, Microsoft, and custom-SMTP inboxes to Lemlist, lemwarm warmup, sending limits, ESP matching, inbox rotation, LinkedIn limits, blocklist/unsubscribe, and vendor-managed versus in-house setup. Triggers on Lemlist setup, lemwarm, Lemlist connect inboxes, Email Provider Matchmaker, Lemlist LinkedIn limits, Deliverability Hub. Do NOT use for writing sequences or copy (use gt-cold-email), buying domains (use the domain-research sub-skill), or another sequencer (use instantly-setup / emailbison-setup / smartlead-setup)."
---

# Lemlist Inbox Setup · [Sales Ops]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §5 · `{SKILL_BASE}/resources/approved-vendors.md` · **Related:** provisioning, warmup-golive, campaign-building.

> 🔒 **Read-only area.** Connecting an inbox to the sequencer is done from the **email infra management system**. Follow this sub-skill for the standard each inbox must meet and to read and verify live state (setup-audit rows 1–7); do not connect, reconnect or swap inboxes by hand.

Set up sending inboxes in **Lemlist** (one of the sequencers Growth Today runs). Lemlist is **multichannel** (email + LinkedIn), so this covers LinkedIn limits too. Infrastructure/inbox side only, sequences and copy live in `gt-cold-email`. Numbers in `{SKILL_BASE}/resources/reference.md` §1, §5.

---

## Part 0, Who does the setup

**Rule:** 1 Lemlist user = **5 campaign inboxes + 1 LinkedIn account** minimum.

**Default: a vendor** (e.g. ScaledMail) connects the inboxes to the users, send the vendor a brief ("connect these 5 inboxes for user X; do not remove them from Bison"). **Fallback: in-house** (Parts 1–4). Growth Today always owns QA, warmup, and the GTM handoff.

Also connect the **client's primary inbox** (to receive replies) but **keep its seat OFF**: we don't send from it. Turn the **active seat ON** for each campaign inbox.

---

## Part 1, Connecting inboxes + LinkedIn

Settings → Sending settings → **connect email address** → pick provider.
- **Google/Gmail:** OAuth + Gmail API (not SMTP, not app-password), grant all permission boxes. One at a time.
- **Microsoft/Outlook:** OAuth, enter credentials, accept permissions, one at a time. MFA/conditional-access can block it → have the client's IT admin allow Lemlist.
- **Custom SMTP/IMAP:** both required. STARTTLS: SMTP 587 / IMAP 143 (SSL off); or SSL: SMTP 465 / IMAP 993 (SSL on).

**Client LinkedIn:** send the client the connect instructions and follow up, it's a blocker for multichannel. LinkedIn limits per account: **20 invites/day, 30 messages/day, 30 profile visits/day, max 100 actions/day**; new accounts ramp from **2–5 invites/day**; only **3 custom-note invites/month** (standard invites unaffected).

---

## Part 2, Warmup (lemwarm)

> **Only use lemwarm if the inboxes are NOT already warmed in another tool.** If warmed elsewhere, skip.

- Lemwarm dashboard → Connect email → start.
- **Ramp:** lemwarm steps up on its own; set the **ceiling** to §1 `google_warmup` / `outlook_warmup` for the provider. Lemwarm emails **don't** count toward the Lemlist daily send limit, but keep **total per mailbox ≤ 60–70/day** (Lemlist + lemwarm + manual replies).
- **Duration:** warm **≥ 21 days / 3 weeks** (GT floor, `reference.md` §5). Lemlist's own deliverability-score gates: <65 pause & fix DNS; 65–90 warmup only; >90 ready for campaigns. That score is Lemlist's scale, not ours — it does not replace §2 `warmup_score_active`, which is what our classifier uses. Both have to clear.
- lemwarm is a **separate Lemlist product/plan**: confirm it's active for the account.

---

## Part 3, Sending limits + deliverability

Set on **each inbox and each user**:
- **Google 20/day, Microsoft 5/day** per inbox (align with `{SKILL_BASE}/resources/reference.md` §1).
- **Disable open/link tracking:** Campaign → Settings → Tracking (opens/clicks OFF; replies on). Note: enabling any tracking now **requires a Custom Tracking Domain**.
- **ESP matching (Email Provider Matchmaker):** enable at team level if the account has **both** a Google and a Microsoft mailbox (Settings → Sending settings → Deliverability boost). Use as a lever the dashboard matrix supports (the campaign-building sub-skill), not a blind rule.
- **Inbox rotation:** for multi-sender / higher volume, select multiple senders on the email step (round-robin); force a specific sender only where a named person must send a step.
- **First email plain text**, no links (the warmup-golive sub-skill launch gate).
- **Warning notifications ON:** high bounce rate + LinkedIn disconnection.

---

## Part 4, Blocklist, CRM, preferences

- **Blocklist/unsubscribe:** turn ON "add unsubscribes to blocklist automatically"; add opt-out keywords (unsubscribe; stop; remove; not interested; …). Upload the client's existing blocklist (customers, active deals) and exclude those domains from Clay tables to save credits. Ask the client to unsubscribe leads as replies come in.
- **CRM (HubSpot):** connect at **team level**; create contacts/companies on reply; map fields, users, activities; check Logs for sync errors.
- **Preferences:** set opportunity value (confirm ACV with the AM), correct timezone (EU vs US), AI auto-tag replies ON, AI Inbox Manager OFF, OOO auto-tag ON.
- **Custom tracking domain (only if a client insists):** CNAME **Host = a subdomain you choose** → **Target `custom.lemlist.com`** + a TXT verification record; Cloudflare set to DNS-only. GT default = none.

---

## Part 5, Cross-sequencer rule

If an inbox is used in Lemlist, prevent double-sending from another sequencer: set its cold send to **0 in Instantly / 1 in EmailBison** and **tag it "Lemlist."**

Placement/health: check the **Deliverability Hub** (delivery + bounce rate by provider/mailbox/domain, warmup score, manual inbox-placement tests, threshold alerts).

---

## ✅ LEMLIST SETUP CHECKLIST (copy-paste)

```
INBOXES & LINKEDIN
[ ] 5 campaign inboxes per user, active seat ON
[ ] Client primary inbox connected, seat OFF (receive-only)
[ ] Google 20/day, Microsoft 5/day set per inbox
[ ] LinkedIn: 20 invites / 30 msgs / 30 visits / max 100 actions/day; new accounts ramp 2-5 invites/day
[ ] Client connected LinkedIn (blocker for multichannel)

WARMUP
[ ] lemwarm ONLY if not warmed elsewhere; ceiling set from §1 `google_warmup` / `outlook_warmup`
[ ] Total per mailbox <= 60-70/day (Lemlist + lemwarm + manual)
[ ] Warmed >= 21 days; Lemlist deliverability score > 90 AND §2 `warmup_score_active` met

DELIVERABILITY
[ ] Open + link tracking OFF; first email plain text
[ ] ESP Matchmaker evaluated (needs a Google + a Microsoft inbox)
[ ] Inbox rotation set for multi-sender/high volume
[ ] Warning notifications ON (bounce, LinkedIn disconnect)
[ ] No custom tracking domain (unless client insists -> dedicated)
[ ] Cross-sequencer: cold 0 in Instantly / 1 in Bison, tag "Lemlist"

CRM & BLOCKLIST
[ ] HubSpot connected at team level; field/user/activity mapping; logs clean
[ ] Blocklist auto-add ON + opt-out keywords; client blocklist uploaded
[ ] Preferences: opportunity value, timezone, AI auto-tag on / Inbox Manager off
[ ] DNS verified (SPF/DKIM/DMARC) per inbox (the provisioning sub-skill)
[ ] GTM Engineer + AM notified inboxes are ready
```

---

> **Internal reference (Growth Today team).** In-house step-by-step SOP (access-gated; do not delete, referenced by this skill): [Lemlist Account Setup SOP](https://app.notion.com/p/growth-today/Lemlist-Account-Setup-SOP-38199b4b261981ce98dedb0d65d391be). This sub-skill is the primary source going forward; verify Lemlist figures in-product, as Lemlist revises these often.

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
