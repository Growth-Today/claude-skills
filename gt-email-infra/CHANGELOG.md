# Changelog

All notable changes to the `gt-email-infra` skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/); versions use
[SemVer](https://semver.org/) (patch = fix, minor = additive, major = breaking
layout/restructure).

## [v5.0.0] - 2026-07-30

Major restructure and 2026 deliverability rebuild.

### Changed
- **Restructured to the Growth Today sub-skill pattern.** The flat topic files
 became **7 role-tagged sub-skills** under `.claude/skills/` (each with its own
 frontmatter name + description + "Do NOT use" boundary, individually
 triggerable) plus a root orchestrator that resolves `SKILL_BASE` dynamically.
 Matches `gt-linkedin-content` / `gt-hubspot-admin`.
- **Reference files moved to `resources/`** (`reference.md`, `approved-vendors.md`,
 `benchmarks.md`); every sub-skill derives its numbers from `reference.md`.
- **Send limits now governed by the warm-to-cold ratio** (Google 1.5:1,
 Outlook 2.5:1) with concrete values (warming 25/8 at +4/+2; sending 30/13),
 replacing the old flat "Google 30 / Microsoft 10" figures.

### Added
- Per-sequencer setup sub-skills (vendor-managed + in-house paths), each sourced
 from the vendor's live help center: **instantly-setup, emailbison-setup,
 smartlead-setup, lemlist-setup**, replacing the ScaledMail + Instantly/Bison
 and Lemlist Notion SOPs.
- **setup-audit** sub-skill, connect a live workspace (any sequencer) and verify
 all 20 config dimensions PASS/WARN/FAIL against the Growth Today standard; the
 setup-side counterpart to blacklist-bounce-audit.
- **benchmarks.md**: 2026 market benchmarks (results-side vs automation-side).
- **approved-vendors.md**: approved SMTP / sequencer / masking vendors.
- **blacklist-bounce-audit**: folded in the executable EmailBison audit runbook (MCP/API pull with cursor pagination, the broken `?type=bounced` filter workaround, Hard/Soft/Block/Unknown SMTP-code classification incl. Microsoft-specific block codes, the report sections + CSV schema + chat summary, and a Known API Limitations table). Sanitized from a teammate's internal `gt-bounce-audit` runbook.
- Per-sub-skill **"Reads:"** dependency lines and a copy-pasteable **checklist**
 at the end of every sub-skill.
- Composite **Routing Rules** in the orchestrator for chained requests.

### Fixed (2026 deliverability corrections)
- **Masking or a real landing page, never a bare 301/302 redirect** (the #1
 pre-send blocklisting cause).
- **Domain naming:** drop `go/get/try/meet` prefixes, hyphens, and numbers.
- **ESP matching is no longer a fixed rule**: route from the Lead-ESP ×
 sending-vendor matrix.
- **No links / no custom tracking domain** in cold email by default.
- **Strip OOO/auto-replies before reading any bounce rate** (~54% inflation).
- **SURBL de-scoped to monitor-only**; only Spamhaus DBL + URIBL count.
- Multi-registrar purchasing spread; failover gap flagged.

---

*Created by [Growth Today](https://www.growthtoday.co), the AI-native GTM engineering firm. Maintained by [Brigitta Ruha](https://www.linkedin.com/in/brigittaruha/). More open Claude Skills for go-to-market teams: https://www.growthtoday.co/claude-skills*
