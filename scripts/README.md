# scripts

poeskill 知识库生成脚本。全部由本项目维护，可复现 `knowledge/` 的输出。

| 文件 | 作用 |
|---|---|
| `powers_phil_p1.py` | 四大专题知识库数据 Part 1（科学认识论 + 市场秩序，19 条能量） |
| `powers_phil_p2.py` | 四大专题知识库数据 Part 2（人性动机 + 价值哲学，31 条能量） |
| `build_phil.py` | 构建脚本：生成 `powers_poe.jsonl`（带 language 字段）、12 个 Skill 知识包、哲学概念词典 |

复现知识库：

```bash
python scripts/build_phil.py
```

> i18n：`powers_poe.jsonl` 每条带 `language: zh-CN` 标记；翻译请复制条目并改 `language` 与 `knowledge` 字段，见 [i18n/](../i18n/)。
