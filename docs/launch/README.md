# docs/launch — 发布战役物料

首日发布战役的完整物料包。围绕定位钩子 **"Your AI keeps agreeing with you"**（反主流叙事）编写。

## 文件索引

| 文件 | 内容 | 用途 |
|---|---|---|
| `01-show-hn.md` | Show HN 主帖 + 评论区自答 + 发布时机规则 | Hacker News 首发（流量峰值来源） |
| `02-reddit.md` | r/ClaudeAI + r/LocalLLaMA 两帖（不同角度） | 英文社区扩散 |
| `03-x-twitter.md` | X Thread（1 hook + 6 条）+ 备选单条 | X 自然流量 |
| `04-v2ex-jike.md` | V2EX + 即刻中文帖 | 中文社区 |
| `05-awesome-lists.md` | 7 个候选列表 + PR 模板 + 提交步骤 | 长尾流量 |
| `08-launch-checklist.md` | 发布前中后总清单 + 复盘表 + 诚实目标口径 | 总控 |

## 使用顺序

1. 发布前：按 `08-launch-checklist.md` 的 A 部分逐项完成（替换 `POESKILL_GITHUB_USER`、push、打 tag、建 Release）
2. 发布日：按 `08` 中 A3 的渠道顺序发 01→02→03→04，间隔 ≥ 2h
3. 发布后 48h：提交 `05` 的 awesome PR，回评所有渠道
4. 复盘：把指标填进 `08` 的 C 表，用于判断下一步

## 注意

- 所有文案中的 `POESKILL_GITHUB_USER` 为占位符，发布前必须全局替换为真实 GitHub 用户名
- 文案围绕"反主流叙事"钩子统一风格：诚实、具体、欢迎反驳——这和项目本身的定位一致
- 当前知识库 305 条为中文策展，英文翻译是 star 过千后的复利引擎（见 ROADMAP）
