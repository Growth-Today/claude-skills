# GT LinkedIn Content

A LinkedIn organic content skill for Claude, built by [Growth Today](https://www.growthtoday.co). It turns Claude into a B2B LinkedIn content strategist for founders and GTM leaders: writing scroll-stopping hooks, structuring posts that get saved and shared, choosing the right visual format, timing posts for maximum reach, optimizing your profile as a conversion funnel, and repurposing one idea across many posts.

## Install

```bash
npx skills add Growth-Today/claude-skills/gt-linkedin-content
```

Or copy the `gt-linkedin-content/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Full walkthrough: **https://www.growthtoday.co/claude-skills/gt-linkedin-content**

## What it covers

Ask it anything about LinkedIn organic content and it routes to the right sub-skill:

- **Hooks** — the first 210 characters that decide whether a post gets read; number-led, contrarian, and story hooks with formulas.
- **Storytelling** — post structures and narrative frameworks that hold attention and build trust.
- **Formats** — choosing between single image, infographic, cheat sheet, proof visual, or video; a single-image-first policy and why.
- **CTAs & P.S.** — comment-gates, follow asks, and P.S. sections that convert, matched to funnel stage.
- **Engagement** — the Distribution Window (first 60–90 minutes), comment strategy, and how to build reach.
- **Scheduling** — posting cadence, best-time benchmarks, and the Distribution Window routine.
- **Profile** — optimizing your headline, about, banner, and featured section as a conversion funnel.
- **Repurposing** — getting many posts out of one newsletter, video, or idea.

Plus reference resources: LinkedIn algorithm mechanics, a writing/voice guide, post-structure templates, topic ideas by content pillar, a wording guide, a performance playbook, a designer brief guide, and example post sets to study.

## Structure

```
gt-linkedin-content/
├── SKILL.md                       ← orchestrator (routing + rules)
├── README.md
├── LICENSE
├── .claude/skills/
│   ├── hooks/        storytelling/   formats/      cta/
│   └── engagement/   scheduling/     profile/      repurposing/
└── resources/
    ├── references/   ← algorithm mechanics, content strategy, LinkedIn limits
    ├── performance/  ← performance playbook + wording guide
    ├── templates/    ← ready-to-use post structure templates
    ├── topics/       ← topic ideas by content pillar
    ├── voice/        ← writing voice and tone guide
    ├── design/       ← designer brief guide
    └── posts/        ← example post sets to study (hooks, structure, format)
```

Note: the numbers in the reference data are benchmarks drawn from real B2B GTM content. LinkedIn's algorithm shifts every few months, so treat them as a starting point and always cross-check against your own analytics. Replace any `[X]` placeholder with your own real figures.

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
