# poeskill i18n / Internationalization

poeskill is designed to be **language-neutral at the data layer** and **translatable at the content layer**. The source language is `zh-CN`; every part of the repository carries an explicit language marker so contributors can add translations without touching the original.

## Design principles

1. **Metadata is tagged, not hardcoded.** Every `SKILL.md` frontmatter has a `lang:` field. Every power unit (能量单元) in `powers/powers_poe.jsonl` has a `language` field.
2. **Translation never overwrites the source.** A translated file is a *new file* with a language suffix — e.g. `SKILL.en.md`, `SKILL.ja.md` — and the original `SKILL.md` stays as the `zh-CN` master.
3. **Slash commands stay universal.** Skill names (`/poe-diagnosis`, `/poe-verify`, ...) are identifiers, not translated text. Only descriptions, instructions, and knowledge content get translated.
4. **The knowledge base is additive.** To translate a power unit, copy its JSON line, change `language` and `knowledge` (and optionally `original`/`url` to a localized edition), and keep `id`, `topics`, `skills`, `type`, `confidence`, `audience` unchanged. Then regenerate or extend the knowledge packs.

## File naming convention

| File | Convention | Example |
|---|---|---|
| Skill definition | `SKILL.<lang>.md` alongside the master | `poe-diagnosis/SKILL.en.md`, `poe-diagnosis/SKILL.ja.md` |
| Master (source of truth) | `SKILL.md` (always zh-CN) | — |
| README | `README.<lang>.md` | `README.en.md`, `README.ja.md` |
| Knowledge packs | keep the pack filename; add a `> 语言:` header line per translation section | see `Skill知识包/` |

## Language code table

See [languages.md](languages.md) for the full table and current translation status.

## Contribution checklist

- [ ] Frontmatter has `lang:` matching the file suffix (`en`, `ja`, `es`, `fr`, `de`, `ko`, `pt`, `ru`, ...)
- [ ] Do not translate: skill names, JSON field names, `id`, `type`, `confidence`
- [ ] Preserve all markdown structure, tables, and code fences
- [ ] Keep emoji audience tags (🔬 🔥 💼 ⚠️) unchanged
- [ ] Do not alter the meaning of the 4 core principles (see README "Critical use")
- [ ] Update `languages.md` translation status when you add a language
