---
name: email-infra-instantly-setup
description: "Set up and connect sending inboxes in Instantly (infrastructure side). Use for connecting Google, Microsoft and custom-SMTP inboxes, warmup configuration, advanced deliverability settings, the required Unibox toggles (Save undelivered emails is off by default and gates what the reporting can see), and vendor-managed versus in-house setup. Triggers on Instantly setup, connect inboxes, Instantly warmup, advanced deliverability, Unibox, Unibox settings, save undelivered emails, show auto-replies, ScaledMail, IMAP SMTP host, provider matching. Do NOT use for writing sequences or copy (use gt-cold-email) or buying domains (use the domain-research sub-skill)."
---

# Instantly Inbox Setup · [Sales Ops]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §5 · `{SKILL_BASE}/resources/approved-vendors.md` · **Related:** provisioning, warmup-golive, campaign-building.

> 🔒 **Read-only area.** Connecting an inbox to the sequencer is done from the **email infra management system**. Follow this sub-skill for the standard each inbox must meet and to read and verify live state (setup-audit rows 1–7); do not connect, reconnect or swap inboxes by hand.

Set up sending inboxes in **Instantly** (one of the sequencers Growth Today runs). This is the **infrastructure / inbox side only** (connecting mailboxes, warmup, deliverability settings). Sequences and copy live in `gt-cold-email`. Numbers in `{SKILL_BASE}/resources/reference.md` §1, §5.

> **This sub-skill replaces the old "Setting up Domains & Inboxes with ScaledMail + Instantly" SOP.** Everything you need to execute is here; no separate SOP required.

---

## Part 0, Who does the setup (two paths)

**ScaledMail does it.** ScaledMail **buys the domains and connects the inboxes**, creates and configures the mailboxes, sets DNS, and does first QA. Growth Today keeps **domain research and verification only** — hand off the domain-research output plus a brief, then **verify on delivery**. Buying a batch ourselves at a single registrar is what we are moving away from: it produces exactly the bulk pattern spam filters look for (`reference.md` §9). Vendor domains cost a bit more (≈10% markup) but the purchase is **spread across registrars/time** for us, worth it.

**Fallback: in-house.** If we buy and build ourselves, Growth Today purchases the domains (the domain-research sub-skill), provisions mailboxes + DNS (the provisioning sub-skill), and connects them in Instantly manually (Parts 2–4 below). Full in-house step-by-step (Namecheap purchase → Instantly connect → warmup): **[MASTER Setting Up Domains and Inboxes with ScaledMail + Instantly](https://app.notion.com/p/growth-today/MASTER-Setting-Up-Domains-and-Inboxes-with-ScaledMail-Instantly-34599b4b261980c49775fa47c5c0e2a4)** (Growth Today internal, access-gated).

**Either way, Growth Today always owns:** QA, warmup configuration, placement tests, and the handoff to the GTM Engineer for campaigns.

---

## Part 1, Vendor-managed setup (default path)

1. **Create the Instantly workspace first** (the vendor form needs it): Instantly → Settings → Workspace Group → **Add sub-workspace** → confirm via email.
2. **Buy the vendor plan** choosing **"bring my own domain."**
3. **Fill the vendor config form:** domain(s); **destination = masking or a real landing page, NOT a bare redirect** (critical rule, the provisioning sub-skill); domain-provider credentials; **sequencer credentials** (dedicated vendor login from the password manager, never a personal login); sender names; **Generate Mailboxes**; tags (e.g. `Vendor - Google - <sender>`, `Vendor - Microsoft - <sender>`, plus any special tag like "Newsletter only").
4. **Brief the vendor** (client, plan + inbox counts with MS/Google split, sender names, domains + per-domain inbox counts, tags, sequencer = Instantly, workspace, sequencer login to use, any "don't touch" existing inboxes).
5. **Update nameservers** when the vendor requests it (delegates DNS to them).
6. **Vendor builds + first QA**: mailboxes + MX/SPF/DKIM/DMARC, usually 2–3 days; they send a completion confirmation.
7. **Growth Today QA on delivery** (see checklist): counts and MS/Google totals match the brief, all inboxes tagged, connected to the correct Instantly workspace, sending limits correct, placement OK.
8. **Add to warmup**: Google/Microsoft **native accounts only** (no SMTP) can go into Instantly's Premium pool; request via your Instantly contact.
9. **Set warmup + cold logic** (Part 3) and **placement tests** (Part 6).
10. **After 21 days**, ramp to fully-warmed volumes and **notify the GTM Engineer + AM** that inboxes are ready.

---

## Part 2, Connecting inboxes in Instantly (in-house path)

Entry: **Email Accounts → Add New → Connect existing accounts →** pick provider.

**Google Workspace**
- **OAuth (recommended):** one login connects all accounts in the same Workspace.
- **App password:** create an app password per account, use it as **both** the IMAP and SMTP password.
- **Bulk CSV:** supported (app password per account).

**Microsoft / Outlook**
- **One-by-one only** (OAuth Microsoft connector; no bulk, no CSV).
- **First** enable **Authenticated SMTP + IMAP** in the Microsoft Admin Center, then **wait ~1 hour**.
- On connect, tick **"Consent on behalf of your organization"** (shown for org accounts).

**Custom SMTP** (needs **both** IMAP and SMTP, SMTP-only is not allowed). Common hosts:

| Provider | IMAP (port) | SMTP (port) |
|---|---|---|
| Gmail | imap.gmail.com (993) | smtp.gmail.com (587/465) |
| Namecheap Private Email | mail.privateemail.com (993) | mail.privateemail.com (465/587) |
| Zoho (paid) | imappro.zoho.com (993) | smtppro.zoho.com (465/587) |
| Titan | imap.titan.email (993) | smtp.titan.email (465) |
| IONOS | imap.ionos.com (993) | smtp.ionos.com (465) |
| GoDaddy | imap.secureserver.net (993) | smtpout.secureserver.net (465) |

---

## Part 3, Warmup configuration

Enable via the **flame icon** (or bulk via the ⋯ menu); warmup starts at the next 00:00 UTC.

**Growth Today warmup values** (these override Instantly's generic defaults of 10/day, +1/day, 30% reply):

| | Warming (first 21 days) | Fully warmed |
|---|---|---|
| **Google** | warmup 25/day, **+4/day** increase, cold 0 | warmup 30/day, cold 20 |
| **Microsoft** | warmup 8/day, **+2/day** increase, cold 0 | warmup 15/day, cold 5 |

- **Reply rate:** ScaledMail SOP uses **75%**; **Growth Today prefers ramping to 100% after warmup** to lift reputation.
- Keep **Read Emulation on** and the recommended Open Rate / Spam Protection / Mark Important defaults.
- **Warmup pools:** Standard = green flame; **Premium = blue** (Google/MS only, higher quality); Basic = orange (SMTP overflow); **red = warmup disabled**. Put Google/MS native inboxes in Premium.
- **Duration:** Instantly's own minimum is 2 weeks, but **Growth Today's floor is 21 days / 3 weeks** (`reference.md` §5), 4 weeks on a cautious build. Launch only when Instantly's **Health Score > 90%** *and* §2 `warmup_score_active` is met. Those are two different scales, not one number written two ways: Health Score is Instantly's own 0-100 read on the account, `warmup_score_active` is the threshold our classifier uses to call an inbox Active. Instantly can say 92 while the classifier still says not Active. Both have to be true.
- **Warmup filter** (keep warmup mail out of the inbox): copy the account's warmup tag → Gmail filter (tag in Subject + Has-the-words → Skip Inbox, label "Warmup") / Outlook rule (subject-or-body contains tag → mark read, move to "Instantly Warmup").

Cross-check the cold/warmup **targets and the ratio** against `reference.md` §1, this table must stay consistent with it.

---

## Part 4, Advanced deliverability settings

Set per campaign (**Campaign → Options**) or workspace-wide (**Settings → Advanced Deliverability**):

- ✅ **Send first email as text-only**: also auto-disables open tracking, strips images, converts links to plain URLs. Growth Today default.
- ✅ **Open tracking OFF, link tracking OFF.**
- **ESP / Provider Matching + Routing:** available, but **do not hard-code it**: route from the Lead-ESP × sending-vendor matrix (the campaign-building sub-skill). Instantly's Routing rules can enforce a decision once the matrix says so.
- **Company send limit:** default **2 leads/day per domain**; set **extra-low into SEG orgs** (the campaign-building sub-skill, Part 3).
- ✅ **Insert unsubscribe header** (compliance, see the warmup-golive sub-skill, Part 5).
- **Stop on reply** (and Stop Company on Reply), on.
- **Slow ramp:** +2 campaign emails/day; **new accounts only**: never re-enable on an established sender (it resets it).
- **Minimum time gap** between emails (default 9 min + 5 min random).

---

## Part 4b, Unibox settings (required — the reporting depends on these)

**Settings → Unibox.** These four toggles decide what the email infra management system can
actually see. Get them wrong and the dashboard reports numbers that look fine and aren't.

| Toggle | GT setting | Why |
|---|---|---|
| **Save undelivered emails in Unibox** | ✅ **ON** | **The important one.** Off by default. If it's off, undelivered mail never lands in Unibox, so bounces can't be counted from Instantly and the bounce rate reads low |
| **Show auto-replies in Unibox** | ✅ ON | You need to see them to strip them. Auto-replies inflate reply counts and, on EmailBison, more than doubled the bounce count in one audit. Visible, then excluded — not hidden |
| **Save non-Instantly emails in Unibox** | ⬜ OFF | Pulls in unrelated mailbox traffic. Noise, and a privacy question on client mailboxes |
| **Only show notification in CRM** | ⬜ OFF | Keep replies visible in Unibox, not only in the CRM |

> **Why this is a setup step and not a preference.** Undelivered mail that never lands in Unibox
> can't be read out of Instantly by anything downstream. Turn it on at setup and the bounce data is
> there when you need it; leave it off and you find out later, when a number looks too good.
>
> *(For the record: the 1.47%-vs-4% bounce gap we chased in August was **not** caused by this. It
> was historical Instantly data from campaigns that ran until Dec 2025, plus an ESP filter mixing
> Bison rows in. Both fixed 24 Aug. The toggle is still worth setting — it just wasn't that bug.)*

Set it on **every workspace**, including client sub-workspaces. It is per workspace, not global.

---

## Part 5, Custom tracking domain (only if a client insists)

**Growth Today default = no custom tracking domain and no links in cold email** (the provisioning sub-skill). Only when a client strongly insists, set up a **dedicated, never-shared** one:
- CNAME → Host **`inst`**, Target **`prox.itrackly.com`**, TTL auto/3600.
- Enter in Instantly (account → Settings → Custom tracking domain) as **`inst.yourdomain.com`** → **Check Status** → "CNAME Verified."

---

## Part 6, Placement tests (Instantly native)

Instantly's **Automated Inbox Placement** tests report inbox / promotions / spam, score deliverability, and monitor blacklists, with automations to pause mailboxes on a placement drop or blocklisting. Note **spintax/variables aren't supported** in placement tests. This complements Growth Today's own dashboard placement tests (the dashboard-reading sub-skill). Growth Today convention: placement tests on **all Google inboxes**, **2 Microsoft inboxes per domain**.

---

## ✅ INSTANTLY SETUP CHECKLIST (copy-paste)

```
PATH
[ ] Setup path decided: vendor-managed (default) or in-house
[ ] Instantly (sub)workspace created

CONNECT
[ ] Google: OAuth / app-password (IMAP+SMTP) / bulk CSV as appropriate
[ ] Microsoft: SMTP+IMAP enabled in Admin Center, waited ~1h, connected one-by-one, org consent ticked
[ ] Custom SMTP: both IMAP + SMTP set with correct host/port
[ ] Destination = masking / real landing page, NOT a bare redirect
[ ] Inboxes tagged; correct workspace; counts + MS/Google split match the brief

WARMUP
[ ] Warmup enabled; Google 25/day (+4), Microsoft 8/day (+2), cold 0 during warming
[ ] Premium pool for Google/MS native inboxes; no SMTP in premium
[ ] Read emulation on; recommended sub-settings kept
[ ] Warmup filter set in Gmail/Outlook
[ ] Warmed 21 days min (4 weeks on a cautious build); Instantly Health Score > 90% AND §2 `warmup_score_active` met
[ ] Fully-warmed ramp set: Google 30 warmup/20 cold, Microsoft 15 warmup/5 cold

UNIBOX (Settings -> Unibox) - reporting depends on these
[ ] Save undelivered emails in Unibox = ON   <- off by default, breaks bounce reporting
[ ] Show auto-replies in Unibox = ON         <- see them, then strip them
[ ] Save non-Instantly emails in Unibox = OFF
[ ] Only show notification in CRM = OFF
[ ] Checked on EVERY workspace, including client sub-workspaces

DELIVERABILITY
[ ] First email text-only; open + link tracking OFF
[ ] Company send limit set (default 2/domain/day; lower for SEG)
[ ] Unsubscribe header on; stop-on-reply on
[ ] Slow ramp on for NEW accounts only
[ ] ESP routing left to the dashboard matrix (the campaign-building sub-skill), not hard-coded
[ ] Custom tracking domain: none (unless client insists → dedicated)

VERIFY & HANDOFF
[ ] MX/SPF/DKIM/DMARC verified (the provisioning sub-skill)
[ ] Instantly automated placement tests set up
[ ] Sending limits verified per state (reference §1)
[ ] GTM Engineer + AM notified inboxes are ready
```

---

> **Internal reference (Growth Today team).** The in-house step-by-step SOP backing this sub-skill is **[MASTER Setting Up Domains and Inboxes with ScaledMail + Instantly](https://app.notion.com/p/growth-today/MASTER-Setting-Up-Domains-and-Inboxes-with-ScaledMail-Instantly-34599b4b261980c49775fa47c5c0e2a4)** (access-gated; external readers can't open it). **Do not delete this Notion page, it is referenced by this skill.** This sub-skill is the primary source going forward; the Notion page is retained for the in-house detail (screenshots and vendor walkthroughs) not duplicated here. **Inbox documentation now lives in the email infra management system, handled automatically — Row Zero is retired and must not be used.**

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
