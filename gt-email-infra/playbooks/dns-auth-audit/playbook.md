---
name: dns-auth-audit
description: "Audit MX, SPF, DKIM, DMARC and SRV hygiene across a set of sending domains, classify each domain's provider, and prove a DNS fix landed. Replaces the manual MXToolBox / easyDMARC / dmarcian click-through."
license: MIT
metadata:
  author: growthtoday
  version: "1.0"
  category: deliverability
---

# DNS / Auth Audit

Check every sending domain against the four records cold email requires, plus two defects the manual workflow kept missing. Read-only: it queries public DNS and touches nothing at any provider.

## Why This Matters

The old process was one person opening MXToolBox, typing in a domain, eyeballing four tabs, and moving to the next one. At 30–50 domains per client that is an hour of clicking, and it only ever catches what someone remembered to look at.

Three things slipped through it every time:

- **Two SPF records.** Both are ignored by the receiver, so SPF silently fails while every tool shows "SPF found."
- **An over-budget SPF chain.** More than 10 DNS lookups is a permerror under RFC 7208 §4.6.4. You cannot see this by reading the record — you have to walk every `include:` recursively.
- **Stray Lync/Skype SRV records**, copy-pasted from the Microsoft 365 setup guide into domains that will never run Teams.

And the real risk isn't setup, it's **silent drift**: a provider quietly breaks a record months later. That is why this playbook has an after-state that diffs against a saved baseline.

## Prerequisites

- The domain list. Nothing else — no API key, no account access.
- `uv` (recommended) or Python 3.10+ with `dnspython`.

## Interview: Gather Requirements

**Q1: Which domains?**
Either paste them, or point at a file with one per line. If the client is on Instantly, the inbox list is the domain list — pull it and dedupe on the part after the `@`.

**Q2: Is this a pre-launch gate or a drift check?**
- *Pre-launch* — run `execute.py` and use the exit code: 0 = clear, 2 = blocked.
- *Drift check* — run `execute.py` against last month's CSV baseline, then `after.py` to see what moved.
- Default: pre-launch gate.

**Q3: Does this client run anything other than cold email on these domains?**
Matters for DMARC. `p=reject` is the GT standard, but if a domain also sends transactional or marketing mail through a third party that isn't in SPF/DKIM, moving to reject will bin that mail. Confirm before recommending the change.

**Q4: Do you already have a baseline CSV for these domains?**
If yes, pass it and skip straight to the after-state diff.

## Plan

1. Collect the domain list.
2. Run `execute.py` — audits every domain, prints per-dimension verdicts, writes a CSV baseline.
3. Triage: MX, SPF, DKIM and DMARC must all be PASS. A WARN on any of the four (p=quarantine, no DKIM) blocks launch too — the exit code says so. SRV hygiene is tidiness and does not block.
4. Route the fixes (DNS host for records; the email infra management system if it's a drift on a live inbox — see the read-only boundary in `SKILL.md`).
5. Run `after.py` to prove the fix landed and nothing else regressed.

## Two modes

| Mode | Whose domains | Answers |
|---|---|---|
| default | **ours** (sending) | Is this domain safe to send from? |
| `--esp-mix` | **theirs** (recipients) | What are we sending into, and how much of it is behind a SEG? |

`--esp-mix` replaces the manual Clay MX-analysis column in campaign-building (added by
PR #29) with a direct DNS lookup — same provider list, no Clay credits, no HTTP API
column. It also separates **`no-email`** (no MX at all, so guaranteed hard bounces —
strip before sending) from **`other`** (mail routed somewhere we don't recognise),
a distinction the audit column didn't make.

```bash
uv run execute.py --esp-mix --file lead_domains.txt --csv acme_esp_mix.csv
```

## Execute

```bash
cd playbooks/dns-auth-audit/scripts

# Pre-launch gate on a handful of domains
uv run execute.py acme-outreach.com acmehq-mail.com

# A full client batch from a file
uv run execute.py --file domains.txt --csv acme_baseline.csv
```

Exit code is `0` when nothing failed and `2` when something did, so it drops into CI or a pre-launch hook unchanged.

### What each dimension means

| Dimension | PASS | WARN | FAIL |
|---|---|---|---|
| **MX** | present, provider classified | — | absent, or a null MX (`0 .`) — the domain cannot receive mail, so replies and bounce handling are dead |
| **SPF** | exactly one record, ≤ 10 lookups | — | zero records, more than one record, or over the lookup budget |
| **DKIM** | a usable key on a known selector | — | nothing on 14 known selectors, or a key that is revoked (empty `p=`) or a CNAME pointing at nothing |
| **DMARC** | `p=reject` | `p=none` or `p=quarantine` — GT standard is reject | no record, or an unparseable policy |
| **SRV-hygiene** | clean | stray Lync/Skype SRV present — tidy it up, but no mail filter reads it | — |

**The gate.** MX, SPF, DKIM and DMARC must all be **PASS** for exit 0. A WARN on any of the four
blocks launch, because the two WARNs that exist there — a `p=quarantine` DMARC and an unresolved
DKIM selector — are exactly the states you do not want to launch on. SRV hygiene is outside the
gate on purpose: SIP records are read by Teams clients, not by mail filters.

Provider classification comes from the MX hostnames. The table lives in `MX_PROVIDERS` in `execute.py` and covers **google · microsoft · proofpoint · mimecast · barracuda · fortinet · rackspace · trendmicro · securemx · mxthunder · mtaroutes · zoho**, plus `other` and `no-email`. Six of those are security gateways and get a `[SEG]` marker, which is what campaign routing isolates on.

> **Keep it in sync.** This list mirrors the Clay MX-analysis formula in campaign-building (PR #29). They must not diverge — add a provider in both places.

## After State

```bash
uv run after.py --csv acme_baseline.csv
```

Re-queries every domain in the baseline and reports each dimension as FIXED, STILL FAIL, REGRESSED or CHANGED.

**REGRESSED is the one to care about.** A record that was healthy and is now broken means a provider changed something underneath you. Treat it as P0: dead auth means mail goes to the bin, and nothing in the sequencer will tell you.

**Verification checklist:**

1. Every previously-failing dimension now reads FIXED.
2. Zero REGRESSED.
3. Exit code `0`.
4. Spot-check one fixed domain by hand — `dig TXT _dmarc.<domain>` — so you are not trusting a single tool.

## Key Technical Learnings

- **Read the limits from the source, not from memory.** DMARC's GT standard is defined in `reference.md` §6 and the script checks against it. When policy changes, the reference file changes and the audit follows.
- **"SPF found" is not "SPF works."** Count the records and walk the chain. Both failure modes present as a green tick in every UI tool.
- **A missing DKIM is a FAIL, not a shrug.** Fourteen selectors covers Google, Microsoft and the common vendors. A custom selector is legitimate, but "we probably use a custom one" is not a launch condition: confirm it in the provider UI and add it to `SELECTORS`, so the next run proves it instead of assuming it.
- **A published key can still be a dead key.** `v=DKIM1; p=` with nothing after it means the key was revoked, and a selector CNAME whose target has no TXT is a dangling delegation. Both used to report PASS. Both mean the domain cannot sign mail.
- **A timeout is not a finding.** The script tells "the name answered with nothing" apart from "the lookup failed", and only calls the first one broken. Reporting a slow resolver as a dead key is how you fail a healthy domain.
- **Set the baseline early.** The audit's value compounds only if you have something to diff against. Save the CSV per client, per month.
- **Fixing a live inbox's records is a DNS-host action, not a system-side one** — but if the *drift alert* came from the email infra management system's weekly re-check, report it there too. Don't build a competing scheduler.

---

*Part of [gt-email-infra](https://www.growthtoday.co/claude-skills) by [Growth Today](https://www.growthtoday.co) · maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/).*
