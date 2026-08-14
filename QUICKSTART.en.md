# Quickstart (3 minutes, no jargon)

> No technical background needed. Follow along — 3 minutes to your first "push back" from your AI.

🌐 [简体中文](QUICKSTART.md) · [English](QUICKSTART.en.md) · [한국어](QUICKSTART.ko.md) · [Русский](QUICKSTART.ru.md) · [Español](QUICKSTART.es.md) · [日本語](QUICKSTART.ja.md) · [Français](QUICKSTART.fr.md) · [Deutsch](QUICKSTART.de.md) · [Português](QUICKSTART.pt.md)

---

## The one thing you need to remember

**After install, you only need to remember one command: `/poe`**

It figures out what you're trying to do and routes you to the right tool.
**You don't need to learn any of the 32 skill names.**

---

## Step 1 — Install (≈30 seconds)

In a terminal (Windows: use Git Bash or WSL):

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

Or, if you already downloaded the project folder, run this inside it:

```bash
bash install.sh
```

The installer auto-detects your AI tools (Claude Code, Codex, Cline,
WorkBuddy, …), asks for confirmation, and installs the skills. You'll see:

```
[poeskill] done. Run /poe in your Agent to get started.
```

> **No bash?** See [Windows tips](#windows-tips).

## Step 2 — Say your first sentence (30 seconds)

Open your AI tool and just type — plain language, no format needed:

```
/poe I have an idea: a coffee shop AI queue-ordering mini-app. Should I do it?
```

That's it. It takes it from there.

## Step 3 — Experience the pushback (2 minutes)

A normal AI says "great idea, here's how to build it." An AI with poeskill
argues with you first:

- It challenges your premise: "**Is the queue really their biggest pain
  point? Have you verified that?**"
- It asks for evidence: "Will the owner actually pay for this? Do you have
  proof?"
- It gives a falsifiable conclusion: "**Don't do it — unless** X happens"
  instead of "it depends on your execution."

**That's the whole point: it argues first so you make better decisions.**

---

## How do I know the install worked?

| Method | How |
|---|---|
| Just try it | Type `/poe` — if you get onboarding/routing, it's installed |
| Check the folder | 32 `poe-*` folders exist in your skills dir (e.g. `~/.claude/skills/`) |
| Check install output | `skills installed → <dir> (32 skills)` means success |

## Common situations, plain language

You don't need this table — `/poe` routes automatically. It's just to give
you a mental map:

| What you want | Just say | Under the hood |
|---|---|---|
| Decide if an idea is worth doing | "help me analyze whether I should do this" | `/poe-diagnosis` |
| Fact-check a claim or article | "help me verify this claim" | `/poe-verify` |
| Can't articulate what you want | "help me clarify this goal" | `/poe-goal` |
| Know what to do but can't start | "why do I keep procrastinating" | `/poe-action` |
| A buzzword means nothing concrete | "dismantle this word for me" | `/poe-deconstruct` |
| Can't write a good opening | "help me improve this hook" | `/poe-hook` |
| A decision you might regret later | "help me track this decision long-term" | `/poe-decision` |

## Windows tips

1. **Use Git Bash or WSL** to run the installer — it's a bash script, and
   both ship with bash.
2. **Don't want bash at all?** Fine: have someone (or your AI tool) run the
   install for you. After that, using it is just typing `/poe` — no terminal
   needed.
3. **Where did it install?** The installer prints `skills installed → <path>`.
   Remember that path.
4. **Installer stuck or erroring?** Paste the error to `/poe` ("I hit an
   install problem"), or open an issue.

---

## Next steps

- What each tool actually does → [README](README.en.md)
- Proof it works → [`benchmark/`](benchmark/) (same question: bare 6/25 vs
  with poeskill 25/25)
- Any problem → tell `/poe` "I have a problem", or open an
  [issue](https://github.com/wastefulthink/poeskill/issues/new)

> v3.5.0 ｜ MIT ｜ Runs locally: no telemetry, no signup, no account
