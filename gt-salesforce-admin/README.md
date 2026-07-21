# GT Salesforce Admin

A comprehensive Salesforce CRM administration skill for Claude, built by [Growth Today](https://www.growthtoday.co). A master router orchestrates **52 playbooks across 8 sub-skills** covering audit, data hygiene, data model, segmentation, opportunities & sales, automation (Flow), reporting, security & access, and governance/integrations.

## Install

```bash
npx skills add Growth-Today/claude-skills gt-salesforce-admin
```

Or copy the `gt-salesforce-admin/` folder into your `.claude/skills/`. Walkthrough: **https://www.growthtoday.co/claude-skills/gt-salesforce-admin**

## Structure

```
gt-salesforce-admin/
├── SKILL.md                 ← master router (auto-loaded)
├── .claude/skills/          ← 8 sub-skills, each a gt-SKILL.md router
│   ├── sf-data-hygiene/ · sf-data-model/ · sf-segmentation/
│   ├── sf-opportunities-sales/ · sf-automation-flow/ · sf-reporting/
│   └── sf-security-access/ · sf-governance-integrations/
├── playbooks/               ← 52 playbooks (shared; sub-skills route to them)
├── requirements.txt · .env.example · README.md · LICENSE
```

## Coverage — 52 playbooks across 8 sub-skills

| Sub-skill | Playbooks |
|---|---|
| sf-data-hygiene | 13 |
| sf-data-model | 6 |
| sf-segmentation | 5 |
| sf-opportunities-sales | 7 |
| sf-automation-flow | 5 |
| sf-reporting | 3 |
| sf-security-access | 3 |
| sf-governance-integrations | 6 |
| Cross-cutting (audit, implementation plan, weekly & quarterly) | 4 |

## Safety

Scripts read Salesforce credentials from `.env` (`SF_USERNAME/PASSWORD/SECURITY_TOKEN/DOMAIN`) — no credentials stored in the skill. Export a backup before destructive operations (Recycle Bin is ~15 days).

## License

MIT — see [LICENSE](LICENSE).

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
