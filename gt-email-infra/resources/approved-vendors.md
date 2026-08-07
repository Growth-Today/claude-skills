# Approved Vendors

The tools and services Growth Today uses (or benchmarks) for cold-email infrastructure. Sub-skills reference "an approved vendor" and point here rather than hard-coding a single name, swap in whichever approved option fits the engagement.

> These are the vendors we consider fit for purpose. Pick per engagement; the *process* (multi-registrar spread, masking-not-redirect, warmup discipline) matters more than the specific brand.

---

## Domain purchasing & DNS setup

| Vendor | Role | Why approved |
|---|---|---|
| **ScaledMail** | Buys domains across multiple registrars over ~24h, configures DNS across multiple Cloudflare accounts, provisions mailboxes | Handles the registrar/date/DNS spread for us so a batch doesn't share one abuse fingerprint; ~1 day to buy + ~1 day to configure |

The buying vendor should always: spread across multiple registrars, keep **< 5 domains per registrar per day**, stagger over ~24h, and spread DNS across multiple accounts. Any vendor that bulk-buys from one registrar on one day is not fit for purpose (see `reference.md` §9 for the research basis).

---

## Custom SMTP / mailbox vendors (approved)

Approved providers for custom-SMTP sending infrastructure (as an alternative or complement to native Google Workspace / Microsoft 365 mailboxes). Pick per engagement; whichever is used, the same rules apply, masking not redirect, warmup discipline, and correct MX/SPF/DKIM/DMARC.

- **Winnr**
- **MissionInbox**
- **ScaledMail**
- **InboxedUp**
- **Lunatro** (Azure)
- **Maildoso**

Only these are approved. A vendor not on this list should not be used without GTM/account-owner sign-off.

---

## Sequencers / sending platforms

Growth Today runs cold outreach across these approved sequencers, pick per engagement and use the matching setup sub-skill:

| Vendor | Setup sub-skill | Notes |
|---|---|---|
| **EmailBison** | emailbison-setup | Warmup fully automated (set the max daily limit only); pairs with EmailGuard for placement tests; min cold limit = 1 (cannot be 0) |
| **Instantly** | instantly-setup | Auto-warmup; can set cold limit 0 and reroute a lead to a healthy inbox; native placement tests |
| **Smartlead** | smartlead-setup | Auto-warmup with smart-adjust; SmartDelivery placement tests |
| **Lemlist** | lemlist-setup | Multichannel (email + LinkedIn); lemwarm warmup; Deliverability Hub |

## Placement testing & masking

| Vendor | Role |
|---|---|
| **EmailGuard** | Inbox-placement testing and domain masking (used with EmailBison) |
| **Instantly** | Native inbox-placement testing (used when Instantly is the sequencer) |

Pick the placement-testing tool that matches the sequencer for the engagement. EmailGuard pairs with EmailBison; Instantly has built-in placement tests when it is the sending platform.

---

## Not covered here

- **Email verification** providers (list hygiene) → handled in `gt-list-building`, not this skill.
- **Cold email copy** tooling → `gt-cold-email`.

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
