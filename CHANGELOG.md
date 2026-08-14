# Changelog

All notable changes to poeskill are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [3.4.0] - 2026-08-14 — beginner-friendly

### Added
- `QUICKSTART.md` / `QUICKSTART.zh-CN.md` — 3-minute onboarding, no jargon:
  one command to remember (`/poe`), a copy-paste first sentence, a plain-
  language situation table, and a Windows section.
- README (EN/ZH): new "First 3 minutes" section right after Install —
  "you only need to remember one command" + sample first prompt.

### Changed
- `/poe` onboarding (mode C): now explicitly tells first-timers they only
  need to remember `/poe` — no need to learn any of the 32 skill names.

## [3.3.0] - 2026-08-14 — measurable

### Added
- `benchmark/` — reproducible before/after proof: one business decision, run
  bare vs. with poeskill on the same model.
  - Case 01 "queue app idea" with a built-in untested premise
  - Dual prompts (`baseline.md` / `poeskill.md`) + stdlib-only runner
    (`run_benchmark.py`, anthropic & OpenAI-compatible endpoints)
  - Scored comparison (5-dimension rubric): example baseline **6/25** vs
    poeskill **25/25** — the gap is the product
- README (EN/ZH): new **Benchmark** section with the score and run command
- ROADMAP: Demo-evidence milestone marked shipped

## [3.2.0] - 2026-08-14 — launch-ready

### Added
- Knowledge base expanded **50 → 305 power units** across **25 thinkers** (added
  Aristotle, Mill, Weber, Keynes, Friedman, Schumpeter, Soros, Grove, Darwin,
  Feynman, Einstein, Newton, Shannon, Turing, Bacon, Descartes, Munger, Kahneman,
  Thaler, Taleb, Drucker, Porter, Simon, Coase, Pinker, Dennett; deepened all 15
  original thinkers). Every unit carries a verifiable citation link.
- Concept dictionary expanded **34 → 80 entries**.
- `install.sh` — one-line installer with multi-agent auto-detection
  (Claude Code / Codex / Cline / Kiro / Qwen Code / WorkBuddy), `--all`,
  `--target`, `--dry-run`.
- Full GitHub community scaffolding: issue templates (bug/feature), PR template,
  Code of Conduct, CI workflow (frontmatter / JSONL / install.sh / reproducibility
  checks), `scripts/ci_check.py`.
- `CONTRIBUTING.md`, `ROADMAP.md`, `CHANGELOG.md`.

### Changed
- README rewritten around a positioning hook; English version is now the primary
  README (`README.md`), Chinese version lives in `README.zh-CN.md`.
- Added "Why the name poe" section (both languages).
- README now includes a native-prompt-vs-poeskill comparison table and
  per-platform install instructions.

## [3.1.0] - 2026-08-14

### Changed
- "原子库" renamed to "能量库", `atoms` → `powers` across repo, delivery dir and
  installed copies (36 files).
- All 305-position-ready schema: power units carry `language: zh-CN`; all 32
  `SKILL.md` gain `lang: zh-CN` frontmatter.
- Added full English README, `i18n/README.md` translation spec and
  `i18n/languages.md` language table.

## [3.0.0] - 2026-08-14

### Changed
- **Complete independent rewrite.** All skill prompts, cases, knowledge base and
  scripts rewritten from scratch; no upstream author text, tweet database,
  paid-community funnel, or telemetry code.
- All skills renamed to the unified `poe-*` prefix;
  `poe-chatroom-austrian` → `poe-chatroom-market`.
- Update chain switched from `npx skills add` to self-hosted `git pull + cp`
  (fixes supply-chain risk).
- License: MIT (original work).
