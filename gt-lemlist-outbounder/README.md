# Lemlist Outbounder

Strategy and advisory layer for multichannel outbound in Lemlist (email + LinkedIn + calls in one sequence). It supplies the judgment; the connected official Lemlist MCP performs the actions.

| | |
|---|---|
| **What it does** | Decides whether Lemlist multichannel is the right motion at all, shapes the cadence, sets personalization standards (AI variables, snippets, voice profiles), wires buying signals / watch lists to a campaign, and runs the pre-launch QA gate - then names the exact MCP tools, in order, to execute. |
| **Use it when** | Planning or running a Lemlist campaign, choosing multichannel vs email-only vs LinkedIn-only, designing a cadence, personalizing at scale, turning a watch list into a campaign, or QA-ing before launch. Not for email-only strategy (use `cold-email-writer`), LinkedIn-only (use `linkedin-outbounder`), or deliverability doctrine (use `email-infra`). |
| **Outputs** | A channel-fit decision, a staged cadence/campaign plan, and the MCP tool run-order. Every write and launch waits for an explicit human yes (GT publishing gate). |
| **Entry point** | [`SKILL.md`](SKILL.md) - the strategist: channel-fit decision table, play router, core rules, and the human gate. |

## Resource groups

| Location | Holds |
|---|---|
| `plays/` | The routed plays: channel-strategy, sequence-design, personalization, deliverability-infra, signals-to-campaign |
| `resources/` | MCP handoff (connection, tool groups, rate limit) and the pre-launch readiness checklist |

If the Lemlist MCP is not connected, the skill can still advise and stage plans but cannot execute - connecting it is an admin connector-approval step at `app.lemlist.com/mcp`.
