---
name: readiness-checklist
description: GT's pre-launch QA gate for a Lemlist campaign. Read before any campaign goes live. Walk the checklist, then call validate_campaign_readiness, then launch only on an explicit human go.
---

# Pre-launch readiness checklist

No Lemlist campaign launches until it clears this gate. The gate is GT's judgment layer; `validate_campaign_readiness` is Lemlist's automated check. Run both, in that order, then wait for a human to say go.

## The gate (GT checks, before the MCP check)

Walk each item. If any fails, fix it before proceeding — do not launch around a red item.

1. **Deliverability set.** SPF/DKIM/DMARC pass on every sending domain; custom tracking domain live. Confirm state with `list_domains` and `run_deliverability_audit`. Doctrine lives in `gt-email-infra` — this is a check, not a setup.
2. **Domains warmed.** Sending mailboxes have completed warmup and are inside daily send caps. Confirm with `list_mailboxes`. New domains that skipped warmup do not launch.
3. **List verified.** 100% of email addresses verified; bounces removed before send, not during. Duplicates and existing customers/opt-outs suppressed.
4. **Sequence reviewed.** Every step read end to end: copy approved, condition branches correct, channel steps (email / LinkedIn / call) in the intended order, spacing sane. Preview against a real lead.
5. **Unsubscribe handling.** Opt-out present and working; suppression list applied. Confirm with `get_unsubscribes`. This is non-negotiable and a compliance item.
6. **Sender rotation.** Senders assigned and rotation strategy set so no single mailbox is overloaded. Confirm with the sender tools.

## Quick reference — launch thresholds

| Item | Must be true before launch |
|---|---|
| Domains authenticated | SPF + DKIM + DMARC all pass |
| Warmup | Complete on every sending mailbox |
| Email verification | 100% verified, bounces pre-removed |
| Suppression | Opt-outs + existing customers excluded |
| Sequence | Every step reviewed, branches correct |
| Sender load | Rotation set, within per-mailbox caps |

## Execution (hand off to the Lemlist MCP)

Run in order. Stop at the gate.

```
get_campaign_details → get_campaign_sequences   (read the campaign as built)
list_domains → run_deliverability_audit         (deliverability state)
list_mailboxes                                  (warmup + caps)
get_unsubscribes                                (suppression working)
preview_email / preview_sequence_update         (see it as a lead would)
validate_campaign_readiness                     (Lemlist's automated gate)
→ present findings to the human →
(on explicit "go") launch_campaign
```

If `validate_campaign_readiness` returns any blocker, do not launch — report it, fix, re-validate. The human go is required even when every check is green.
