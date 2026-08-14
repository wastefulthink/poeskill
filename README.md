# poeskill

一个面向真实处境的商业思维工具箱。给你一套可交互的诊断、内容、认知与系统工具，帮你把模糊的问题想清楚、把想清楚的事做出来。

> **完全独立重写的开源版本**：本仓库不包含上游  的任何作者署名文本、个人推文原子库、付费社群导流或遥测代码。方法论思路受  启发，但全部内容（skill 提示词、案例、知识库、脚本）均已重写为原创表达。许可证为 MIT。

## 它能做什么

按使用场景分四组：

**诊断业务 / 商业问题**
- `/poe-diagnosis` — 商业模式诊断，问诊 + 体检两种模式，逐层消解问题
- `/poe-decision` — 把长期决策建成可回填、可复盘的本地档案
- `/poe-standard-answer` — 从商业史中寻找与你困境同构的历史机制
- `/poe-benchmark` — 找对标，用筛选流程排除噪音

**内容创作全流程**
- `/poe-good-question` — 把模糊问题改写成可推理的问题说明书
- `/poe-content` — 选题到文案的完整内容诊断
- `/poe-hook` — 短视频开头优化
- `/poe-script-flow` — 逐字稿衔接与流失点检查
- `/poe-resonate` / `/poe-spread` — 共鸣检测与传播心理解码
- `/poe-ai-check` — 识别 AI 写作痕迹
- `/poe-content-risk-check` — 发布前风险与平台审核检查
- `/poe-xhs-title` — 小红书标题公式
- `/poe-wechat-html` — Markdown 转微信公众号 HTML

**思维 / 认知工具**
- `/poe-deconstruct` — 用语言分析视角拆解模糊概念
- `/poe-action` — 用目的论视角诊断"知道该做却做不动"
- `/poe-slowisfast` — 识别贪快与必要摩擦，设计长期复利路径
- `/poe-goal` — 把模糊愿望整理成可检查的目标

**系统工具（维护 poeskill 自身）**
- `/poe` — 主入口与动态路由
- `/poe-chatroom` / `/poe-chatroom-market` — 多角色讨论（含市场秩序学派视角）
- `/poe-save` / `/poe-restore` / `/poe-report` — 诊断状态存档、恢复与报告
- `/poe-knowledge` / `/poe-content-system` — 本地知识库与内容资产工程
- `/poe-learning` — 交互式学习
- `/poe-verify` — 对任何结论做反方核查（证据溯源 / 反例 / 信源评级 / 利益冲突检查）
- `/poe-update` — 从本仓库更新
- `/poe-bridge` / `/poe-agent-migration` — 桥接到其他 Agent 与工作台迁移

## 安装

```bash
# 1. 克隆仓库
git clone https://github.com/<你的用户名>/poeskill.git

# 2. 复制 skills 到你的 Agent 技能目录（以 WorkBuddy 为例）
cp -r poeskill/skills/* ~/.workbuddy/skills/

# 3. 知识库（可选，诊断类 skill 引用它做信源核验）
cp -r poeskill/知识库/* 你希望存放的位置/
```

> 若你的 Agent 支持相对路径引用，直接把 `skills/` 与 `知识库/` 放在同一父目录下即可，skill 内已使用相对路径引用知识包。

## 知识库：四大知识专题

`知识库/` 内含 50 条原子知识，来自 15 位哲学家/物理学家的思想（休谟、康德、波普尔、维特根斯坦、多伊奇、罗素、斯密、米塞斯、哈耶克、老子、阿德勒、叔本华、马可·奥勒留、尼采、加缪），每条带原著出处与受众标注（🔬 科学家高偏好 / 🔥 大众高流量 / 💼 商业圈层高频 / ⚠️ 需选择性参考）。

- `原子库/atoms_poe.jsonl` — 主数据（格式与原库兼容）
- `Skill知识包/` — 按 skill 聚合的 12 个知识包
- `哲学概念词典.md` — 高频概念速查

## 批判性使用（重要）

poeskill 是思维工具，不是答案提供者：

1. 所有结论型 skill 输出**必须**附带信源强度标注（A/B/C/D），C 级以下只能当思路
2. 定性归因必须附可证伪条件
3. 拿不准时跑 `/poe-verify` 做反方核查
4. 涉及重大决策（投资、职业、健康），请交叉验证，不采信单一框架结论
5. `/poe-action` 等心理类工具是自我认知辅助，不是心理咨询

## 更新

- 主入口每 24 小时最多联网检查一次版本（只读本仓库 `UPDATE.json`）
- `/poe-update` 从本仓库同步，保留你的 `~/.poe/` 存档
- 更新前建议先 `git pull` 对比变更

## 许可证

MIT License。详见 [LICENSE](LICENSE)。

## 致谢与声明

- 方法论思路受 [](https://github.com//)（）启发，本仓库为独立重写的原创实现，不含其受保护内容
- 本仓库无付费社群、无课程导流、无任何形式的商业变现入口
- 知识库内容基于公开的哲学与经济学著作整理，引用均标注原著出处
