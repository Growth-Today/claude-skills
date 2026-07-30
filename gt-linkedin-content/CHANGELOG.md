# Changelog

Notable changes to the `gt-linkedin-content` skill.

## [2.1.4] - 2026-07-30

### Added
- design-families: fill-in-the-bracket brief templates (single graphic, carousel,
  motion graphic), a match-the-format-to-the-content table, and build rules for
  carousels and single graphics. The catalog now feeds the design-briefer sub-skill,
  which references it for family naming.

## [2.1.3] - 2026-07-30

### Changed
- engagement-scorecard: reformatted for scannability, one-line intro, short how-to-score,
  comment-gate, and tiering; per-author key metrics + tier breakdown + hooks ranked +
  character length + top-performing patterns as Pattern 1/2/3 with bulleted hook,
  structure, and engagement; added a combined Untapped opportunities section, the
  engagement multiplier, and a reference block.

## [2.1.2] - 2026-07-30

### Added
- cta: an at-a-glance CTA effect table (comment lift vs no-CTA, median comments,
  avg engagement, best-for), matching the format and hook at-a-glance tables.

## [2.1.1] - 2026-07-30

### Added
- formats: an at-a-glance "design format effect" table (reach multiplier vs
  text-only, avg engagement, best-for). hooks: an at-a-glance "hook effect" table
  (reach multiplier, C/R ratio, avg engagement, best-for), so hook choice can be
  read by both reach and discussion in one view.

## [2.1.0] - 2026-07-30

### Added
- Benchmarks are now broken down by follower band (<2k, 2-5k, 5-10k, 10-20k,
  20-50k, 50k+), from ~8,900 original GTM posts across 233 creators whose follower
  counts were captured. performance-playbook: baseline per band (reactions,
  comments, comment/reaction ratio, reactions per 1k followers), percentile tiers
  (typical/strong/top/breakout), and format, CTA, hook, and length each by band,
  plus a three-tier "what to do by size" summary. cta, hooks, and formats each get
  their by-band table; algorithm gets a volatile-tail and per-follower-dilution note.
- Key findings: engagement per follower falls ~7x from smallest to largest while
  comments climb faster than reactions; the comment-gate only pays at ~10k+ and
  dominates at 20k+; length interacts with size (small tight, large long); carousel
  over-performs the typical post; video is weaker in GTM than broad-market benchmarks.

## [2.0.4] - 2026-07-30

### Changed
- engagement-scorecard: added key metrics, character length, and top-performing
  patterns (hook, structure, engagement) for Brigi (23K) and Jani (13K) as worked
  showcase examples.
- algorithm: named the four ranking stages (content quality filter, initial
  distribution, engagement scoring, extended distribution), made content velocity
  explicit, and added a content-type-to-format mapping plus a format-fatigue note.
- content-strategy: first-line strategies and curiosity-gap techniques are now tables.
- writing-guide: the weekly plan is now bulleted, and @tagging is reframed from
  mandatory to a deliberate, engage-likely recommendation (master output note aligned).

## [2.0.3] - 2026-07-30

### Added
- storytelling sub-skill: a "Core Frameworks" section (AIDA, PAS, BAB,
  Mistake-to-Lesson, Contrarian) with a coded structure and a when-to-reach-for-it
  line each, mapped to the six formulas. Reformatted the worked examples as
  structure-first, then a fenced code block.

## [2.0.2] - 2026-07-30

### Added
- hooks sub-skill: a "Growth Today Hook Types (Battle-Tested on Real Posts)" section,
  six hook types shown as structure-then-example code templates, plus a first-line
  openers list and a curiosity-gap list. Output now returns 6 to 8 opener options.

## [2.0.1] - 2026-07-30

### Changed
- engagement sub-skill: restored the engagement-weight table (saves, comments,
  shares, likes, and their relative value), gave dwell time its own section with a
  short how-to-earn-it list, and moved the engagement-pods guidance into bullets.

## [2.0.0] - 2026-07-29

### Added
- **post-production** sub-skill: produce and fix the parts of a post (hook, body,
  team body copy, P.S./CTA, auto-scheduled comments, alt text, formatting), with
  adaptable starter prompts.
- **design-briefer** sub-skill: turn a post into a design brief for your design
  tool of choice (Figma, Canva, Claude, or similar).

### Changed
- Refreshed and re-audited every sub-skill and resource, corrected the data-backed
  claims, and applied a consistent writing standard (plain, human tone).
