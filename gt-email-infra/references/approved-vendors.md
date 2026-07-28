# Approved Vendors

The tools and services Growth Today uses (or benchmarks) for cold-email infrastructure. Playbooks reference "an approved vendor" and point here rather than hard-coding a single name — swap in whichever approved option fits the engagement.

> These are the vendors we consider fit for purpose. Pick per engagement; the *process* (multi-registrar spread, masking-not-redirect, warmup discipline) matters more than the specific brand.

---

## Domain purchasing & DNS setup

| Vendor | Role | Why approved |
|---|---|---|
| **ScaledMail** | Buys domains across multiple registrars over ~24h, configures DNS across multiple Cloudflare accounts, provisions mailboxes | Handles the registrar/date/DNS spread for us so a batch doesn't share one abuse fingerprint; ~1 day to buy + ~1 day to configure |

The buying vendor should always: spread across multiple registrars, keep **< 5 domains per registrar per day**, stagger over ~24h, and spread DNS across multiple accounts. Any vendor that bulk-buys from one registrar on one day is not fit for purpose (see `reference.md` §9 for the research basis).

---

## Custom SMTP / mailbox vendors (approved)

Approved providers for custom-SMTP sending infrastructure (as an alternative or complement to native Google Workspace / Microsoft 365 mailboxes). Pick per engagement; whichever is used, the same rules apply — masking not redirect, warmup discipline, and correct MX/SPF/DKIM/DMARC.

- **Winnr**
- **MissionInbox**
- **ScaledMail**
- **InboxedUp**
- **Lunatro** (Azure)
- **Maildoso**

Only these are approved. A vendor not on this list should not be used without GTM/account-owner sign-off.

---

## Sequencers / sending platforms

| Vendor | Status at Growth Today | Notes |
|---|---|---|
| **EmailBison** | Current sending platform | The automated inbox-management system runs on it today |
| **Instantly** | Migrating to | Can set cold limit 0 and continue a lead from a healthy inbox (closes the failover gap); auto-warmup |
| **Smartlead** | Benchmarked | Third option we compare against; auto-warmup |

## Placement testing & masking

| Vendor | Role |
|---|---|
| **EmailGuard** | Inbox-placement testing and domain masking |

---

## Not covered here

- **Email verification** providers (list hygiene) → handled in `gt-list-building`, not this skill.
- **Cold email copy** tooling → `gt-cold-email`.

---

*Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
