# poeskill

> **Language**: English (current) | [简体中文](README.zh-CN.md) | translations: see [i18n/](i18n/)

**Your AI keeps agreeing with you. poeskill is the toolkit that teaches it to push back.**

32 skills that turn any agent (Claude Code, Codex, Cline, WorkBuddy, …) into a critical-thinking partner for real business situations — diagnosing problems, stress-testing conclusions, dismantling buzzwords, and turning vague wishes into checkable goals.

- ✅ **Original, from scratch.** No upstream author text, no personal tweet database, no paid-community funnel, no telemetry. Fully rewritten from the ground up, MIT licensed.
- 📚 **A verified knowledge core.** 305 power units distilled from 25 thinkers — Hume to Hayek, Feynman to Kahneman — every unit carrying its original source (citation link, title, year).
- 🌍 **Language-neutral data, translatable content.** Power units are tagged `language`, skills carry `lang:` in frontmatter, i18n workflow documented.

## Why the name "poe"

Three layers:

1. **A tribute to Edgar Allan Poe** — the founding figure of detective fiction. His detectives never trust surface narratives; they reconstruct the truth from small clues. That is exactly the temperament of this toolbox: `/poe-diagnosis` traces symptoms to root causes, `/poe-verify` stress-tests conclusions with counter-evidence, `/poe-deconstruct` dismantles abused buzzwords.
2. **Problem-Oriented Engine** — the expansion of the three letters. Every tool starts from a problem, not from an answer.
3. **An independent renaming** — the upstream project was a personal skill set; this rewrite stands on its own. "poe" is short, pronounceable, and carries no negative connotations in any major language.

## Native prompt vs. poeskill

| | Plain prompting | poeskill |
|---|---|---|
| Problem statement | Vague, as you think it | `/poe-good-question` rewrites it into a reasoning-ready spec |
| Diagnosis | Your first guess | `/poe-diagnosis` runs consultation + checkup modes, forces falsifiable conditions |
| Conclusion quality | Sounds confident | `/poe-verify` adds source-strength grades (A–D) and counter-evidence |
| Vague wish | Stays vague | `/poe-goal` turns it into a checkable deliverable with acceptance criteria |
| "I know what to do but can't" | Advice | `/poe-action` finds the hidden goal the avoidance is serving |
| Buzzwords | Repeated | `/poe-deconstruct` asks what the word actually refers to |
| Knowledge | Generalization | 305 cited power units, per-skill knowledge packs |

## What it does

**Diagnosing business / commercial problems**
- `/poe-diagnosis` — business model diagnosis, consultation + checkup modes
- `/poe-decision` — turn long-term decisions into local, reviewable archives
- `/poe-standard-answer` — find historical mechanisms isomorphic to your dilemma
- `/poe-benchmark` — find benchmarks, filter out noise with a screening process

**Full content-creation pipeline**
- `/poe-good-question` — rewrite vague questions into reasoning-ready problem statements
- `/poe-content` — complete content diagnosis from topic to copy
- `/poe-hook` — short-video opening optimization
- `/poe-script-flow` — script continuity and drop-off checks
- `/poe-resonate` / `/poe-spread` — resonance detection and communication psychology
- `/poe-ai-check` — detect AI writing traces
- `/poe-content-risk-check` — pre-publish risk and platform review checks
- `/poe-xhs-title` — Xiaohongshu (RED) title formulas
- `/poe-wechat-html` — Markdown to WeChat Official Account HTML

**Thinking / cognition tools**
- `/poe-deconstruct` — dismantle vague concepts from a language-analysis angle
- `/poe-action` — diagnose "I know what to do but can't move"
- `/poe-slowisfast` — identify impatience vs. necessary friction, design compounding paths
- `/poe-goal` — turn vague wishes into checkable goals

**System tools (maintaining poeskill itself)**
- `/poe` — main entry and dynamic router
- `/poe-chatroom` / `/poe-chatroom-market` — multi-role discussions (incl. market-order school view)
- `/poe-save` / `/poe-restore` / `/poe-report` — diagnostic state archiving & reporting
- `/poe-knowledge` / `/poe-content-system` — local knowledge base & content asset engineering
- `/poe-learning` — interactive learning
- `/poe-verify` — counter-verification of any conclusion (evidence tracing / counter-examples / source grading / conflict-of-interest checks)
- `/poe-update` — self-update from this repository
- `/poe-bridge` / `/poe-agent-migration` — bridge to other agents & workspace migration
- `/poe-skill-cleaner` — audit skills for hidden commercial intent

## Install

One line (any platform with bash / Git Bash / WSL):

```bash
curl -fsSL https://raw.githubusercontent.com/<your-user>/poeskill/main/install.sh | bash
```

Or from a local clone:

```bash
git clone https://github.com/<your-user>/poeskill.git
cd poeskill
bash install.sh            # auto-detects your agent's skills directory
bash install.sh --all      # install into every detected agent
bash install.sh --target ~/.claude/skills
```

Manual install for a specific agent:

```bash
# Claude Code
cp -r skills/* ~/.claude/skills/
# Codex
cp -r skills/* ~/.codex/skills/
# WorkBuddy
cp -r skills/* ~/.workbuddy/skills/
# Knowledge base (optional, used by diagnostic skills for source verification)
cp -r 知识库 ~/poeskill-知识库
```

> Windows without bash: run the same `cp -r` commands in PowerShell, or use Git Bash / WSL.

## Knowledge base: 305 power units, 25 thinkers

`知识库/` contains **305 power units** distilled from **25 thinkers** (Hume, Kant, Popper, Wittgenstein, Deutsch, Russell, Smith, Mises, Hayek, Laozi, Adler, Schopenhauer, Marcus Aurelius, Nietzsche, Camus, Aristotle, Mill, Weber, Keynes, Friedman, Schumpeter, Soros, Grove, Darwin, Feynman, Einstein, Newton, Shannon, Turing, Bacon, Descartes, Munger, Kahneman, Thaler, Taleb, Drucker, Porter, Simon, Coase, Pinker, Dennett), each with an original source and an audience tag (🔬 scientist-leaning / 🔥 broad appeal / 💼 business-frequency / ⚠️ use selectively).

- `能量库/powers_poe.jsonl` — the master dataset (format-compatible with the original library)
- `Skill知识包/` — 12 per-skill knowledge packs (30–160 units each)
- `哲学概念词典.md` — 80-concept quick reference

## Why you should star this repo

- **It argues with you.** The entire point is to disagree — every diagnostic skill must attach a falsifiable condition and a source-strength grade to its conclusion.
- **Everything is verifiable.** 305 units, each with a citation. No vibes, no "trust me".
- **It runs locally.** No telemetry, no SaaS, no account. Your questions never leave your machine.
- **MIT + fully original.** You can fork, vendor, and build on it.

## Critical use (important)

poeskill is a thinking tool, not an answer machine:

1. Every conclusion-type skill **must** attach a source-strength grade (A/B/C/D); below C it's only an idea
2. Qualitative attributions must come with falsifiable conditions
3. When unsure, run `/poe-verify` for counter-verification
4. For high-stakes decisions (investment, career, health), cross-validate — never trust a single framework
5. `/poe-action` and other psychological tools are self-awareness aids, not psychotherapy

## Updating

- The main entry checks `UPDATE.json` at most once per 24h
- `/poe-update` syncs from this repository, keeping your `~/.poe/` archive
- `git pull` before updating to review changes

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) (incl. i18n workflow), [ROADMAP.md](ROADMAP.md), and [CHANGELOG.md](CHANGELOG.md).

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgements

- This repository is an original, from-scratch implementation. All skills, knowledge units, scripts, and documentation were written independently for this project
- No paid community, no course funnel, no monetization of any kind
- Knowledge base content is organized from publicly available philosophical and economic works; every unit cites its original source
