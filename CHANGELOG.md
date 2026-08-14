# Changelog

All notable changes to poeskill are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
