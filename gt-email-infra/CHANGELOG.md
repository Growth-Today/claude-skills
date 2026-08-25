# Changelog

All notable changes to the `gt-email-infra` skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/); versions use
[SemVer](https://semver.org/) (patch = fix, minor = additive, major = breaking
layout/restructure).

## [v5.1.0] - 2026-08-25

Knowledge corrections, the first executable playbooks, and a terminology rename.

### Added
- **`playbooks/`** — the skill's first runnable steps, following the
 `gt-hubspot-admin` convention (`playbook.md` with an interview section +
 `scripts/` carrying PEP-723 headers, so `uv run` needs no install).
 - **dns-auth-audit** — MX / SPF (record count + recursive RFC 7208 lookup
 budget) / DKIM across 14 selectors / DMARC against the GT standard / stray
 Lync SRV. `--esp-mix` profiles a recipient list by ESP, replacing the manual
 Clay MX column. `after.py` diffs a re-run against a saved baseline to catch
 silent drift. Exit 2 on FAIL, so it works as a launch gate.
 - **sizing-calculator** — goal (or contacts × steps ÷ days-to-clear) →
 mailboxes → domains. Parses the cold limits out of §1 at run time instead of
 hardcoding them. `--validate` reproduces the §4 table.
- **`requirements.txt`**, **`.env.example`**, **`.gitignore`**.
- **reference.md §1 and §2 key tables** — addressable keys (`google_cold`,
 `cold_warming`, `warmup_floor_days`, `placement_active`, …) so executable
 checks cite a key instead of copying a number.
- **instantly-setup Part 4b** — required Unibox settings. *Save undelivered
 emails in Unibox* is OFF by default and gates what the reporting can see.
- **setup-audit dimension 21** — Unibox settings check.

### Changed
- **setup-audit Part B is now executable**: six columns (Check · Source ·
 Call → field · Pass if · On fail · Write?). 13 of 21 rows verified against a
 live Instantly workspace; 2 confirmed not exposed by the API (signature,
 sender name); the rest labelled honestly.
- **Renamed OpsLab → "email infra management system"** throughout. The
 Supabase + Railway + n8n stack is Growth Today's own, and the plainer name
 reads better for an agent.
- **dashboard-reading Parts 1 and 4** reframed as verify-only tables.
- **dashboard-reading Part 2b** rewritten from a defect list to fixed vs still
 open, reflecting the 20–25 Aug QA.
- **Warmup floor 14 → 21 days**; Outlook fully-warmed warmup 13 → 15; Outlook
 warm-to-cold ratio 2.5:1 → 3:1.
- **Sizing divisor 20–25 → 14.** The old figure came from deprecated Google 30
 / Microsoft 10 limits and under-bought inventory by 43–79%.
- **DMARC standard is `p=reject`.**
- **Purchasing** — multi-day spread, max 4 per registrar per day, owned by
 ScaledMail; GT verifies on delivery.
- **MX→ESP classification** now mirrors the 12-provider Clay formula from
 PR #29, with a SEG flag and a `no-email` case.

### Removed
- **SURBL** as a blacklist reason, everywhere. Only Spamhaus DBL and URIBL
 count. It is not tracked by the email infra management system, and leaving it
 in as "monitor-only" is how it kept reappearing in checklists.

### Fixed
- Three write instructions in `setup-audit` that breached the read-only
 boundary (warmup enable, limit correction, throttle + tag) now report instead.
- `SKILL.md` still carried the deprecated ÷20–25 sizing divisor after
 `reference.md` §4 had been corrected.
- `setup-audit` dimension 9 passed `p=quarantine`; realigned to §6.

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
 all 20 config dimensions PASS/WARN/FAIL against the GT standard; the setup-side
 counterpart to blacklist-bounce-audit.
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
- **Blacklist scope cut to Spamhaus DBL + URIBL only**; no other list is a blacklist reason.
- Multi-registrar purchasing spread; failover gap flagged.
