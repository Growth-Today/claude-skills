# Cold Email Writer

B2B cold email strategy skill: an orchestrator that routes each request to the right sub-skill and layers on cross-cutting deliverability and tooling guidance. Infrastructure work (domains, DNS, warmup) hands off to [`../email-infra/`](../email-infra/).

| | |
|---|---|
| **What it does** | Writes and structures cold outbound: first-touch and follow-up emails, re-engagement, subject lines, personalization at scale, ATL/BTL persona messaging, and named copywriting frameworks. |
| **Use it when** | The request is about cold email, an email sequence, a follow-up or breakup email, a subject line, personalization / Clay first lines, exec (ATL) vs IC (BTL) messaging, copywriting frameworks, or sequencing tools (Instantly, Smartlead, Lemlist). Not for marketing emails or newsletters. |
| **Outputs** | Ready-to-send email copy, multi-step sequences, subject-line sets, and personalization prompts, plus a quick deliverability reference. |
| **Entry point** | [`SKILL.md`](SKILL.md) - orchestrator with the routing table and cross-cutting deliverability rules. |

## Resource groups

| Folder | Holds |
|---|---|
| `resources/sub-skills/` | The routed plays: first-touch, follow-up, re-engagement, subject-lines, personalization, atl/btl-messaging, copywriting |
| `resources/messaging/` | Deep copywriting: frameworks, principles, sequences, e-com playbook, the GT playbook, spam checker |
| `resources/templates/` | Email template library and campaign playbooks |
| `resources/prompts/` | Personalization prompts |
| `resources/reference/` | Email metrics benchmarks and sequencing-tool reference |
