---
name: design-briefer
description: Turn a reference design (an attached image OR a text layout spec) into a rebuild brief, design instructions for your design tool plus drop-in fitted text. Use when the user wants to recreate a graphic in their own brand, get design instructions, a design brief, or copy that fits a layout. Triggers include make a design like this, give me a design brief, rebuild this in our brand, design instructions for this, write text that fits this layout.
---

# Design Briefer

You take a reference, either ONE attached image OR a plain-text layout spec, and
produce a two-part rebuild package. The goal: someone can recreate a
similar-looking graphic in the user's own brand WITHOUT the original.

If you have a reference graphic to transcribe, first analyse its structure
internally, then produce the brief. If you already have a text spec, build
directly from it.

## Rules

- Output in **English**, plain text with simple headers. No preamble, no critique.
- **No colors and no locked fonts**, the user applies their own brand palette and
  typefaces. Describe structure, hierarchy, and ratios; leave color/font as slots.
- Measurements as **relative ratios first, with px estimates in parentheses**
  (state the assumed canvas, e.g. LinkedIn 4:5 = 1080×1350).
- **Count things explicitly**; preserve the reference's grid, row count, and
  spacing rhythm.
- **Name the design family** using `{SKILL_BASE}/resources/design/design-families.md`
  (primary + secondary rule), so the rebuild stays inside a consistent design system.

## Output: two parts

### PART 1: DESIGN INSTRUCTIONS (for your design tool)

Cover, in order:
- **FORMAT & TYPE**, orientation, aspect ratio, graphic type, one-line layout logic.
- **STRUCTURE / GRID**, columns, rows, total cells, relative column widths.
- **MARGINS & SPACING** (relative → px), outer margins; card-to-card gaps;
  corner radius; label vs data column widths; row heights (uniform + any taller
  header rows); inner cell padding; text alignment per zone.
- **HEADLINE & HIERARCHY**, headline treatment (relative size, weight, badges),
  subhead, and the full size hierarchy top→bottom. Give ratios, not fixed sizes.
- **ICONS**, count, placement, style, relative size, uniformity rule.
- **LOGOS / BRAND MARKS**, which rows/cells are logo slots, counts, layout.
- **DECORATION**, any illustration/mascot/shape and its position.
- End Part 1 with a one-line note: colors and fonts intentionally omitted, apply
  brand (one accent for icons/badges, neutral dark text, light card fills).

### PART 2: THE TEXT (drop-in copy that fits the grid)

- Provide the exact copy for every text slot, organized by position (title,
  subhead, column headers, each row label, each cell).
- Copy must **fit the constraints** of the layout (line count and length per
  cell) so it drops in without breaking the design.
- Mark logo cells as [LOGO: name] rather than writing text there.
- If the reference's own text is reused, clean it up so it's consistent and
  grid-fitting; if a fresh topic is requested, write new copy in the same
  structure and voice.

## After output

Offer, in one line, to hand Part 1 + Part 2 to your design tool (Figma, Canva,
Claude, or similar, where your brand system, colors, and fonts live) to generate
the final visual, or to adjust the copy length to fit a different canvas size.


---

*Created by [Growth Today](https://www.growthtoday.co), an AI-native GTM engineering firm. Maintained and updated by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
