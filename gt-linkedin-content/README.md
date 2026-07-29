# GT LinkedIn Content

A LinkedIn organic content strategist for Claude, built by [Growth Today](https://www.growthtoday.co), an AI-native GTM engineering firm. It turns Claude into a specialist for B2B LinkedIn content: hooks, post structure, formats, CTAs, engagement, posting cadence, profile optimization, repurposing, post production, and design briefs, grounded in what actually works for GTM audiences.

## Install

Add it to your project with the [skills CLI](https://www.growthtoday.co/claude-skills):

```bash
npx skills add Growth-Today/claude-skills/gt-linkedin-content
```

Or copy the `gt-linkedin-content/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

New to Claude Skills? Full walkthrough: **https://www.growthtoday.co/claude-skills**

## What it does

Trigger it with any LinkedIn organic-content intent: "write a LinkedIn post", "fix this hook", "what format should this be", "best time to post", "write a P.S. / comment-gate", "optimize my LinkedIn profile", "repurpose this post", or "turn this into a design brief". The master skill classifies the funnel stage (top, middle, bottom), routes to the right sub-skill, and returns a structured post with a hook, body, CTA, format, and posting guidance.

It is a multi-sub-skill skill, so Claude loads only the relevant part:

- **hooks** first lines and openers that earn the click
- **storytelling** post body structure and narrative frameworks
- **formats** single image, carousel, video, poll, and format specs
- **scheduling** posting times, cadence, and the distribution window
- **engagement** comments, engagement weights, and community building
- **cta** end-of-post CTAs, P.S. types, and comment-gates
- **profile** headline, banner, about, and featured optimization
- **repurposing** turning one post into many formats
- **post-production** producing and fixing the parts of a locked post (hook, body, CTA, comments, alt text)
- **design-briefer** turning a post into a design brief for your design tool

Not for LinkedIn Ads (use `gt-linkedin-ads`) or cold outreach (use `gt-linkedin-outbound`).

## Structure

```
gt-linkedin-content/
├── SKILL.md                    ← orchestrator (auto-loaded by Claude)
├── README.md                   ← this file
├── LICENSE                     ← MIT
├── .claude/skills/             ← sub-skills, loaded on demand
│   ├── hooks/ storytelling/ formats/ scheduling/
│   ├── engagement/ cta/ profile/ repurposing/
│   └── post-production/ design-briefer/
└── resources/                  ← loaded on-demand
    ├── writing/                ← voice, content strategy, post templates
    ├── performance/            ← what wins, scorecard, winning words
    ├── platform/               ← algorithm mechanics
    ├── design/                 ← general design-family vocabulary
    ├── social-selling/         ← converting the audience your content builds
    └── posts/                  ← annotated example posts
```

## Work with us

Growth Today runs LinkedIn content as a service for B2B GTM teams. If you want the engine behind this skill run for you, more open skills and guides are at **https://www.growthtoday.co/claude-skills**.

## License

MIT, see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co), an AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
