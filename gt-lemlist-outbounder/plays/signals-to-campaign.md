---
name: signals-to-campaign
description: Turning a buying signal into a launched Lemlist multichannel campaign via watch lists and generate_campaign_for_watch_list. Read when a signal or intent trigger should become live outreach. Ends with the MCP hand-off and the launch gate.
---

# Signals to campaign — from a trigger to a launched touch

The strongest Lemlist campaigns start from a **signal**, not a static list. Lemlist's watch lists monitor for a trigger (a job change, a hiring move, a funding event, a tech-stack shift) and can generate a campaign directly from the leads that match. This play is the GT judgment about which signals are worth acting on and how the resulting outreach should be shaped.

## Which signals are worth a campaign

- **Specific and recent.** "Hired a VP of Sales last week" beats "is a mid-size SaaS company." The tighter and fresher the signal, the more relevant the opener and the higher the reply rate.
- **Actionable.** The signal must map to a real reason to reach out *now* — a problem your offer touches, freshly true for this account.
- **Stackable.** Two signals on the same account (funding + hiring) is a stronger trigger than either alone. Prefer multi-signal watch lists where you can.

For sourcing and scoring signals themselves, cross to `gt-buying-signal-sourcer` — this play is about turning a sourced signal into Lemlist outreach.

## From signal to sequence

1. **Define the watch list** around the signal — the tighter the filter, the better the downstream copy.
2. **Let the trigger populate leads** as accounts match, rather than a one-time static import.
3. **Shape the campaign around the signal.** The first touch names the reason (see `personalization.md`); the cadence interleaves channels (see `sequence-design.md`).
4. **Gate before launch.** A signal-triggered campaign still clears `readiness-checklist.md` — a fresh trigger is not a reason to skip QA.

## Why signal-led outperforms

Signal-anchored outreach lands because it's relevant and timely: the message references something true and recent about the account. Expect materially higher reply rates than a generic list — but only if the copy actually uses the signal instead of burying it under a template.

## Execution (hand off to the Lemlist MCP)

```
list_watch_list_library → list_watch_list_filters      (see available signals)
suggest_watch_lists                                    (GT picks the worthwhile ones)
create_watch_list                                      (define the trigger — human-gated)
find_watch_list_linkedin_urls                          (resolve matched leads)
generate_campaign_for_watch_list                       (draft the campaign from the signal)
→ shape it via sequence-design.md + personalization.md →
→ run readiness-checklist.md → validate_campaign_readiness →
(on explicit human go) launch_campaign
```

`create_watch_list`, `generate_campaign_for_watch_list`, and `launch_campaign` are all writes/launches — stage, show, wait for the explicit human go.
