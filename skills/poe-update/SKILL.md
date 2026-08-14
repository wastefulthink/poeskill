---
lang: zh-CN
name: poe-update
description: 从 GitHub 更新 poeskill，并保留其他 Skill 与用户存档。用户要求更新、升级、检查 poeskill 版本，或在更新提醒后回复 1 时使用。
---

# poe-update：更新 poeskill

用户已经明确要求更新 poeskill，或在上一条 poeskill 更新提醒后回复了 `1`。两种情况都直接执行更新，不再做第二次文字确认；宿主若要求 Shell 权限，由用户在宿主的权限窗口中决定。

只有上一条助手回复明确包含 poeskill 更新提醒时，单独回复的 `1` 才代表更新。缺少这段上下文时，不要自行解释数字含义。

## 更新范围

- 只更新本仓库 `POESKILL_GITHUB_USER/poeskill`（GitHub）。
- 保留用户在 `~/.poe/` 中的存档、报告和决策记录。
- 不更新用户安装的其他 Skill。
- 不创建后台任务、定时任务或 Agent Hook。
- **不使用任何第三方下载执行工具**（如 `npx skills add`）。更新只走 git，全程可审计。

## 执行步骤

1. 定位本 `SKILL.md` 所在目录，确定当前 Agent 的 skills 目录（WorkBuddy 为 `~/.workbuddy/skills/`，其他 Agent 见 README）。

2. 拉取最新源码到本地缓存目录：

   ```bash
   mkdir -p "$HOME/.poe/repo"
   if [ -d "$HOME/.poe/repo/.git" ]; then
     git -C "$HOME/.poe/repo" pull --ff-only
   else
     git clone --depth 1 https://github.com/POESKILL_GITHUB_USER/poeskill.git "$HOME/.poe/repo"
   fi
   ```

3. 对比版本：若本地已安装版本的 VERSION 与仓库 `VERSION` 一致，告知用户已是最新，结束。

4. 有新版时，先展示 `UPDATE.json` 中的更新说明（notice），再执行同步：

   ```bash
   cp -r "$HOME/.poe/repo/skills/poe"* ~/.workbuddy/skills/
   cp -r "$HOME/.poe/repo/知识库"* "$HOME/.poe/knowledge-base/"
   ```

   目标 skills 目录按当前 Agent 的实际目录调整。同步前可先 `git -C "$HOME/.poe/repo" diff HEAD~1` 检查变更内容，确认无异常再复制。

5. 记录本次更新时间，避免当前对话仍加载旧 Skill 时重复提醒：

   ```bash
   mkdir -p "$HOME/.poe" && date +%s > "$HOME/.poe/update_check_at"
   ```

6. 根据退出状态确认是否完成。成功时告诉用户更新已完成，并提醒用户新建一次对话后再使用新能力。

7. 失败时，用一句话说明失败原因和下一步需要用户处理的权限或网络问题。不要把完整终端日志直接贴给用户，除非用户要求。

## 回复格式

成功：

> poeskill 已更新完成。当前对话如果还没有读取到新能力，新建一次对话后即可使用。

失败：

> poeskill 没有更新完成：{简短原因}。处理完 {权限或网络问题} 后，再说一次「更新 poeskill」。

## 边界

- 用户只问版本、更新内容或是否需要更新时，先回答问题，不执行命令。
- 用户明确要求检查更新且希望实际同步时，按本 Skill 更新。
- 不使用 `npx skills add/update` 等第三方工具，只使用 git 与 cp。

---

完成当前任务后直接结束。只有用户明确询问下一步，且当前环境已经安装 `/poe` 时，简短提示：「下一步不确定时，可以输入 `/poe`。」
