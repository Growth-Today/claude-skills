# Changelog

All notable changes to the `gt-email-infra` skill are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/); versions use
[SemVer](https://semver.org/) (patch = fix, minor = additive, major = breaking
layout/restructure).

## [v5.1.0] - 2026-08-11

Lemlist sub-skill additions from the internal Notion SOP.

### Added
- **reference.md:** new §10, CRM preference defaults (default opportunity
 value $4,500, single source for all sub-skills to link rather than
 hardcode).
- **lemlist-setup:** default opportunity value (reference.md §10, unless the
 AM confirms a different ACV) and lead preferences OFF.
- **lemlist-setup:** account-signature and sender-name checks (no images,
 logos, or links in the account signature, signatures live in sequence steps
 only, sender names checked across all connected inboxes).
- **lemlist-setup:** bi-directional cross-sequencer rule, written out
 platform-neutral, whichever sequencer's lead gets a positive or neutral
 reply first stops that lead in the other sequencer(s).
## [v5.1.0] - 2026-08-26

Knowledge corrections, the first executable playbooks, a terminology rename,
and an adversarial pass over all of it.

### Fixed after the adversarial pass
Two independent reviewers were pointed at this branch and told to break it.
Thirteen findings held up; all are fixed here.

- **The launch gate did not gate.** `dns-auth-audit` exited 2 only on FAIL, so
 a `p=quarantine` DMARC and a missing DKIM key both cleared go-live. MX, SPF,
 DKIM and DMARC must now all be PASS. SRV hygiene moved FAIL → WARN and out of
 the gate — no mail filter reads a SIP record. `test_gate.py` proves all ten
 states, including the two that must still exit 0.
- **A revoked DKIM key reported PASS.** `"p=" in rec` matched any TXT record
 containing those two characters. Now requires `v=DKIM1` with a real key.
- **A DNS timeout was reported as a missing record** on MX, SPF and DMARC —
 a hard FAIL on a healthy domain. The lookup now says which one happened.
- **Null MX (RFC 7505) classified as `other`,** so domains that publish "we
 accept no mail" survived the `--esp-mix` strip and hard-bounced. Fixed in the
 script and in the Clay formula. `--esp-mix` also takes the domain off each
 email address now — a lead list is addresses, not domains.
- **`after.py` missed the drift it exists to catch.** PASS → WARN (p=reject
 dropping to p=none, a DKIM key vanishing) printed `[CHANGED]` and exited 0.
 Any downgrade is now a REGRESSION.
- **provisioning shipped `p=none`** in its copy-paste checklist, against §6 and
 its own Part 3.
- **§4's sizing grid and the calculator disagreed on three of five rows,** and
 `--validate` could not catch it because its expected values were hand-copied.
 One rounding rule now, and validate parses both tables out of the doc.
- **`--split-google` silently defaulted to 0.60** while its own playbook called
 it a required judgement call. Now required, with an error that says why.
- **EmailBison calls were written as MCP tools.** There is no connector; REST
 is the primary path, with the Instantly equivalents named alongside.
- **Bounce codes:** 5.4.1 was "address invalid" here and "Microsoft tenant
 block" elsewhere; 5.2.2 was Block in one file and Soft in two. §7 now carries
 a "permanent, but NOT a bad address" table, and the audit thresholds are keys.
- **Three vendor scores treated as one gate.** Instantly's Health Score and
 Lemlist's deliverability score are vendor scales, not `warmup_score_active`.
- **Rows 15 and 16** moved MCP → MANUAL; a live read returns neither field.
- **Unsourced numbers removed** — "~43% under-bought", "inflated by ~54%" (it
 was more than double), "~3× the reply chance" (the table says 1.3×), "top 10%
 sit near 27–33" (the table says 38), and a bare 80/20.

### Changed after Nikola's review
- **Connecting inboxes and campaign build/routing are read-only** — both are
 done from the email infra management system. Seven setup-audit rows moved
 `setup-only` → `never`.
- **ScaledMail buys the domains.** Step 2 of the flow is "ideate and brief
 ScaledMail", and domain-research's headings say so.
- **Voice pass.** Consultant filler, sections that opened by explaining
 themselves, and the same aphorism restated across four files.

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
- **setup-audit Part B is now executable**: seven columns (Check · Source ·
 Call → field · Pass if · On fail · Write?). 14 of 21 rows run automatically
 (13 MCP + 1 playbook), verified against a live Instantly workspace. The other
 7 are marked MANUAL with the reason: signature, Unibox toggles, ESP routing
 and the per-company cap are confirmed absent from the API, and the rest need
 a second platform or a live campaign.
- **Renamed OpsLab → "email infra management system"** throughout. The
 Supabase + Railway + n8n stack is Growth Today's own, and the plainer name
 reads better for an agent.
- **dashboard-reading Parts 1 and 4** reframed as verify-only tables.
- **dashboard-reading Part 2b** rewritten from a defect list to fixed vs still
 open, reflecting the 20–25 Aug QA.
- **Warmup floor 14 → 21 days**; Outlook fully-warmed warmup 13 → 15; Outlook
 warm-to-cold ratio 2.5:1 → 3:1.
- **Sizing no longer publishes a fixed divisor.** The provider mix is a
 per-client decision, so §4 now gives the formula
 (`google_share × 20 + microsoft_share × 5`) plus a scenario grid, and the
 mix is a required input rather than an assumption. The old "20–25" was two
 different figures collapsed into a range — 20 is Growth Today's per-mailbox
 number for a Google inbox, 25 is ScaledMail's — and both describe a Google
 mailbox, while a Microsoft one sends 5. At 15k/month the answer ranges from
 57 mailboxes (all Google) to 129 (25/75).
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
- `SKILL.md` and `reference.md` §4 disagreed on the sizing divisor; both now
 point at the same formula instead of a number.
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
- **Strip OOO/auto-replies before reading any bounce rate** (2,687 raw vs 1,231 real in one audit).
- **Blacklist scope cut to Spamhaus DBL + URIBL only**; no other list is a blacklist reason.
- Multi-registrar purchasing spread; failover gap flagged.
