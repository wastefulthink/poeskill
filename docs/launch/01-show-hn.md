# Show HN 发布物料

> 发布前替换：`POESKILL_GITHUB_USER` → 真实 GitHub 用户名，并核对仓库 URL。

## 推荐标题（≤80 字符，择一）

1. `Show HN: I built 32 skills that teach AI agents to disagree with you`
2. `Show HN: Your AI keeps agreeing with you – so I made it push back`
3. `Show HN: 32 agent skills + 305 cited power units to fight AI sycophancy`

## 主帖正文（英文）

```
Show HN: I built 32 skills that teach AI agents to disagree with you

Your AI has never once told you that your idea is bad. It agrees because it's
trained to be agreeable, and that is quietly destroying the quality of your
decisions.

I spent the last month building poeskill: 32 skills that turn Claude Code,
Codex, Cline, WorkBuddy (any agent with a skills directory) into a
critical-thinking partner for real business situations.

What it actually does:

- /poe-good-question  — rewrites a vague ask into a reasoning-ready spec
- /poe-diagnosis      — runs consultation + checkup modes, forces falsifiable
                        conditions instead of your first guess
- /poe-verify         — stress-tests a conclusion with counter-evidence and
                        grades source strength A–D
- /poe-deconstruct    — asks what a buzzword actually refers to
- /poe-goal           — turns "I want to do something" into a checkable
                        deliverable with acceptance criteria
- /poe-action         — finds the hidden goal your procrastination is serving
                        (Adlerian psychology, not productivity tips)

Why it's not just 32 prompts:

The knowledge layer is the part I'm most proud of. 305 "power units"
distilled from 25 thinkers — Hume, Hayek, Smith, Mises, Popper, Feynman,
Kahneman, Taleb, Drucker, Porter, Schumpeter, Shannon, Turing, Aristotle,
Keynes, Soros, Groves, and more. Every single unit carries its original
source: citation link, title, year. No paraphrased-slop knowledge base.

Technical details:

- All 32 skills rewritten from scratch. No content, no telemetry, no community
  funnel was carried over from anywhere.
- MIT licensed.
- Data layer is language-neutral (units tagged `language`), content is
  translatable (`lang:` in frontmatter). English + Simplified Chinese now.
- One-line installer that auto-detects Claude Code / Codex / Cline / Kiro /
  Qwen Code / WorkBuddy skill directories: `curl -fsSL <URL>/install.sh | bash`
- Local CI that validates frontmatter, JSONL integrity, and cross-references.

Honest limitations:

- The 305 units are curated, not exhaustive. Some classical thinkers are
  underrepresented; I'd rather ship 305 verified units than 3000 unverified.
- Skills run as slash commands in agent shells — they don't hook into your
  model's weights. If your model is aggressively sycophantic at the
  foundation level, no skill wrapper fully fixes that. It does give it
  explicit tools and procedures to disagree *productively*.
- 100% of the knowledge base is in Chinese-derived curation right now;
  English translations of the 305 units are next on the roadmap.

Try it in 60 seconds (no account, no API key):

  git clone <repo-url>
  cd poeskill && ./install.sh --dry-run   # see what it would do
  ./install.sh                            # install to detected agents

Then in any agent: /poe-deconstruct "synergy" or /poe-verify "my plan is solid"

Star if you want the English knowledge base next:
<repo-url>

All feedback — especially "this skill is actually bad at X" — is the entire
point of the project. The repo has issue templates for exactly that.
```

## 评论区自答（发帖后立即贴出）

```
Author here. Happy to answer questions about:

1. How the knowledge base was built (the 25 thinkers, the citation pipeline,
   the 80-term dictionary)
2. Why skill-layer critique beats prompt-layer critique for agents
3. The CI design — how a "knowledge repo" validates itself
4. Anything you think is wrong with the approach

One thing I deliberately did NOT do: collect any usage data. No telemetry,
no "community" signup, no hidden funnel. If you want to know how it's used,
open an issue and ask.
```

## 发布时机与规则

- 周一至周四 07:00–09:00 PT 为 HN 活跃高峰；避开发布当天同时发 Reddit（错开 ≥ 2 小时）。
- 发帖后 30 分钟内持续刷新回复区，逐条认真回答（HN 排名权重最高的是作者参与度）。
- 不删负面评论；把"这没用"类评论当成 `/poe-verify` 的实战，用反例回应。
- 标题一旦发出不可修改，只改一次；若标题无人问津（1 小时 < 5 评论），用新账号思路换标题重发一次（间隔 ≥ 24h）。
