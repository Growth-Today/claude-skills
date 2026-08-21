# Approved Vendors

The tools and services Growth Today uses for cold-email infrastructure. Sub-skills say "an approved vendor" and point here rather than naming one brand, so swap in whichever approved option fits the engagement.

> **The process matters more than the brand.** Spreading purchases across registrars and days, using masking instead of a redirect, and warmup discipline all matter more than which registrar's logo is on the invoice.

---

## Who does what

**ScaledMail buys the domains and connects the inboxes.** Growth Today keeps **domain name research and verification**. We no longer place domain orders ourselves — see `reference.md` §9 and the domain-research sub-skill.

ScaledMail spreads purchases across registrars and dates, and spreads DNS across multiple Cloudflare accounts, so a batch doesn't all look like it was bought at once. They charge roughly a 10% markup, and it usually takes about a day to buy and a day to configure.

**What GT verifies on delivery:** registrars actually differ across the batch, creation dates are staggered, no more than 4 domains landed on one registrar in one day, and the destination is masking or a real landing page rather than a redirect.

---

## Registrars

| Registrar | Role | Notes |
|---|---|---|
| **Dynadot** | Primary at scale (20+ domains) | The only one built for agencies — client folders, team logins, proper bulk tools and a full API. Flat **$10.88/yr**, no renewal surprise. One quirk: the API handles one request at a time, so batch jobs queue rather than run in parallel |
| **Spaceship** | Approved | **$4.99** first year, **$9.98** renewal. Bulk tools, good API, much cleaner interface than Namecheap. ⚠️ Owned by Namecheap, and one GT domain bought here was flagged *before* it was ever used |
| **NameSilo** | Secondary, large batches | Cheapest at volume — **$9.89/yr at 100+ domains**. Dated interface, weaker team tooling |
| **Porkbun** | Small batches (under 20) | Runs on Cloudflare infrastructure. Fine for one client, not built for managing many |
| **Namecheap** | Legacy, still in use | Existing domains only |
| **GoDaddy** | Kept — client-held only | Clients own domains here, so we keep it on the list. ⚠️ Most expensive renewals (**$20–22**), and in Feb 2026 they rewrote their terms to reclassify all customers as business customers, removing consumer protections. **Not recommended for new GT purchases** |
| **Cloudflare** | **DNS, not a registrar** | Best DNS, instant propagation — but no bulk registration and you can't register at scale through the API. Buy elsewhere, point DNS here |

**Not approved:** IONOS (a 2026 rule change removed WHOIS privacy for business customers), Hover (no API at all), Hostinger, Gandi ($38.38/yr), Network Solutions ($44.99/yr), Name.com, Squarespace, Vercel.

> **Registrar choice matters less than spread.** The registrars that are best for agency work — Dynadot, NameSilo, Namecheap and Spaceship — are also the ones that show up most in abuse data. That's because they're popular and cheap, not because they're bad. The control that actually protects us is buying across several registrars over several days (max 4 per registrar per day), not avoiding a particular brand.

---

## Mailbox and custom SMTP vendors

Approved providers for sending infrastructure, as an alternative or complement to native Google Workspace and Microsoft 365 mailboxes. Whichever is used, the same rules apply: masking not redirect, warmup discipline, and correct MX/SPF/DKIM/DMARC.

- **ScaledMail** — current default
- **Winnr**
- **MissionInbox**
- **InboxedUp**
- **Lunatro** (Azure)
- **Maildoso** — kept on the list for future use; not in use today
- **InboxKit** — ⚠️ approved by GT, but not approved by EmailBison. Check before using on a Bison workspace

Only these are approved. Anything else needs sign-off from the GTM or account owner.

**Not approved:** Zapmail, Mailreef.

---

## Sequencers

| Vendor | Setup sub-skill | Notes |
|---|---|---|
| **Instantly** | instantly-setup | **Primary platform.** Auto-warmup; can set cold limit to 0 and reroute a lead to a healthy inbox; native placement tests. ⚠️ No built-in domain masking — see below |
| **EmailBison** | emailbison-setup | **Being retired** — all campaigns finish by end of August 2026. Warmup fully automated; minimum cold limit is 1, it cannot be set to 0 |
| **Smartlead** | smartlead-setup | Auto-warmup with smart-adjust; SmartDelivery placement tests |
| **Lemlist** | lemlist-setup | Email plus LinkedIn; lemwarm warmup |

---

## Masking and placement testing

| Vendor | Role |
|---|---|
| **EmailGuard** | Inbox-placement testing and domain masking (used with EmailBison) |
| **Instantly** | Native inbox-placement testing (used when Instantly is the sequencer) |
| **ScaledMail** | Domain masking — free, offered as an option alongside redirect when ordering domains |
| **Cloudflare** | Possible self-hosted masking route — under review |

Pick the placement-testing tool that matches the sequencer for the engagement. EmailGuard pairs with EmailBison; Instantly has built-in placement tests when it is the sending platform.

> **⚠️ Open item — masking.** Instantly has no built-in domain masking, so moving off EmailBison
> removes the masking we had. Four options were priced (Aug 2026 research):
>
> | Option | Cost | Status |
> |---|---|---|
> | **ScaledMail** built-in masking | **$0** | Free option when ordering domains, alongside redirect. In development, ETA end of Aug 2026. **Open question: does it cover domains we already own, or only new orders?** |
> | **EmailGuard** proxies | **~$465.60/mo** | 771 client domains total, 120 already held. 500 more at $0.75, remainder at $0.60 |
> | **Cloudflare Worker** (self-built) | ~$5/mo | Cheap, but we own the maintenance |
> | **Mailforge** | $2/domain/mo | ❌ Ruled out — only works on domains bought through Mailforge |
>
> **Owner: Fezekile.** Decide once ScaledMail confirms delivery and existing-domain coverage.

---

## Not covered here

- **Email verification** providers → `gt-list-building`
- **Cold email copy** tooling → `gt-cold-email`

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
