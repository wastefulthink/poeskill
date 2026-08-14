# poeskill language codes & translation status

## Language code table (ISO 639-1 + region where needed)

| Code | Language | Status |
|---|---|---|
| `zh-CN` | 简体中文 (source) | ✅ master |
| `en` | English | ✅ README.en.md shipped; skills translatable via `SKILL.en.md` |
| `ja` | 日本語 | 🟡 open for contribution |
| `es` | Español | 🟡 open for contribution |
| `fr` | Français | 🟡 open for contribution |
| `de` | Deutsch | 🟡 open for contribution |
| `ko` | 한국어 | 🟡 open for contribution |
| `pt` | Português | 🟡 open for contribution |
| `ru` | Русский | 🟡 open for contribution |
| `id` | Bahasa Indonesia | 🟡 open for contribution |
| `ar` | العربية | 🟡 open for contribution |

Legend: ✅ shipped · 🟡 open for contribution

## What is tagged

| Layer | Marker | Location |
|---|---|---|
| Skill definitions | `lang:` in frontmatter | `skills/<poe-*>/SKILL.md` (all 32) |
| Power units (能量单元) | `language` field per JSON entry | `知识库/能量库/powers_poe.jsonl` (all 50) |
| Knowledge packs | `> 语言:` header line | `知识库/Skill知识包/*.md` |
| README | file suffix | `README.md` (zh-CN) / `README.en.md` (en) |

## Adding a language — quick path

1. Pick a code from the table above (e.g. `ja`)
2. Translate `README.md` → `README.ja.md` (or start from `README.en.md`)
3. Translate any skill: create `skills/poe-xxx/SKILL.ja.md` with frontmatter `lang: ja`
4. Translate power units: duplicate JSON lines with `"language": "ja"` and translated `knowledge`
5. Update this table (move the row to ✅ or note partial coverage)
