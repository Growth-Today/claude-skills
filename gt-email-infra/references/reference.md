# Email Infrastructure — Reference

Single source of truth for every number, limit, timeline, threshold, and taxonomy used across this skill. All playbooks point here — never restate a number in a playbook; link to this file. If a value changes, change it here once.

> **Platform note.** Growth Today runs cold sending on **EmailBison today** and is **migrating to Instantly** (Smartlead is the third option we benchmark against). The classification/limit logic below is what our automated inbox-management system enforces today on Bison; the *targets* (warmup length, ratios, healthy thresholds) are platform-independent and carry over. Where a limit is platform-specific (e.g. EmailBison's minimum cold limit = 1, not 0), it is flagged.

---

## 1. Send limits per provider (per mailbox / day)

**Govern by the warm-to-cold ratio, not by a fixed warmup number.** Set the cold limit for the inbox state, then size warmup from the ratio. This keeps the setup correct across platforms — and note that **Instantly and Smartlead offer auto-warmup**, where warmup volume is managed for you rather than set as an absolute number.

**Warm-to-cold ratio target:**
- Google **1.5 : 1**
- Microsoft / Outlook **2.5 : 1** (deliberately stricter)

**Cold limit by inbox state:**

| Inbox state | Google cold | Outlook cold |
|---|---|---|
| First 14 days (warming) | 0–1 * | 0–1 * |
| After warmup (sending) | 20 | 5 |
| Warmup Needed / Burnt (throttled) | 0–1 * | 0–1 * |

\* During warming and when throttled, cold is effectively off. Instantly/Smartlead can set **0**; **EmailBison's minimum is 1** (it cannot do 0) — the failover gap below.

**Warmup = cold × ratio** (worked example for a healthy sending inbox): Google 20 × 1.5 = **~30**; Outlook 5 × 2.5 = **~13**. Treat these as *derived* targets, not fixed constants — change the cold limit and the warmup target moves with it; on auto-warmup platforms (Instantly/Smartlead) the tool sets it.

- **Failover gap (EmailBison):** cold can't be set to 0, so an unhealthy inbox is throttled to 1 rather than silenced — and a lead being prospected by that inbox keeps getting sent from it; Bison won't hand the lead to another healthy inbox on the campaign. Instantly *can*, which is the main reason for the migration.
- Limits auto-adjust on day 15 (after the 14-day warmup floor).

> **Do not** copy the old "Google 30/day, Microsoft 10/day safe limit" figure — it conflated cold+warmup and the Microsoft cold number was wrong. Govern by the ratio above.

---

## 2. Inbox classification (state definitions)

Exact thresholds the classification engine uses. These are also the thresholds a human/agent reads a dashboard against.

| State | Rule |
|---|---|
| **New Inbox** | Total emails ever sent **< 100**. (Campaign routing also excludes any inbox **< 14 days** old by creation date.) |
| **Active** | Placement **> 70/100** AND bounce **< 2%** AND reply **≥ 0.5%** AND warmup score **≥ 97**. |
| **Burnt** | Bounce **> 3%** AND reply **< 0.5%** AND warmup score **< 95** (all three). |
| **Warmup Needed** | Anything that is not New / Active / Burnt. |
| **Blacklisted** | Domain listed on a blacklist that counts (Spamhaus DBL / URIBL). Volume auto-reduced. |

**Placement overrides:** placement **< 70** forces Warmup Needed even if everything else is strong; placement **< 50** hard-forces Warmup Needed. When placement recovers, the inbox returns to Active automatically.

**No timeout:** an inbox can sit in Warmup Needed indefinitely — there is no auto-escalation to Burnt. Burnt requires all three thresholds concurrently.

---

## 3. Healthy / warning / stop metrics

| Metric | Healthy | Warning | Stop / act |
|---|---|---|---|
| Bounce rate (after OOO stripping — see §7) | < 2% | 2–3% | > 3% (hard action at > 5%) |
| Reply rate (human) | ≥ 0.5% classification floor | — | Below ~1% total often means **bouncing**, not low interest |
| Placement score | ≥ 70 | 50–70 (watch zone) | < 50 (forced warmup) |
| Warmup score | ≥ 97 (Active) | 95–97 | < 95 |
| Spam / unsub | ~0% | any | multiple |

- **Open rate is not tracked.** Open tracking is turned OFF by policy (tracking pixels hurt placement and trip SEGs), so do not use open rate as a health metric.
- **~1% reply from out-of-office alone is the floor.** If total reply is below that, suspect bounces before low interest — check the bounce/auto-reply folder.

---

## 4. Infrastructure sizing

Work backwards: **monthly goal → daily volume → mailboxes → domains.**

1. Monthly email goal ÷ **20 working days** = daily volume.
2. Daily volume ÷ **20 (conservative) or 25 (aggressive)** per mailbox = mailboxes.
3. Mailboxes **× 1.5** (buffer for rotation, warmup, issues) = mailboxes with buffer.
4. Mailboxes with buffer ÷ **2** (max 2 mailboxes per domain) = domains.
5. Provider split: **60% Google Workspace, 40% Microsoft 365.**

| Monthly goal | Daily volume | Mailboxes (w/ buffer) | Domains |
|---|---|---|---|
| 3,000 | 150 | 10–12 | 5–6 |
| 7,500 | 375 | 18–23 | 9–12 |
| 15,000 | 750 | 38–45 | 19–23 |
| 30,000 | 1,500 | 75–90 | 38–45 |

**Max 2 mailboxes per domain** (hard rule). Verify this did not drift above 2 during scale-ups.

---

## 5. Warmup, domain age & ramp

| Item | Value |
|---|---|
| Minimum warmup before sending | **14 days / 2 weeks** (hard floor) |
| Recommended warmup | **3–4 weeks** |
| Age-before-link gate | Link/campaign only from domains **> 30 days old AND past warmup** |
| Never | Disable warmup once campaigns are running |

**Aged domains are a GTM-owner decision, not the default.** Pre-aged domains come from specialized, pricier providers and usually carry generic (off-brand) names — so by default we age our own through the **> 30-day + warmup gate** before linking. The GTM / account owner may choose to buy aged domains as a deliberate trade-off (faster reputation vs. higher cost and off-brand naming).

Going-live ramp (per mailbox/day, first weeks of live sending):

| Week | Google | Microsoft |
|---|---|---|
| 1 | 10–15 | 5 |
| 2–3 | 15–20 | 5 |
| 4+ | 20 | 5 |

Scaling rules: increase volume **≤ 20%/week**; stagger new-domain launches (**1 batch/week** cadence); never add volume *and* change copy at once.

---

## 6. DNS records required (all 4)

| Record | Purpose | Notes |
|---|---|---|
| MX | Routes incoming mail to the provider | Set at provisioning |
| SPF | Which servers may send for the domain | **Only ONE** SPF TXT record per domain; keep total DNS lookups ≤ 10 |
| DKIM | Signature proving authenticity | Copy the exact key, no stray spaces |
| DMARC | Policy for SPF/DKIM failures | Start `p=none` (monitor), tighten later |

**Redirect vs masking:** a secondary domain must reach a real destination via **masking or a genuine landing page — never a bare 301/302 redirect** to the main site. Blocklists (SURBL) follow redirects, and many domains → one site is the exact spam fingerprint. See playbook 02.

**Silent DNS drift** is the real risk, not initial setup — records can be quietly broken by a provider later. Re-check MX/SPF/DKIM/DMARC on a schedule.

---

## 7. Bounce codes (soft vs hard) + the OOO rule

**Read the SMTP code to find the root cause — do not treat every bounce the same.** Codes have the form X.X.X: first digit = outcome (4 temporary, 5 permanent), second = category (1 addressing, 2 mailbox, 3 mail system).

| Soft (4XX = temporary, often clears on retry) | Meaning |
|---|---|
| 4.1.1 | Recipient temporarily unavailable |
| 4.2.2 | Mailbox full |
| 4.4.1 | Connection timeout |
| 4.7.1 | Temporary policy rejection |

| Hard (5XX = permanent, take the address off the list) | Meaning |
|---|---|
| 5.1.1 | Invalid recipient (does not exist) |
| 5.2.1 | Mailbox disabled |
| 5.4.1 | Host not responding / address rejected |
| 5.7.1 | Blocked by policy / security rejection |

Root cause by type: **hard 5XX → list/verification/data**; **soft 4XX → temporary/infra**; **5.7.1 → corporate filtering/SEG/reputation** (not the address).

> **⚠️ Strip auto-replies BEFORE reading any bounce rate.** EmailBison miscounts out-of-office and auto-replies as bounces — this inflated one real audit by **~54%** (raw 2,687 "bounces" → 1,231 real). Reclassify OOO/auto-reply out of the bounce bucket first, or every bounce number you read is wrong. See playbook 06.

---

## 8. ESP & SEG taxonomy

**Recipient ESP** (who receives): **Google** (Gmail/Workspace), **Microsoft/Outlook** (Exchange Online), **Enterprise/SEG**, **Other** (Zoho, custom mail servers).

**SEG (Secure Email Gateway)** — a filtering layer a company puts *in front of* Google/Microsoft: **Mimecast, Proofpoint, Barracuda**. A SEG block is the recipient's security policy working as designed, **not a defect on our side**. SEG leads get isolated onto dedicated domains (playbook 04).

**ESP matching is dead as a fixed rule.** Sending from the same provider the recipient uses was a 2024 tactic. Do **not** hard-code it. Decide keep/drop per segment from our own Lead-ESP × sending-vendor reply data on the dashboard (playbook 05).

---

## 9. Domain sourcing quick-reference (detail in playbook 01)

- **Naming:** keep the brand word; **drop prefixes** (`go/get/try/meet`); no hyphens, no numbers; `.com` first.
- **Avoid** cheap TLDs `.top / .xyz / .cc` and the most-abused registrar/date bulk-buy pattern.
- **Buy** across multiple registrars, spread over ~24h at 2–3h intervals, **< 5 per registrar per day**; spread DNS across multiple Cloudflare accounts (ScaledMail does this).
- **Links:** no custom tracking domain and no links in cold email by default; share via LinkedIn or an unlinked URL.

*Source basis: Spamhaus/Mashood-Nabeel malicious-domains study (Jun 2026) — median flagged attacker domain age 60 days; 77.9% sit in a single registrar+date bulk batch; most-abused registrars and `.top/.xyz/.cc` TLDs.*

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
