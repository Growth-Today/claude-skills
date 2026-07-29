# Playbook 05 — Reading the Inbox-Health Dashboard  ·  [GTM Engineer]

> **Reads:** `../references/reference.md` §1, §2, §3, §7  ·  **Related:** playbooks 04, 06.

How to read the automated inbox-management dashboard and turn each panel into an action. Don't track health by hand — the system classifies every inbox and domain continuously; your job is to read it correctly and act. All thresholds live in `../references/reference.md` §1–§3.

---

## Part 1 — Inbox classification (what the tags mean)

Every inbox is auto-tagged. Exact thresholds in `reference.md` §2; the short version:

| Tag | Meaning | What you do |
|---|---|---|
| **New Inbox** | < 100 lifetime sends (excluded from campaigns until ≥ 14 days old) | Don't scale it; let it graduate |
| **Active** | placement > 70, bounce < 2%, reply ≥ 0.5%, warmup ≥ 97 | Safe to send at full cold limit |
| **Warmup Needed** | anything not New/Active/Burnt (placement < 70 forces this) | Throttled to cold 0–1, stays attached; investigate placement |
| **Burnt** | bounce > 3% AND reply < 0.5% AND warmup < 95 (all three) | Excluded from campaigns; rest & re-test (Part 5) |
| **Blacklisted** | domain on Spamhaus DBL / URIBL | Volume cut; go to playbook 06 |

**No timeout:** an inbox can sit in Warmup Needed forever — there's no auto-escalation. Placement < 50 hard-forces Warmup Needed; when placement recovers, it returns to Active on its own.

---

## Part 2 — The panels and how to read each

**1. Inbox health.** Counts by tag (New / Active / Warmup Needed / Burnt / Blacklisted) per client and total. Read it as a distribution: a rising Warmup-Needed/Burnt share is an early warning before it shows up in campaign metrics.

**2. Bounce intelligence.** Bounce split **by recipient ESP** and **by reason** (hard / block / soft), with **auto-replies stripped** (`reference.md` §7). Read the *categorized* number, never the raw one. A domain at 60% "bounce" tells you nothing until you see whether it's bad data (5.1.1), a Microsoft tenant block (5.4.1), a corporate/SEG block (5.7.1), or soft (4xx). Full workflow in playbook 06.

**3. Vendor performance by ESP (the decision matrix).** Rows = recipient Lead ESP; columns = sending vendor / inbox ESP; toggle **Automated vs Human reply**. This is the panel playbook 04 routes from. Always read **Human reply**. Collapse to "Inbox ESP only" (Google/Outlook/SMTP) for a vendor-agnostic read.

**4. Client overview.** One row per client: contacted, sends, active/warmup-needed/burnt/blacklisted, bounce, reply, human reply, unsub, placement, ESP mix. The at-a-glance triage view — drill into any row.

**5. DNS / auth health.** MX / SPF / DKIM / DMARC status per domain, with counts of OK / broken / never-checked. The point is catching **silent drift** — a record a provider quietly broke — not just initial setup. A broken record should fire an alert; treat it as P0 (dead auth = mail binned).

**6. Blacklist by vendor.** Domains on **Spamhaus DBL vs URIBL vs SURBL**, per client and per domain. **SURBL is monitor-only** — it should not tag an inbox Blacklisted or cut sending on its own (see playbook 06). If SURBL is still forcing Blacklisted status or firing alerts, that's a bug to fix, not a real listing.

---

## Part 3 — Reading signals together (diagnosis order)

One metric alone rarely tells the story. Read in this order:

- **Low reply?** → check **inbox placement** first (are you in spam?).
- **Failing placement?** → check **warmup score** over the last week.
- **High bounce?** → sender reputation declining *or* the domain is flagged — go to playbook 06.
- **Everything healthy but no replies?** → it's the **offer/targeting or copy**, not deliverability.

Timing: a **rising bounce rate is a leading indicator** (acts the same day) — a **blacklist listing is a lagging indicator** (damage already done). Watch bounces daily; never wait for a blacklist hit.

**Reply floor:** even pure out-of-office produces ~1%. Total reply **below ~1%** usually means you're **bouncing**, not that interest is low — check the bounce folder before concluding anything.

---

## Part 4 — Send limits by state (act on the tag)

Govern by the warm-to-cold **ratio**, set the cold limit by state (`reference.md` §1):

| State | Cold (Google / Outlook) | Warmup target |
|---|---|---|
| Warming (first 14 days) | 0–1 / 0–1 | cold × ratio (G 1.5 / O 2.5) |
| Active (sending) | 20 / 5 | ~30 / ~13 |
| Warmup Needed / Burnt | 0–1 / 0–1 | reduced |

> **Failover watch (EmailBison):** a throttled inbox stays attached at cold 1 and keeps sending to its in-flight leads; Bison won't reroute those leads to a healthy inbox on the campaign. Scan for leads stranded on Warmup-Needed inboxes — this is a real bounce driver and the reason for the Instantly migration.

---

## Part 5 — Rest & recover a burnt inbox

When an inbox goes Burnt, don't just leave it throttled forever. Write the cadence down and follow it:

- **Day 0:** cold effectively off; keep warmup running.
- **Days 2–10:** re-test placement; if placement + warmup recover, it re-classifies toward Active automatically.
- **After 10 days** with no recovery: retire the inbox.

For a **SEG-burnt domain**, don't retire outright — recycle onto easy Google/Outlook leads and re-test first (playbook 04, Part 3).

---

## ✅ HEALTH-REVIEW CHECKLIST (weekly)

```
[ ] Inbox-health distribution reviewed per client (Warmup Needed/Burnt share trending?)
[ ] Bounce read from the CATEGORIZED panel (auto-replies stripped), not raw
[ ] Vendor-performance matrix read on HUMAN reply; volume shifted to winners
[ ] Client overview triaged; drilled into any red row
[ ] DNS/auth health: no broken/never-checked records (broken = P0)
[ ] Blacklist-by-vendor: SURBL is monitor-only; only Spamhaus DBL/URIBL = real
[ ] Diagnosis order applied to any anomaly (reply→placement→warmup; bounce→playbook 06)
[ ] Stranded-lead check on throttled inboxes (failover gap)
[ ] Burnt inboxes on the rest-and-retest cadence
```

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
