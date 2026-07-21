# Claude Skills for Go-To-Market Teams

Open, ready-to-install **Claude Skills** for B2B go-to-market teams — HubSpot, Salesforce, LinkedIn, paid ads, and outbound — built by [Growth Today](https://www.growthtoday.co), an AI-native GTM engineering firm.

Each skill turns Claude into a specialist for a real GTM job: CRM administration, data audits, ad strategy, LinkedIn growth, and outbound. Install one with a single command and Claude uses it automatically when relevant.

## Install

Install any skill with the [skills CLI](https://www.growthtoday.co/claude-skills):

```bash
npx skills add Growth-Today/claude-skills <skill-name>
```

For example:

```bash
npx skills add Growth-Today/claude-skills gt-hubspot-admin
```

Or copy the skill's folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

New to Claude Skills? Full walkthrough: **https://www.growthtoday.co/claude-skills**

## Skills

| Skill | What it does | Learn more |
|---|---|---|
| **gt-hubspot-admin** | HubSpot CRM administration & RevOps — 68 playbooks across data hygiene, data model, pipelines, automation, reporting, and governance | [→](https://www.growthtoday.co/claude-skills/gt-hubspot-admin) |
| **gt-salesforce-admin** | Salesforce org administration, data hygiene, and RevOps maintenance | [→](https://www.growthtoday.co/claude-skills) |
| **gt-data-audit** | B2B contact data audit framework — score your CRM data across 10 dimensions | [→](https://www.growthtoday.co/claude-skills) |
| **gt-google-ads** | B2B Google Ads strategy — search, PMax, negatives, Smart Bidding, wasted-spend audits | [→](https://www.growthtoday.co/claude-skills) |
| **gt-meta-ads** | B2B Meta (Facebook/Instagram) Ads — Advantage+, CAPI, creative, retargeting | [→](https://www.growthtoday.co/claude-skills) |
| **gt-linkedin-ads** | B2B LinkedIn Ads — targeting, bidding, Thought Leader Ads, funnel architecture | [→](https://www.growthtoday.co/claude-skills) |
| **gt-linkedin-outbound** | LinkedIn outbound — DMs, connection requests, sequences, rented-engine setup | [→](https://www.growthtoday.co/claude-skills) |
| **gt-gtm-strategy-advisor** | GTM strategy guidance for B2B go-to-market motions | [→](https://www.growthtoday.co/claude-skills) |

## How Claude Skills work

A skill is a folder with a `SKILL.md` (instructions + metadata) plus optional playbooks and scripts. Once installed, Claude loads a skill automatically when your request matches what it does — no commands to remember. Larger skills (like `gt-hubspot-admin`) use a **multi-sub-skill** structure so Claude loads only the relevant part.

Learn more about Agent Skills in [Anthropic's documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

## About Growth Today

[Growth Today](https://www.growthtoday.co) is an AI-native GTM engineering firm. We build and maintain open Claude Skills for go-to-market teams. More skills and guides: **https://www.growthtoday.co/claude-skills**

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.
