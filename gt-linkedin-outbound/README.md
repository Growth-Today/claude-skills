# gt-linkedin-outbound

Growth Today's LinkedIn outbound skill: the full cold-outreach motion, from the connection request to the booked meeting, run either on a rented multi-account engine or a founder-led profile.

## What it is

Call this skill in Claude for anything LinkedIn outbound: connection notes and DMs, post-acceptance sequences, follow-up discipline, persona tone (ATL and BTL), rented-engine infrastructure and account safety, campaign strategy and decay, and the LinkedIn-first GTM case. The master `SKILL.md` resolves its install directory dynamically, then routes each request to one of six sub-skills.

## Structure

```
gt-linkedin-outbound/
├── SKILL.md                         ← master router (Setup + routing + core rules)
├── CHANGELOG.md
├── README.md
├── LICENSE
├── resources/
│   ├── copywriting/     connection-request, connection-notes, copywriting, personalization
│   ├── sequences/       dm-sequence, drip-campaigns, re-engagement, follow-up-system
│   ├── personas/        atl-messaging, btl-messaging
│   ├── infrastructure/  rented-engine
│   ├── strategy/        campaign-strategy, linkedin-first-engine
│   └── knowledge/       linkedin-metrics-benchmarks, heyreach-knowledge-base, lemlist-knowledge-base
└── .claude/skills/
    ├── copywriting/gt-SKILL.md
    ├── sequences/gt-SKILL.md
    ├── personas/gt-SKILL.md
    ├── infrastructure/gt-SKILL.md
    ├── strategy/gt-SKILL.md
    └── knowledge/gt-SKILL.md
```

Each `resources/<group>/` folder holds the full playbooks; the matching `.claude/skills/<group>/gt-SKILL.md` is a lightweight router that indexes its resources and carries the core rules for that domain.

## Install (private repo)

Team members install from the private repo (fork and pull request) or via a shared zip. The hidden `.claude/` folder must ship with the skill. Browser and Finder uploads drop hidden folders, so publish from the terminal and confirm with `git status` that the `.claude/skills/.../gt-SKILL.md` lines are present.

## A note on benchmarks

Benchmark figures in this skill are industry-reported ranges to validate against the account's own data, not Growth Today guarantees. Verify volatile numbers (sending limits, InMail response rates) against official documentation before advising a client.

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Restructured to v2.0.0 by Nikola Siljanoski. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
