# GT Email Infrastructure

A cold email infrastructure and deliverability skill for Claude, built by [Growth Today](https://www.growthtoday.co). Covers the full lifecycle: sizing your infrastructure, ideating and buying domains, DNS setup (MX/SPF/DKIM/DMARC), warmup, going live, monitoring, automated inbox management at scale, and diagnosing bounces and blacklists down to the root cause.

## Install

```bash
npx skills add Growth-Today/claude-skills/gt-email-infra
```

Or copy the `gt-email-infra/` folder into your project's `.claude/skills/` (or `~/.claude/skills/` for global use).

Full walkthrough: **https://www.growthtoday.co/claude-skills/gt-email-infra**

## What it covers

Ask it anything about cold email infrastructure and it routes to the right resource:

- **Sizing & setup** — how many domains and mailboxes for your volume goal, naming patterns, registrars, Google Workspace + Microsoft 365 provisioning, DNS records.
- **Domain research** — ideating on-brand domains and avoiding spam-trap naming patterns.
- **Warmup & going live** — warmup timelines, ramp schedules, send limits per provider.
- **Deliverability & compliance** — SPF/DKIM/DMARC, inbox placement, CAN-SPAM/GDPR.
- **Automation at scale** — how to run inbox classification, tagging, campaign routing, blacklist monitoring, and reporting automatically across many inboxes and workspaces.
- **Bounce & blacklist auditing** — find where a bounce actually comes from: categorize bounces, read soft vs hard SMTP codes, and trace the root cause to infrastructure, list/data, or copy.

## Structure

```
gt-email-infra/
├── SKILL.md                            ← orchestrator (routing + critical rules + sizing formula)
├── README.md
├── LICENSE
└── resources/
    ├── email-infra-guide.md            ← complete setup guide
    ├── email-infra-step-by-step.md     ← step-by-step walkthrough
    ├── email-infra-troubleshooting.md  ← diagnosis (DNS, warmup, blacklist)
    ├── deliverability-guide.md         ← deliverability concepts + compliance
    ├── email-infra-reference.md        ← all numbers, limits, benchmarks, bounce codes
    ├── domain-research.md              ← domain ideation and naming rules
    ├── email-infra-automation.md       ← automated inbox management at scale
    └── blacklist-bounce-audit.md       ← bounce/blacklist root-cause diagnosis
```

Note: GT runs this on EmailBison as the sending platform. The automation and audit workflows reference EmailBison specifics as a worked example — the concepts, thresholds, and diagnostics apply to any ESP; adapt the tool-specific steps to your own stack.

## License

MIT — see [LICENSE](LICENSE). Free to use, copy, and adapt.

---

Created by [Growth Today](https://www.growthtoday.co) — AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills
