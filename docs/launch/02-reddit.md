# Reddit 发布物料（r/ClaudeAI + r/LocalLLaMA）

> 发布前替换：`POESKILL_GITHUB_USER` → 真实 GitHub 用户名。
> 规则：两个 sub 帖错开 ≥ 2 小时发；正文不用同一模板，角度不同，避免"多平台同文"被降权。

---

## r/ClaudeAI 帖

**标题（择一）**
- `I built 32 Claude Code skills that make it argue with you instead of agreeing with you`
- `Claude Code keeps agreeing with me, so I built a skillset that forces it to disagree productively`

**正文**

```
TL;DR: a free, MIT, open-source skillset for Claude Code (and Codex/Cline/WorkBuddy)
that turns "whatever you say" into "here's why that's wrong, and here's what to
check instead". 305 knowledge units with real citations, 32 slash-commands.

Why I built it
---------------
The single most expensive failure mode I see with Claude Code isn't bad code —
it's agreement. I say "my plan is solid", it says "yes, your plan is solid".
No pushback, no falsifiable check, no counter-example. That's sycophancy, and
it compounds on every decision you make with it.

What the skills do (the ones I reach for daily)
---------------
/poe-good-question  — feeds it a vague ask, gets a reasoning-ready spec back
/poe-verify         — takes any conclusion, grades its sources A–D, demands
                      counter-evidence
/poe-diagnosis      — business-model diagnosis with consultation + checkup modes
/poe-deconstruct    — "synergy", "AI-native", "moat" → what do these actually
                      refer to?
/poe-decision       — long-term decisions become versioned, reviewable archives
                      you can reopen months later

Why it's not just a prompt
---------------
The knowledge layer. 305 power units distilled from 25 thinkers — Kahneman,
Taleb, Popper, Hayek, Mises, Drucker, Porter, Schumpeter, Shannon, Turing,
Keynes, Soros… every unit cites its original source (link + title + year).
A prompt is a mood; this is a reference library the agent can actually pull
from when you ask it to push back.

Also: no telemetry, no signup, no hidden "community", MIT. The upstream
project it's methodologically inspired by () is credited in the repo.

Install
---------------
curl -fsSL <repo-url>/install.sh | bash
(or: ./install.sh --all / --target claude-code / --dry-run)

Question for you: when Claude Code agrees with you, do you usually notice it
before or after it costs you something? Genuinely curious.
```

---

## r/LocalLLaMA 帖

**标题（择一）**
- `Model-agnostic "critical thinking" skillset for agents — works with local models too`
- `I built a citation-backed knowledge layer that makes any agent disagree with you (works with your local setup)`

**正文**

```
One of the things I noticed running local models: quantized models are *more*
sycophantic, not less. They'll agree with whatever framing you give them,
because that's what the alignment data rewards. So I built the fix at the
layer we actually control — the skill/agent layer, not the weights.

What this is
---------------
poeskill: 32 skills for any agent that supports a skills directory (Claude
Code, Codex, Cline, Kiro, Qwen Code, WorkBuddy — and anything else where you
can drop a folder of SKILL.md files). It works identically on a local
7B or a hosted frontier model, because the mechanics are procedural, not
parametric.

The part I want r/LocalLLaMA to critique
---------------
The knowledge layer is 305 "power units" distilled from 25 thinkers, each
with its source citation. My claim is: a *verifiable* knowledge base matters
more than a big one, especially for local models that can't afford huge
context. 305 units with citations beats 3000 units of paraphrase.

Questions I genuinely want feedback on:
1. Is a citation-per-unit knowledge layer useful for your local workflows,
   or does it mostly add context tokens for little gain?
2. Would you want this as a plain .md / RAG corpus (not skill-shaped), so you
   can plug it into your own retrieval setup?
3. For a 7B model — does procedural instruction (skills) actually overcome
   sycophancy at inference time in your experience, or does it just feel like
   it does?

Repo: <repo-url> (MIT, no telemetry, one-line installer)

Not selling anything. I want the design critiqued — that's the entire point
of the project.
```

---

## 通用规则

- 发完 30 分钟内逐条回评；把尖锐批评回复到主帖评论区，别私信。
- 不要用"upvote"引导语；用问题收尾，诱导讨论而非点赞。
- 两帖标题都避免大写轰炸和 emoji。
- 若帖子 2 小时内无互动，视为标题失败，换标题 24h 后重发（同 sub 一帖即可，别刷屏）。
