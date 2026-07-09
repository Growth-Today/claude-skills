# GT GTM Strategy Advisor

A signal-based GTM playbook builder for Claude, built by [Growth Today](https://www.growthtoday.co). Turn your own CRM data, sales deck, website, and call recordings into a complete, data-backed GTM playbook — delivered as a ready-to-use Excel workbook.

Built for VP of Sales, Heads of Growth, RevOps leads, and founder-led sales teams who want a GTM motion grounded in their real data, not a generic template.

## Install

Add it to your project with the [skills CLI](https://www.growthtoday.co/claude-skills):

```bash
npx skills add Growth-Today/claude-skills/gt-gtm-strategy-advisor
```

Or copy the `gt-gtm-strategy-advisor/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Not sure how to install or use Claude Skills? Full walkthrough here: **https://www.growthtoday.co/claude-skills/gt-gtm-strategy-advisor**

## What it does

Feed it your data — connect your HubSpot or Salesforce, upload your sales deck, website copy, a CRM export, and any recent call recordings. In six stages it builds:

1. **Company + Market** — a plain-English read of what you do and who you sell to
2. **ICP + Pain per Persona** — your real ideal customer, validated against actual closed-won patterns (not what you assume)
3. **Signal Library + Combo Plays** — 25+ buying signals and multi-signal plays built around your product
4. **Sales Battlecard** — competitor displacement and objection handling, speakable in 10 seconds
5. **Messaging Matrix** — messaging variants from your real pain language and proof
6. **Excel Assembly** — the complete workbook, ready to hand to your team

Review each tab as you go — ideally with someone in the execution day to day (a working rep or your marketing lead). Once you have a real sales-call recording, re-run to produce a validated version that flags every gap between your assumptions and what your calls actually show.

The more real data you feed it, the sharper the output: materials only = a starting hypothesis; CRM data = grounded in who actually buys; call recordings = confirmed against real conversations.

Pairs well with `gt-hubspot-admin` / `gt-salesforce-admin` (to pull and clean your CRM data) and `gt-clay` (for enrichment).

## Structure

```
gt-gtm-strategy-advisor/
├── SKILL.md                        ← orchestrator (auto-loaded by Claude)
├── README.md                       ← this file
├── LICENSE                         ← MIT
└── resources/
    ├── skill-1-research.md         ← Company + Market (Tab 0, 1)
    ├── skill-2-icp-persona.md      ← ICP + Pain per Persona (Tab 2, 4)
    ├── skill-3-signal-library.md   ← Signal Library + Combo Plays (Tab 6, 7)
    ├── skill-4-battlecard.md       ← Sales Battlecard (Tab 9)
    ├── skill-5-messaging.md        ← Messaging Matrix (Tab 8)
    └── skill-6-excel-assembly.md   ← Excel workbook assembly
```

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
