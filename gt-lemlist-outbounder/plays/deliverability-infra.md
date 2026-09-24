---
name: deliverability-infra
description: How the Lemlist skill handles deliverability and email infrastructure — a pointer to gt-email-infra for doctrine, plus the Lemlist infra tools that check and act on state. Read when a Lemlist campaign has a deliverability or domain question.
---

# Deliverability & infra — doctrine elsewhere, checks here

**The doctrine lives in `gt-email-infra`.** SPF/DKIM/DMARC design, how many domains and mailboxes, warmup schedules, blacklist recovery, bounce root-cause — all of that is `gt-email-infra`'s job, and this play does not restate it. What this play does: use Lemlist's own infra tools to *check the state* of the email channel and act on it inside Lemlist.

## The split

| Question | Where it's answered |
|---|---|
| How do I set up domains / DNS / warmup correctly? | `gt-email-infra` (doctrine) |
| Are *these* Lemlist domains and mailboxes actually healthy right now? | this play, via the MCP |
| Why is deliverability doctrine what it is? | `gt-email-infra` |
| Is *this* campaign about to land in spam? | this play, via the audit tools |

If the request is "how should infra be built," route to `gt-email-infra`. If it's "check whether this Lemlist setup is sound before we send," stay here.

## What to check inside Lemlist

- **Domains authenticated.** SPF/DKIM/DMARC passing on every sending domain; tracking domain live.
- **Mailboxes warmed and within caps.** Warmup complete; daily send volume inside safe limits.
- **Inbox placement.** Where do sends actually land — inbox, promotions, spam?
- **Audit before scale.** Run the deliverability audit before increasing volume, not after replies drop.

## Benchmarks (for triage, not doctrine)

- Bounce rate under 2%; above that, pause and diagnose (root-cause is a `gt-email-infra` job).
- Keep per-mailbox daily volume within warmup-appropriate caps — don't let a campaign push a cold mailbox.

## Execution (hand off to the Lemlist MCP)

```
list_domains → check_domain_health → get_domain_dns    (authentication state)
list_mailboxes                                         (warmup + caps)
run_deliverability_audit                               (overall health)
run_inbox_placement_test → get_inbox_placement_result  (where sends land)
→ if doctrine or a real setup change is needed, route to gt-email-infra
→ if healthy, proceed to readiness-checklist.md
```

These are all reads/diagnostics and run freely. Any actual DNS or mailbox change is a `gt-email-infra`-doctrine decision and a human-gated write.
