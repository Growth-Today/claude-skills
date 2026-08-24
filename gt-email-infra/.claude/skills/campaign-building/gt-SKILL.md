---
name: email-infra-campaign-building
description: "Build cold-email campaigns and route by ESP and SEG. Use for campaign setup, the Lead-ESP by sending-vendor decision matrix (ESP matching is dead as a fixed rule), isolating SEG leads onto dedicated domains, and the launch gate. Triggers on build campaign, ESP matching, provider matching, SEG, Mimecast, Proofpoint, Barracuda, campaign routing, sending-vendor matrix. Do NOT use for writing copy or sequences (use gt-cold-email) or reading the dashboard (use the dashboard-reading sub-skill)."
---

# Campaign Building & ESP/SEG Routing · [GTM Engineer]

> **Reads:** `{SKILL_BASE}/resources/reference.md` §1, §2, §7, §8 · **Related:** dashboard-reading, bounce-audit · gt-list-building.

How to build a campaign that routes to the right inboxes and gets optimized from data, not from a 2024 rule of thumb. Numbers and taxonomy live in `{SKILL_BASE}/resources/reference.md` §1, §2, §8.

**The one mindset shift:** you are not A/B-testing copy. You are reading a **matrix of already-segmented sends** and pushing volume toward what works. The winning combination is `lead list × sending vendor/ESP × recipient ESP × SEG`, and you find it on the dashboard, not by guessing.

---
### Determining the recipient ESP mix on a lead list

**Fastest path — run the playbook, no Clay credits:**

```bash
cd {SKILL_BASE}/playbooks/dns-auth-audit/scripts
uv run execute.py --esp-mix --file lead_domains.txt --csv acme_esp_mix.csv
```

Queries MX directly and prints the distribution, the SEG share, and a `no-email`
count (domains with no MX at all — guaranteed hard bounces, strip them before sending).
It uses the **same provider list** as the Clay formula below; the two are kept in
lockstep in `MX_PROVIDERS` inside `execute.py`. Add a provider in one place, add it
in the other.

Use Clay instead when the domains already live in a Clay table and you want the ESP
as a column alongside the rest of the enrichment.

### Clay version — How To Run MX Analysis in Clay to Determine ESP Mix on Lead Lists

First Rule: To ensure accuracy, run this MX analysis on a target account list or existing customer list. To know exactly what type of inboxes (Google vs. Microsoft vs. others) to optimize for.
### Tools Needed:
- Clay workspace
- Company domains normalized (e.g. `growthtoday.co`)
- Target account list or existing customer list

Step 1: Add Enrichment Column in Clay
- Column name: **`HTTP API`**

Step 2: Set Up the HTTP API**

- Paste this endpoint:
    
    ```
    https://dns.google/resolve?name=domain&type=mx
    ```
    
- Replace `domain` with the normalized company domain field in Clay.
    - Example: https://dns.google/resolve?name=`{{company_domain}}`&type=mx

Step 3: Rename This Column

- Rename the `HTTP API` column to: **`get_mx`**

Step 4: Add a Formula Column (copy-paste)
- Column name: MX Provider

```
  javascript
CopyEdit
{{get_mx}}?.Answer?.some(data => data?.data?.includes("google")) ? "google" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("outlook.com") || data?.data?.includes("office365")) ? "microsoft" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("pphosted.com") || data?.data?.includes("ppe-hosted") || data?.data?.includes("ppsmtp") || data?.data?.includes("sophos.com")) ? "proofpoint" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("mimecast")) ? "mimecast" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("barracuda")) ? "barracuda" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("fortimail") || data?.data?.includes("fortimailcloud.com")) ? "fortinet" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("emailsrvr.com")) ? "rackspace" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("trendmicro.com")) ? "trendmicro" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("securemx")) ? "securemx" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("mxthunder.net")) ? "mxthunder" :
{{get_mx}}?.Answer?.some(data => data?.data?.includes("mtaroutes.com")) ? "mtaroutes" :
{{get_mx}}?.Answer?.length ? "other" : "no-email"
```  

## Part 1, ESP matching is dead as a rule

Sending from the same provider the recipient uses (Google→Gmail, Outlook→Outlook) was a 2024 band-aid. **Do not hard-code it.** It can still *turn out* to be the right call for a given segment, but only the data decides, per segment, per week.

- Do **not** set "ESP matching" as a global campaign rule.
- **Do** read the Lead-ESP × sending-vendor matrix (Part 2) and route toward the cells with the best **human** reply rate.
- We are already heavily segmented, so this is a **diagnostic matrix we read**, not a set of experiments we run.

---

## Part 2, The decision matrix (read it, then route)

On the dashboard's vendor-performance panel (the dashboard-reading sub-skill), read **human reply rate** per cell. Rows = the recipient's ESP; columns = the sending vendor / inbox ESP.

| | Sending: Google | Sending: Outlook | Sending: SMTP/Custom |
|---|---|---|---|
| **Recipient: Google** | cell | cell | cell |
| **Recipient: Microsoft/Outlook** | cell | cell | cell |
| **Recipient: Enterprise / SEG** | → Part 3 (isolate) | → Part 3 | → Part 3 |
| **Recipient: Other (Zoho/custom)** | cell | cell | cell |

**How to read it**
- **Metric = human reply, never total reply.** Automated replies (OOO/auto-responders) inflate the number and mean nothing. Use the Automated-vs-Human toggle and read Human. (Bounce and positive-reply don't belong in this matrix, see `reference.md` §7 and the dashboard-reading sub-skill.)
- **Winning cell** (high human reply, bounce in range) → push more leads/volume there.
- **Losing cell** (near-zero human reply, or rising bounce) → pull leads out of that pairing; don't force it.
- **Don't assume the diagonal wins.** Google→Google or Outlook→Outlook may or may not be best; let the cell decide.
- **Data hygiene:** flag untagged inboxes and any large "Custom Mail Server / SMTP" share, an untagged column makes the matrix lie.

**Iterate weekly.** Week over week you get clear winners per `lead list + sending vendor + recipient ESP` combo. Shift weight to winners; on a pay-per-lead engagement, volume on winners is revenue.

---

## Part 3, SEG leads go in their own campaigns, on dedicated domains

Enterprise recipients behind a **Secure Email Gateway (Mimecast, Proofpoint, Barracuda)** are a separate track, not a cell in the normal matrix. A single spam complaint on a SEG can poison a whole domain, so SEG traffic must never share domains with normal leads.

**Rules**
1. **Isolate SEG leads** into their own campaign(s).
2. Run them on **dedicated, never-reused sending domains**, used for nothing else.
3. **Low concurrency into one org**: don't fire many inboxes at a single company at once (SEGs block a domain that pushes many messages into the org in a short window).
4. **No links, no tracking** (already our default), SEGs weight these heavily.
5. **Go multi-channel**: pair with LinkedIn/phone; email won't be your only path into SEG accounts.
6. **Recycle, don't waste.** When bounce climbs on a SEG campaign, swap the domain out, then re-test it on easy **Google/Outlook** segments before retiring. A SEG-burnt domain often still performs on regular leads. Use placement + warmup score as the swap trigger (the dashboard-reading sub-skill).

**Expectation-setting:** lower reply rates on SEG-heavy segments are the recipient's policy working as designed, not a broken setup. Prioritize reachable segments; shift weight off aggressively-gated ones rather than burning domains forcing them.

---

## Part 4, Building the campaign (mechanics)

Build so the campaign is **visible to and managed by the inbox-management system** and so **nothing sends from an unhealthy inbox**.

1. **Create the campaign through the management dashboard, not directly in the sequencer.** A campaign built directly in the sequencer is invisible to routing, dashboard, and health management. (If you must draft in the sequencer, attach **no inboxes** until the system equips it, so it can't send unmanaged.)
2. **Set the routing rule:** `Google` | `Microsoft` | `Both` (based on Part 2, not on ESP-matching dogma).
3. **Scope the inbox pool** with tag filters: *include-by-tag* to restrict to a chosen pool, *exclude-by-tag* to keep away from inboxes used elsewhere; set the **region** tag where a client sends by region.
4. **Let the automation attach/detach.** It attaches only eligible inboxes and maintains membership:
 - **Active / New Inbox** → eligible (New Inbox only if ≥ 14 days old by creation date).
 - **Warmup Needed** → throttled to cold 0–1 but kept attached.
 - **Burnt** → excluded.
5. **Naming convention:** `Segment – ESP`, e.g. `Webvisits – Google`, `Webvisits – Microsoft`; low volume (< 500 leads) → `Webvisits – All` (Both); by rep → `Webvisits – Andrew`.

> **Failover caveat (EmailBison only):** a lead being prospected by an inbox that turns Warmup Needed keeps getting sent from that throttled inbox, Bison won't move the lead to a healthy inbox on the campaign. Instantly and Smartlead can reroute the lead to a healthy inbox; EmailBison can't. Watch for leads stranded on throttled inboxes (the dashboard-reading sub-skill).

---

## Part 5, Launch gate (hard, before any send)

These are non-negotiable gates, not suggestions:

- [ ] **List 100% verified** (and re-verified if > 30 days old), see `gt-list-building`.
- [ ] **First email is plain text**: no HTML, no images (incl. signature), no links.
- [ ] **Spintax / variance present** on subject + body.
- [ ] **Blacklist pre-check** on any domain < 60 days old (Spamhaus DBL / URIBL), see the bounce-audit sub-skill.
- [ ] **SEG leads isolated** onto dedicated domains (Part 3), not mixed into normal campaigns.
- [ ] **Routing rule set from the matrix** (Part 2), not from ESP-matching.

---

## ✅ CAMPAIGN CHECKLIST (copy-paste)

```
ROUTING
[ ] Segment defined: lead list × recipient ESP × (SEG? yes/no)
[ ] SEG leads split into their own campaign on dedicated, never-reused domains
[ ] Routing rule (Google/Microsoft/Both) chosen from the dashboard matrix, NOT ESP-matching
[ ] Include/exclude-by-tag set; region tag set if client sends by region

BUILD
[ ] Campaign created via the management dashboard (or drafted with NO inboxes attached)
[ ] Only Active/eligible New Inbox attached; Burnt excluded; Warmup Needed throttled+attached
[ ] Naming convention applied (Segment – ESP)

LAUNCH GATE
[ ] List 100% verified (re-verified if >30 days)
[ ] First email plain text: no HTML / images / links
[ ] Spintax / variance present
[ ] Blacklist pre-check on domains <60 days
[ ] Low concurrency into any single SEG org

OPTIMIZE (weekly)
[ ] Read human (not automated) reply per matrix cell
[ ] Push volume to winning cells; pull leads out of losing cells
[ ] Swap SEG domains on rising bounce; re-test on easy Google/Outlook before retiring
[ ] Flag untagged inboxes / large Custom-SMTP share
```

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
