# Contributing to poeskill

Thanks for considering a contribution. poeskill is a toolbox whose whole point is
to *argue* — so argue with us: open issues, challenge conclusions, propose skills,
add power units.

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). Be respectful,
be constructive.

## What kind of contribution helps most

1. **New power units** (knowledge base) — the fastest way to make poeskill smarter.
2. **Skill improvements** — sharper prompts, fewer edge cases.
3. **New skills** — especially ones that fit the philosophy: they must push back,
   verify sources, and work locally.
4. **Translations** — see [i18n/README.md](i18n/README.md) for the workflow.
5. **Docs** — README, launch materials, guides.

## Repository layout

```
skills/                      32 skills (SKILL.md + optional scripts/docs)
知识库/能量库/powers_poe.jsonl   master dataset (305 power units)
知识库/Skill知识包/            per-skill knowledge packs (generated)
知识库/哲学概念词典.md          80-concept dictionary (generated)
scripts/                     build + CI scripts
install.sh                   one-line installer
```

## Adding power units

1. Edit the source files: `scripts/powers_phil_p1.py` … `powers_phil_p6.py`
   (or add `powers_phil_p7.py` and wire it into `scripts/build_phil.py`).
2. Every unit **must** have: `id` (unique, `<thinker>_NN`), `knowledge`
   (with a business implication), `original` (source title), `url` (verifiable
   link), `date`, `topics` (non-empty list), `skills` (non-empty list of existing
   skill names), `type` (`principle|method|case|anti-pattern|insight|tool`),
   `confidence` (`high|medium|low`), and optionally `audience`.
3. Regenerate artifacts:

   ```bash
   python scripts/build_phil.py
   python scripts/ci_check.py
   ```

4. Commit the generated artifacts too (they are part of the release).

## Adding or modifying a skill

- Keep `SKILL.md` frontmatter with a `lang:` field (source language is `zh-CN`).
- Slash-command names are identifiers — do not translate them.
- Every conclusion-type skill must instruct the model to attach a
  source-strength grade (A/B/C/D) and falsifiable conditions.
- Run the CI checks locally before opening a PR.

## i18n

Full workflow in [i18n/README.md](i18n/README.md). Quick rules:

- Metadata is tagged (`lang:` in frontmatter, `language` in JSON), never hardcoded.
- A translation is a *new file* with a language suffix (`SKILL.en.md`), the master
  stays `zh-CN`.
- Do not translate: skill names, JSON field names, `id`, `type`, `confidence`.

## Commit conventions

- One logical change per commit; write a clear imperative subject line.
- Prefix subjects: `feat:` `fix:` `docs:` `i18n:` `kb:` `ci:` `chore:`.
- Keep the CHANGELOG updated for user-facing changes.

## Opening a PR

Use the [PR template](.github/PULL_REQUEST_TEMPLATE.md). Small, focused PRs get
reviewed much faster. If you're unsure whether a change belongs, open an issue
first and ask.
