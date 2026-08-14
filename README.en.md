# poeskill

> 🌐 [简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

---

**Your AI keeps agreeing with you.**

You ask "is this idea any good?" — it says "great potential." You ask "should I do this?" — it says "it depends on your execution."

It never says no. It never asks "have you verified that?"

poeskill fixes exactly that. 32 skills that turn any AI tool into a partner that pushes back — it questions your premise first, demands your data, then gives you a conclusion you can actually falsify. Not "sounds right," but "right or wrong — here's how you check."

---

## Why we built this

I used AI tools for a long time and noticed a pattern: **the smarter it gets, the faster it agrees with you.**

You hand it a business plan full of holes, it fills them in. You give it a vague wish, it breaks it into steps — but nobody stops to ask: "wait, is the premise even true?"

Good decisions don't come from "help me execute." They come from "help me question." So I took the thinking methods of 25 thinkers — Hume to Hayek, Feynman to Kahneman — distilled them into 305 cited knowledge units, and packed them into 32 one-command-install skills.

Every skill follows one design principle: **it must argue with you before it helps you.**

---

## 30-second install

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

Or from a local clone:

```bash
git clone https://github.com/wastefulthink/poeskill.git
cd poeskill
bash install.sh            # auto-detects your AI tool
bash install.sh --all      # install into every detected tool
bash install.sh --target ~/.claude/skills
```

Works with Claude Code, Codex, Cline, WorkBuddy, Kiro, Qwen Code — any agent that reads skills from a folder.

After install, **you only need to remember one command: `/poe`.** Don't learn any of the 32 skill names — it routes automatically.

---

## Your first 3 minutes

1. Open your AI tool and type, plain language:

   ```
   /poe I have an idea: a coffee shop AI queue app. Should I do it?
   ```

2. A normal AI says "great idea, here's how to build it." An AI with poeskill argues first:
   - "Is the queue really their biggest pain point? Have you verified that?"
   - "Will the owner actually pay for this? Do you have proof?"
   - Then: "**Don't do it — unless** X happens" instead of "it depends on your execution."

3. **It argues first so you make better decisions.** That's the whole point.

New here? Read the [3-minute quickstart](QUICKSTART.en.md) (zero jargon).

---

## What it does

**Diagnosing business problems**
- `/poe-diagnosis` — business model diagnosis, consultation + checkup modes
- `/poe-decision` — turn long-term decisions into reviewable local archives
- `/poe-standard-answer` — find historical mechanisms isomorphic to your dilemma
- `/poe-benchmark` — find benchmarks, filter out noise with a screening process

**Full content-creation pipeline**
- `/poe-good-question` — rewrite vague questions into reasoning-ready specs
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

---

## Knowledge base: 305 units · 25 thinkers

`knowledge/` doesn't contain vague "AI summaries." It holds 305 power units distilled from the original works of 25 thinkers — Hume, Kant, Popper, Wittgenstein, Deutsch, Russell, Smith, Mises, Hayek, Laozi, Adler, Schopenhauer, Marcus Aurelius, Nietzsche, Camus, Aristotle, Mill, Weber, Keynes, Friedman, Schumpeter, Soros, Grove, Darwin, Feynman, Einstein, Newton, Shannon, Turing, Bacon, Descartes, Munger, Kahneman, Thaler, Taleb, Drucker, Porter, Simon, Coase, Pinker, Dennett.

Every unit carries its original source. No "trust me" — only "here's the citation, judge for yourself."

- `powers/powers_poe.jsonl` — the master dataset
- `Skill知识包/` — 12 per-skill knowledge packs
- `philosophy-glossary.md` — 80-concept quick reference

---

## It's measurable

The same business decision, run twice on the same model — bare vs. with poeskill. On case 01 the bare model scores **6/25**; poeskill **25/25**. Same model, same question; the only difference is whether the AI was told to argue with you.

```bash
python benchmark/run_benchmark.py --prompt both   # needs an API key
```

See [`benchmark/`](benchmark/) for the case, prompts, runner and scoring rubric. **The gap is the product.**

---

## Why the name "poe"

Three layers:

1. **A tribute to Edgar Allan Poe** — the founding figure of detective fiction. His detectives never trust surface narratives; they reconstruct truth from small clues. That is exactly this toolbox's temperament: `/poe-diagnosis` traces symptoms to root causes, `/poe-verify` stress-tests conclusions with counter-evidence, `/poe-deconstruct` dismantles abused buzzwords.
2. **Problem-Oriented Engine** — every tool starts from a problem, not from an answer.
3. **An independent name** — short, memorable, no negative connotations in any major language.

---

## Why you should star this repo

- **It argues with you.** The entire point is to disagree — every diagnostic skill must attach a falsifiable condition and a source-strength grade to its conclusion.
- **Everything is verifiable.** 305 units, each with a citation. No vibes, no "trust me."
- **It runs locally.** No telemetry, no SaaS, no account. Your questions never leave your machine.
- **MIT + fully original.** Written from scratch. Fork it, vendor it, build on it.

---

## Critical use (important)

poeskill is a thinking tool, not an answer machine:

1. Every conclusion-type skill **must** attach a source-strength grade (A/B/C/D); below C it's only an idea
2. Qualitative attributions must come with falsifiable conditions
3. When unsure, run `/poe-verify` for counter-verification
4. For high-stakes decisions (investment, career, health), cross-validate — never trust a single framework
5. `/poe-action` and other psychological tools are self-awareness aids, not psychotherapy

---

## Updating

- The main entry checks `UPDATE.json` at most once per 24h
- `/poe-update` syncs from this repository, keeping your `~/.poe/` archive
- `git pull` before updating to review changes

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) (incl. i18n workflow), [ROADMAP.md](ROADMAP.md), and [CHANGELOG.md](CHANGELOG.md).

## License

MIT. See [LICENSE](LICENSE).

## Buy Me a Coffee

If poeskill helped you think through a decision, consider buying me a coffee:

[![Buy Me a Coffee](https://img.shields.io/badge/☕-Buy_Me_a_Coffee-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xueyegog)

Entirely voluntary — no sponsorship required to use or get updates.

## Acknowledgements

- This repository is an original, from-scratch implementation. All skills, knowledge units, scripts, and documentation were written independently for this project.
- The project is free and open source; the only way to support it is voluntary donations (see above). No paid community, no course funnel.
- Knowledge base content is organized from publicly available philosophical and economic works; every unit cites its original source.
