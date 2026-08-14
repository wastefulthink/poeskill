# poeskill

> 🌐 [简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

---

**你的 AI 一直在附和你。**

你问它"这个想法行不行"，它说"很有潜力"。你问它"我该不该做"，它说"取决于你的执行力"。

它永远不说"不"。它永远不追问"你验证过吗"。

poeskill 改的就是这件事——32 个技能，把任何 AI 工具变成一个会跟你抬杠的伙伴。它先质疑你的前提，再追问你的数据，最后给出一个可以被证伪的结论。不是"听起来很对"，而是"对或者不对，你能验证"。

---

## 为什么做这个

我用了很久的 AI 工具，发现一个规律：**它越聪明，附和你越快**。

你给它一个漏洞百出的商业计划，它帮你补全；你给它一个模糊的愿望，它帮你拆成步骤——但从没人在第一步问你："等等，这件事的前提成立吗？"

真正好的决策，不是来自"帮我执行"，而是来自"帮我质疑"。所以我把 25 位思想家——从休谟到哈耶克、从费曼到卡尼曼——的思维方法，做成了 305 条带出处的知识单元，塞进了 32 个可以一键安装的技能里。

每个技能的设计原则只有一条：**它必须先跟你抬杠，才能帮你做事。**

---

## 30 秒安装

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

或者本地克隆：

```bash
git clone https://github.com/wastefulthink/poeskill.git
cd poeskill
bash install.sh            # 自动检测你的 AI 工具
bash install.sh --all      # 装进所有检测到的工具
bash install.sh --target ~/.claude/skills
```

支持 Claude Code、Codex、Cline、WorkBuddy、Kiro、Qwen Code 等所有"从文件夹读技能"的 Agent。

装完之后，**你只需要记住一个命令：`/poe`。** 32 个技能的名字一个都不用记——它会自动帮你路由。

---

## 头 3 分钟会发生什么

1. 打开你的 AI 工具，用大白话输入：

   ```
   /poe 我有个想法：想做个咖啡店的 AI 排队小程序，该不该做？
   ```

2. 普通 AI 会说"这个想法很好，建议你……"。装了 poeskill 的 AI 会先问你：
   - "排队真的是这家店最大的痛点吗？你验证过吗？"
   - "老板愿意为这个功能掏多少钱？你有证据吗？"
   - 最后给出："**不建议做，除非**出现 XX 情况"——而不是"取决于你的执行力"

3. **它先抬杠，是为了帮你做对决定。** 这就是全部意义。

第一次用？看 [3 分钟上手指南](QUICKSTART.md)（零术语）。

---

## 它能干什么

**诊断商业问题**
- `/poe-diagnosis` — 商业模式诊断，问诊 + 体检双模式
- `/poe-decision` — 把长期决策建成可回填、可复盘的档案
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

---

## 知识库：305 条 · 25 位思想家

`knowledge/` 里装的不是泛泛的"AI 总结"，而是从 25 位思想家的原著中提炼的 305 条能量知识——休谟、康德、波普尔、维特根斯坦、多伊奇、罗素、斯密、米塞斯、哈耶克、老子、阿德勒、叔本华、马可·奥勒留、尼采、加缪、亚里士多德、密尔、韦伯、凯恩斯、弗里德曼、熊彼特、索罗斯、格鲁夫、达尔文、费曼、爱因斯坦、牛顿、香农、图灵、培根、笛卡尔、芒格、卡尼曼、塞勒、塔勒布、德鲁克、波特、西蒙、科斯、平克、丹尼特。

每一条都带原著出处。没有"信我没错"，只有"出处在这里，你自己判断"。

- `powers/powers_poe.jsonl` — 主数据集
- `Skill知识包/` — 按 skill 聚合的 12 个知识包
- `philosophy-glossary.md` — 80 个高频概念速查

---

## 效果可量化

同一道商业决策题，同一个模型跑两遍——裸跑 vs 挂载 poeskill。案例 01 中裸跑得分 **6/25**，poeskill **25/25**。模型相同、问题相同，唯一变量是 AI 有没有被要求跟你抬杠。

```bash
python benchmark/run_benchmark.py --prompt both   # 需要 API key
```

题目、双 prompt、运行脚本与评分标准见 [`benchmark/`](benchmark/)。**差距本身就是产品。**

---

## 为什么叫 poe

三层意思：

1. **致敬埃德加·爱伦·坡**——推理文学奠基人。他笔下的侦探从不轻信表面叙事，而是从细小线索反推真相。这正是本工具的气质：`/poe-diagnosis` 从症状探病根、`/poe-verify` 对任何结论做反方核查、`/poe-deconstruct` 拆解被滥用的大词。
2. **Problem-Oriented Engine**——面向问题的引擎，每个工具都以问题为起点，不生产标准答案。
3. **独立命名**——poe 简短、好记、跨语言无负面联想。

---

## 值得你点 star 的理由

- **它会跟你抬杠。** 整个工具箱的意义就是不同意你——每个诊断型 skill 都必须给结论附可证伪条件与信源强度评级
- **一切可验证。** 305 条能量，每条带出处，没有"信我没错"
- **完全本地运行。** 无遥测、无 SaaS、无账号，你的问题不出你的机器
- **MIT + 完全原创。** 从零独立撰写，可以自由 fork、vendoring、在其上构建

---

## 批判性使用（重要）

poeskill 是思维工具，不是答案机器：

1. 所有结论型 skill 输出**必须**附带信源强度标注（A/B/C/D），C 级以下只能当思路
2. 定性归因必须附可证伪条件
3. 拿不准时跑 `/poe-verify` 做反方核查
4. 涉及重大决策（投资、职业、健康），请交叉验证，不采信单一框架结论
5. `/poe-action` 等心理类工具是自我认知辅助，不是心理咨询

---

## 更新

- 主入口每 24 小时最多联网检查一次版本（只读本仓库 `UPDATE.json`）
- `/poe-update` 从本仓库同步，保留你的 `~/.poe/` 存档
- 更新前建议先 `git pull` 对比变更

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)（含 i18n 流程）、[ROADMAP.md](ROADMAP.md)、[CHANGELOG.md](CHANGELOG.md)。

## 许可证

MIT License。详见 [LICENSE](LICENSE)。

## 请我喝杯咖啡

如果 poeskill 帮你想清楚了某个决定，可以请我喝杯咖啡：

[![Buy Me a Coffee](https://img.shields.io/badge/☕-请我喝咖啡-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xueyegog)

完全自愿——不赞助也照样用、照样更新。

## 致谢与声明

- 本仓库为完全独立的原创实现，全部 Skill、知识单元、脚本与文档均为本项目独立撰写
- 项目本身免费开源，唯一支持方式是自愿赞赏（见上方），无付费社群、无课程导流
- 知识库内容基于公开的哲学与经济学著作整理，引用均标注原著出处
