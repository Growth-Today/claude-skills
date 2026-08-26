---
name: email-infra-dashboard-reading
description: "Read the inbox-health dashboard from the email infra management system and act on it. Use for inbox classification (Active, Warmup Needed, Burnt, New, Blacklisted), per-state send limits, reading each panel, the diagnosis order, and resting burnt inboxes. Classification and limit tables are verify-only: recompute the expected state and report a mismatch, never retag or change a limit. Triggers on inbox classification, inbox health, dashboard, warmup score, placement score, inbox tagging, burnt inbox, sending limits, verify the tags, why is this inbox warmup needed. Do NOT use for auditing a specific bounce or blacklist to root cause (use the blacklist-bounce-audit sub-skill) or building campaigns (use the campaign-building sub-skill)."
---

# Reading the Inbox-Health Dashboard · [GTM Engineer]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §2, §3, §7 · **Related:** campaign-building, bounce-audit.

How to read the automated inbox-management dashboard and turn each panel into an action. Don't track health by hand, the system classifies every inbox and domain continuously; your job is to read it correctly and act. All thresholds live in `{SKILL_BASE}/resources/reference.md` §1–§3.

---

## Part 1, Inbox classification (what the tags mean)

Every inbox is auto-tagged by the email infra management system. Exact thresholds in `reference.md` §2.

**This table is executable as a verification, never as a change.** With the sequencer MCP
connected, you can recompute what each inbox's state *should* be and compare it to the tag
the system actually applied. A mismatch is a finding to report — it is how bugs in the system get caught —
and it is never something GT retags. Every row here is `Write? never`.

| Tag | Threshold (`reference.md` §2 keys) | Verify with | What you do |
|---|---|---|---|
| **New Inbox** | lifetime sends < `new_inbox_sends`; routing also excludes age < `new_inbox_age_days` | `list_accounts` → `timestamp_created` · `analytics_daily_account` → lifetime sent | Don't scale it; let it graduate |
| **Active** | placement `placement_active` · bounce `bounce_active` · reply `reply_active` · warmup `warmup_score_active` | `list_accounts` → `stat_warmup_score` · `inbox_placement_analytics_*` · `get_campaign_analytics` | Safe to send at full cold limit |
| **Warmup Needed** | anything not New/Active/Burnt; placement `placement_forced_warmup` hard-forces it | same reads as Active | Throttled to cold 0–1, stays attached; investigate placement |
| **Burnt** | bounce `bounce_burnt` AND reply < `reply_active` AND warmup `warmup_score_burnt` — **all three** | same reads as Active | Excluded from campaigns; rest & re-test (Part 5) |
| **Blacklisted** | domain on `blacklists_that_count` (Spamhaus DBL / URIBL) — nothing else | check at source (Spamhaus DBL / URIBL). The blacklist card itself now follows the client filter correctly (Part 2b) | Volume cut; go to the bounce-audit sub-skill |

> **What a mismatch means.** If an inbox reads Active on the dashboard but the live numbers put
> it in Burnt, that is a classification-engine finding to raise, not a tag for you to correct.
> Report the inbox list and the computed state. Same in reverse.

**No timeout:** an inbox can sit in Warmup Needed forever, there's no auto-escalation. Placement < 50 hard-forces Warmup Needed; when placement recovers, it returns to Active on its own.

---

## Part 2, The panels and how to read each

**1. Inbox health.** Counts by tag (New / Active / Warmup Needed / Burnt / Blacklisted) per client and total. Read it as a distribution: a rising Warmup-Needed/Burnt share is an early warning before it shows up in campaign metrics.

**2. Bounce intelligence.** Bounce split **by recipient ESP** and **by reason** (hard / block / soft), with **auto-replies stripped** (`reference.md` §7). Read the *categorized* number, never the raw one. A domain at 60% "bounce" tells you nothing until you see whether it's bad data (5.1.1), a Microsoft tenant block (5.4.1), a corporate/SEG block (5.7.1), or soft (4xx). Full workflow in the bounce-audit sub-skill.

**3. Vendor performance by ESP (the decision matrix).** Rows = recipient Lead ESP; columns = sending vendor / inbox ESP; toggle **Automated vs Human reply**. This is the panel the campaign-building sub-skill routes from. Always read **Human reply**. Collapse to "Inbox ESP only" (Google/Outlook/SMTP) for a vendor-agnostic read.

**4. Client overview.** One row per client: contacted, sends, active/warmup-needed/burnt/blacklisted, bounce, reply, human reply, unsub, placement, ESP mix. The at-a-glance triage view, drill into any row.

**5. DNS / auth health.** MX / SPF / DKIM / DMARC status per domain, with counts of OK / broken / never-checked. The point is catching **silent drift**, a record a provider quietly broke, not just initial setup. A broken record should fire an alert; treat it as P0 (dead auth = mail binned).

**6. Blacklist by vendor.** Domains on **Spamhaus DBL and URIBL**, per client and per domain. Those two lists are the only blacklist reasons GT recognises. Any other list shown in the panel is **not a reason to tag an inbox Blacklisted, cut sending, or fire an alert** — if one still does, that's a bug to report, not a real listing (see the bounce-audit sub-skill).

---

## Part 2b, What was fixed, and what is still open

The dashboard had a run of data problems through July and August 2026. **Most were fixed and
signed off by GT's own QA between 20 and 25 August.** Read this before repeating an old warning
to a client.

### Fixed and verified

| What | Status |
|---|---|
| **Bounce rate** | ✅ Fixed. The Bison view now matches Bison exactly. The Instantly view is driven by campaign-level records with a **source selector** (Campaign records / Inbox counters) above the cards. Verified by GT on Ramp, Quickbox and Growth Today. The old "dashboard says 1.47%, sequencer says 4%" gap turned out to be **historical data** — GT ran Instantly campaigns until Dec 2025 — plus an ESP filter that was mixing Bison rows in. Both corrected |
| **Bounce column logic** | ✅ Shows Instantly where data exists, otherwise Bison. It no longer combines the two, so the headline and the per-sequencer breakdown agree |
| **Inbox counts** | ✅ Reflect what is actually in each sequencer today. Removed accounts no longer inflate the number; their history is kept for all-time stats |
| **Blacklist card** | ✅ Follows the client filter. A clean client shows no card |
| **Campaign tags** | ✅ Include and Exclude can no longer contradict each other. Senders stop silently detaching |
| **Inbox tagging** | ✅ Applied correctly — confirmed by GT on 25 Aug |
| **Placement tests** | ✅ Running on the weekly automated schedule (Fri–Sun, professional accounts, Google + Outlook) across client workspaces |

**Reading the Instantly bounce card:** the 30-day and 7-day figures on the *Campaign records*
source fill in as daily tracking accumulates — 7 days completes within a week, 30 days within a
month. An empty recent window on a workspace with no recent Instantly sending is correct, not a bug.

### Still open

| What | Status |
|---|---|
| **"Warmup Needed" definition** | ⏸️ Under discussion. The tag uses warmup score, placement, bounce **and a 0.5% reply rate**. Mailboxes that are healthy on the first three still get tagged Warmup Needed on reply rate alone, and then don't attach to campaigns. Simone has proposed dropping the reply threshold. **Until this is decided, a Warmup Needed tag does not necessarily mean the warmup is bad** — check which of the four conditions actually failed |
| **Placement tests: Cavalry, TDCX** | ⏸️ Instantly returns **402 Payment Required** when creating recurring tests. That's a billing/plan limit on Instantly's side, not a system fault — the Inbox Placement Tests add-on needs checking on those workspaces |
| **Inbox count "inc. retired"** | ⏸️ Minor. Reads 151 for Growth Today; historical-data question raised by Gaze, not yet answered |
| **Weekly Inbox Health Report** | ⏸️ The 21 Aug report was Bison data. Whether an Instantly version is configured is still an open question from Fezekile |

### A limits finding worth knowing

On one client, **100 of 136 mailboxes were capped at 5/day and 32 at 20/day**, giving the whole
workspace a ceiling of roughly **1,180 emails/day**. The system did not set those limits — the
audit log has no record, and its limits automation has never been switched on for that
environment. They came from the original Instantly setup.

Two things follow. **Volume complaints are often a limits problem, not a tagging problem** — check
the caps before blaming classification. And because the limits automation is off, sending limits
today are whatever a human set at setup, which is exactly what `setup-audit` dimension 6 checks.

---

## Part 3, Reading signals together (diagnosis order)

One metric alone rarely tells the story. Read in this order:

- **Low reply?** → check **inbox placement** first (are you in spam?).
- **Failing placement?** → check **warmup score** over the last week.
- **High bounce?** → sender reputation declining *or* the domain is flagged, go to the bounce-audit sub-skill.
- **Everything healthy but no replies?** → it's the **offer/targeting or copy**, not deliverability.

Timing: a **rising bounce rate is a leading indicator** (acts the same day), a **blacklist listing is a lagging indicator** (damage already done). Watch bounces daily; never wait for a blacklist hit.

**Reply floor:** even pure out-of-office produces ~1%. Total reply **below ~1%** usually means you're **bouncing**, not that interest is low, check the bounce folder before concluding anything.

---

## Part 4, Send limits by state (read-only — the email infra management system sets these)

**The email infra management system sets these limits. Your job is to check them, not change them.** Governed by the
warm-to-cold **ratio**, with the cold limit driven by inbox state (`reference.md` §1). If an inbox
is on the wrong limit, report it with the inbox list — do not fix it yourself.

**Executable as a verification.** `list_accounts → daily_limit` and `warmup.limit` give you the
live values; compare them to the §1 keys below. **Every row is `Write? never`** — `update_account`
and `manage_account_state` are out of bounds for a GTM engineer regardless of what the audit finds.

| State | Cold (Google / Outlook) | Warmup target | Verify with |
|---|---|---|---|
| Warming (first `warmup_floor_days`) | §1 `cold_warming` | cold × §1 `ratio_google` / `ratio_outlook` | `list_accounts` → `daily_limit`, `warmup.limit`, `timestamp_created` |
| Active (sending) | §1 `google_cold` / `outlook_cold` | §1 `google_warmup` / `outlook_warmup` | same |
| Warmup Needed / Burnt | §1 `cold_warming` | reduced | same + `warmup_status` |
| New Inbox | §1 `cold_new_inbox` | — | same + lifetime sends |

Numbers are deliberately not repeated here. Read the current values from the §1 key table at run
time — that is what stops this page drifting from the standard the way the old sizing SOP did.

> **Failover watch (EmailBison):** a throttled inbox stays attached at cold 1 and keeps sending to its in-flight leads; Bison won't reroute those leads to a healthy inbox on the campaign. Scan for leads stranded on Warmup-Needed inboxes, a real bounce driver. Instantly and Smartlead can reroute the lead to a healthy inbox; EmailBison can't.

---

## Part 5, Rest & recover a burnt inbox

When an inbox goes Burnt, don't just leave it throttled forever. Write the cadence down and follow it:

- **Day 0:** cold effectively off; keep warmup running.
- **Days 2–10:** re-test placement; if placement + warmup recover, it re-classifies toward Active automatically.
- **After 10 days** with no recovery: retire the inbox.

For a **SEG-burnt domain**, don't retire outright, recycle onto easy Google/Outlook leads and re-test first (the campaign-building sub-skill, Part 3).

---

## ✅ HEALTH-REVIEW CHECKLIST (weekly)

```
[ ] Inbox-health distribution reviewed per client (Warmup Needed/Burnt share trending?)
[ ] Bounce read from the CATEGORIZED panel (auto-replies stripped), not raw
[ ] Vendor-performance matrix read on HUMAN reply; volume shifted to winners
[ ] Client overview triaged; drilled into any red row
[ ] DNS/auth health: no broken/never-checked records (broken = P0)
[ ] Blacklist-by-vendor: only Spamhaus DBL / URIBL count; any other list is not a reason
[ ] Diagnosis order applied to any anomaly (reply→placement→warmup; bounce→the bounce-audit sub-skill)
[ ] Stranded-lead check on throttled inboxes (failover gap)
[ ] Burnt inboxes on the rest-and-retest cadence
```

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
