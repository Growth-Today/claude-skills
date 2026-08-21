---
name: email-infra-setup-audit
description: "Audit a live sequencer workspace to verify inboxes are set up correctly against the Growth Today standard. Connect a client's Instantly / EmailBison / Smartlead / Lemlist workspace, pull the live config, and report per-item PASS / WARN / FAIL with the exact fix, connection, warmup, sending limits, DNS/auth, tracking, deliverability toggles, and cross-sequencer hygiene. Triggers on setup audit, config audit, is this workspace set up right, verify inbox setup, account audit, check warmup settings, audit sending limits, did we configure this correctly, pre-launch setup check. Do NOT use to diagnose bounces/blacklists (use the blacklist-bounce-audit sub-skill), read ongoing inbox health (use the dashboard-reading sub-skill), or do first-time setup (use the platform setup sub-skills)."
---

# Setup Audit, Verify a Workspace · [GTM Engineer]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §2, §6 · `{SKILL_BASE}/resources/approved-vendors.md` · the platform setup sub-skills · **Runs:** `{SKILL_BASE}/playbooks/dns-auth-audit` · **Related:** emailbison-setup, instantly-setup, smartlead-setup, lemlist-setup, dashboard-reading.

Connect a client's sequencer workspace, pull the **live configuration**, and check every setting against the Growth Today standard, so you (or an agent) can say, item by item, *"this is set up right"* or *"this was missed, here's the fix."* This is the setup-side counterpart to the blacklist-bounce-audit sub-skill: not a static checklist, a **live verification** you run on a real workspace.

**When to run:** before launch on a new workspace · after a vendor delivers inboxes · monthly config drift check · when results look off and you suspect a misconfiguration · onboarding audit.

**Ask if not provided:** which **workspace / sequencer** (Instantly, EmailBison, Smartlead, Lemlist) and its MCP server / API host; the **expected inbox + domain count** (from the brief); and the **client's segment** (US/EU) for timezone checks. Always audit the correct workspace with its own IDs.

---

## Part A, Pull the live config

Platform-aware, use the connected sequencer's MCP/API. Pull:
1. **Inboxes:** every sending account, its provider (Google/Microsoft/SMTP), connection status, tags, warmup on/off + score, cold + warmup daily limits, lifetime sent, creation date.
2. **Domains:** distinct sending domains and how many mailboxes each has.
3. **DNS/auth:** MX/SPF/DKIM/DMARC status per domain. Most sequencers don't expose this, so **don't check it by hand** — run the playbook:
   ```bash
   cd {SKILL_BASE}/playbooks/dns-auth-audit/scripts
   uv run execute.py --file domains.txt --csv <client>_baseline.csv
   ```
   It needs no credentials, grades every domain PASS/WARN/FAIL, classifies the provider from MX (which is also how you spot a recipient-side SEG), and writes a CSV you can diff next month with `after.py`. Save the CSV per client — drift is the real risk, and you can only see drift against a baseline.
4. **Campaigns:** per campaign, tracking on/off, first-email content type (plain/HTML), sending interval + schedule/timezone, company send limit, unsubscribe/stop-on-reply settings, ESP routing.
5. **Account settings:** custom tracking domain present? warning notifications on? (Lemlist: LinkedIn limits, blocklist, HubSpot sync.)

Report the baseline first (inbox count vs brief, provider split, domains), then run the checks below.

---

## Part B, Check each dimension (PASS / WARN / FAIL)

**This table is executable.** If the sequencer's MCP is connected, walk it row by row and run
the call in the `Call → field` column instead of asking a human to look. If the MCP is not
connected, fall back to the UI check and **say in the report which rows were done by hand** —
a skipped row is not a passed row.

### How to read a row

| Column | What it tells you |
|---|---|
| **Source** | `MCP` = run the call · `PLAYBOOK` = run the script · `MANUAL` = a person must look |
| **Call → field** | The exact tool and field path. Do not infer a different one |
| **Pass if** | The comparison. Thresholds are **keys into `reference.md`**, not numbers written here — read the current value from §1/§2 keys at run time |
| **On fail** | The verdict and who acts |
| **Write?** | `never` = read the value, report the gap, escalate. `setup-only` = writable at first provisioning, never after go-live. **No row in this table is a licence to change a live inbox** |

Calls below are Instantly V2 tool names. For EmailBison / Smartlead / Lemlist the *check* is
identical; substitute that platform's equivalent read and note the substitution in the report.

### The table

| # | Check | Source | Call → field | Pass if | On fail | Write? |
|---|---|---|---|---|---|---|
| 1 | **Inbox count** | MCP | `list_accounts` → count, group by `provider_code` | matches the brief, count and Google/Microsoft split | WARN → reconcile with ScaledMail. If the brief itself is doubtful, re-derive with `playbooks/sizing-calculator` first — older briefs used the deprecated ÷20–25 divisor and under-buy by 43–79% | n/a |
| 2 | **Mailboxes per domain** | MCP | `list_accounts` → `email`, split on `@`, count per domain | Google ≤ ~3 · Microsoft ≤ ~25 | WARN → redistribute on the next build | n/a |
| 3 | **Connection** | MCP | `list_accounts` → `status`, `setup_pending`, `email` | `status == 1` and `setup_pending == false` on every inbox; no role addresses (`sales@`, `info@`, `hello@`) | FAIL → reconnect, or replace the role address | setup-only |
| 4 | **Warmup on** | MCP | `list_accounts` → `warmup_status` | `warmup_status == 1` on every live inbox | FAIL → **report to OpsLab with the inbox list. Do not enable it yourself on a live inbox** | never |
| 5 | **Warmup age** | MCP | `list_accounts` → `timestamp_created` | age ≥ §2 `warmup_floor_days` before any cold send; domain > 30 days before carrying a link | FAIL → hold and age. Note the trap: OpsLab releases at §2 `new_inbox_age_days`, GT's floor is longer | n/a |
| 6 | **Cold limits by state** | MCP | `list_accounts` → `daily_limit`, `warmup.limit`, `warmup.increment` | matches §1 `google_cold` / `outlook_cold` for the inbox's state; warming and throttled at §1 `cold_warming`; New Inbox at §1 `cold_new_inbox`; warmup ≈ cold × §1 `ratio_google` / `ratio_outlook` | FAIL → **list the inboxes and report to OpsLab. GT does not set limits** | never |
| 7 | **Randomized interval** | MCP | `list_accounts` → `sending_gap` | a gap is set and is not near-zero; jitter enabled per platform | WARN → randomize | setup-only |
| 8 | **Timezone** | MCP | `list_campaigns` → `campaign_schedule.schedules[].timezone`, `.timing`, `.days` | window matches the client's segment (US vs EU); weekdays only | FAIL → fix the schedule | setup-only |
| 9 | **DNS / auth** | PLAYBOOK | `playbooks/dns-auth-audit` → `uv run execute.py --file domains.txt` | exit code 0; exactly one SPF inside the 10-lookup budget; DMARC `p=reject` (§6) | FAIL → fix at the DNS host (provisioning). **A record that was healthy and is now broken is P0** | n/a |
| 10 | **Destination** | MANUAL | not exposed by any sequencer API | masking or a real landing page, never a bare 301/302 | FAIL → switch to masking. GT runs no client redirects today, so a FAIL means an inherited or client-held domain | n/a |
| 11 | **Tracking** | MCP | `list_campaigns` → `open_tracking` | `open_tracking == false` on every campaign; no shared custom tracking domain | FAIL → turn off | setup-only |
| 12 | **First email plain text** | MCP | `list_campaigns` → `sequences[0].steps[0].variants[].body` | no `<img`, no `<a href`, no tracking pixel in step 1 | FAIL → strip. Launch-blocking | setup-only |
| 13 | **Signature** | MANUAL | **not exposed** — absent from `list_accounts` and `get_account` | no links, images, or promotional wording | FAIL → clean it in the UI | setup-only |
| 14 | **Unsubscribe** | MCP | `list_campaigns` → step-1 `body` · `workspace_get` → `add_unsub_to_block` | no unsubscribe *link* in cold copy — plain-text opt-out only; `add_unsub_to_block == true` so opt-outs are suppressed | FAIL → remove the link (it forces HTML) | setup-only |
| 15 | **ESP routing** | MCP ⚠️ | `get_campaign` → ESP-matching field *(field name unconfirmed — see the note below)* | no blind ESP matching; routing follows the dashboard matrix | WARN → review against the matrix (campaign-building) | never |
| 16 | **Company send limit** | MCP ⚠️ | `get_campaign` → per-company cap *(field name unconfirmed — see the note below)* | a cap is set (≈ 2/company/day; lower for SEG orgs) | FAIL → set a cap | setup-only |
| 17 | **Spintax / variance** | MCP | `list_campaigns` → `variants[].subject` and `.body` | `{{RANDOM \| … }}` present on subject **and** body; more than one variant per step | WARN → add variance | setup-only |
| 18 | **Cross-sequencer** | MANUAL | requires reading two platforms — no single call | an inbox live in another sequencer is at cold 0 (Instantly) / 1 (EmailBison) and tagged | FAIL → **report to OpsLab** (throttling and tagging are theirs) | never |
| 19 | **% automated replies** | MCP | `list_emails` → reply bodies, strip OOO before any rate | auto-replies stripped before bounce/reply is quoted | WARN → strip (blacklist-bounce-audit). Needs a live campaign | n/a |
| 20 | **Warning alerts** | MANUAL | not exposed by the account or workspace read | high-bounce alerts ON (plus LinkedIn-disconnect on Lemlist) | WARN → enable in the UI | setup-only |

> **⚠️ Rows 15 and 16.** Instantly returns campaign fields **only once they have been configured** —
> an unset field is simply absent from the response, not present-and-empty. On every GT campaign
> checked so far these two were absent. Treat absent as **not configured**, which is the audit
> answer anyway, and confirm the exact field name against a campaign where the setting *is* on
> before hardening the row.

> **🔒 Read-only reminder.** Rows 4, 6, 15 and 18 sit inside OpsLab-owned territory. The audit
> reads them and reports the gap. It never fixes them — see the read-only boundary in `SKILL.md`.
> `setup-only` means writable at first provisioning; once an inbox is live and OpsLab is
> classifying it, that window is closed.

---

## Part C, Report

Present a per-dimension result the team (or an agent) can act on:

```
## Setup Audit, [Workspace] ([Sequencer]), [Date]
Source: MCP [connected / not connected] · X of 20 checked automatically, Y by hand, Z not checked
Baseline: X inboxes across Y domains (Google Z / Microsoft W) vs brief [match/mismatch]

✅ PASS (n): [dimensions that are correct]
⚠️ WARN (n): [borderline, dimension + which inboxes + why]
❌ FAIL (n): [dimension + exact inboxes/campaigns + the fix]
⬜ NOT CHECKED (n): [dimension + why — no MCP, no data, field unconfirmed]

🔒 OpsLab items found (read-only — reported, not fixed):
- [dimension + inbox list]

Top fixes (priority order):
1. [most impactful fix]
2. …
Overall: [ready to launch / fix N blockers first]
```

Rules: **numbers first**, name the exact inboxes/campaigns for every WARN/FAIL, and give the one-line fix (or point to the setup sub-skill). A launch-blocking FAIL (bad DNS, bare redirect, warmup off, tracking on, HTML first email) means **do not launch** until fixed.

**Two reporting rules that matter more than the format:**

1. **Never report a skipped row as a pass.** If the MCP wasn't connected, the field was absent, or
   there was no data, it goes under NOT CHECKED with the reason. An audit that quietly drops
   rows reads as cleaner than it is, which is worse than no audit.
2. **Separate OpsLab findings from GT findings.** Anything on a `Write? never` row goes in its own
   block, addressed to OpsLab. Mixing them invites someone to "just fix" a sending limit.

---

## Part D, Worked example (real run, GT workspace, 21 Aug 2026)

Condensed from an actual MCP-driven run, as a pattern to imitate.

```
## Setup Audit — GT (Instantly) — 21 Aug 2026
Source: Instantly MCP connected · 13 of 20 automatic · 3 inconclusive · 4 manual
Baseline: 25 inboxes / 13 domains · 25 Google / 0 Microsoft · created 2026-08-15 (6 days) · 0 active campaigns

✅ PASS (9): mailboxes-per-domain (max 2) · connection (25/25 status=1) · interval (sending_gap=10)
            · timezone (America/Detroit, Mon–Fri) · DNS (playbook exit 0, 13/13 clean, p=reject on all)
            · tracking off · first email plain · unsubscribe · spintax

⚠️ WARN (1): provider split 100% Google vs the 60/40 standard — decide it, don't drift into it

❌ FAIL (3) — one root cause:
   4  warmup_status=0 on all 25; stat_warmup_score=0; warmup analytics empty
   5  6 days old vs §2 warmup_floor_days = 21 (also under OpsLab's 14-day exclusion)
   6  daily_limit=20 = §1 google_cold (the ACTIVE value) on inboxes still in the warming window
   → 25 inboxes set to send 20 cold/day each with warmup off, 6 days after creation.
     Nothing has sent yet — caught pre-launch, which is the point.
     Warmup config itself is correct: warmup.limit=30 = §1 google_warmup, increment=4 = §1 ramp_google.

🔒 OpsLab (reported, not fixed — rows 4 and 6 are Write? never):
   "All 25 inboxes have warmup disabled and daily_limit=20 inside the warming window.
    Requesting warmup enabled and cold set to the warming value until 2026-09-05. List attached."

⬜ NOT CHECKED (7): destination · signature (confirmed not in the API) · ESP routing (field absent)
   · company cap (field absent) · cross-sequencer (needs 2nd platform) · auto-replies (no live
   campaign) · alerts (not exposed)

Overall: not ready to launch. 3 blockers, all warmup, all OpsLab-owned.
```

**Three things this example is showing you:**

1. **Group by root cause.** Three FAILs, one problem. Listing them as three unrelated items is
   technically accurate and practically useless.
2. **NOT CHECKED is an outcome, not an omission.** Seven rows, each with a reason. A report that
   showed "13 of 13 passed" would read cleaner and be a lie by omission.
3. **The OpsLab block is pre-drafted as a message.** The finding travels to its owner without
   anyone being tempted to fix a sending limit in place.

---

## ✅ SETUP-AUDIT CHECKLIST (copy-paste)

```
[ ] Correct workspace / sequencer confirmed; live config pulled
[ ] MCP connection status stated (and which rows fell back to manual)
[ ] Baseline reported (inbox + domain count vs brief, provider split)
[ ] All 20 dimensions graded PASS / WARN / FAIL / NOT CHECKED
[ ] Thresholds read from reference.md §1/§2 keys, not from memory
[ ] No write executed on any `Write? never` row; OpsLab findings listed separately
[ ] Every WARN/FAIL names the exact inboxes/campaigns + the fix
[ ] Launch-blocking FAILs flagged (DNS, redirect, warmup off, tracking on, HTML email 1)
[ ] Report delivered; top fixes prioritized
[ ] Re-audit after fixes to confirm PASS
```

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
