# GT Email Infrastructure & Deliverability

A cold email infrastructure and deliverability skill for Claude, built by [Growth Today](https://www.growthtoday.co). Covers the full lifecycle — organized around the two people who actually run it (**Sales Ops** and **GTM Engineer**), with every playbook ending in a copy-pasteable checklist.

## Install

```bash
npx skills add Growth-Today/claude-skills/gt-email-infra
```

Or copy the `gt-email-infra/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Full walkthrough: **https://www.growthtoday.co/claude-skills/gt-email-infra**

## What it covers

Ask it anything about cold email infrastructure and it routes by **role and task**:

- **[Sales Ops] Domain research & purchasing** — on-brand naming rules, avoiding spam-trap patterns, and buying safely (multi-registrar spread, no bulk-buy fingerprint).
- **[Sales Ops] Provisioning, DNS & auth** — Google Workspace / Microsoft 365 / custom-SMTP mailboxes, MX/SPF/DKIM/DMARC, masking vs. redirect, DNS-drift monitoring.
- **[Sales Ops] Instantly inbox setup** — connect Google/Microsoft/custom-SMTP inboxes, warmup config, and advanced-deliverability settings (vendor-managed or in-house).
- **[Sales Ops → GTM] Warmup & go-live** — warmup timelines, ramp schedules, and a hard launch gate.
- **[GTM] Campaign building** — routing by the Lead-ESP × sending-vendor matrix (ESP-matching is dead as a rule), and isolating SEG leads onto dedicated domains.
- **[GTM] Dashboard reading** — inbox classification, per-state limits, and turning each panel into an action.
- **[GTM] Blacklist & bounce audit** — strip auto-replies first, categorize bounces, read soft vs. hard SMTP codes, and trace the root cause to infra, list/data, or copy.

Plus references for all numbers/limits, approved vendors, and market performance benchmarks.

## Structure

```
gt-email-infra/
├── SKILL.md                                  ← router: roles, critical rules, sizing, GT point of view
├── README.md
├── LICENSE
├── references/
│   ├── reference.md                          ← all numbers, limits, timelines, thresholds, taxonomy
│   ├── approved-vendors.md                   ← approved SMTP / sequencer / masking vendors
│   └── benchmarks.md                          ← 2026 market benchmarks (results-side, good vs. bad)
└── playbooks/
    ├── 01-domain-research-and-purchasing.md  [Sales Ops]      + BUY checklist
    ├── 02-provisioning-dns-auth.md           [Sales Ops]      + PROVISIONING checklist
    ├── 03-warmup-and-go-live.md              [Sales Ops→GTM]  + HARD LAUNCH GATE
    ├── 04-campaign-building.md               [GTM Engineer]   + CAMPAIGN checklist
    ├── 05-dashboard-reading.md               [GTM Engineer]   + HEALTH-REVIEW checklist
    ├── 06-blacklist-bounce-audit.md          [GTM Engineer]   + AUDIT checklist
    └── 07-instantly-setup.md                 [Sales Ops]      + INSTANTLY SETUP checklist
```

Note: Growth Today runs this on **EmailBison** today and is **migrating to Instantly** (Smartlead is benchmarked as a third option). The concepts, thresholds, and diagnostics are ESP-agnostic — platform-specific steps are called out inline; adapt them to your own stack.

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
