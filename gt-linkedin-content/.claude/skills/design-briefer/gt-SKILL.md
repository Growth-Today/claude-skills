---
name: design-briefer
description: Turn a LinkedIn post into a clear, brand-agnostic design brief for a designer or a design tool. Use when the user wants a design brief for a post, instructions for the visual, or copy that fits the layout. Triggers include give me a design brief, brief the visual for this post, what should the graphic look like, write the visual copy. Do NOT use to pick the format (use formats) or to write the post body (use storytelling).
---

# Design Briefer

You turn a LinkedIn post (or a topic and its key point) into a clear, brand-agnostic design brief: what the visual should say, how it should be structured, and the exact copy that fits. The goal is a brief a designer or a design tool can execute in any brand.

## Rules

- Output in **English**, plain text, simple headers, no preamble.
- **Brand-agnostic.** Describe structure, hierarchy, and layout. Leave colors and fonts as slots for the user's own brand (one accent, neutral text, light fills). Do not prescribe a specific look.
- Give sizes as **relative hierarchy** (biggest, medium, small), not fixed pixels. Assume LinkedIn 4:5 (1080x1350) unless told otherwise.
- **One idea per visual.** The graphic carries a single message and must read at thumbnail size.

## Output: two parts

### PART 1: DESIGN BRIEF

- **Goal + funnel stage.** What the visual is for: reach (ToF), proof or teaching (MoF), or save-bait or an offer (BoF).
- **The one message.** The single point or number the visual must land. This is the visual headline, lead with a number where you can.
- **Format and family.** The visual type that fits as a single image: dense infographic, two-column comparison, single hero stat, step or tool map, or cheat sheet. Name the design family from `{SKILL_BASE}/resources/design/design-families.md` so the visual stays recognizable and consistent.
- **Structure.** A simple layout suggestion with a count: title plus 3 to 5 rows, two-column before and after, one hero stat with 3 supporting points, and so on.
- **Hierarchy.** What is biggest (the headline or number), what is secondary, what is small.
- **Must-include.** A logo slot, one accent for emphasis, and any icons or labels the content needs. Keep repeated elements uniform.
- **Brand note.** Colors and fonts left as slots, the user applies their own brand.

### PART 2: THE COPY (fits the layout)

- Provide the exact text for every slot: headline, subhead, each row or section label, each value.
- Keep each piece short enough to fit (line count and length per slot) so it drops in without breaking the layout.
- Mark logo slots as [LOGO].
- Write in the user's voice, one idea per line, no filler.

## After output

Offer, in one line, to hand the brief and copy to the user's design tool (Figma, Canva, Claude, or similar, where their brand system, colors, and fonts live) to generate the final visual, or to tighten the copy for a different canvas size.

---

*Created by [Growth Today](https://www.growthtoday.co), an AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
