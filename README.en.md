# poeskill

> **Language**: English (current) | [简体中文](README.md) | Translations for other languages: see [i18n/](i18n/)

A business thinking toolbox for real situations. It gives you an interactive set of diagnostic, content, cognitive, and system tools to help you think clearly about vague problems and execute what you have figured out.

> **Fully independent open-source rewrite**: This repository contains none of the upstream  author's text, personal tweet database, paid-community funnel, or telemetry code. The methodological approach is inspired by , but all content (skill prompts, cases, knowledge base, scripts) has been rewritten from scratch as original expression. Licensed under MIT.

## What it does

Four groups by use case:

**Diagnosing business / commercial problems**
- `/poe-diagnosis` — business model diagnosis, with "consultation" and "checkup" modes
- `/poe-decision` — turn long-term decisions into local, reviewable archives
- `/poe-standard-answer` — find historical mechanisms isomorphic to your dilemma in business history
- `/poe-benchmark` — find benchmarks, filter out noise with a screening process

**Full content-creation pipeline**
- `/poe-good-question` — rewrite vague questions into reasoning-ready problem statements
- `/poe-content` — complete content diagnosis from topic to copy
- `/poe-hook` — short-video opening optimization
- `/poe-script-flow` — script continuity and drop-off checks
- `/poe-resonate` / `/poe-spread` — resonance detection and communication psychology decoding
- `/poe-ai-check` — detect AI writing traces
- `/poe-content-risk-check` — pre-publish risk and platform review checks
- `/poe-xhs-title` — Xiaohongshu (RED) title formulas
- `/poe-wechat-html` — Markdown to WeChat Official Account HTML

**Thinking / cognition tools**
- `/poe-deconstruct` — dismantle vague concepts from a language-analysis angle
- `/poe-action` — diagnose "I know what to do but can't move" from a teleological angle
- `/poe-slowisfast` — identify impatience vs. necessary friction, design long-term compounding paths
- `/poe-goal` — turn vague wishes into checkable goals

**System tools (maintaining poeskill itself)**
- `/poe` — main entry and dynamic router
- `/poe-chatroom` / `/poe-chatroom-market` — multi-role discussions (including a market-order school view)
- `/poe-save` / `/poe-restore` / `/poe-report` — diagnostic state archiving, restoring, and reporting
- `/poe-knowledge` / `/poe-content-system` — local knowledge base and content asset engineering
- `/poe-learning` — interactive learning
- `/poe-verify` — adversarial review of any conclusion (evidence tracing / counterexamples / source rating / conflict-of-interest check)
- `/poe-update` — update from this repository
- `/poe-bridge` / `/poe-agent-migration` — bridge to other agents and workspace migration

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/poeskill.git

# 2. Copy skills into your agent's skill directory (WorkBuddy example)
cp -r poeskill/skills/* ~/.workbuddy/skills/

# 3. Knowledge base (optional; diagnostic skills reference it for source verification)
cp -r poeskill/知识库/* your-preferred-location/
```

> If your agent supports relative-path references, simply keep `skills/` and `知识库/` under the same parent directory — skills already reference knowledge packs via relative paths.

## Knowledge base: Four Knowledge Topics

`知识库/` contains 50 power units (能量单元) distilled from the thought of 15 philosophers/physicists (Hume, Kant, Popper, Wittgenstein, Deutsch, Russell, Smith, Mises, Hayek, Laozi, Adler, Schopenhauer, Marcus Aurelius, Nietzsche, Camus). Each entry carries an original-work citation and an audience tag (🔬 scientist-preferred / 🔥 mass-appeal / 💼 business-circles / ⚠️ selective use, avoid out-of-context quoting).

- `能量库/powers_poe.jsonl` — master data (format-compatible, each entry tagged with `language`)
- `Skill知识包/` — 12 knowledge packs aggregated per skill
- `哲学概念词典.md` — quick reference of high-frequency concepts

## Critical use (important)

poeskill is a thinking tool, not an answer provider:

1. Every conclusion-producing skill **must** attach a source-strength rating (A/B/C/D); below C it is only an idea
2. Qualitative attributions must include falsifiable conditions
3. When unsure, run `/poe-verify` for adversarial review
4. For major decisions (investment, career, health), cross-validate; never rely on a single framework
5. Psychological tools like `/poe-action` are self-awareness aids, not psychotherapy

## i18n

- All SKILL.md files carry a `lang:` field in frontmatter (`zh-CN` for the source language)
- Power units in `powers_poe.jsonl` are tagged with a `language` field; translate entries by duplicating and changing `language` + `knowledge`
- See [i18n/](i18n/) for the translation guide, language code table, and contribution conventions

## Updates

- The main entry checks for versions at most once per 24h (read-only fetch of this repo's `UPDATE.json`)
- `/poe-update` syncs from this repository, preserving your `~/.poe/` archives
- Review changes with `git pull` and diff before updating

## License

MIT License. See [LICENSE](LICENSE).

## Acknowledgments & statement

- Methodological approach inspired by [](https://github.com//) (); this repository is an independently rewritten original implementation containing none of its protected content
- This repository has no paid community, no course funnel, and no commercial monetization of any kind
- Knowledge base content is compiled from public philosophy and economics works, with original-work citations
