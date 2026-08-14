# Roadmap

Where poeskill is going. Roughly ordered by impact; dates are targets, not
commitments.

## Now — launch (v3.2.0)

- [x] Knowledge base 305 units / 25 thinkers
- [x] One-line installer (`install.sh`)
- [x] CI + community scaffolding
- [x] English-first README with positioning hook
- [ ] Publish to GitHub, tag v3.2.0
- [ ] Launch posts: Show HN, r/ClaudeAI, r/LocalLLaMA, X/Twitter, V2EX
- [ ] Submit to awesome lists (claude-code, agent skills, etc.)

## Next 30 days — reach 1k stars

- **Demo evidence**: a real worked example per flagship skill
  (`/poe-verify` on a viral claim, `/poe-diagnosis` on a public business case),
  screenshots + a GIF in the README.
  - [x] `benchmark/` shipped: case 01 + dual prompts + stdlib runner +
        scored comparison (baseline 6/25 vs poeskill 25/25)
  - [ ] extend benchmark to cases 02–03, publish a multi-model scoreboard
- **i18n launch pack**: `SKILL.en.md` for the 10 most-used skills (frontmatter
  translations only — keep command names).
- **Multi-platform verification**: test install paths for Codex, Cline, Kiro,
  Qwen Code; document caveats.
- **Monthly release cadence**: one tagged release per month with changelog.
- **Eval suite**: extend `/poe-standard-answer` evals to 10+ scenarios and add
  evals for `/poe-verify` and `/poe-good-question`.

## 3–6 months — reach 5–10k stars

- **Knowledge base 300 → 1000+ units**: add East-Asian business thinkers,
  systems theory, and modern decision science; keep citation quality bar.
- **Knowledge packs v2**: per-skill packs auto-ranked by confidence + audience,
  with "falsifiability" annotations.
- **`poe-pack`**: a sub-tool to author & publish third-party skill packs.
- **Community translations**: ja / es / de first, driven by contributors.
- **CLI**: `poeskill` CLI to install / update / verify without curl|bash.

## Long-term — ecosystem

- **Plugin registry**: opt-in directory of community skill packs with verified
  provenance (no telemetry, MIT-compatible).
- **Agent-agnostic standard**: advocate a minimal `SKILL.md` + `lang` +
  source-grade convention across agents.
- **Benchmarks**: a public dataset of "prompt vs poeskill" outcomes so the value
  claim is measurable, not vibes.

---

**Principles that don't change**: argue with the user · every conclusion carries
a source grade · everything runs locally · fully original, MIT.
