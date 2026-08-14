# Awesome 列表提交指引

> 目标：发布后 48h 内提交到 3–5 个高流量 awesome 列表，带来长尾自然流量。
> 提交前确认：仓库已有 README（英文主文件）、LICENSE（MIT）、可用的一行安装命令。

---

## 候选列表（按优先级排序）

| 列表 | 仓库 | 提交方式 | 说明 |
|---|---|---|---|
| awesome-claude-code | `hesreallyhim/awesome-claude-code` | PR README | 直接对口 Claude Code 用户 |
| awesome-ai-agents | `eurekadotai/awesome-ai-agents` | PR README | 高流量聚合列表 |
| awesome-llm-apps | `Shubhamsaboo/awesome-llm-apps` | PR README | 覆盖各类 LLM 应用 |
| awesome-ai-tools | `mahseema/awesome-ai-tools` | PR README | 通用 AI 工具 |
| awesome-agi-agents | `edarchimbaud/awesome-AGI-agents` | PR README | Agent 专项 |
| awesome-chatgpt-prompts 系 | 若干镜像 | PR README | 若有 skills 分类可投 |
| 中文侧：awesome-chatgpt-zh / 各类"AI 工具箱" | 按搜索热度 | PR | 发布后 1 周内补投 |

## 通用提交模板（PR body）

```
## What

Add poeskill — 32 skills that teach AI agents (Claude Code, Codex, Cline,
WorkBuddy) to argue with you instead of agreeing with you.

## Why it fits this list

- MIT licensed, zero telemetry, one-line installer (auto-detects 6 agent
  skill directories)
- Ships a verified knowledge core: 305 power units from 25 thinkers, every
  unit with its original source citation
- Not a wrapper/prompt dump — full skills system with local CI

## Checklist

- [x] README in English (main) + zh-CN
- [x] LICENSE (MIT)
- [x] One-line install: `curl -fsSL <repo-url>/install.sh | bash`
- [x] Screenshots? → 需要时补一张 ASCII/终端演示

Repo: https://github.com/wastefulthink/poeskill
```

## 操作步骤

1. `gh auth login`（或浏览器 fork）后 fork 目标列表仓库。
2. 在目标 README 的**对应分类**（如 `Tools` / `Agent frameworks` / `Productivity`）插入一行，格式严格遵循该列表的条目格式（通常 `- [name](url) - one-line description`）。
3. 提交 PR，body 用上方模板，勾选真实项。
4. 24h 无回应 → 在 PR 下礼貌 @ 维护者一次；48h 无回应 → 不催第二遍（避免被标记 spam）。
5. 记录每个 PR 的链接和状态到 `docs/launch/08-launch-checklist.md` 复盘表。

## 红线

- 每个列表最多提交一次；被拒后不要换账号重提。
- 描述里不写"10x""revolutionary"这类词；只写事实。
- 不提交到"赞助位/置顶位"类商业化列表（那是付费区，不划算且伤信誉）。
