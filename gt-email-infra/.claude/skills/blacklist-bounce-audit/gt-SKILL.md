---
name: email-infra-bounce-audit
description: "Audit a bounce or blacklist problem to root cause and produce a full bounce report. Use for pulling replies via the EmailBison MCP/API, working around the broken type=bounced filter, stripping auto-replies, classifying bounces (Hard/Soft/Block) by SMTP/DSN code, running the neutral-copy test, and tracing the cause to infrastructure, list/data, or copy. Triggers on bounce audit, why are my emails bouncing, blacklist, Spamhaus, URIBL, hard bounce, soft bounce, block bounce, SMTP codes, DSN codes, bounce report, deliverability drop. Do NOT use for reading the health dashboard (use the dashboard-reading sub-skill) or list verification (use gt-list-building)."
---

# Blacklist & Bounce Audit · [GTM Engineer]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §7 · **Tools:** EmailBison MCP (`accounts_list`, `campaigns_list`, `replies_list`), optional Notion MCP · **Related:** dashboard-reading, domain-research · gt-list-building.

Find where a bounce or blacklist problem *actually* comes from, then produce a report the team can act on. The output is a clear root cause, **infrastructure, list/data, or copy**, plus a full bounce breakdown and the right owner. Runs on any EmailBison workspace (specify the MCP server / API host). Codes and thresholds in `{SKILL_BASE}/resources/reference.md` §7.

**When to run:** monthly/quarterly check-in · bounce rate crosses 3% · before scaling send volume · a client asks "why are my emails bouncing?" · after onboarding new domains/inboxes.

**Ask if not provided:** which **EmailBison MCP server / API host** (the workspace), **output location** for the CSV + report, and an optional **Notion page URL** to push the report to. Always run against the correct workspace with that workspace's own IDs, never audit the wrong workspace by accident.

---

# Part A, Runbook (pull the data)

## Step 0, Workspace baseline

- `accounts_list` (paginate all pages, 15/page): total inboxes, provider split (Google vs Microsoft/Outlook), warmup-status distribution (Active / Warmup Needed / Blacklisted).
- `campaigns_list` (all statuses, active, paused, completed): per-campaign `id`, `name`, `status`, `total_leads_contacted`, `emails_sent`, `bounced`, `unique_replies`, `created_at`.
- Workspace totals: leads contacted (Σ `total_leads_contacted`), emails sent (Σ `emails_sent`), dashboard bounce count (Σ `bounced`) and rate vs contacts.

> **Denominator rule:** always compute bounce rate against **`total_leads_contacted`** (people), never `emails_sent` (messages). One lead can get several emails but bounces once.

## Step 1, Pull all replies from campaigns with bounces

> **⚠️ The `?type=bounced` filter on the replies endpoint is BROKEN**: it returns all reply types unfiltered. You must pull everything and filter client-side (Step 2).

For each campaign where `bounced > 0`: `replies_list` with the `campaign_id` filter, paginate all pages (15/page). If a campaign exceeds ~15,000 replies (page-1001 returns 422), switch to **cursor pagination**. For very large volumes (50K+), pull with a shell script instead of MCP calls:

```bash
# adapt the host + API key per workspace
BASE="https://<your-emailbison-host>/api"
KEY="$EMAILBISON_API_KEY"
CAMPAIGN_ID="XXXX"
curl -s -H "Authorization: Bearer $KEY" \
 "$BASE/campaigns/$CAMPAIGN_ID/replies?pagination_type=cursor&per_page=15"
# then follow meta.next_cursor
```

## Step 2, Filter to real bounces (the tool-level auto-reply strip)

Keep ONLY records where **`type == "Bounced"` AND `folder == "Bounced"`**. Discard everything else, regardless of which endpoint returned it.

> **This is why bounce numbers lie.** Auto-replies/OOO come back as **`Tracked Reply`** and our own follow-ups as **`Outgoing Email`**, neither is a bounce. Counting them inflated one real audit by **~54%** (raw 2,687 → 1,231 real). Text markers that confirm an auto-reply if you filter the body: `Out of office`, `Auto-reply`, `automatic reply`, `on leave`, `currently away`, `will respond when`.

Document the filter (this proves the real count):

| EmailBison `type` | Count | % of records | A bounce? |
|---|---|---|---|
| Tracked Reply (auto-replies/OOO) | X | X% | No |
| Outgoing Email (our follow-ups) | X | X% | No |
| Bounced (real bounce notifications) | X | X% | **Yes** |

## Step 3, Classify each bounce by SMTP/DSN code

Parse `text_body` / `html_body`, extract the SMTP status + DSN code, and bucket. Fundamentals (4xx=temporary, 5xx=permanent) in `reference.md` §7.

| Pattern | Category |
|---|---|
| `550 5.1.1`, `550 5.1.10`, `550 5.4.1`, `550 5.2.1`; "does not exist", "unknown user", "invalid recipient" | **Hard**: address invalid / mailbox disabled |
| `554 5.4.14` (hop count exceeded) | **Hard** |
| `421`, `450`, `451`, `452`; "temporarily", "try again", "rate limit" | **Soft**: temporary failure |
| `554` (no sub-code), `550 5.7.1` (policy); "blocked", "spam", "blacklist", "reputation", "policy" | **Block**: reputation/policy |
| `550 5.7.352`, `550 5.7.193`, `550 5.7.129` (Microsoft DMARC/SPF/sender-reputation) | **Block**: Microsoft auth/reputation |
| `554 5.2.2` (mailbox full / quota) | **Block**: often an abandoned mailbox |
| no code + no keyword match | **Unknown** |

**Priority if multiple signals match:** Block > Hard > Soft > Unknown. (Maps to `reference.md` §7 buckets: Hard ≈ Unverified/bad-data; Block ≈ Corporate/SEG + Microsoft-tenant; Soft ≈ Other/temporary.)

---

# Part B, Read the results (diagnosis)

## Blacklist read (two lists only)

- **Only Spamhaus DBL and URIBL count.** Listed there → treat the domain as compromised. Nothing else is a blacklist reason.
- **Do not act on any other list.** Google and Microsoft barely weight the rest, and the email infra management system does not track them. A hit on another list must **not** tag an inbox Blacklisted, cut sending, or fire an alert — if it does, report the bug. Don't chase those delistings.
- **One flag is domain-level, not inbox-level**: a single SEG/blacklist hit poisons the whole domain.
- **Pre-launch gate:** blacklist-check every domain **< 60 days old** before it sends (Spamhaus DBL / URIBL).
- **Microsoft drops:** before blaming infra for an Outlook cluster, check dates against **Microsoft BCL recalibration**: a provider-side threshold change can junk mail with no change on your end.

## Neutral-copy test (copy vs infrastructure)

The diagnostic behind most "is it the copy or the domain?" confusion. Run on each flagged domain **before** deciding retire vs delist.
1. Send from **one provider's inboxes only** (all Google, or all Outlook, don't mix).
2. Swap the sales copy for a **neutral one-liner**: no links, HTML, or images ("See you next week!").
3. Neutral inboxes but sales copy doesn't → **copy**. Still fails from specific inboxes/providers → **inbox/reputation**.

## Root cause → owner

| Root cause | Signal | Owner / action |
|---|---|---|
| **Infra / automation** | warmup ratio off, DNS/auth drift, throttling/failover | Email infra management system |
| **List / data** | wave of Hard `5.1.1` / bad-data bounces | Verification/enrichment, confirm which verifier ran, fix the step (`gt-list-building`) |
| **Copy** | consistent spam placement everywhere, empty liquid, weak variance, spam words, aggressive volume | GTM Engineer rewrites (client conversation if they supplied the copy) |
| **Domain burned** | large share of inboxes on Spamhaus/URIBL-listed domains | Buy new domains + new infra (the domain-research and provisioning sub-skills); recycle SEG-burnt domains first |

Also check: spintax present? complaints/unsubs overall vs on these inboxes? any inbox used in another sequencer in parallel? **Exposure decides urgency**: state what share of inboxes/domains/leads is affected; scale sets priority, not one bad case.

## Fix root cause before delisting; rest burnt inboxes

- **Never request delisting before fixing the root cause**: you'll just get re-listed.
- **Retire vs delist** per domain, after the neutral-copy test.
- **Rest a burnt inbox:** cold off → re-test days 2–10 → retire after 10 with no recovery (the dashboard-reading sub-skill, Part 5).

---

# Part C, Report output

## Sections to build

**1. Real bounces by time window** (7D / 30D / 60D / ALL): Real Bounces · Hard/Hard% · Soft/Soft% · Block/Block% · Unknown.

**2. Rates against contacts** (denominator = leads contacted):

| Type | Count | Rate | Meaning |
|---|---|---|---|
| Block / reputation | X | X% | spam filters rejecting |
| Hard | X | X% | address doesn't exist |
| Soft | X | X% | temporary |
| Unknown | X | X% | |
| **Overall** | **X** | **X%** | |

**Audit thresholds:** Block > **2%** = problem · Hard > **1.5%** = list-quality issue · Overall > **3%** = act · Overall > **5%** = critical, pause and fix. (Overall aligns with `reference.md` §3.)

**3. Block bounces by era** (group campaigns by quarter from `[Qn]` name markers or `created_at`), shows whether block/reputation is trending up or stable.

**4. Top 10–15 SMTP/DSN codes** by frequency (code · count · type).

**5. Worst campaigns**: top 10 by real bounce count (campaign · hard · soft · block). Flag any campaign at **100% Block**: pure reputation problem.

**6. What to do**: recommendations keyed to the data (block-heavy → check DMARC/SPF/DKIM, cut volume, rotate worst domains, review copy; hard-heavy → verify lists pre-upload; soft → mailbox-full/timing; Microsoft block codes 5.7.352/5.7.193/5.7.129 → DMARC/SPF alignment for Microsoft).

## Files + Notion

- **CSV** `bounce-audit-YYYY-MM-DD.csv`: `campaign_id,campaign_name,status,leads_contacted,emails_sent,total_bounces,hard,soft,block,unknown,bounce_rate,block_rate` + a TOTAL row.
- **Markdown** `bounce-audit-YYYY-MM-DD.md`: the six sections, plain language, numbers first.
- **Notion (if a URL is given):** push the report, then fetch the page back and verify tables rendered before confirming.

## Chat summary (present before confirming output)

```
## Bounce Audit, [Workspace], [Date]
X real bounces from X contacts (X% bounce rate)
- Block/reputation: X (X%), [trending up/stable/down]
- Hard: X (X%), [above/below] 1.5%
- Soft: X (X%), negligible / needs attention
Worst campaign: [Name], X bounces, X% block
Top block code: [code], [meaning]
Action required: 1) [most urgent] 2) … 3) …
```

---

## Known API limitations (EmailBison)

| Issue | Workaround |
|---|---|
| `?type=bounced` filter broken on replies endpoint | Pull all replies, filter client-side by `type == "Bounced"` AND `folder == "Bounced"` |
| 15-per-page hard limit | Paginate all pages; use cursor pagination for 15K+ |
| Page 1001+ returns 422 | Switch to `pagination_type=cursor` |
| `campaign-events/stats` with `sender_email_ids[]` returns zeros | Use `campaign_ids[]` instead |
| `campaigns/{id}/stats` returns 405 on some workspaces | Use the campaign-list object stats for all-time |

---

## ✅ AUDIT CHECKLIST (copy-paste)

```
PULL
[ ] Correct workspace / MCP server confirmed; baseline pulled (accounts + campaigns)
[ ] All replies pulled from every campaign with bounced > 0 (cursor for 15K+)
[ ] Filtered to real bounces: type == "Bounced" AND folder == "Bounced"
[ ] Auto-replies (Tracked Reply / OOO) and Outgoing Email excluded, filter table built

CLASSIFY
[ ] Each bounce classified Hard / Soft / Block / Unknown by SMTP/DSN code (Block > Hard > Soft > Unknown)
[ ] Warmup bounces separated from campaign bounces
[ ] Rates computed against leads_contacted (not emails_sent)

DIAGNOSE
[ ] Blacklist read: only Spamhaus DBL + URIBL count; no other list is a reason
[ ] Domains < 60 days blacklist-pre-checked
[ ] Outlook drops checked against Microsoft BCL recalibration dates
[ ] Neutral-copy test run on each flagged domain (copy vs infra)
[ ] Root cause named + routed to the right owner; exposure quantified

REPORT + FIX
[ ] 6 report sections + CSV built; Notion pushed & verified (if requested)
[ ] Chat summary presented
[ ] Root cause fixed BEFORE any delisting request
[ ] Burnt inboxes on the rest-and-retest cadence
```

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
