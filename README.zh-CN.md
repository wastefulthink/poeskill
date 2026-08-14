# poeskill

> **Language**: [English](README.md) | **简体中文** (current) | 其他语言翻译见 [i18n/](i18n/)

**你的 AI 一直在附和你。poeskill 是教它唱反调的工具箱。**

32 个 skill，把任意 Agent（Claude Code、Codex、Cline、WorkBuddy……）变成面对真实商业处境的批判性思维伙伴——诊断问题、压力测试结论、拆解大词、把模糊愿望变成可验收的目标。

- ✅ **完全原创。** 不含任何上游作者的署名文本、个人推文数据库、付费社群导流或遥测代码。全部内容从零独立撰写，MIT 许可
- 📚 **可验证的知识内核。** 305 条能量知识，提炼自 25 位思想家——从休谟到哈耶克、从费曼到卡尼曼，每条都带原著出处（链接/书名/年份）
- 🌍 **数据层语言中立，内容层可翻译。** 能量单元带 `language` 标记、skill 带 `lang:` frontmatter、i18n 流程文档化

## 为什么叫 poe

三个层面：

1. **致敬埃德加·爱伦·坡**——推理文学奠基人。他笔下的侦探从不轻信表面叙事，而是从细小线索反推真相。这正是本工具箱的气质：`/poe-diagnosis` 从症状探病根、`/poe-verify` 对任何结论做反方核查、`/poe-deconstruct` 拆解被滥用的大词
2. **Problem-Oriented Engine**——三字母展开：面向问题的引擎，每个工具都以问题为起点，不生产标准答案
3. **独立改名**——上游是作者个人技能集，本项目原创重写后连名独立；poe 简短、跨语言无负面联想

## 原生提示词 vs poeskill

| | 直接提问 | poeskill |
|---|---|---|
| 问题描述 | 模糊，停留在你的第一直觉 | `/poe-good-question` 改写成可推理的问题说明书 |
| 诊断 | 你的第一个猜测 | `/poe-diagnosis` 问诊+体检双模式，强制给出可证伪条件 |
| 结论质量 | 听起来很自信 | `/poe-verify` 附信源强度评级（A–D）与反例 |
| 模糊愿望 | 一直模糊 | `/poe-goal` 变成带验收标准的可检查交付物 |
| 知道该做却做不动 | 讲道理 | `/poe-action` 找到拖延行为在服务的隐藏目标 |
| 大词 | 跟着重复 | `/poe-deconstruct` 追问这个词到底指什么 |
| 知识来源 | 模型泛化 | 305 条带出处能量 + 按 skill 聚合的知识包 |

## 它能做什么

**诊断业务 / 商业问题**
- `/poe-diagnosis` — 商业模式诊断，问诊 + 体检两种模式
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
- `/poe-action` — 诊断"知道该做却做不动"
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
- `/poe-skill-cleaner` — 审计 skill 中的隐藏商业意图

## 安装

一行命令（任意带 bash / Git Bash / WSL 的平台）：

```bash
curl -fsSL https://raw.githubusercontent.com/<你的用户名>/poeskill/main/install.sh | bash
```

本地克隆安装：

```bash
git clone https://github.com/<你的用户名>/poeskill.git
cd poeskill
bash install.sh            # 自动检测你的 Agent skills 目录
bash install.sh --all      # 装进所有检测到的 Agent
bash install.sh --target ~/.claude/skills
```

手动安装到指定 Agent：

```bash
# Claude Code
cp -r skills/* ~/.claude/skills/
# Codex
cp -r skills/* ~/.codex/skills/
# WorkBuddy
cp -r skills/* ~/.workbuddy/skills/
# 知识库（可选，诊断类 skill 引用它做信源核验）
cp -r 知识库 ~/poeskill-知识库
```

> Windows 无 bash：用 PowerShell 执行同样的 `cp -r`，或用 Git Bash / WSL。

## 前 3 分钟

装完之后，你只需要记住**一个命令：`/poe`**——它会自动帮你路由到正确的 skill，32 个名字一个都不用记。

1. 安装（一行命令，约 30 秒）
2. 打开你的 AI 工具，用大白话输入，不需要任何格式：
   `/poe 我有一个想法：想做个咖啡店的 AI 排队小程序，该不该做？`
3. 注意看它先质疑你的前提、再给出结论——这就是它的价值。

新手？→ [QUICKSTART.zh-CN.md](QUICKSTART.zh-CN.md) · English → [QUICKSTART.md](QUICKSTART.md)

## 知识库：305 条能量 · 25 位思想家

`知识库/` 内含 **305 条能量知识**，提炼自 **25 位思想家**（休谟、康德、波普尔、维特根斯坦、多伊奇、罗素、斯密、米塞斯、哈耶克、老子、阿德勒、叔本华、马可·奥勒留、尼采、加缪、亚里士多德、密尔、韦伯、凯恩斯、弗里德曼、熊彼特、索罗斯、格鲁夫、达尔文、费曼、爱因斯坦、牛顿、香农、图灵、培根、笛卡尔、芒格、卡尼曼、塞勒、塔勒布、德鲁克、波特、西蒙、科斯、平克、丹尼特），每条带原著出处与受众标注（🔬 科学家高偏好 / 🔥 大众高流量 / 💼 商业圈层高频 / ⚠️ 需选择性参考）。

- `能量库/powers_poe.jsonl` — 主数据（格式与原库兼容）
- `Skill知识包/` — 按 skill 聚合的 12 个知识包（每包 30–160 条）
- `哲学概念词典.md` — 80 个高频概念速查

## 为什么值得点 star

- **它会跟你抬杠。** 整个工具箱的意义就是不同意你——每个诊断型 skill 都必须给结论附可证伪条件与信源强度评级
- **一切可验证。** 305 条能量，每条带出处，没有"信我没错"
- **完全本地运行。** 无遥测、无 SaaS、无账号，问题不出你的机器
- **MIT + 完全原创。** 可以自由 fork、vendoring、在其上构建

## Benchmark：效果可量化

同一道商业决策题，同一个模型跑两遍——裸跑 vs 挂载 poeskill。案例 01 中裸跑
得分 **6/25**，poeskill **25/25**。模型相同、问题相同，唯一变量是 AI 有没有
被要求跟你抬杠。

```bash
python benchmark/run_benchmark.py --prompt both   # 需要 API key
```

题目、双 prompt、运行脚本与评分标准见 [`benchmark/`](benchmark/)。
差距本身就是产品。

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

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)（含 i18n 流程）、[ROADMAP.md](ROADMAP.md)、[CHANGELOG.md](CHANGELOG.md)。

## 许可证

MIT License。详见 [LICENSE](LICENSE)。

## 致谢与声明

- 本仓库为完全独立的原创实现，全部 Skill、知识单元、脚本与文档均为本项目独立撰写
- 本仓库无付费社群、无课程导流、无任何形式的商业变现入口
- 知识库内容基于公开的哲学与经济学著作整理，引用均标注原著出处
