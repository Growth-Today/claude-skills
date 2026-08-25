---
name: gt-email-infra
version: v5.1.0
description: "Email Infrastructure & Deliverability by Growth Today (growthtoday.co). Expert cold-email infrastructure and deliverability strategist. Use for infrastructure sizing, domain research and purchasing, DNS and auth (MX/SPF/DKIM/DMARC), masking versus redirect, mailbox provisioning (Google Workspace / Microsoft 365 / custom SMTP), Instantly inbox setup and warmup, going live, campaign building and ESP/SEG routing, inbox-health dashboards, and blacklist/bounce auditing. Works across EmailBison, Instantly, Smartlead, and Lemlist. Triggers on: email infra, buy or setup domains, DNS, MX, SPF, DKIM, DMARC, warmup, mailbox setup, EmailBison, Instantly, Smartlead, deliverability, inbox placement, scaling email, how many domains or mailboxes, ESP matching, SEG, Mimecast, Proofpoint, blacklist, Spamhaus, URIBL, bounce rate, bounce audit, why are my emails bouncing. Do NOT use for cold email copywriting or sequences (use gt-cold-email); the lead list (use gt-list-building); or marketing emails/newsletters."
---

## Setup (Run Once Per Session)

Before loading any sub-skill or resource, locate this skill's install directory:
1. Use Glob to search for `**/gt-email-infra/SKILL.md`.
2. The directory containing this SKILL.md is `SKILL_BASE`.
3. Sub-skills are at: `{SKILL_BASE}/.claude/skills/{sub-skill}/gt-SKILL.md`.
4. Resources are at: `{SKILL_BASE}/resources/...`.

Always resolve `SKILL_BASE` dynamically, never assume a hardcoded install location.

# Email Infrastructure & Deliverability, Orchestrator

Expert cold-email **infrastructure and deliverability** strategist. This skill is the *plumbing that gets cold email delivered*, not the message itself. Route by **who you are** and **what you're doing** to the one sub-skill that matches. Each sub-skill is self-contained and ends in a copy-pasteable checklist.

Platform: this skill supports the sequencers Growth Today uses, **EmailBison, Instantly, Smartlead, and Lemlist**. Use the matching setup sub-skill for whichever you run. Concepts are ESP-agnostic; platform-specific steps are called out inline.

## When NOT to use this skill

- Writing the email, subject lines, body, sequences, personalization → `gt-cold-email`.
- Building or verifying the lead list → `gt-list-building`.
- Marketing emails / newsletters, this is cold-outreach infrastructure only.
- CRM setup or data hygiene → `gt-hubspot-admin` / `gt-salesforce-admin`.

---

## Sub-Skill Routing

| You are… | You want to… | Sub-skill | Path |
|---|---|---|---|
| **Sales Ops** | Research and buy sending domains | **domain-research** | `{SKILL_BASE}/.claude/skills/domain-research/gt-SKILL.md` |
| **Sales Ops** | Provision mailboxes + DNS/auth (masking, not redirect) | **provisioning** | `{SKILL_BASE}/.claude/skills/provisioning/gt-SKILL.md` |
| **Sales Ops** | Set up / connect inboxes in **EmailBison** | **emailbison-setup** | `{SKILL_BASE}/.claude/skills/emailbison-setup/gt-SKILL.md` |
| **Sales Ops** | Set up / connect inboxes in **Instantly** | **instantly-setup** | `{SKILL_BASE}/.claude/skills/instantly-setup/gt-SKILL.md` |
| **Sales Ops** | Set up / connect inboxes in **Smartlead** | **smartlead-setup** | `{SKILL_BASE}/.claude/skills/smartlead-setup/gt-SKILL.md` |
| **Sales Ops** | Set up / connect inboxes in **Lemlist** (email + LinkedIn) | **lemlist-setup** | `{SKILL_BASE}/.claude/skills/lemlist-setup/gt-SKILL.md` |
| **Sales Ops → GTM** | Warm up and take domains live | **warmup-golive** | `{SKILL_BASE}/.claude/skills/warmup-golive/gt-SKILL.md` |
| **GTM Engineer** | Build campaigns, route by ESP/SEG | **campaign-building** | `{SKILL_BASE}/.claude/skills/campaign-building/gt-SKILL.md` |
| **GTM Engineer** | Read the inbox-health dashboard, act on it | **dashboard-reading** | `{SKILL_BASE}/.claude/skills/dashboard-reading/gt-SKILL.md` |
| **GTM Engineer** | Verify a workspace is set up correctly (live audit) | **setup-audit** | `{SKILL_BASE}/.claude/skills/setup-audit/gt-SKILL.md` |
| **GTM Engineer** | Audit a bounce / blacklist to root cause | **blacklist-bounce-audit** | `{SKILL_BASE}/.claude/skills/blacklist-bounce-audit/gt-SKILL.md` |

---

## Cross-Cutting Resources

- **All numbers, limits, timelines, thresholds, and the ESP/SEG taxonomy** (the single source of truth every sub-skill derives from) → Read `{SKILL_BASE}/resources/reference.md`.
- **Approved SMTP / sequencer / masking vendors** → Read `{SKILL_BASE}/resources/approved-vendors.md`.
- **2026 market performance benchmarks** (results-side: is a bounce/reply rate good or bad vs the market) → Read `{SKILL_BASE}/resources/benchmarks.md`.

---

## ▶️ Playbooks (run these, don't do them by hand)

A playbook is an executable version of a checklist: an interview that collects the inputs, a script that does the work, and an after-state that proves it landed. Read `playbook.md` first — it contains the interview questions — then run the script.

| Playbook | What it does | Needs | Status |
|---|---|---|---|
| **dns-auth-audit** | MX / SPF (record count + recursive lookup budget) / DKIM across 14 selectors / DMARC policy vs the GT standard / stray Lync SRV, plus MX→provider and SEG detection. `after.py` diffs against a saved baseline to catch silent drift. | nothing — public DNS only | ✅ tested on 6 live GT domains |
| **sizing-calculator** | Monthly goal *or* contacts × steps ÷ days-to-clear → daily volume → mailboxes → mailboxes to buy → Google/Microsoft split → domains. Parses the cold limits out of `reference.md` §1 rather than hardcoding them. | nothing — stdlib only | ✅ reproduces the §4 table exactly (`--validate`) |

```bash
cd {SKILL_BASE}/playbooks/<name>/scripts
uv run execute.py --help          # every playbook is self-documenting
```

`uv` reads the PEP-723 header in each script, so there is nothing to install. `pip install -r requirements.txt` is the fallback.

> **Scope note.** Both playbooks above are **read-only and provider-independent** — they query public DNS or do arithmetic. Anything that touches a sending platform is governed by the email infra management system boundary below: reads are fine, writes to sending limits, warmup config, tagging or routing are not GT's to make.

---

## 🔒 Email infra management system: read-only

The **email infra management system** is Growth Today's own stack — Supabase, Railway and n8n crons.
It is the source of truth for the automated inbox layer. This skill holds that knowledge and
exposes it as a **read-only checklist**. It is never a second source of truth, and the system's
dashboard stays primary.

**Read-only is not about ownership, it's about having one answer.** The system is ours, so the
rule is not "someone else's tool, hands off". It is that the moment a GTM engineer changes a
sending limit in Instantly by hand, the system's number and Instantly's number disagree and
nobody knows which is right. That is how we ended up with four inbox trackers.

**GTM engineers and Sales Ops do not change these. Read the state, report the gap, escalate.**

| Area | We may | We may NOT |
|---|---|---|
| Inbox classification / tagging | read the tag and act on it | change a tag or override a state |
| Sending limits (cold + warmup) | read and check against `reference.md` §1 | set, raise, lower or "correct" a limit |
| Warmup config (once live) | read warmup score and on/off | enable, disable or retune on a live inbox |
| Campaign routing | read the performance matrix | change routing rules |
| Blacklist monitoring | read listings | change what counts as a listing |
| Placement tests | read scores | change cadence or thresholds |
| Bounce classification | read categorised bounce | reclassify |
| Weekly DNS re-check | read the result | build a second scheduled checker |
| Inbox documentation | read it | keep a parallel tracker |
| Disconnected-inbox automation | read alerts | change the automation |
| Which lists count as a blacklist | read listings (Spamhaus DBL / URIBL only) | add a list back, or score/tag/alert on any other list |

**The one time we do set these:** at first setup, before an inbox is live and being classified,
Sales Ops or the vendor sets the starting warmup and cold values (see the instantly-setup
sub-skill). **That window closes at go-live.** After that, limits, warmup and tags belong to the email infra management system.

**Access:** no token given to a GTM engineer may change sending limits, warmup config, tagging or
routing. Instantly's account-update endpoint can change daily limits and is deliberately out of
scope — a permission test must confirm it is refused before any settings check ships.

---

## Critical Rules (Never Break)

1. **Never** cold-send from the primary/brand domain, only dedicated secondary domains.
2. **Mailboxes per domain is provider-specific: Google 2–3, Microsoft up to ~25 (average).** Google stays lean for deliverability; Microsoft can host many per domain.
3. **One domain = one workspace.**
4. **Buy across multiple registrars, spread across multiple days, max 4 per registrar per day.** ScaledMail owns the buying; GT verifies it happened.
5. **Warm up ≥ 21 days / 3 weeks** (hard floor; 4 weeks on a cautious build) before sending; **link only from domains > 30 days old**.
6. **Never disable warmup** once campaigns are running.
7. **Masking or a real landing page, never a bare 301/302 redirect** to the main site. *(Currently held: GT runs no client redirects. The open item is replacing EmailBison's masking — see `approved-vendors.md`.)*
8. **No links and no custom tracking domain** in cold email by default (share via LinkedIn or an unlinked URL).
9. **ESP matching is not a rule**: decide keep/drop from our own dashboard data.
10. Start conservative, scale gradually (**≤ 20%/week**).

## Sizing formula (detail in `{SKILL_BASE}/resources/reference.md` §4)

Monthly goal ÷ 20 workdays = daily volume → **÷ 14 per mailbox** = mailboxes → × 1.5 buffer. Domains: **Google mailboxes ÷ 2–3 + Microsoft mailboxes ÷ ~25** (Microsoft packs far more per domain). Split **60% Google / 40% Microsoft**.

> **Do not divide by 20–25.** That divisor came from the deprecated Google 30 / Microsoft 10 limits and under-buys by 43–79%. The correct blended figure falls out of §1: `0.60 × 20 + 0.40 × 5 = 14`.

**Don't do this by hand — run it:**

```bash
cd {SKILL_BASE}/playbooks/sizing-calculator/scripts
uv run execute.py --monthly-goal 15000
uv run execute.py --contacts 9000 --steps 4 --days-to-clear hiring
```

The script reads the cold limits out of `reference.md` §1 at run time, so it cannot drift from the standard the way the old spreadsheet did.

## What we can and cannot see

- **We can see and control:** each domain's public footprint (WHOIS, registrar, creation date, DNS, nameservers, masking host) and our own per-inbox/per-domain sending metrics (bounce, reply, placement, warmup).
- **We cannot inspect or split:** the vendor's shared warmup/seed pool (EmailBison + EmailGuard under one shared Growth Today account). **This risk materialised in June–July 2026: 13 of 17 audited clients were flagged at once on a shared-pool blocklist, and the shared warmup/seed pool is the suspected cause.** The escalation path is no longer hypothetical: DNS-footprint check across clients → written per-tenant isolation from the vendor → separate workspace + placement-test account per client.

## Growth Today's point of view (our answers)

- **Blacklists:** **only Spamhaus DBL and URIBL count.** Everything else is out of scope — Google and Microsoft barely weight the other lists and the email infra management system does not track them. The real fix is **domain sourcing**, not chasing delistings.
- **Microsoft / Outlook:** expect weaker Outlook placement; check sudden drops against **Microsoft BCL recalibration** dates before blaming infra; conservative limits; short copy.
- **SEG (Mimecast/Proofpoint/Barracuda):** a block is the recipient's policy working as designed. **Isolate SEG leads onto dedicated, never-reused domains**, low concurrency into one org, no links/tracking, go multi-channel, and **recycle burnt SEG domains** onto easy Google/Outlook segments before retiring.
- **Bounces:** **strip OOO/auto-replies first**: Bison inflates bounce counts by counting them (~54% in one audit). Read the real number, then diagnose.
- **Failover gap:** EmailBison can't set a cold limit of 0, so it strands leads on unhealthy inboxes, a real bounce driver. Instantly and Smartlead can set 0 and reroute the lead to a healthy inbox on the campaign.

---

## Routing Rules (composite requests)

Most real requests chain sub-skills. Common ones:

1. **"Set up cold email infra for X/month"** → domain-research → provisioning → the matching platform setup sub-skill (emailbison / instantly / smartlead / lemlist) → warmup-golive (in order).
2. **"Is this workspace set up correctly / audit our setup"** → setup-audit (live per-item PASS/WARN/FAIL).
3. **"Audit our deliverability / why are we bouncing?"** → blacklist-bounce-audit (root cause) + dashboard-reading (health context).
4. **"Build / launch a campaign"** → campaign-building (route from the matrix), then the launch gate in warmup-golive.
5. **"How many domains and mailboxes do I need?"** → `{SKILL_BASE}/resources/reference.md` §4 (sizing).
6. **"Is this bounce/reply rate good?"** → `{SKILL_BASE}/resources/benchmarks.md`.
7. **Single-topic question** → the one matching sub-skill above.

---

## Decision Tree

```
Who / what?
├─ Sales Ops: ideate or buy domains? → domain-research
├─ Sales Ops: mailboxes / DNS / auth? → provisioning
├─ Set up / connect inboxes (Bison/Instantly/Smartlead/Lemlist)? → the matching *-setup sub-skill
├─ Warm up / go live? → warmup-golive
├─ GTM: build or route a campaign (ESP/SEG)? → campaign-building
├─ GTM: read the dashboard / act on health? → dashboard-reading
├─ GTM: verify a workspace is set up right? → setup-audit
├─ GTM: something bouncing / blacklisted? → blacklist-bounce-audit
├─ Just need a number / limit / threshold? → resources/reference.md
└─ Is this metric good or bad vs the market? → resources/benchmarks.md
```

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
