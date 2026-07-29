# Playbook 03 — Warmup & Go-Live  ·  [Sales Ops → GTM]

> **Reads:** `../references/reference.md` §1, §2, §5 · `gt-list-building` (list verification)  ·  **Related:** playbooks 01, 02, 04.

Take provisioned domains (playbook 02) from cold to live safely. The whole point is patience: warm long enough, age before you link, and cross a hard gate before the first send. Numbers in `../references/reference.md` §1, §5.

---

## Part 1 — Warmup

- **Minimum 14 days / 2 weeks** before any cold send (hard floor). **Recommended 3–4 weeks.**
- **Never disable warmup** once campaigns are running.
- Warmup runs on every mailbox from day one of provisioning.

**Warmup volume = cold limit × the warm-to-cold ratio** (`reference.md` §1): Google **1.5:1**, Outlook **2.5:1**. During the first 14 days cold is effectively 0–1, so warmup carries the load.

> **Auto-warmup platforms.** Instantly and Smartlead manage warmup volume automatically — you set the behavior, not an absolute daily number. On EmailBison you set the warmup number explicitly (derive it from the ratio). Either way, keep warmup copy **neutral** so the warmup score reflects reputation, not campaign content.

**Monitor during warmup:** warmup/health score trending up (target ≥ 97 for Active, `reference.md` §2), sent *and* received both increasing, no red/disabled warmup. A red or disabled warmup is almost always a DNS/bounce problem → playbook 02 troubleshooting.

---

## Part 2 — Age-before-link gate

Warmup length is not the only clock. **Link/campaign only from domains > 30 days old AND past warmup** (`reference.md` §5). A fresh domain is in the most dangerous window regardless of warmup score — a too-new domain reads as suspect on its own, and linking from it is a documented blocklist trigger.

Don't buy pre-aged domains to skip this (owner's call, playbook 01) — age our own.

---

## Part 3 — Going live (settings)

When a domain clears the gate, take it live conservatively.

**Deliverability settings (every platform):**
- **First email plain text** — no HTML, no images (incl. signature images), no links. This is do-or-die: until you consistently reach the inbox, email #1 stays plain.
- **Open tracking OFF** — tracking pixels hurt placement (and we don't use open rate as a metric anyway).
- **No links / no tracking domain** by default (playbook 02).
- **ESP routing:** set the routing rule from the **dashboard matrix** (playbook 04), **not** from ESP-matching-as-a-rule.
- **Limit emails per company:** 2–3/day workspace-wide; extra-low concurrency into SEG orgs (playbook 04, Part 3).

**Ramp (per mailbox/day, `reference.md` §5):**

| Week | Google | Microsoft |
|---|---|---|
| 1 | 10–15 | 5 |
| 2–3 | 15–20 | 5 |
| 4+ | 20 | 5 |

**First campaign:** start with **50–100 leads**, random delays between sends, monitor **2–3 days**, then scale. **Scale by adding mailboxes, not by pushing limits higher.** Increase volume ≤ 20%/week; never add volume *and* change copy at once.

---

## Part 4 — The HARD LAUNCH GATE (nothing sends until all pass)

These are gates, not suggestions. If any is unchecked, do not launch.

```
INFRA
[ ] Every mailbox warmed ≥ 14 days (ideally 3–4 weeks)
[ ] Warmup/health scores healthy (≥ 97 target); no red/disabled warmup
[ ] Domain > 30 days old (age-before-link gate)
[ ] MX/SPF/DKIM/DMARC verified green (playbook 02)
[ ] Destination is masking / real landing page — NOT a bare redirect
[ ] Blacklist pre-check clean on domains < 60 days (Spamhaus DBL / URIBL)

LIST & COPY
[ ] List 100% verified (re-verified if > 30 days) — gt-list-building
[ ] First email plain text: no HTML / images / links
[ ] Spintax / variance present
[ ] Compliant: unsubscribe path + physical address (see reference/compliance)

ROUTING
[ ] Routing rule set from the dashboard matrix (playbook 04) — NOT ESP-matching
[ ] SEG leads isolated onto dedicated domains
[ ] Open tracking OFF; limit-per-company set; low concurrency into SEG orgs

FIRST SEND
[ ] 50–100 leads only; random delays
[ ] Monitored 2–3 days before scaling
[ ] Scale plan = add mailboxes, not raise limits; ≤ 20%/week
```

---

## Part 5 — Compliance quick-reference

Cold B2B email is legal with the basics in place (full detail can live alongside the reference):
- **CAN-SPAM (US):** accurate From/Reply-To, non-deceptive subject, valid physical postal address, clear opt-out honored promptly. No prior consent required.
- **GDPR (EU/UK):** legitimate-interest basis, relevant to the professional role, easy opt-out, lawful data source, privacy notice. Germany is restrictive (consent generally required).
- **One-click unsubscribe** headers for bulk senders to Gmail/Yahoo.

Compliant footer pattern: *"You're receiving this because of your role as [Role] at [Company]. To opt out, reply 'unsubscribe'. Privacy policy: [link]."*

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
