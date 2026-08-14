# scripts

poeskill 知识库与原创化处理的生成脚本。全部由本项目维护，可复现 `知识库/` 的输出。

| 文件 | 作用 |
|---|---|
| `powers_phil_p1.py` | 四大专题知识库数据 Part 1（科学认识论 + 市场秩序，19 条能量） |
| `powers_phil_p2.py` | 四大专题知识库数据 Part 2（人性动机 + 价值哲学，31 条能量） |
| `build_phil.py` | 构建脚本：生成 `powers_poe.jsonl`（带 language 字段）、12 个 Skill 知识包、哲学概念词典 |
| `originalize.py` | 原创化第一轮：品牌统一与去独断话术（→poeskill、公理→假设） |
| `originalize2.py` | 原创化第二轮：作者个人案例通用化、作者指代清理、风格标记清理 |

复现知识库：

```bash
python scripts/build_phil.py
```

> i18n：`powers_poe.jsonl` 每条带 `language: zh-CN` 标记；翻译请复制条目并改 `language` 与 `knowledge` 字段，见 [i18n/](../i18n/)。

> 注：`originalize*.py` 记录的是本项目从上游思路到原创版的清洗过程，供审计使用；新贡献者不需要运行它们。
