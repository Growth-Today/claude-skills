---
name: personalization
description: GT copy and personalization standards mapped to Lemlist's AI variables, snippets, and voice profiles. Read when personalizing a sequence at scale. Defers copy mechanics to Lemlist's own load_skill copywriting advisory.
---

# Personalization — GT standards on Lemlist's rails

Lemlist gives you the machinery: AI variables, snippets, voice profiles. This play is the GT judgment about *what good personalization is* so the machinery produces replies, not obviously-templated filler.

## GT standards (what "personalized" actually means)

- **Relevance over mail-merge.** `{{firstName}}` is not personalization. A specific, true reason this message is landing in this inbox now is.
- **One earned observation, then the point.** Lead with something real about their world; don't stack three "I noticed" lines.
- **No flattery openers.** "Loved your post", "impressive growth" lower reply rate — they read as automation.
- **Written to be read aloud.** If it doesn't sound like something a person would say, cut it.
- **Signal-led beats generic.** Personalization anchored to a buying signal (see `signals-to-campaign.md`) outperforms generic first lines by a wide margin.

## Mapping to Lemlist features

| Lemlist feature | Use it for | GT rule |
|---|---|---|
| **AI variables** | generating a personalized line per lead at scale | The prompt must reference a real data field, not invent facts. Verify a sample before trusting the batch. |
| **Snippets** | reusable, approved copy blocks | Keep a snippet library of GT-approved angles so quality is consistent across senders. |
| **Voice profiles** | matching tone to persona / sender | Pick the profile that matches the prospect's own register — formal to formal, casual to casual. |

## Guardrails on AI variables

- **Spot-check before scale.** Generate for a handful of leads with `personalize_step_for_lead`, read them as a human, then run the batch.
- **Fail closed.** If the data field is missing, the AI variable should fall back to a safe generic line, never a hallucinated one.
- **Keep it short.** One personalized sentence beats a personalized paragraph.

For the exact prompt syntax and product mechanics of AI variables, call Lemlist's `load_skill` copywriting advisory. For GT's email copy frameworks, cross to `gt-cold-email-writer`; for LinkedIn step craft, `gt-linkedin-outbounder`.

## Execution (hand off to the Lemlist MCP)

```
get_ai_variable_prompts → list_snippets → list_voice_profiles   (see what exists)
create_ai_variable_prompt / update_ai_variable_prompt           (stage the prompt — human-gated)
personalize_step_for_lead                                       (spot-check on real leads)
→ read the samples with a human →
(on go) apply across the campaign, then readiness-checklist.md
```

Every prompt create/update and any apply-at-scale is a write — spot-check, show, wait for the human go.
