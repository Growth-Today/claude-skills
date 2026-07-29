# Playbook 06 — Blacklist & Bounce Audit  ·  [GTM Engineer]

> **Reads:** `../references/reference.md` §7  ·  **Related:** playbooks 05, 01 · `gt-list-building`.

How to find where a bounce or blacklist problem *actually* comes from, so you fix the real cause instead of treating every bounce the same. The output is a clear root cause — **infrastructure, list/data, or copy** — and the right owner. Codes and thresholds in `../references/reference.md` §7.

---

## Step 0 — Strip auto-replies FIRST (or every number is wrong)

Before you read any bounce rate: **out-of-office and auto-replies are miscounted as bounces.** In one real audit this inflated the count by **~54%** (raw 2,687 → 1,231 real). Reclassify OOO/auto-reply *out* of the bounce bucket first.

Auto-reply / OOO markers to pull out: `Out of office`, `Auto-reply`, `automatic reply`, `on leave`, `annual leave`, `currently away`, `will respond when`. Everything below is read on the **cleaned** bounce set.

---

## Step 1 — Categorize every bounce

Read the SMTP text body and bucket by distinctive markers:

| Category | Markers |
|---|---|
| **Unverified / bad data** (hard) | `550 5.1.1`, "does not exist", "No such user", "User Unknown", "Address not found", "Domain name not found", "DNS Error", "Invalid recipient", "Undeliverable address" |
| **Microsoft tenant** | `550 5.4.1 ... Access denied`, `outlook.com`, `aka.ms/EXOSmtpErrors`, `Exchange Online`, `SN1PEPF`, `NAMPRD`, `prod.outlook.com` |
| **Corporate / SEG** | `550 5.7.1`, "Policy rejection", "Relay access denied", "marked as invalid", "administratively denied", "security policy", "firewall", "gateway rejected" |
| **Other** | `4xx` / `450` / `451` / `452` / `421`, "Mailbox full", "Quota exceeded", "Spam detected", "SPF/DKIM/DMARC", "Authentication failed", "Blocked", "Rate limit", "Message too large", `552` |

Plot counts per category, split by **inboxes on all domains vs inboxes on blacklisted domains**, and separate **warmup bounces from campaign bounces**.

---

## Step 2 — Read soft vs hard to get the cause

Code form X.X.X: first digit = outcome (4 temporary, 5 permanent), second = category. Full table in `reference.md` §7.

- **Hard 5XX** (5.1.1 "does not exist") → **list / verification / data accuracy**. A wave of these = the addresses weren't valid when sent.
- **Soft 4XX** → **temporary / infra** (retry, sending limits, mailbox state).
- **5.7.1 / policy / blocked** → **corporate filtering / SEG / reputation** — not the address itself.

---

## Step 3 — The blacklist read (SURBL is de-scoped)

- **Only Spamhaus DBL and URIBL count.** If a domain is listed there, treat the domain as compromised.
- **SURBL is monitor-only.** Google and Microsoft barely weight it. A SURBL listing must **not** tag an inbox Blacklisted or cut its sending on its own — if it does, that's a bug to fix, not a real problem. Don't chase SURBL delistings.
- **One flag is domain-level, not inbox-level.** A single SEG/blacklist hit poisons the whole domain — state that plainly when scoping exposure.
- **Pre-launch gate:** blacklist-check every domain **< 60 days old** before it sends (Spamhaus DBL / URIBL).
- **Microsoft drops:** before blaming infra for an Outlook cluster, check the dates against **Microsoft BCL recalibration** — a provider-side threshold change can move mail to junk with no change on your end.

---

## Step 4 — Neutral-copy test (copy vs infrastructure)

The missing diagnostic behind most "is it the copy or the domain?" confusion. Run it on each flagged domain **before** deciding retire vs delist.

1. Send from **one provider's inboxes only** (all Google, or all Outlook — don't mix).
2. Swap the sales copy for a **neutral, transactional one-liner** — no links, no HTML, no images ("See you next week!").
3. Compare: neutral inboxes but sales copy doesn't → **copy** is the problem. Still fails from specific inboxes/providers → **inbox/reputation** is the problem.

---

## Step 5 — Root cause → owner

Name the cause explicitly and route it:

| Root cause | Signal | Owner / action |
|---|---|---|
| **Infra / automation** | warmup ratio off, DNS/auth drift, throttling/failover | Automation/OpsLab team |
| **List / data** | wave of hard 5.1.1 / bad-data bounces | Verification/enrichment — confirm which verifier ran, fix the step (`gt-list-building`) |
| **Copy** | consistent spam placement everywhere, empty liquid, weak variance, spam words, aggressive volume | GTM Engineer rewrites (client conversation if they supplied/insisted on the copy) |
| **Domain burned** | large share of inboxes on Spamhaus/URIBL-listed domains | Buy new domains + new infra (playbooks 01–02); recycle SEG-burnt domains first |

Also check before you conclude: spintax present? complaints/unsubs overall vs on these inboxes? any inbox used in another sequencer in parallel?

**Exposure decides urgency:** always state what share of inboxes/domains/leads is affected (e.g. "~half the inboxes sit on flagged domains"). Scale, not severity of one case, sets priority.

---

## Step 6 — Fix root cause before delisting; rest burnt inboxes

- **Never request delisting before fixing the root cause** — you'll just get re-listed.
- **Retire vs delist** per domain, decided after the neutral-copy test.
- **Rest a burnt inbox:** cold off → re-test days 2–10 → retire after 10 with no recovery (playbook 05, Part 5).

---

## Workflow note (data pull)

The mechanical pull (export leads → map sender email → domain → cross-reference listed domains → pull the bounce folder → categorize) can run in Clay or any table tool against the sequencer's API. Keep it **in the client's own workspace with the client's IDs** — never run an audit against the wrong workspace. The *analysis* above is what matters; the extraction is just plumbing.

---

## ✅ AUDIT CHECKLIST (copy-paste)

```
[ ] Auto-replies / OOO stripped BEFORE reading any bounce rate
[ ] Bounces categorized (bad-data / MS-tenant / corporate-SEG / other)
[ ] Soft vs hard read → cause mapped (data / infra / policy)
[ ] Warmup bounces separated from campaign bounces
[ ] Blacklist read: only Spamhaus DBL + URIBL count; SURBL monitor-only
[ ] Domains <60 days blacklist-pre-checked
[ ] Outlook drops checked against Microsoft BCL recalibration dates
[ ] Neutral-copy test run on each flagged domain (copy vs infra)
[ ] Root cause named + routed to the right owner
[ ] Exposure quantified (share of inboxes/domains/leads affected)
[ ] Root cause fixed BEFORE any delisting request
[ ] Burnt inboxes on the rest-and-retest cadence
```

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
