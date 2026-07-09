# Blacklist & Bounce Audit

How to find where a bounce actually comes from, so you fix the real cause instead of treating every bounce the same. This is a deep-analysis workflow: it pulls sender and bounce data out of EmailBison via Clay, cross-references blacklisted domains, categorizes every bounce, reads the SMTP codes, and lands on a clear root cause — infrastructure, list/data, or copy.

The workflow runs on the EmailBison + Clay stack. The three working tables are: **Leads**, **Inboxes**, and **Bounced Emails**.

---

## Part 1 — Export lead data from EmailBison

1. Go to EmailBison, select the correct workspace (e.g. Growth Today).
2. Navigate to Leads → Select All Leads → Export Leads → download CSV.

## Part 2 — Upload to Clay

Create a new Clay table, upload the CSV, name it `ClientName - Bison Leads Raw`.

## Part 3 — Map sender data via API

- **Find Lead ID** — enrichment `Find Lead` (Bison). Maps the internal Bison Lead ID + Sender ID (required for API calls).
- **Get sent email data** — HTTP API GET against your ESP's API — the sender-emails endpoint for a lead (EmailBison: `/api/leads/{Lead_Id}/sent-emails`). Retrieves `{Sender ID}`.

## Part 4 — Extract domain

Clay free enrichment "Identify email type & extract company domain". Input `{Sender ID}` → output Domain.

## Part 5 — Create master Inboxes table

Use "Send table data" to create `ClientName - Inboxes`, pushing: Sender email, Sender ID, Domain.

---

## Part 6 — Get blacklisted domains

Two sources:

**Option A — Airtable Deliverability Dashboard:** filter `Blacklisted = TRUE` for the workspace, export the list.

**Option B — EmailGuard (SURBL tab):** navigate to SURBL, scrape the domain list (Instant Data Scraper Chrome extension), import + dedupe in Clay, create `ClientName - Blacklisted Domains`. Validate against your team's spam-results channel (e.g. the EmailGuard result count).

## Part 7 — Lookup blacklisted domains

In `ClientName - Inboxes`, add a Lookup column matching inbox domain against the blacklisted-domain table. Now you know which inboxes sit on blacklisted domains.

## Part 8 — Get sender email data

Add an HTTP API column against your ESP's sender-emails endpoint (EmailBison: `/api/sender-emails/{Sender_ID}`). Map: Emails Sent Count, Unsubscribed Count, Bounced Count, Total Replied Count, Total Leads Contacted Count.

## Part 9 — Warmup data

HTTP API against your ESP's warmup endpoint (EmailBison: `/api/warmup/sender-emails/{Sender_ID}`). Map Warmup Email Sent. Formula for tags: `({{Get Warmup data}}?.data?.tags||[])?.map(t=>t?.name)?.filter(Boolean)?.join(", ")`.

## Part 10 — Key formulas

- **Warmup vs cold send ratio:** `Warmup Email Sent / Cold Email Send Count` — compare against the SOP ratios (Google 1.5, Microsoft 2.5).
- **Bounce rate:** `Bounce Count / Total Leads Contacted`.
- **Reply rate:** `Total Replied Count / Total Leads Contacted`.

## Parts 11–14 — Pull and enrich bounce emails

- **Get bounce folder** — HTTP API against your ESP's replies endpoint filtered to the bounced folder (EmailBison: `/api/sender-emails/{Sender_ID}/replies?folder=bounced`).
- **Push to a new table** — `ClientName - Bounce Emails`, mapping Sender Email, Domain, Text body, subject.
- **Clean the text body** (Clay cell limit): `({{Rows from: GT Inboxes}}?.text_body || "").slice(0,1000)`.
- **Extract the lead email** from the bounce body — free enrichment "Extract URLs & Emails", then `({{Extract URLs and emails from text}}?.urlsAndEmails||[])?.map(x=>x?.linkType?.toLowerCase()==="email"?x?.value:"")?.filter(Boolean)?.[0]||""`.
- **Map bounce to campaign** — Find Lead (Bison) → Campaign ID; HTTP API against your ESP's campaigns endpoint (EmailBison: `/api/campaigns/{Campaign_ID}`) → Campaign Name.

---

## Part 15 — Categorize bounce reasons

Filter the Text Body of `ClientName - Bounce Emails` and create a Clay view per category. Distinctive identifiers:

**Unverified / Bad Data** — `550 5.1.1`, "does not exist", "No such user", "User Unknown", "email account that you tried to reach is inactive", "Address not found", "Domain name not found", "DNS Error", "couldn't be found", "Invalid recipient", "Recipient unknown", "Undeliverable address".

**Microsoft Tenant** — `550 5.4.1 Recipient address rejected: Access denied`, `outlook.com`, `aka.ms/EXOSmtpErrors`, `Exchange Online`, `SN1PEPF`, `NAMPRD`, `prod.outlook.com`.

**Corporate** — `550 5.7.1`, "Policy rejection", "Relay access denied", "marked as invalid", "User email address is marked as invalid", "administratively denied", "security policy", "corporate policy", "firewall", "gateway rejected".

**Other** — `4xx` / `450` / `451` / `452` / `421`, "Mailbox full", "Quota exceeded", "Auto-reply", "Out of office", "Spam detected", "SPF/DKIM/DMARC", "Authentication failed", "Blocked", "Blacklisted", "Rate limit", "Message too large", `552`.

Plot the counts across: Corporate / Microsoft tenant / Unverified-bad data / Other, split by inboxes on all domains vs inboxes on blacklisted domains.

---

## Part 15b — Soft vs hard bounce: what the codes mean

The categories tell you *where* a bounce belongs. The SMTP code tells you *what the underlying cause is* — read it so you find the root cause instead of just bucketing.

**The one rule to remember:**

- **4XX = soft bounce (temporary).** The server is saying "not now" — mailbox full, server busy, temporary rate limit or policy. Often clears on retry. These map to the "Other" category.
- **5XX = hard bounce (permanent).** The server is saying "no" — the address does not exist, the domain is wrong, or the message is blocked outright. These do not fix themselves; the address should come off the list.

Enhanced codes have the form X.X.X: first digit = outcome (2 success, 4 temporary, 5 permanent), second = category (1 addressing, 2 mailbox, 3 mail system).

| Soft (4XX) | Meaning |
|---|---|
| 4.1.1 | Recipient temporarily unavailable |
| 4.2.2 | Recipient's mailbox full |
| 4.3.2 | System resource issue |
| 4.4.1 | Connection timeout with recipient server |
| 4.7.1 | Temporary rejection due to policy |

| Hard (5XX) | Meaning |
|---|---|
| 5.1.1 | Invalid recipient address (does not exist) |
| 5.2.1 | Recipient mailbox disabled |
| 5.3.0 | Undefined mail system error |
| 5.4.1 | Recipient host not responding / address rejected |
| 5.7.1 | Blocked by policy / relay or security rejection |

**Read the bounce type to find the cause.** A wave of hard `5.1.1` / "does not exist" / "no such user" bounces (the Unverified/Bad Data category) almost always means a **data accuracy problem** — the addresses were not valid when sent. Match the fix to the bounce type:
- **Hard 5XX** → list / verification / data accuracy
- **Soft 4XX** → temporary or infra (retry, sending limits, mailbox state)
- **5.7.1 / policy / blocked** → corporate filtering or reputation, not the address itself

---

## Part 16 — Manual check: is bad data the cause?

1. In EmailBison, find which campaign has a relatively high bounce rate (> 3%).
2. In `ClientName - Bounce Emails`, filter for that campaign by Campaign Name.
3. Check the original Clay table the campaign was pushed from.
4. Note which email provider was used (map it manually in a text column).
5. Read the Text Body to identify the cause; look for a pattern.

## Part 17 — Pull the picture together

Three quick checks before writing the conclusion:
1. Do the campaigns use spintax? If not, why not (it's part of the Launch Checklist)?
2. How many complaints/unsubscribes overall vs on these inboxes/domains?
3. Are any inboxes used elsewhere (e.g. Lemlist)?

Lay out two tables. **Inbox-level:** domain, no. of Google/MS inboxes, warmup ratio, bounce rate, reply rate, blacklisted flag, tags (New Inbox / Active / Warmup needed / Burnt / Total), split by all vs blacklisted domains. **Bounce-level:** sender email, lead email, campaign name, provider, bounce category, full bounce message. Export as CSV/Sheet.

---

## Part 18 — Write up what you found (the deliverable)

This is where the analysis becomes something the team can act on. Before writing, make sure you understand how the system runs (see `email-infra-automation.md` and the EmailBison warmup logic) so your recommendations line up.

1. Use a working doc (a shared doc or wherever your team records analyses) as the record.
2. Post next steps in your team's internal Slack channel (CC the team manager; only loop in leadership if it's genuinely founder-level). Make three things obvious:
   - **Analysis conducted** — link the working doc + the key TL;DR.
   - **Root cause** — is it the email infrastructure, the list, the copy, or a combination? Name it explicitly. This is the GTM Engineer's responsibility to land.
   - **Exposure** — what share of inboxes/domains/leads is affected (e.g. "48% of inboxes on blacklisted domains")? Scale decides urgency and who acts.
3. Conclusion + who to escalate to, based on cause:
   - **Infra / automation** (warmup ratios, Supabase/automation) → your ops/automation team.
   - **Copy** (no liquid syntax, weak variance, spam-trigger wording, aggressive volume) → GTM Engineer rewrites; may be a client conversation if the client supplied/insisted on the copy.
   - **List / data** → verification/enrichment. Escalate in order: resolve → team manager → leadership/sales only if genuinely commercial or founder-level.

### Finding → action reference

| Finding | Action |
|---|---|
| DMARC issue | Set up + update DMARC |
| Warmup vs cold ratio off (not 1.5 Google / 2.5 MS) | Current SOP: Google 1.5, MS 2.5. If off, ping your ops/automation team in your ops Slack channel with a video + your findings |
| Bounce > 3% from provider | Review campaigns for a campaign/audience pattern; review the Clay table; communicate which provider caused it (enrichment vs verification) |
| Cross-platform inbox use | Reduce cold sends for 14 days in the other sequencer; 14 days later check the inbox tag in Bison — if Active/New Inbox, safe to reuse. Or swap to good inboxes if the client needs Lemlist |
| Blacklisted domains | If a large share (e.g. 48%) of inboxes are on blacklisted domains, talk to the client: buy new domains and set up new infrastructure |
| SPF / DKIM / MX issue | Authentication/routing misconfigured. Spot-check SPF, DKIM, DMARC, MX. If mis-provisioned, loop in your infrastructure vendor via your infra Slack channel |
| Copy is the cause | Check liquid syntax (no empty `{{ }}`), spintax variance, spam-trigger words, volume. Rewrite. Client conversation if they supplied/insisted on the copy |
| Bad data / verification (hard 5.x.x) | Confirm which verification was used on the list and whether bad data slipped through (Part 15b). Fix the Clay verification step; communicate which provider caused it |

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
