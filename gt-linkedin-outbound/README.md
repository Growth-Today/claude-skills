# GT LinkedIn Outbound

A LinkedIn outbound strategy skill for Claude, built by [Growth Today](https://www.growthtoday.co). A single orchestrator routes to 15 sub-skills covering connection requests, DM sequences, copywriting, personalization, rented-engine infrastructure, campaign strategy, follow-up discipline, and LinkedIn-first GTM.

## Install

Add it to your project with the [skills CLI](https://www.growthtoday.co/claude-skills):

```bash
npx skills add Growth-Today/claude-skills/gt-linkedin-outbound
```

Or copy the `gt-linkedin-outbound/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Not sure how to install or use Claude Skills? Full walkthrough here: **https://www.growthtoday.co/claude-skills/gt-linkedin-outbound**

## What it does

Trigger it with any LinkedIn outbound request — connection notes, post-acceptance DM sequences, personalization at scale, copywriting frameworks, rented-engine setup (multi-account infrastructure, proxies, warmup, restrictions), HeyReach/Expandi tooling, campaign decay and micro-segmentation, follow-up cadence, or the strategic case for LinkedIn-first GTM and 90-day pilots. The orchestrator reads the routing index, checks engine type and persona, and loads the matching sub-skill.

## Structure

```
gt-linkedin-outbound/
├── SKILL.md                    ← orchestrator (auto-loaded by Claude)
├── README.md                   ← this file
├── LICENSE                     ← MIT
└── resources/                  ← 15 sub-skills, loaded on-demand
    ├── connection-request.md   ├── dm-sequence.md
    ├── connection-notes.md     ├── re-engagement.md
    ├── atl-messaging.md        ├── btl-messaging.md
    ├── copywriting.md          ├── personalization.md
    ├── rented-engine.md        ├── campaign-strategy.md
    ├── follow-up-system.md     ├── drip-campaigns.md
    ├── linkedin-first-engine.md├── linkedin-metrics-benchmarks.md
    └── heyreach-knowledge-base.md
```

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
