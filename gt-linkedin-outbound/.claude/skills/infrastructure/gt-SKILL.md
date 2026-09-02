---
name: linkedin-outbound-infrastructure
description: LinkedIn rented-engine infrastructure and account safety. Covers multi-account sourcing, anti-detect browsers, mobile proxies, daily and weekly sending limits, account restrictions and recovery, profile-change hygiene, and the 2-3 week warmup. Triggers include rented engine, LinkedIn accounts, anti-detect browser, mobile proxies, HeyReach or Expandi setup, account restricted, LinkedIn jail, warmup, and how many connections per day. Do NOT use for message copy (use copywriting), sequence design (use sequences), persona tone (use personas), or benchmarks (use knowledge).
---

# LinkedIn Outbound: Infrastructure

You run the accounts. On a rented engine, infrastructure is as critical as copy: one detection event or one careless bulk edit can restrict a profile permanently. Your job is to keep every sending account safe, warm, and inside the limits.

## Reference

- Sourcing, customization, browser and proxy assignment, warmup schedule, daily limits, restriction diagnosis and recovery: Read `{SKILL_BASE}/resources/infrastructure/rented-engine.md`

## Account rules (full detail in rented-engine.md)

- 15-20 connection requests per day per account. Hard cap; going above invites restrictions.
- ~100 connection requests per week, LinkedIn's enforced ceiling for most accounts. (Verify against official LinkedIn documentation before advising a client, limits shift.)
- One profile change per day (headline, company, photo). Never bulk-edit.
- Anti-detect browser required: every rented account runs in its own isolated browser profile.
- One mobile proxy per account (sticky residential or 4G/5G, geo-matched). Never share an IP across accounts.
- 2-3 week warmup: new accounts accept connections, like, comment, and post for 14-21 days before any outbound DMs.

## When an account is restricted

Diagnose recent activity volume, recent profile changes, and bot-detection signals first, then follow the recovery flow in the resource. Do not resume sending at full volume.

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
