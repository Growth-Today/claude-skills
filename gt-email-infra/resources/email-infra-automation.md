# Automated Inbox Management System

How GT runs deliverability at scale without manual spreadsheet work. This is the automation layer that sits on top of the manual infrastructure covered in the rest of this skill — it syncs inbox metadata, warmup stats, campaign metrics, and blacklist status, maintains a live deliverability dashboard across 50+ inboxes and multiple workspaces, and runs fully automated on schedules with controlled rate limiting.

The system is the single source of truth for monitoring inbox health, detecting deliverability issues early, and driving data-driven optimization at the inbox, domain, and workspace level.

---

## Architecture

GT's deliverability automation runs as a custom TypeScript application:

| Layer | Tool | Role |
|---|---|---|
| Data / source of truth | Supabase (Postgres) | Every state transition runs inside a Postgres transaction |
| Dashboard + deployment | Railway | The UI and the scheduled worker processes |
| ESP | EmailBison | The sending platform GT runs on |
| Alerting | Slack | your team's deliverability + ops Slack channels |

**Tools used:** Railway (UI), Supabase, EmailBison admin access, Slack (your team's deliverability Slack channel).

---

## The 10 automations

1. **Deliverability Dashboard** — onboard EmailBison workspaces, view every sending inbox grouped by domain, sync on demand.
2. **Scheduled Placement Tests** — weekly EmailGuard inbox-placement tests, 3 inboxes per domain, refreshed every 6 hours.
3. **Sync Deliverability Data** — atomic, audited persistence of every inbox status change.
4. **Inbox Classification Engine** — nightly tagging (Active / Warmup Needed / Burnt / New Inbox / Blacklisted).
5. **Sync Tags Back to EmailBison** — pushes classification changes back into Bison (tags + sending limits).
6. **Campaign Routing Using Tags and ESP** — auto-attaches eligible inboxes to campaigns.
7. **Warmup and Recovery** — handled by the rotation model (see Automation 10).
8. **Blacklist Monitoring** — daily DNS-based blacklist scan, auto-throttle + Slack alert.
9. **Weekly Deliverability Report** — scheduled digests and real-time alerting to Slack.
10. **Inbox Rotation** — Batch A / Batch B, 15-day sending/warmup alternation.

---

## 1. Deliverability Dashboard

The onboarding and monitoring surface. Each row on the Clients page is one workspace's EmailBison workspace.

- **Add client:** paste the EmailBison API key → live validation against Bison → workspace auto-saved under the actual Bison workspace name.
- **Sync client:** force-sync a single workspace.
- **Sender Emails page:** central view of every sending inbox across all clients, grouped by sending domain, with filters (email/domain/name, workspace, status, warmup on/off, ESP, tag, minimum lifetime sent). Live top metrics: total inboxes, connected, not connected, warmup active, domains.
- Each inbox row shows: full email, sender name, workspace, connection status, lifetime sent, reply rate, bounce rate, warmup status + score bar, tags.
- **Sync All Data:** syncs all onboarded workspaces with a live per-client progress popover. Runs on demand from the sidebar, or automatically via a nightly n8n cron job.

---

## 2. Scheduled Placement Tests

Automated EmailGuard inbox-placement testing runs the deliverability checks on a schedule with no manual effort.

- Every week, the system runs EmailGuard placement tests on **3 inboxes per sending domain**, no manual effort.
- For each test it records inbox-vs-spam placement across Google and Microsoft plus an overall deliverability score, **refreshed every 6 hours**.
- Results live in a searchable, filterable "Placement Tests" dashboard (by inbox, domain, status, score).
- Each client can have its own placement-test subject + body; if none exists it uses the default; if no version exists at all it skips sending and alerts in Slack (prevents accidental placeholder sends).

---

## 3. Sync Deliverability Data

The persistence layer that guarantees every inbox status change is recorded consistently and atomically.

Whenever an inbox deliverability status changes, the system performs all related writes in a single atomic transaction: updates the inbox record, creates a status-history entry, records an audit-log event. If any part fails, the whole transaction rolls back — inbox state, history, and audit logs can never drift apart. If no actual status change occurs, all writes are skipped (clean audit trail, no duplicate entries).

Each status transition stores: previous status, new status, bounce rate, reply rate, warmup score, classification timestamp. Access at **Sidebar → Audit Log**; drill into a record with `?recordId=<uuid>`.

---

## 4. Inbox Classification Engine

The core tagging engine. Runs nightly (and on demand) against live EmailBison sending data, using GT's classification formula. This is what removes manual spreadsheet health reviews.

### The five tags

| Tag | Meaning |
|---|---|
| New Inbox | Not enough sending history yet |
| Active | Healthy and safe to send at full volume |
| Warmup Needed | Needs more warmup/monitoring before full use |
| Burnt | Poor deliverability — should not be actively used |
| Blacklisted | Domain is on a blacklist — volume auto-reduced |

### Tagging logic (exact thresholds)

**New Inbox** — total emails sent < 100.

**Burnt** — ALL three of:
- Bounce rate > 3%
- Reply rate < 0.5%
- Warmup score < 95

**Active** — ALL of:
- Inbox placement score > 70/100 (if below 70, forced to Warmup Needed even if everything else looks strong)
- Bounce rate < 2%
- Reply rate ≥ 0.5%
- Warmup score ≥ 97

**Warmup Needed** — anything that does not meet New Inbox, Burnt, or Active.

**Blacklisted** — domain detected on a blacklist (see Automation 8). Sending volume reduced while listed.

Placement guards: an inbox is prevented from being tagged Active below a 70 placement score and forced to Warmup Needed below 50. Demotion behavior: poor placement → Warmup Needed. Classification thresholds live in a single version-controlled config layer, so tuning is a deliberate, reviewable change rather than an undocumented workflow edit.

---

## 5. Sync Tags Back to EmailBison

Whenever classification changes, the system pushes updates back into Bison: updates the inbox tag, adjusts cold sending limits, adjusts warmup limits, and removes inboxes from active campaigns when marked Burnt or Warmup Needed. An hourly reconciliation sweep keeps Bison and the dashboard in sync, with automatic retries, Slack alerts for sync failures, and drift-prevention safeguards.

### Limit changes by state

Bison does not allow a 0 daily limit, so throttled inboxes go to 1.

| Inbox state | Google cold | Google warmup | Outlook cold | Outlook warmup |
|---|---|---|---|---|
| 1–14 days (warmup) | 1 | 25 (reply auto) | 1 | 8 (reply 3) |
| >14 days (sending) | 20 | 30 (reply auto) | 5 | 13 (reply 3) |
| Warmup Needed / Burnt | 1 | 25 | 1 | 8 |

---

## 6. Campaign Routing Using Tags and ESP

Campaigns are created directly from the Railway UI (`/campaigns`), which atomically creates the Bison campaign, writes the internal campaigns row, and bulk-attaches the eligible inbox set. Membership is maintained by a 15-minute reconciliation loop plus instant refresh on any classification change.

**Routing rule:** `google` | `microsoft` | `both` (ESP gate). Optional `sender_name_include` (exact match on inbox name) and `custom_tag_exclude` (substring).

**Inbox eligibility (all required):** same workspace + status Connected + age > 14 days + ESP matches routing rule + classification is Active or New Inbox + passes tag filters. Burnt inboxes are excluded; Warmup Needed inboxes are throttled to cold limit 1 (warmup 25 Google / 8 Outlook) but stay attached.

### ESP-based routing use cases

| Situation | ESP selection | Why |
|---|---|---|
| Lead list ~90% Gmail | Google | IP reputation + domain alignment |
| B2B leads mostly Outlook/Exchange | Microsoft | Better delivery to corporate servers |
| Mixed recipient ESPs | Both | Sender pool scales with ESP distribution |
| Large campaign (50k+ leads) | Both | Higher combined daily send capacity |

Campaign naming examples: `Webvisits - Google` (Google inboxes), `Webvisits - All` (Both, for <500 leads), `Webvisits - Andrew` (rep-specific, Both + `sender_name_include`).

---

## 7. Warmup and Recovery Automation

Warmup and recovery are handled by the rotation model — see Automation 10, which manages warmup and sending phases dynamically per inbox rather than with static age-based limits.

---

## 8. Blacklist Monitoring Automation

Every sending domain is scanned **daily at 04:00 UTC** against three real-time blacklist providers via direct DNS lookups (no paid APIs): **SURBL, Spamhaus DBL, URIBL**.

If a domain is detected on a blacklist:
- Every inbox under that domain is immediately marked Burnt.
- Sending limits reduced to 1 (warmup 25 Google / 8 Outlook).
- A P0 Slack alert fires instantly with the total number of blacklisted domains; a thread lists every affected inbox.

If the domain later clears: a two-step soft recovery begins — inboxes move back to Warmup Needed, then the normal classification engine resumes. In practice blacklist removal is rare; for planning, treat blacklisted domains as permanently unavailable. The automation handles recovery automatically if it does happen.

---

## 9. Weekly Deliverability Report

All reporting and alerting centralized through one monitoring service.

**Scheduled:** daily bounce digest (Mon–Fri 08:00 Europe/Berlin), weekly inbox health report (Friday 17:00 New York), sent to your team's deliverability Slack channel.

**Real-time alerts:** cascade burn detection (3+ inboxes Burnt within 24h), placement-score drops ≥ 30 points, persistent worker/automation failures. Every alert emission is logged to the database regardless of whether Slack accepts it.

The weekly report covers: inbox counts by tag, ESP performance breakdown (Google vs Microsoft — total, avg bounce, avg reply, avg placement), placement trend analysis (healthy ≥ 70 vs weak < 70, % in the watch zone), and a risk summary (low-reply actives, high-bounce inboxes, blacklisted domains).

---

## 10. Inbox Rotation

Inboxes are split into **Batch A** and **Batch B**, alternating every **15 days** between a full sending phase and a high-intensity warmup phase. When one batch sends, the other recovers. All rotation runs from a centralized `/rotation` dashboard.

**Logic per workspace:** Google and Microsoft inboxes each split evenly into A and B; both batches stay attached to campaigns. At period start Batch A = sending, Batch B = warmup; over the period the limits gradually swap, and at the end they are fully reversed.

Example (Google): Batch A starts at daily send 20 / warmup 5; Batch B at daily send 5 / warmup 20; over the period they cross over. Additional functionality: automatic graduation of new inboxes into rotation, ESP-balanced distribution, dynamic per-inbox limit recalculation, per-workspace settings, manual include/exclude, full audit logging. The batch-assignment automation runs every 4 hours so new inboxes join without manual work.

---

## SOP for the team

### Sales Ops — onboard a client workspace

1. In EmailBison, create an API key for the workspace, name it `Client Automated Inbox System`.
2. Save the API key in your team's password manager.
3. On the Railway Clients page, click **Add Client**, paste the key, **Save Client**.

Inbox data syncs immediately when the workspace is created in Bison and added to Railway. A full "Sync All" across all onboarded workspaces takes ~8 minutes for ~18 workspaces / 5,000+ inboxes.

### GTM Engineers — new campaign

1. Always create campaigns from the Railway UI (`/campaigns`) — never Bison directly — so the system gets routing-rule management, dashboard visibility, audit history, and campaign-membership visibility.
2. Set the routing rule (Google / Microsoft / Both).
3. Optionally set `custom_tag_exclude` and `sender_name_include`.
4. Let the automation handle attach/detach. Sync Tags Back to Bison throttles bad inboxes to limit 1 and keeps them attached; Campaign Routing reconciles membership every 15 minutes and on every classification change.

For an existing campaign where you want to add newly purchased inboxes: pause it → add sender emails → filter for the ESP and tag DOES NOT CONTAIN "Burnt"/"Warmup Needed" → review sending limits → resume.

### Global limits and the warmup SOP

Clients Page → Global Limits. Warmup period default 14 days. Per ESP:

**Google** (warm-to-cold ratio 1.5:1):

| | Cold sends | Warmup sends |
|---|---|---|
| First 14 days | 1 | 25 |
| After warmup | 20 | 30 |

**Microsoft** (stricter, 2.5:1):

| | Cold sends | Warmup sends |
|---|---|---|
| First 14 days | 1 | 8 |
| After warmup | 5 | 12.5 |

Limits auto-adjust on the 15th day (07:00 UTC). Click "Save to All Workspaces" to push new values on the next daily sync, or update a single workspace via Rotation Page → Select Workspace → Settings.

---

## FAQ highlights

- **Force reclassification on demand:** per inbox (Sender Emails → Inbox → Reclassify), per client (Clients → Select client → Reclassify), or all clients (Clients section — also runs automatically daily at 2 AM).
- **Syncing a newly added client:** adding a client just inserts the row and seeds rotation settings — no automatic sync. Either click "Sync All" in the sidebar, or wait for the nightly n8n cron. When sync runs it pulls all historical inbox data (full sender-email list + warmup rows + 90 days of stats).
- **How long a full "Sync All" takes:** ~8 minutes for ~18 workspaces / 5,000+ inboxes. Sync is not transactional at the job level — phases (inboxes → tags → stats) commit independently, but the UI reads from the DB so pages always show a self-consistent snapshot.
- **If a sync partially fails:** it re-queues automatically with exponential backoff (5min × 2^(attempts-1), max 3 attempts). Per-inbox reconcile failures are retried by an hourly safety-net sweep.
- **Pre-warmed inboxes:** mark them Excluded in the Sender Emails UI (bulk-select by email or domain).
- **"Floored at 20 sends":** a sample-size filter on the Bounces page — inboxes with < 20 sent are hidden so a 1-in-5 bounce doesn't show as a misleading 20% rate. Not a sending limit.
- **Warmup Needed with no timeout:** no escalation exists; an inbox can sit in Warmup Needed indefinitely. Burnt requires all three thresholds (bounce > 3%, reply < 0.5%, warmup < 95) concurrently.
- **"Upstream error" in the UI:** the background stats job and the dashboard share a database connection pool; under load the job can starve the UI's connections. Redeploying restores it; the longer-term fix is splitting the UI and cron jobs into separate services.
- **Worker/automation failures:** a worker failure means the ESP's API rejected a request even after retries (a tag no longer exists, a campaign was archived, or the ESP rate-limited). Rare in healthy weeks; a cluster is usually an ESP hiccup. Escalate infra issues to your ops/automation team.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
