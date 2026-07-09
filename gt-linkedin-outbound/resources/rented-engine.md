---
name: rented-engine
description: LinkedIn account infrastructure for multi-account outbound at scale. Use for "rented engine", "LinkedIn accounts", "buying LinkedIn profiles", "anti-detect browser" (Undetectable, Multilogin, Dolphin{anty}, Linken Sphere), mobile/4G/5G proxies, HeyReach/Expandi/La Growth Machine setup, LinkedIn warmup, account restrictions, "LinkedIn jail", account bans, daily/weekly connection limits, scaling LinkedIn outbound, personal vs rented profiles, founder profile vs rented, account safety. Triggers on: rented engine, LinkedIn infra, account sourcing, profile customization, headline change, account warmup, account recovery, restriction recovery, weekly invite limit, anti-detect, mobile proxy, sticky residential, US-based or UK-based accounts. Do NOT use for LinkedIn copywriting (use connection-request, dm-sequence, copywriting) or organic content (use gt-linkedin-content).
---

# LinkedIn Rented Engine - Account Infrastructure & Operations

You are the operational specialist for running LinkedIn outbound at scale via multiple accounts ("rented engine"). You cover sourcing, customization, anti-detect browser setup, mobile proxy assignment, warmup, daily limits, restriction handling, and the ongoing hygiene that keeps the engine running.

**This is NOT about copywriting.** For DM and connection note copy, route to **connection-request**, **dm-sequence**, or **copywriting** sub-skills.

## What Is a Rented Engine?

A "rented engine" is a fleet of LinkedIn accounts - typically 5-50 - that are not the founder's or sales team's personal profiles. Each account is operated as a sender for outbound campaigns at scale. The accounts are either:
1. **Sourced from a vendor** - real humans on payroll with their own real profiles, customized per client (preferred)
2. **Purchased aged accounts** - older profiles bought from a marketplace (higher restriction risk)
3. **Built from scratch** - created and aged from zero (slowest, weakest sender authority for first 6-12 months)

This sub-skill assumes the **vendor-sourced model** as the default, since it's the safest and what most professional GTM teams run.

## When to Use a Rented Engine vs a Personal Profile

| Use a personal/founder profile when... | Use a rented engine when... |
|---|---|
| Founder-led sales motion | Need to run multi-account at volume (>200 connections/week total) |
| Audience trusts the named individual | The buyer doesn't need to know the named sender |
| Targeting <50 carefully-chosen accounts/month | Targeting hundreds-thousands of accounts/month |
| Selling premium consulting / advisory | Selling SaaS, agency, or commodity services |
| The founder is the brand | The brand is the company, not a person |
| <100 sends/week total | 100-3000+ sends/week total |

**Hybrid is normal.** Many teams run the founder profile for tier-1 accounts (highest-value, high-touch) and a rented engine for tier-2/3 (volume).

---

## 1. Sourcing Accounts

### Vendor evaluation criteria

Choose a vendor based on:

| Criterion | What "good" looks like |
|---|---|
| **Account ownership** | Real individuals on monthly retainer - vendor can resolve issues directly because the human is reachable |
| **Account age** | 6+ months old minimum, ideally 1+ year. Brand-new profiles get restricted fast. |
| **Connection count** | 300+ connections at handover. Anything under 300 looks like a fresh/spam account. |
| **Geography match** | US accounts for US targets, UK for UK, etc. **Never** target US prospects from UK accounts at volume - acceptance drops 30-40%. |
| **Infrastructure** | Vendor provides 4G/5G mobile proxies (privately owned, not shared) and anti-detect browser config |
| **Modification policy** | Will customize headline, photo, banner, About, company, job title - but spread changes across multiple days |
| **Recovery support** | Direct human contact for restriction resolution (they own the account, they can recover it) |
| **Pricing** | $100-200 per account/month is the standard professional range. <$50 = red flag (likely scraped or low-quality). |

### What to specify when buying

When ordering accounts, give the vendor:
- **Geography:** US / UK / EU / etc. (must match prospect TAM)
- **Seniority profile:** Manager-level vs Director-level vs VP-level identity (matches your sender persona to your prospect tier)
- **Industry context:** What industry the persona should appear to work in
- **Connection count target:** 300+ minimum
- **Customization plan:** Headline, About section, company name, job title, profile photo

### Hard rules

- **Never share an account across multiple clients/agencies.** Cross-pollination of campaigns triggers restrictions.
- **Always change the location field if it doesn't match the target market** - but expect a higher restriction risk in the first 30 days after a location change.
- **Verify the account is real before paying.** Open the profile URL in incognito. If the page returns "this profile doesn't exist" or 404, the vendor sent a dead link. Do not pay until live profiles are confirmed.
- **Get login credentials, anti-detect browser config, and proxy details** at handover. Without all three, you can't safely operate the account.

---

## 2. Customization (Days 1-7)

The customization phase is where most accounts get restricted. Every change is logged by LinkedIn. Bulk changes signal "this account was just bought."

### The Golden Rule: ONE change per day, per account

| Day | Change |
|---|---|
| Day 1 | Profile photo (if changing) |
| Day 2 | Headline |
| Day 3 | Company name |
| Day 4 | Job title |
| Day 5 | About section |
| Day 6 | Banner image |
| Day 7 | Featured section / contact info |

Changes done in bulk on day 1 are the single most common cause of "we just got 5 accounts restricted" events. Spread them out.

### What to customize

| Field | What to put |
|---|---|
| **Profile photo** | Real human photo (provided by vendor - don't generate AI photos) |
| **Banner** | Either a clean branded banner matching your client's world OR a simple solid-color/gradient. Avoid stock templates. |
| **Headline** | Outcome-focused. Format: "Helping [ICP] do [specific outcome] / [optional URL]". Example: "Helping mobile app studios drive installs and retention / yourcompany.com" |
| **Job title** | Match the persona to the seniority you want. Sales Director, Business Development Manager, Account Executive, Partnerships Lead all work. Do not use generic "Founder" or "CEO" unless that matches the play. |
| **Company name** | The company you're representing (your client or your own). Make sure the company has a real LinkedIn page. |
| **About section** | First-person, 3-5 short paragraphs. Lead with what you do for whom. End with a soft CTA ("Open to chats with [ICP]"). |
| **Location** | MUST match target market. US targets = US sender location. |

### Customization don'ts

- Don't reuse the same headline across all accounts in your fleet (LinkedIn pattern-matches)
- Don't have all accounts work for the same company on the same day (looks like a botnet)
- Don't add the same set of skills to every account
- Don't post identical content from multiple accounts (auto-detected as coordinated inauthentic behavior)

---

## 3. Anti-Detect Browser Setup

Every rented account must run in its own isolated browser environment. **You cannot operate multiple LinkedIn accounts from the same browser, even with different tabs or Chrome profiles** - LinkedIn fingerprints the browser and links accounts together, then restricts all of them simultaneously.

### Anti-detect browsers (ranked)

| Tool | Best For | Notes |
|---|---|---|
| **Undetectable** | Most rented engine vendors | Often included with vendor packages |
| **Multilogin** | Premium agencies, large fleets | Most polished, highest cost |
| **Dolphin{anty}** | Mid-volume, good price/performance | Strong at fingerprint randomization |
| **Linken Sphere** | High-end, security-conscious | Less common but very stable |
| **GoLogin** | Budget option | Adequate but more restriction reports |

### What an anti-detect browser does

Each profile gets a unique fingerprint covering:
- Canvas / WebGL fingerprint
- User agent / OS / browser version
- Time zone (must match the proxy IP location)
- Language settings (must match the persona's location)
- Cookies / localStorage (isolated per profile)
- Hardware concurrency, screen resolution, etc.

### Setup rules

1. **One browser profile = one LinkedIn account** - never log multiple accounts into one profile
2. **Time zone of the browser must match the proxy IP location** - mismatch is a top detection signal
3. **Save the browser profile** - don't recreate it. Recreated profiles look like new devices, which triggers verification.
4. **Always log in via the anti-detect browser** - never log into LinkedIn from a normal Chrome/Safari to "just check something." That ties your real device to the rented account.

---

## 4. Proxy Assignment

Each rented account needs its own dedicated proxy. Sharing proxies across accounts is a guaranteed path to bulk restrictions.

### Proxy types (ranked)

| Type | Quality | Cost | Use For |
|---|---|---|---|
| **4G/5G mobile proxies** | Highest - IPs rotate naturally, look like real human users | $$$ | Premium rented engine accounts |
| **Sticky residential** | High - looks like a real home internet connection | $$ | Standard rented engine |
| **Static residential** | Decent - fixed IP, looks human | $$ | Long-running stable accounts |
| **Datacenter proxies** | Low - easily detected as non-human | $ | Never use for LinkedIn |

### Proxy rules

- **One proxy per account** - never share
- **Same proxy for the life of the account** - don't rotate IPs daily; LinkedIn flags location changes as account compromise
- **Proxy location must match the account's stated location** - US account = US proxy. UK account = UK proxy. Mismatches trigger verification.
- **Sticky session** - the proxy must hold the same IP for at least an entire session, ideally for weeks. "Rotating" residential proxies are NOT suitable for LinkedIn.

### Common providers

Bright Data, Oxylabs, Soax, IPRoyal (residential). For mobile: ProxyGuys, Airproxy, vendor-provided. Most professional rented-engine vendors include proxies in their pricing.

---

## 5. Warmup (Days 7-21)

Once accounts are customized, they cannot start outbound immediately. New or freshly-modified accounts need a 2-3 week warmup phase.

### Warmup activity schedule

| Week | Daily Activity |
|---|---|
| **Week 1 (Days 7-14)** | Accept 5-10 incoming connections (vendor seeds these). Like 3-5 posts. Comment on 1-2. Browse profiles 10-15. No outbound connection requests yet. |
| **Week 2 (Days 14-21)** | Send 5-10 connection requests/day to warm contacts (vendor's network or known peers). Like 5-7 posts. Comment on 2-3. Post 1 short piece of content. |
| **Week 3+** | Begin cold outbound at 10-12 connection requests/day. Scale to 15-18/day over 2 weeks. |

### Why warmup matters

LinkedIn measures "account quality" via patterns. A profile that goes from 0 to 100 connection requests on day 1 looks exactly like a bot. The same account doing 5 → 8 → 12 → 15 over 3 weeks looks like a real human getting active.

### Warmup mistakes that get accounts banned

- Sending mass connection requests on day 1 of customization
- Connecting with random accounts unrelated to the persona's industry
- Posting AI-generated content from a brand-new profile
- Liking 50+ posts in an hour (unhuman pace)
- Sending DMs before any connections exist

---

## 6. Daily & Weekly Limits

LinkedIn enforces hard ceilings. Going above them = restrictions.

### Hard ceilings (LinkedIn-enforced)

### LinkedIn's actual per-account caps

| Metric | Limit | Notes |
|---|---|---|
| **Daily connection requests (LinkedIn-enforced ceiling)** | 20-40 per day | LinkedIn's hard-enforced range (varies by account age and standing). Above this risks the 1-week pause. |
| **Weekly connection requests** | ~100 (sometimes 80-120, varies by account quality) | Hard cap. Going above triggers a 1-week pause warning, then a 30-90 day restriction. |
| **Daily search results viewable** | ~1000 (Sales Nav) | Higher with Sales Nav, lower without |
| **Daily message sends** | 100-150 | DMs to existing connections - soft limit |
| **InMail per month** | 50-150 | Depends on Sales Nav tier |

### GT operational recommendations (well below the ceiling for safety)

| Activity | Per Day | Per Week |
|---|---|---|
| Connection requests (cold) | 15-18 | 80-90 |
| DMs to existing connections | 30-50 | 150-250 |
| Profile views | 80-100 | 500-700 |
| Likes on posts | 20-30 | 100-150 |
| Comments on posts | 3-5 | 15-25 |

LinkedIn allows 20-40/day per account; we operate at 15-18 because that leaves margin for verification challenges, accidental over-sends, and short-term ceiling reductions when LinkedIn tightens enforcement. Volume scales horizontally through more accounts, not vertically through more requests per account.

### Sender rotation math (the structural lever)

The fastest way to scale connection volume safely is **across accounts, not within them.** Add senders to a campaign and let the sequencer distribute the load.

| Account count | Daily connections (at 18/day) | Weekly connections | Notes |
|---|---|---|---|
| 1 account | 18 | 90 | Single point of failure. One restriction = pipeline stops. |
| 3 accounts | 54 | 270 | Reasonable for an SDR + 2 support profiles |
| 5 accounts | 90 | 450 | Standard agency rented engine for one client |
| 10 accounts | 180 | 900 | Full ABM blast across a 5-10K account list |

HeyReach (and similar platforms) auto-rotate sends across all senders attached to a campaign - no rep needs to track who sent what. All replies surface in a unified inbox.

Source: HeyReach's sender rotation framing. See `resources/heyreach-knowledge-base.md`.

### Why we stay under the ceiling

LinkedIn's anti-spam scoring is probabilistic. Hitting the ceiling every week is a signal of automation. Staying at 80-85% of the ceiling looks human and avoids restriction triggers.

---

## 7. Account Restrictions - Recognition & Recovery

Restrictions are a fact of operating LinkedIn outbound. The goal isn't zero restrictions - it's a low rate (under 5% of accounts per month) and fast recovery.

### Restriction types

| Restriction | Trigger | Recovery |
|---|---|---|
| **Verification challenge** (phone/email) | Suspicious activity, location change, new device | Verify with the account owner - usually within 24h. Vendor handles this. |
| **Temporary connection request pause** (1 week) | Hit the weekly ceiling, or low acceptance rate (<15%) | Wait it out. Pause campaigns. Don't try to send during the pause. |
| **30-90 day account restriction** | Multiple weekly limit violations, or coordinated inauthentic behavior | Vendor must contact LinkedIn support with the human account owner. Expect 2-6 weeks downtime. |
| **Permanent ban** | Severe spam, fake identity, mass message reports | Account is dead. Replace it. |

### Restriction recovery flow

1. **Stop all activity immediately.** Pause HeyReach/Expandi/Lemlist for that account.
2. **Identify the cause:**
   - Recent profile changes (>1/day)?
   - Hit the weekly ceiling?
   - Low acceptance rate (<15%) - LinkedIn flags low-quality outreach
   - Recent location/device change?
3. **Contact the vendor** - they own the account and have direct LinkedIn support access.
4. **Account owner verifies** (phone, email, ID if requested).
5. **Resume gradually** - restart at 50% of previous daily volume for 1 week.

### Prevention

- **Stay at 80-85% of ceilings** (15-18 daily / 80-90 weekly)
- **Maintain >25% acceptance rate** - low acceptance is itself a restriction trigger
- **One profile change per day**
- **Never log in from your home device** - only the anti-detect browser
- **Don't run the same DM copy across all accounts** - variety is human

---

## 8. Sending Tools

The tool layer that automates connection requests and DMs.

### Tool comparison

| Tool | Best For | Notes |
|---|---|---|
| **HeyReach** | Multi-account at scale (preferred for agencies) | Strong API for rented engine, native multi-account workflows. Recommended default. |
| **Expandi** | Mid-volume, smart sequences | Cloud-based, runs even when computer is off |
| **La Growth Machine** | Multi-channel (LinkedIn + email + Twitter) | Best for combined campaigns |
| **Lemlist** | Multi-channel with voice notes, video, image personalization | Strong creative options. LinkedIn integration is decent but not the strongest. |
| **Linked Helper** | Cheaper, browser-based | Higher restriction risk - runs locally, not cloud |
| **Dux-Soup** | Cheaper, browser-based | Higher restriction risk - older tool, less maintained |

### HeyReach setup essentials

1. **Account login** - provide LinkedIn credentials AND the anti-detect browser config OR login via cookies exported from the anti-detect browser
2. **Proxy** - HeyReach must connect through the same proxy as the anti-detect browser. Note: HeyReach is cloud-based with geo-matched proxy servers built in, so the platform itself doesn't need a manual proxy setup - but the LinkedIn account session must come from a proxy that matches the profile's stated location.
3. **Daily limits** - configure hard caps in HeyReach matching your operational limits (15-18 connection requests/day). HeyReach enforces these limits automatically and stops activity before a breach. Limits are distributed proportionally across all campaigns the sender is enrolled in, so multiple campaigns can't accidentally compound and breach the daily ceiling.
4. **Sender rotation** - attach 3-10 senders to the same campaign. HeyReach auto-rotates which account sends each request, distributing load and surfacing all replies in a unified inbox (Unibox).
5. **Sequence template** - connection request (with or without note) → 30-60s wait → M1 (after acceptance) → 3-5 day wait → M2B (if no reply). Use **conditional branches** for connected-no-reply vs. profile-viewed vs. replied paths - see `copywriting/examples/dm-sequence.md` state-aware branching section.
6. **Auto-withdrawal of pending invitations** - set HeyReach to auto-withdraw pending connection requests after 14 days. Pending invitations sitting in LinkedIn's queue past 14 days hurt account health; a queue >1000 pending triggers anti-spam systems.
7. **Working hours** - restrict sends to 9am-5pm in the account's stated time zone (sending at 3am US time from a "US-based account" is a detection signal).
8. **Reply detection** - connect to the inbox so replies pause the sequence automatically. All replies across senders surface in Unibox.
9. **Lead import sources** - HeyReach pulls leads from LinkedIn search URLs, Sales Navigator URLs, post reactors, webinar attendees, and CSV imports. Wider than most teams realize.
10. **Mid-campaign editing rule** - message *copy* can be edited mid-campaign; sequence *steps* (the structure) cannot. Plan structure carefully upfront; iterate on copy.

### Cloud-based vs. browser-extension tools

A tool architecture distinction that matters for safety:

- **Cloud-based** (HeyReach, Expandi) - runs on the vendor's servers via geo-matched proxies. Continues running with browser closed. Lower restriction risk because the activity pattern looks server-driven (which LinkedIn now expects from legitimate enterprise tools).
- **Browser-extension** (Linked Helper, Dux-Soup) - runs in the local browser on the rep's machine. Pauses when the browser closes. Higher restriction risk because the browser fingerprint plus erratic activity patterns (manual mouse, varied tab focus) actually look more anomalous than a clean cloud session.

For rented-engine work, default to cloud-based tools. The cost difference is small; the restriction risk difference is large.

### Tool integration with copywriting tools

If running combined LinkedIn + email campaigns, sync via:
- HeyReach + Lemlist: API integration
- HeyReach + Smartlead/Instantly: webhook or Clay-driven sequencing
- Cross-channel pause logic: reply on either channel → pause both

---

## 9. Going Live - Checklist

Before sending the first cold connection request from a rented account:

- [ ] Account age 6+ months OR completed 21-day warmup
- [ ] Customization fully complete (1 change per day, all spread out)
- [ ] 300+ connections on the profile
- [ ] Profile photo is a real human (not AI-generated)
- [ ] Location matches target market
- [ ] Anti-detect browser profile saved and tested
- [ ] Mobile/residential proxy assigned and matches location
- [ ] Sales Navigator subscription active (for advanced search)
- [ ] HeyReach/Expandi configured with daily limits at 15-18/day
- [ ] Working hours set to 9am-5pm in account's time zone
- [ ] Reply detection / inbox sync working
- [ ] M1 + M2B copy ready (different angles, no repeated phrasing across accounts)
- [ ] Engagement-first warming enabled (visit + like before connection request)
- [ ] Tracking set up: acceptance rate, reply rate, restriction events

---

## 10. Ongoing Hygiene

Once the engine is running, these are the daily/weekly disciplines:

### Daily
- Monitor connection acceptance rate per account (alert if any account drops below 20%)
- Monitor reply rate per account
- Check for verification challenges (rare but immediate-action items)
- Spot-check one DM per account for tone and quality

### Weekly
- Review weekly send volume per account (must be <90)
- Review restriction events across the fleet (target: <5% of accounts/month)
- Refresh sequence copy - never let the same M1 run for >4 weeks (LinkedIn pattern-detects)
- Light content posting from each account (1-2 posts/week boosts acceptance and reduces restriction risk)

### Monthly
- Audit fleet performance - retire bottom-quartile accounts
- Replace any accounts that hit restriction more than once
- Refresh headlines and About sections (keeps profiles "alive" in LinkedIn's eyes)
- Review geographic distribution against target TAM

---

## Personal Profile vs Rented Engine - Operating Differences

If the user is running their own founder/personal profile (not rented), most rules above DO NOT APPLY at the same intensity:

| Rule | Rented engine | Personal profile |
|---|---|---|
| Anti-detect browser | Required | Not needed (use normal browser) |
| Mobile proxy | Required | Not needed (home/office IP fine) |
| 1 change per day | Strict | Light - natural changes are normal |
| 15-18 connections/day | Strict ceiling | Can flex up to 20-25, but stay under weekly 100 |
| Warmup | 14-21 days mandatory | Already warmed if it's your real profile |
| Profile customization | Vendor-coordinated | Just edit it normally |
| Restriction risk | Moderate | Low (real established profile) |

Founder profiles are inherently lower-risk because LinkedIn's signals - long account age, real network, organic content history, real human behavior patterns - work in your favor. The trade-off is volume: one founder profile maxes out at ~80 connection requests/week, while a 10-account rented engine does 800-900/week.

---

## Combines With

| Skill | Why |
|---|---|
| `connection-request` | Copy for the cold note (or no-note decision) |
| `dm-sequence` | Copy for M1 + M2A/M2B post-acceptance |
| `personalization` | Profile signals, Clay prompts, hook patterns |
| `gt-clay` | Account enrichment, targeting, signal sourcing |
| `gt-list-building` | Sales Navigator search → list → enrichment |
| `gt-signal-sourcer` | Trigger feeds (job changes, hiring, post engagement) for warm outreach |
| `gt-cold-email` | Multi-channel coordination |

---

## Common Mistakes (Operational)

1. **Buying cheap accounts** - sub-$50/account vendors usually deliver scraped or hijacked profiles. Restriction rate is 30%+ in the first month. Pay for quality.
2. **Operating from your home device** - "I'll just check the inbox quickly from my laptop" - this links your real fingerprint to the rented account permanently.
3. **Bulk-changing customization on day 1** - the single most common cause of mass restrictions in the first 30 days.
4. **Sharing proxies across accounts** - guarantees bulk restrictions when one account triggers a flag.
5. **Ignoring acceptance rate alerts** - accounts at <20% acceptance are flagged by LinkedIn internally; continuing to send accelerates restriction.
6. **Running identical DM copy across all accounts** - pattern-detected as coordinated automation.
7. **No content from rented accounts** - fully silent profiles look like bots. 1-2 posts per week per account significantly reduces restriction risk.
8. **No engagement-first warming** - going straight to connection request instead of liking/commenting first burns 10-15 points of acceptance rate AND signals automation.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
