# Email Infrastructure, Reference

Single source of truth for every number, limit, timeline, threshold, and taxonomy used across this skill. All sub-skills point here, never restate a number in a sub-skill; link to this file. If a value changes, change it here once.

> **Platform note.** This skill supports multiple sequencers, **EmailBison, Instantly, Smartlead, and Lemlist** (use the matching setup sub-skill for each). The *targets* below (warmup length, ratios, healthy thresholds) are platform-independent and carry over; platform-specific limits are flagged (e.g. EmailBison's minimum cold limit = 1, not 0). The classification/limit logic is what the automated inbox-management system enforces.

---

## 1. Send limits per provider (per mailbox / day)

**Govern by the warm-to-cold ratio, not by a fixed warmup number.** Set the cold limit for the inbox state, then size warmup from the ratio. This keeps the setup correct across platforms, and note that **Instantly and Smartlead offer auto-warmup**, where warmup volume is managed for you rather than set as an absolute number.

**Warm-to-cold ratio target:**
- Google **1.5 : 1**
- Microsoft / Outlook **3 : 1** (deliberately stricter)

**Limits by inbox state** (the standard Growth Today values these sub-skills all derive from):

| Inbox state | Google cold | Google warmup | Outlook cold | Outlook warmup |
|---|---|---|---|---|
| First 21 days (warming) | 0–1 * | 25 | 0–1 * | 8 |
| After warmup (sending) | 20 | 30 | 5 | 15 |
| Warmup Needed / Burnt (throttled) | 0–1 * | 25 | 0–1 * | 8 |

\* During warming and when throttled, cold is effectively off. Instantly/Smartlead can set **0**; **EmailBison's minimum is 1** (it cannot do 0), the failover gap below.

**Warmup is governed by the warm-to-cold ratio, not a fixed constant.** The sending-row numbers above are the worked example: Google 20 × 1.5 = **30**; Outlook 5 × 3 = **15**. Change the cold limit and the warmup target moves with it; on auto-warmup platforms (Instantly/Smartlead) the tool sets warmup for you. During warming the ramp is Google **+4/day**, Outlook **+2/day** (see the instantly-setup sub-skill).

- **Failover gap (EmailBison):** cold can't be set to 0, so an unhealthy inbox is throttled to 1 rather than silenced, and a lead being prospected by that inbox keeps getting sent from it; Bison won't hand the lead to another healthy inbox on the campaign. Instantly and Smartlead *can* set 0 and reroute the lead to a healthy inbox on the campaign.
- Limits auto-adjust on day 22 (after the 21-day warmup floor).

> **Do not** copy the old "Google 30/day, Microsoft 10/day safe limit" figure, it conflated cold+warmup and the Microsoft cold number was wrong. Govern by the ratio above.
>
> **Where the Google number comes from.** **20/day is Growth Today's own figure.** ScaledMail
> quotes **25/day** for a Google mailbox. We deliberately run the lower one — it's the more
> conservative of the two and it's what every Google inbox in our workspace is actually set to.
> If someone cites 25, that's the vendor's number, not ours.

### §1 keys (referenced by executable tables)

Executable check rows cite these keys instead of repeating the number. **If a value changes, change it here and every check follows.** Never restate one of these figures inside a sub-skill.

| Key | Value | Meaning |
|---|---|---|
| `google_cold` | 20 | Google cold sends/day, inbox fully warmed and Active |
| `google_warmup` | 30 | Google warmup/day at the same state |
| `outlook_cold` | 5 | Outlook cold sends/day, fully warmed and Active |
| `outlook_warmup` | 15 | Outlook warmup/day at the same state |
| `cold_warming` | 0–1 | Cold limit during the first 21 days, and when throttled (Instantly/Smartlead 0; EmailBison floor 1) |
| `cold_new_inbox` | 1 | Cold limit for a New Inbox, both providers |
| `ratio_google` | 1.5 | Warm-to-cold ratio, Google |
| `ratio_outlook` | 3 | Warm-to-cold ratio, Microsoft/Outlook |
| `ramp_google` | +4/day | Warmup increment during warming |
| `ramp_outlook` | +2/day | Warmup increment during warming |
| `blended_per_mailbox` | *computed* | `google_share × google_cold + microsoft_share × outlook_cold`. **Not a constant** — the provider mix is a per-client decision, so this is calculated per client. See §4 |

---

## 2. Inbox classification (state definitions)

Exact thresholds the classification engine uses. These are also the thresholds a human/agent reads a dashboard against.

| State | Rule |
|---|---|
| **New Inbox** | Total emails ever sent **< 100**. (Campaign routing also excludes any inbox **< 14 days** old by creation date.) **Cold send limit = 1/day** for both Google and Outlook. |
| **Active** | Placement **> 70/100** AND bounce **< 2%** AND reply **≥ 0.5%** AND warmup score **≥ 97**. |
| **Burnt** | Bounce **> 3%** AND reply **< 0.5%** AND warmup score **< 95** (all three). |
| **Warmup Needed** | Anything that is not New / Active / Burnt. |
| **Blacklisted** | Domain listed on a blacklist that counts (Spamhaus DBL / URIBL). Volume auto-reduced. **See the warning below — this has not been working.** |

**Placement overrides:** placement **< 70** forces Warmup Needed even if everything else is strong; placement **< 50** hard-forces Warmup Needed. When placement recovers, the inbox returns to Active automatically.

### §2 keys (referenced by executable tables)

| Key | Value | Meaning |
|---|---|---|
| `new_inbox_sends` | < 100 | Lifetime sends below which an inbox is New |
| `new_inbox_age_days` | 14 | Campaign-routing exclusion age in the email infra management system. **Not** the GT warmup floor — that is `warmup_floor_days` in §5 |
| `warmup_floor_days` | 21 | GT's hard warmup floor before any cold send (§5) |
| `placement_active` | > 70 | Placement score required for Active |
| `placement_forced_warmup` | < 50 | Hard-forces Warmup Needed |
| `bounce_active` | < 2% | Bounce ceiling for Active |
| `bounce_burnt` | > 3% | Bounce floor for Burnt (all three Burnt conditions must hold) |
| `reply_active` | ≥ 0.5% | Reply floor for Active. ⏸️ **Under review (Aug 2026):** this one threshold can tag an otherwise-healthy inbox as Warmup Needed, which then stops it attaching to campaigns. A proposal to drop it from the Warmup Needed definition is open. Check before quoting |
| `warmup_score_active` | ≥ 97 | Warmup score for Active |
| `warmup_score_burnt` | < 95 | Warmup score for Burnt |
| `blacklists_that_count` | Spamhaus DBL, URIBL | The only two. No other list is a blacklist reason |

**No timeout:** an inbox can sit in Warmup Needed indefinitely, there is no auto-escalation to Burnt. Burnt requires all three thresholds concurrently.

> **⚠️ The 14-day exclusion and the 21-day warmup floor are two different things.**
> The email infra management system's campaign routing releases a New Inbox at **14 days** old. Growth Today's warmup floor
> is **21 days** (§5). So an inbox can become *eligible* in the system a week before GT policy
> says it should send. **Do not attach an inbox to a campaign just because the system allows it** —
> check warmup age against §5 first. The 14-day rule lives in the email infra management system; raise it with the team that maintains it if we
> want the two aligned.

> **⚠️ Blacklisted has never actually worked as written.** The email infra management system review confirmed that Spamhaus and
> URIBL were both silently failing in the app — URIBL was blocking them, and Spamhaus returned
> "clean" for every domain, so every Blacklisted tag GT has ever seen came from a list we no
> longer track. **Only Spamhaus DBL and URIBL count as a blacklist reason.** The agreed fix turns
> both on (they are free — GT supplies a free Spamhaus DQS key, registered as *Individual*, not
> *Organisation*) and adds a self-test so a list going quiet is caught automatically.
> Until that ships, a Blacklisted tag is **not evidence of a real listing** — verify at source
> (Spamhaus DBL / URIBL) before acting on it.

---

## 3. Healthy / warning / stop metrics

| Metric | Healthy | Warning | Stop / act |
|---|---|---|---|
| Bounce rate (after OOO stripping, see §7) | < 2% | 2–3% | > 3% (hard action at > 5%) |
| Reply rate (human) | ≥ 0.5% classification floor |, | Below ~1% total often means **bouncing**, not low interest |
| Placement score | ≥ 70 | 50–70 (watch zone) | < 50 (forced warmup) |
| Warmup score | ≥ 97 (Active) | 95–97 | < 95 |
| Spam / unsub | ~0% | any | multiple |

- **Open rate is not tracked.** Open tracking is turned OFF by policy (tracking pixels hurt placement and trip SEGs), so do not use open rate as a health metric.
- **~1% reply from out-of-office alone is the floor.** If total reply is below that, suspect bounces before low interest, check the bounce/auto-reply folder.

---

## 4. Infrastructure sizing

Work backwards: **monthly goal → daily volume → mailboxes → domains.**

1. Monthly email goal ÷ **20 working days** = daily volume.
2. **Ask the client's Google / Microsoft mix**, then compute the blended cold capacity:
   `blended = google_share × 20 + microsoft_share × 5` (§1 keys `google_cold`, `outlook_cold`).
3. Daily volume ÷ blended = mailboxes needed.
4. Round that up to a whole mailbox, then **× 1.5** (buffer for rotation, warmup, issues) and
   round up again = mailboxes to buy. The Google/Microsoft split comes **out of** that total,
   so the two provider counts always add back up to it.
5. Domains: **Google mailboxes ÷ 2–3** + **Microsoft mailboxes ÷ ~25**.

> ### 🔑 There is no single divisor. Step 2 is an input, not an assumption.
>
> The provider mix is a **per-client decision** driven by the client's industry and market —
> some need more Microsoft, some more Google. That means the emails-per-mailbox figure changes
> per client and **any fixed number in this file would be wrong for most of them.**
>
> A Google mailbox sends **20** cold/day. A Microsoft mailbox sends **5** — a quarter as much.
> So the mix drives the answer more than the goal does:

| Google share | Blended cold / mailbox / day | 15,000/mo → mailboxes to buy |
|---|---|---|
| 100% Google | **20.0** | 57 |
| 75 / 25 | 16.25 | 71 |
| 60 / 40 | 14.0 | 81 |
| 50 / 50 | 12.5 | 90 |
| 25 / 75 | 8.75 | 129 |

> **Same client, same goal, 57 to 129 mailboxes.** That spread is why you ask for the mix before
> you size anything. If someone hands you a single number without stating the split, the number
> is meaningless.
>
> **Don't compute this by hand.** The calculator takes the split as a flag and reads the limits
> from §1, so it can't drift from the standard:
>
> ```bash
> uv run playbooks/sizing-calculator/scripts/execute.py --monthly-goal 15000 --split-google 0.5
> ```

### Worked example at a 60/40 split

Shown because it's a common starting point for a mixed build, **not** because it's the default.
Substitute the client's real mix.

| Monthly goal | Daily volume | Mailboxes needed | **Mailboxes to buy (×1.5)** | Google / Microsoft | Domains |
|---|---|---|---|---|---|
| 3,000 | 150 | 11 | **17** | 10 / 7 | 5 |
| 7,500 | 375 | 27 | **41** | 25 / 16 | 11 |
| 15,000 | 750 | 54 | **81** | 49 / 32 | 22 |
| 30,000 | 1,500 | 108 | **162** | 97 / 65 | 42 |

The buffer applies to **every** row. (The previous version of this table applied it to the first
row only, which is why the larger tiers looked cheap.) `--validate` reads both tables straight
out of this file, so if you edit a number here and the model disagrees, the check fails.

**Mailboxes per domain (average): Google 2–3, Microsoft up to ~25.** Google stays lean for
deliverability; Microsoft can host many mailboxes per domain. Domain count is therefore driven
almost entirely by the Google side. Verify the per-provider density on scale-ups.

### Days to Clear (how fast the campaign must finish)

The table above assumes a 20-working-day month. Campaigns that must clear faster need
proportionally more daily capacity — a list run in 5 days needs **4× the daily volume** of the
same list run over 20.

| Days to clear | Campaign type | Why |
|---|---|---|
| **1** | Website visitor · app install · churn | Act the same day or the signal is dead |
| **5** | Hiring signals | Roles close quickly, prospect inside a week |
| **20** | One-off campaigns | Standard month; initial tests |
| **45** | Evergreen / high volume | Long-running, balanced against other campaigns |

**Formula when a campaign has a deadline:** `daily volume = contacts × sequence steps ÷ days to clear`,
then continue from step 2 above.

**Campaign types:**
- **Evergreen** — auto-populates a set number of accounts/contacts to prospect daily or weekly, runs on autopilot. *Example: contacts at companies that installed HubSpot last week.*
- **One-off** — built once for a specific list. *Example: members of the Pavilion Slack community.*

---

## 5. Warmup, domain age & ramp

| Item | Value |
|---|---|
| Minimum warmup before sending | **21 days / 3 weeks** (hard floor) |
| Recommended warmup | **3–4 weeks** (21 days is the floor; go to 4 weeks on a cautious build) |
| Age-before-link gate | Link/campaign only from domains **> 30 days old AND past warmup** |
| Never | Disable warmup once campaigns are running |

**Aged domains are a GTM-owner decision, not the default.** Pre-aged domains come from specialized, pricier providers and usually carry generic (off-brand) names, so by default we age our own through the **> 30-day + warmup gate** before linking. The GTM / account owner may choose to buy aged domains as a deliberate trade-off (faster reputation vs. higher cost and off-brand naming).

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
| DMARC | Policy for SPF/DKIM failures | **`p=reject` is the GT standard.** `p=none` only as a short verification phase at first setup |

**Redirect vs masking:** a secondary domain must reach a real destination via **masking or a genuine landing page, never a bare 301/302 redirect** to the main site — many domains resolving to one site is the exact bulk-sender fingerprint. **Current state (Aug 2026): GT runs no client redirects**, so this is a standard to hold, not an open defect. The live question is what replaces EmailBison's masking once we are fully on Instantly — see `approved-vendors.md`. See the provisioning sub-skill.

**Silent DNS drift** is the real risk, not initial setup, records can be quietly broken by a provider later. Re-check MX/SPF/DKIM/DMARC on a schedule.

---

## 7. Bounce codes (soft vs hard) + the OOO rule

**Read the SMTP code to find the root cause, do not treat every bounce the same.** Codes have the form X.X.X: first digit = outcome (4 temporary, 5 permanent), second = category (1 addressing, 2 mailbox, 3 mail system).

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

> **⚠️ Strip auto-replies BEFORE reading any bounce rate.** EmailBison miscounts out-of-office and auto-replies as bounces, this inflated one real audit by **~54%** (raw 2,687 "bounces" → 1,231 real). Reclassify OOO/auto-reply out of the bounce bucket first, or every bounce number you read is wrong. See the bounce-audit sub-skill.

---

## 8. ESP & SEG taxonomy

**Recipient ESP** (who receives): **Google** (Gmail/Workspace), **Microsoft/Outlook** (Exchange Online), **Enterprise/SEG**, **Other** (Zoho, custom mail servers).

**SEG (Secure Email Gateway)**: a filtering layer a company puts *in front of* Google/Microsoft: **Mimecast, Proofpoint, Barracuda**. A SEG block is the recipient's security policy working as designed, **not a defect on our side**. SEG leads get isolated onto dedicated domains (the campaign-building sub-skill).

**ESP matching is dead as a fixed rule.** Sending from the same provider the recipient uses was a 2024 tactic. Do **not** hard-code it. Decide keep/drop per segment from our own Lead-ESP × sending-vendor reply data on the dashboard (the dashboard-reading sub-skill).

---

## 9. Domain sourcing quick-reference (detail in the domain-research sub-skill)

- **Naming:** keep the brand word; **drop prefixes** (`go/get/try/meet`); no hyphens, no numbers; `.com` first.
- **Avoid** cheap TLDs `.top / .xyz / .cc` and the most-abused registrar/date bulk-buy pattern.
- **Buy** across multiple registrars, spread across **multiple days**, **max 4 domains per registrar per day**; spread DNS across multiple Cloudflare accounts. **ScaledMail owns purchasing, spread and timing, and is already spreading across registrars and dates** — GT's job is spot-check verification on delivery, not chasing a gap.
  - Batch size sets the calendar, not the other way round. At 4/registrar/day a 50-domain batch cannot be finished in one day, and a 150-domain batch certainly cannot.
- **Most-abused registrars** (use, but never bulk on one): GNAME, Dynadot, NameSilo, Namecheap. Abuse concentrates there because they are popular and cheap, not because they are defective.
- **Links:** no custom tracking domain and no links in cold email by default; share via LinkedIn or an unlinked URL.

*Source basis: Spamhaus/Mashood-Nabeel malicious-domains study (Jun 2026), median flagged attacker domain age 60 days; 77.9% sit in a single registrar+date bulk batch; most-abused registrars and `.top/.xyz/.cc` TLDs.*

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
