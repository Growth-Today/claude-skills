# Changelog

All notable changes to the `gt-linkedin-outbound` skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/); versions use
[SemVer](https://semver.org/) (patch = fix, minor = additive, major = breaking
layout/restructure).

## [2.0.0] - 2026-08-07

Major restructure into a router plus six sub-skills. Restructured by Nikola Siljanoski.

### Added
- CHANGELOG.md: this file, bringing the skill in line with the rest of the
  Growth Today library (every other skill carries one). Seeded with the v1.0.0
  history from the inline changelog block in SKILL.md.
- Six sub-skill routers under `.claude/skills/<group>/gt-SKILL.md`: copywriting,
  sequences, personas, infrastructure, strategy, knowledge. Each carries its own
  name, description with "Do NOT use" redirects, resource index, and the core
  rules for its domain.
- README.md and LICENSE (MIT, Growth Today), which the deployed copy had dropped.
  README documents the new grouped structure and the install note.
- .gitignore for the skill folder (ignores `.DS_Store`, other OS noise, and
  packaged `*.zip`/`*.skill` build artifacts) so they never get committed.
- resources/knowledge/lemlist-knowledge-base.md: the dedicated multi-channel
  reference, built on the same structure as the HeyReach knowledge base and
  sourced from the internal sequencing SOP. Covers Lemlist's role, the
  multi-channel coordination rules, and a "when Lemlist vs when HeyReach" guide.
  The knowledge router now reads it.

### Changed
- Restructured the 15 flat `resources/*.md` files into six topic folders
  (copywriting, sequences, personas, infrastructure, strategy, knowledge),
  mirroring `gt-linkedin-content`. Resource files stay shared at the top level
  under `resources/<group>/`; only the routers live under `.claude/` (SOP ref 3).
- Master SKILL.md: added the dynamic `SKILL_BASE` Setup block, converted the
  routing table, routing logic, and decision tree to route to the six group
  routers, updated all resource paths to `{SKILL_BASE}/resources/<group>/...`,
  and replaced the inline changelog block with a pointer to this file.
- Fixed a pre-existing defect: every resource file's internal "see also" links
  pointed at a `copywriting/examples/...` + `personalization/...` folder scheme
  that never existed in the flat v1 layout (so the cross-links were all dead).
  Remapped every one to its real location under the new structure.
- linkedin-metrics-benchmarks.md (v1.1): added a dated 2026 freshness pass. The
  HeyReach-anchored ranges still hold against multi-source 2026 industry data
  (all labeled industry-reported, validate); added a LinkedIn platform-limits
  clarification (no published invite cap, ~100/week safe ceiling, pending-invite
  hygiene, ~30k connection cap) framed as verify-against-official.
- Removed the six `heyreach.io/blog` outbound links from the HeyReach knowledge
  base and the resource playbooks, keeping the article titles and "Adapted from
  HeyReach" attribution as plain text (SOP link policy: only growthtoday.co, the
  maintainer profile, and official product docs; no vendor blog links).
- Normalized the footer on every `.md` to the canonical comma form and removed
  all em-dashes (house-style: 0 em-dashes skill-wide).
- SKILL.md frontmatter: added `metadata.author` and `version: "2.0.0"`, and
  credited the restructure to Nikola Siljanoski in the SKILL.md and README footers.

## [1.0.0] - 2026-06-01

### Added
- First versioned release packaged for team-wide distribution: master `SKILL.md`
  router plus 15 resource files (connection-request, dm-sequence, re-engagement,
  connection-notes, personalization, atl-messaging, btl-messaging, copywriting,
  rented-engine, campaign-strategy, follow-up-system, drip-campaigns,
  linkedin-first-engine, linkedin-metrics-benchmarks, heyreach-knowledge-base).
- No changes to skill content on packaging; all 16 files included as-is.

---

*Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/), [Growth Today](https://www.growthtoday.co).*
