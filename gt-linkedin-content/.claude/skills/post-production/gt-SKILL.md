---
name: post-production
description: Turn a locked LinkedIn topic into publish-ready parts, element by element. Use when the user has a validated post and needs the hook, body copy, team body copy, P.S. or CTA, auto-scheduled comments, alt text, or formatting produced or fixed. Prompts work inside this skill or pasted into any AI writing tool. Do NOT use to decide what to post or to design the visual (use formats then your design tool).
---

# Post Production

You take a topic that is already validated and locked, and produce the parts of the post that are not the design: hook, body copy, team body copy, P.S. / CTA, auto-scheduled comments, alt text, and the final formatting pass. Your job is to get each part close to publish-ready so that expert review shrinks over time.

This file is the operator. The starter prompts below are self-contained: run them inside this skill, or paste any one straight into your social scheduling/posting tool or another AI writing tool and adapt it to your brand.

## What this is and is not

- It IS the last mile: given a locked post and a chosen element, produce or fix that element.
- It is NOT the planner (deciding what to post) and NOT the designer (use `formats` then your design tool for the visual).

## Where the prompts run

The prompts work in two ways, use whichever suits you:

- **Inside this skill:** fuller context, can pull the post-reference resources and web-search to validate numbers. Use for depth, benchmarking, and number validation.
- **Pasted into any AI writing tool or your social scheduling/posting tool:** lean and self-contained. Keep the essential voice rules with the prompt when you paste it out, since the external tool cannot load this skill.

## One core insight carries through

Every locked post has one core insight (a single central idea). Feed it into every element that carries an insight (body, comments, alt text). Do not regenerate or reinterpret it per element, carry the one insight so all parts stay on the same point.

## Elements

Each element below is a self-contained job. Produce the matching one, and ask for the failure mode when fixing.

- **Full first draft:** turn a locked topic plus core insight into a complete draft (pick a template from post-templates.md). The entry point before per-element fixing.
- **Hook:** generate (own patterns, benchmark table with results), validate the numbers, or fix a specific weakness (too theoretical, not data-backed, too complex, too boring).
- **Body copy:** the team body copy template (tiered, see below), a rewrite in a named poster's voice, plus the de-AI rewrite passes for any draft that reads as constructed.
- **P.S. / CTA:** generate 3 options matched to funnel stage using the three P.S. types, or fix a weak CTA. For BoF use the comment-gate.
- **Pinned first comment:** the author's own first comment, where the external link goes (links in the body cut reach). Different from the auto-scheduled comments.
- **Comments:** auto-scheduled engagement comments, always carrying the core insight and a reader persona, in typed buckets. This element stays human-reviewed longest, say so.
- **Alt text:** short, structured, tool names as keywords.
- **Formatting:** a plain-text LinkedIn pass (line breaks and spacing only, no wording change).
- **Pre-publish grade:** run the engagement scorecard on the draft for a go / no-go before shipping.
- **Repurpose:** re-run a winner with a new hook and angle.

When run inside this skill, ground the work in the resources that support it: the post-reference data, winning-words.md, post-templates.md, engagement-scorecard.md, and algorithm.md.

## Starter prompts (adapt these in your own tools)

These are short, generic starting points. Copy one, fill the slots, and adjust the voice rules to your brand.

**Hook fix (too theoretical):**
```
Here is a LinkedIn hook that reads as too theoretical: [HOOK].
The post's core insight is: [INSIGHT].
Rewrite it 3 ways. Each version must lead with one specific, verified
number, stay under 15 words, use no emoji, and name the concrete outcome
a reader gets. Keep my voice plain and direct.
```

**De-AI body rewrite:**
```
Rewrite the body copy below so it stops reading as AI-generated: [BODY].
Cut hedging and filler, vary sentence length, remove symmetrical
"not just X but Y" constructions and buzzwords, and keep one core
insight ([INSIGHT]) as the through-line. Return plain text with short
lines and blank lines between sentences. Do not change the facts.
```

**Auto-scheduled comments:**
```
Generate [N] engagement comments for a LinkedIn post whose core insight
is: [INSIGHT], written for this reader persona: [PERSONA].
Sort them into buckets: a question, a personal experience, and a
contrarian take. Each comment is 15+ words, adds a real point, and ends
in a way that invites a reply. No emojis. I will review before scheduling.
```

## Tiering the body copy (by poster)

- **Named voices (for example Brigi and Jani), the bar** write their own body in their own voice, skill- or tool-assisted.
- **The rest of the team** gets the team body copy template with a forced personal layer (`[YOUR TAKE]`, `[SWAP TOOLS]`), so posts stay varied and carry each person's point of view. Everyone posting identical copy is repetitive across profiles and hurts results.

## The de-risk ladder

Set honest expectations. Alt text and hook generation are nearly review-free. P.S. / CTA and body de-AI passes are getting there. Auto-scheduled comments and the named voices' final body copy stay human-touched longest. Every element climbs the ladder over time through the feedback loop.

## The feedback loop (say this when the user rewrites your output)

When an expert has to push back and rewrite, ask whether the fix is post-specific or a pattern. If it is a pattern, update the relevant starter prompt or the rule in the owning sub-skill (`hooks`, `cta`, `engagement`, `writing-guide.md`). That is how expert review shrinks over time.

## Examples

**Example 1, fix a hook.** User: "this hook is too theoretical." Use the hook-fix starter prompt, return 3 rewrites that carry the solution and lead with a verified number.

**Example 2, team copy.** User: "make a team version of Brigi's locked post." Produce the team body copy template with `[HOOK]`, `[YOUR TAKE]`, `[SWAP TOOLS]` and the comment-gate P.S., with the "make it yours" note on top.

**Example 3, comments.** User: "generate 20 comments." Ask for the core insight and the reader persona, use the comments starter prompt in typed buckets, and remind the user to review before scheduling.

---

*Created by [Growth Today](https://www.growthtoday.co), an AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
