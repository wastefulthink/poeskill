# Benchmark

**The falsifiable proof that poeskill changes how an AI answers.**

One business decision, run twice on the same model: once bare, once with the
poeskill stack active. The gap between the two outputs is the product.

## Why this exists

Anyone can claim their skills make AI "think better". Very few projects show
the before/after. `benchmark/` is poeskill's answer to that: a reproducible
setup, a fixed case, and honest scoring — not a screenshot of a lucky run.

## How it works

```
benchmark/
├── case-01-queue-app.md        # the decision case (premise with a trap)
├── prompts/
│   ├── baseline.md             # control: plain helpful assistant
│   └── poeskill.md             # treatment: poeskill routing + knowledge unit
├── run_benchmark.py            # stdlib-only runner (anthropic / OpenAI-compatible)
└── results/
    ├── baseline.md             # example output (control)
    ├── poeskill.md             # example output (treatment)
    └── comparison.md           # scored table
```

**Run it yourself** (needs an API key):

```bash
# Anthropic (Claude)
python benchmark/run_benchmark.py --prompt both --provider anthropic

# OpenAI-compatible (OpenAI / DeepSeek / DashScope...)
python benchmark/run_benchmark.py --provider openai-compatible \
    --model gpt-4o --base-url https://api.openai.com/v1
```

Auth comes from `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` (or `--api-key`).
Results land in `benchmark/results/<timestamp>/` as
`baseline.md` + `poeskill.md` + `comparison.md` (blank scoring table to fill in).

## Current result (example outputs, case 01)

| Dimension (0–5) | baseline | poeskill |
|---|---:|---:|
| Questions the premise | 0 | 5 |
| Asks for missing data | 2 | 5 |
| Falsifiable verdict | 0 | 5 |
| Cheap validation path | 2 | 5 |
| Specific risk warning | 2 | 5 |
| **Total /25** | **6** | **25** |

> The files under `results/` are labeled example outputs — representative
> shapes, not fabricated "fresh" runs. Score them yourself after a real run.

## Eval rubric

Scoring is deliberately coarse (0–5 per dimension, see `comparison.md`) so a
human can grade any model's output in under a minute. The five dimensions
are the minimum a *decision*, as opposed to an *execution plan*, must contain:

1. Premise challenged — is the user's asserted pain verified?
2. Missing data requested — named, not generic ("do research")
3. Falsifiable verdict — "don't, unless X" beats "it depends on you"
4. Cheap validation — a 1-2 week test that costs nothing
5. Specific risk — named competitors/costs, not "beware of competition"

## Roadmap for this dir

- [ ] Case 02 — `/poe-verify` on a viral claim (fake quote debunk)
- [ ] Case 03 — `/poe-decision` on "should we kill this product line"
- [ ] Multi-model scoreboard: same case across Claude/GPT/DeepSeek, published
      as a table in this README
- [ ] CI hook: rerun benchmark on tagged releases, diff the scores
