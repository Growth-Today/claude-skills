---
name: email-infra-setup-audit
description: "Audit a live sequencer workspace to verify inboxes are set up correctly against the Growth Today standard. Connect a client's Instantly / EmailBison / Smartlead / Lemlist workspace, pull the live config, and report per-item PASS / WARN / FAIL with the exact fix — connection, warmup, sending limits, DNS/auth, tracking, deliverability toggles, and cross-sequencer hygiene. Triggers on setup audit, config audit, is this workspace set up right, verify inbox setup, account audit, check warmup settings, audit sending limits, did we configure this correctly, pre-launch setup check. Do NOT use to diagnose bounces/blacklists (use the blacklist-bounce-audit sub-skill), read ongoing inbox health (use the dashboard-reading sub-skill), or do first-time setup (use the platform setup sub-skills)."
---

# Setup Audit — Verify a Workspace  ·  [GTM Engineer]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §2, §6 · `{SKILL_BASE}/resources/approved-vendors.md` · the platform setup sub-skills  ·  **Related:** emailbison-setup, instantly-setup, smartlead-setup, lemlist-setup, dashboard-reading.

Connect a client's sequencer workspace, pull the **live configuration**, and check every setting against the Growth Today standard — so you (or an agent) can say, item by item, *"this is set up right"* or *"this was missed, here's the fix."* This is the setup-side counterpart to the blacklist-bounce-audit sub-skill: not a static checklist, a **live verification** you run on a real workspace.

**When to run:** before launch on a new workspace · after a vendor delivers inboxes · monthly config drift check · when results look off and you suspect a misconfiguration · onboarding audit.

**Ask if not provided:** which **workspace / sequencer** (Instantly, EmailBison, Smartlead, Lemlist) and its MCP server / API host; the **expected inbox + domain count** (from the brief); and the **client's segment** (US/EU) for timezone checks. Always audit the correct workspace with its own IDs.

---

## Part A — Pull the live config

Platform-aware — use the connected sequencer's MCP/API. Pull:
1. **Inboxes:** every sending account, its provider (Google/Microsoft/SMTP), connection status, tags, warmup on/off + score, cold + warmup daily limits, lifetime sent, creation date.
2. **Domains:** distinct sending domains and how many mailboxes each has.
3. **DNS/auth:** MX/SPF/DKIM/DMARC status per domain (or note the sequencer doesn't expose it → check externally).
4. **Campaigns:** per campaign — tracking on/off, first-email content type (plain/HTML), sending interval + schedule/timezone, company send limit, unsubscribe/stop-on-reply settings, ESP routing.
5. **Account settings:** custom tracking domain present? warning notifications on? (Lemlist: LinkedIn limits, blocklist, HubSpot sync.)

Report the baseline first (inbox count vs brief, provider split, domains), then run the checks below.

---

## Part B — Check each dimension (PASS / WARN / FAIL)

Grade each against the Growth Today standard (`{SKILL_BASE}/resources/reference.md`; expected config per platform in the setup sub-skills). For every FAIL, name the exact inboxes/campaigns and the fix.

| # | Check | PASS if… | Common FAIL / fix |
|---|---|---|---|
| 1 | **Inbox count** | matches the brief (count + MS/Google split) | fewer/more than briefed → reconcile with the vendor |
| 2 | **Mailboxes per domain** | ≤ 2 per domain | drifted > 2 → redistribute |
| 3 | **Connection** | all Connected; real-name addresses | disconnected / role addresses (sales@, info@) → reconnect/replace |
| 4 | **Warmup on** | enabled on every inbox; not disabled on live inboxes | any inbox warmup off → enable |
| 5 | **Warmup age** | warmed ≥ 14 days (ideally 3–4 wks) before linking; domain > 30 days | linked too early → hold/age |
| 6 | **Cold limits by state** | Active Google 20 / Outlook 5; warming & unhealthy 0–1 (Bison floor 1); ratio Google 1.5 / Outlook 2.5 (`reference.md` §1) | inboxes on wrong limit (e.g. 30) → correct |
| 7 | **Randomized interval** | a randomized send gap set (e.g. ~5 min + jitter), correct per platform | fixed/too-tight interval → randomize |
| 8 | **Timezone** | sending window matches the segment (US vs EU) | wrong timezone → fix schedule |
| 9 | **DNS/auth** | MX/SPF/DKIM/DMARC green per domain; one SPF record | broken/missing/duplicate SPF → fix (the provisioning sub-skill) |
| 10 | **Destination** | masking or real landing page, not a bare 301/302 redirect | bare redirect → switch to masking |
| 11 | **Tracking** | open + link tracking OFF; no custom tracking domain (unless client insists) | tracking on / shared tracking domain → turn off |
| 12 | **First email** | plain text — no HTML, images, or links | HTML/links/images in email 1 → strip |
| 13 | **Signature** | no links, images, or spam words; not promotional | linked/imaged/spammy signature → clean |
| 14 | **Unsubscribe** | no unsubscribe link in cold copy (plain-text opt-out only) | unsubscribe link present → remove (forces HTML) |
| 15 | **ESP routing** | set from the dashboard matrix, not a hard ESP-matching rule | blind ESP-matching on → review vs matrix (the campaign-building sub-skill) |
| 16 | **Company send limit** | capped (e.g. 2/company/day; lower for SEG orgs) | uncapped → set |
| 17 | **Spintax / variance** | present on subject + body | none → add |
| 18 | **Cross-sequencer** | inbox used elsewhere set to cold 0 (Instantly) / 1 (Bison) + tagged | double-sending risk → throttle + tag |
| 19 | **% automated replies** | tracked and stripped before reading bounce/reply | not accounted for → strip (the blacklist-bounce-audit sub-skill) |
| 20 | **Warning alerts** | high-bounce (+ LinkedIn disconnect on Lemlist) alerts ON | off → enable |

---

## Part C — Report

Present a per-dimension result the team (or an agent) can act on:

```
## Setup Audit — [Workspace] ([Sequencer]) — [Date]
Baseline: X inboxes across Y domains (Google Z / Microsoft W) vs brief [match/mismatch]

✅ PASS (n): [dimensions that are correct]
⚠️ WARN (n): [borderline — dimension + which inboxes + why]
❌ FAIL (n): [dimension + exact inboxes/campaigns + the fix]

Top fixes (priority order):
1. [most impactful fix]
2. …
Overall: [ready to launch / fix N blockers first]
```

Rules: **numbers first**, name the exact inboxes/campaigns for every WARN/FAIL, and give the one-line fix (or point to the setup sub-skill). A launch-blocking FAIL (bad DNS, bare redirect, warmup off, tracking on, HTML first email) means **do not launch** until fixed.

---

## ✅ SETUP-AUDIT CHECKLIST (copy-paste)

```
[ ] Correct workspace / sequencer confirmed; live config pulled
[ ] Baseline reported (inbox + domain count vs brief, provider split)
[ ] All 20 dimensions graded PASS / WARN / FAIL
[ ] Every WARN/FAIL names the exact inboxes/campaigns + the fix
[ ] Launch-blocking FAILs flagged (DNS, redirect, warmup off, tracking on, HTML email 1)
[ ] Report delivered; top fixes prioritized
[ ] Re-audit after fixes to confirm PASS
```

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
