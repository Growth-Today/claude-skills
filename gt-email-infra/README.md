# GT Email Infrastructure & Deliverability

A cold email infrastructure and deliverability skill for Claude, built by [Growth Today](https://www.growthtoday.co). Organized around the two people who run it (**Sales Ops** and **GTM Engineer**) as role-tagged sub-skills, each ending in a copy-pasteable checklist.

## Install

```bash
npx skills add Growth-Today/claude-skills/gt-email-infra
```

Or copy the `gt-email-infra/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Full walkthrough: **https://www.growthtoday.co/claude-skills/gt-email-infra**

## What it covers

The orchestrator routes by role and task to the right sub-skill:

- **[Sales Ops] domain-research**: on-brand naming rules, spam-trap avoidance, safe multi-registrar purchasing.
- **[Sales Ops] provisioning**: Google / Microsoft / custom-SMTP mailboxes, MX/SPF/DKIM/DMARC, masking vs redirect, DNS-drift monitoring.
- **[Sales Ops] setup sub-skills**: connect inboxes, warmup, and advanced deliverability per sequencer: **emailbison-setup, instantly-setup, smartlead-setup, lemlist-setup** (vendor-managed or in-house).
- **[GTM] setup-audit**: connect a live workspace and verify every setting against the GT standard (PASS / WARN / FAIL + fixes).
- **[Sales Ops → GTM] warmup-golive**: warmup timelines, ramp schedules, the hard launch gate.
- **[GTM] campaign-building**: route by the Lead-ESP × sending-vendor matrix (ESP matching is dead as a rule); isolate SEG leads onto dedicated domains.
- **[GTM] dashboard-reading**: inbox classification, per-state limits, turning each panel into an action.
- **[GTM] blacklist-bounce-audit**: strip auto-replies first, categorize bounces, read SMTP codes, trace root cause.

Plus shared resources for all numbers/limits, approved vendors, and 2026 market benchmarks.

## Structure

```
gt-email-infra/
├── SKILL.md ← orchestrator: SKILL_BASE setup, routing, critical rules, GT point of view
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .claude/skills/
│ ├── domain-research/gt-SKILL.md [Sales Ops]
│ ├── provisioning/gt-SKILL.md [Sales Ops]
│ ├── emailbison-setup/gt-SKILL.md [Sales Ops]
│ ├── instantly-setup/gt-SKILL.md [Sales Ops]
│ ├── smartlead-setup/gt-SKILL.md [Sales Ops]
│ ├── lemlist-setup/gt-SKILL.md [Sales Ops] (email + LinkedIn)
│ ├── warmup-golive/gt-SKILL.md [Sales Ops → GTM]
│ ├── campaign-building/gt-SKILL.md [GTM Engineer]
│ ├── dashboard-reading/gt-SKILL.md [GTM Engineer]
│ ├── setup-audit/gt-SKILL.md [GTM Engineer] (live config audit)
│ └── blacklist-bounce-audit/gt-SKILL.md [GTM Engineer]
└── resources/
 ├── reference.md ← single source of numbers, limits, thresholds, taxonomy
 ├── approved-vendors.md ← approved SMTP / sequencer / masking vendors
 └── benchmarks.md ← 2026 market performance benchmarks
```

Note: this skill supports the sequencers Growth Today runs, **EmailBison, Instantly, Smartlead, and Lemlist**, via a setup sub-skill for each. The concepts are ESP-agnostic; platform-specific steps are called out inline. Adapt them to your own stack.

## License

MIT, see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
