# GT GTM Alpha Playbook

A signal-based GTM playbook generator for Claude, built by [Growth Today](https://www.growthtoday.co). Give it a target company domain and it builds a comprehensive, signal-based GTM playbook — mapping the vendor's pain points to high-intent buying signals, designing Clay/Claygent workflows to detect them, and delivering 3-5 outbound plays with email templates.

## Install

Add it to your project with the [skills CLI](https://www.growthtoday.co/claude-skills):

```bash
npx skills add Growth-Today/claude-skills/gt-gtm-alpha-playbook
```

Or copy the `gt-gtm-alpha-playbook/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Not sure how to install or use Claude Skills? Full walkthrough here: **https://www.growthtoday.co/claude-skills/gt-gtm-alpha-playbook**

## What it does

Trigger it with a company domain — "build a GTM Alpha playbook for stamped.io". The skill researches the vendor, loads the reference frameworks, generates an industry-specific playbook (executive summary, signal framework, Clay workflows, outbound plays, email templates, competitive intelligence), and saves it as a Google Doc in your GTM playbooks folder for later reference.

Best paired with a Clay account (for the signal-detection workflows) and Google Drive (to store the generated playbooks). Related GT skills: `gt-clay`, `gt-signal-sourcer`, `gt-cold-email`.

## Structure

```
gt-gtm-alpha-playbook/
├── SKILL.md                              ← orchestrator (auto-loaded by Claude)
├── README.md                            ← this file
├── LICENSE                              ← MIT
└── resources/
    ├── gtm-alpha-concept.md             ← GTM Alpha philosophy, signal categories, principles
    ├── playbook-prompt-framework.md     ← the generation framework and quality standards
    └── clay-case-studies.md             ← real Clay signal-based GTM case studies (with sources)
```

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
