# Baseline prompt — no skill loaded

This is the *control* run: the same user message sent to the model with no
poeskill installed and no methodology instructions.

## System prompt

```
You are a helpful assistant. Answer the user's question in Chinese.
Be friendly and constructive.
```

## User message

```
我想做一个给咖啡店用的 AI 排队小程序：顾客扫码排队，实时显示预计等待
时间，还能提前点单，到店直接取。这主意怎么样？值不值得做？
```

## How to use

```
python benchmark/run_benchmark.py --case benchmark/case-01-queue-app.md \
  --prompt baseline --provider anthropic
```

Results are written to `benchmark/results/<timestamp>/baseline.md`.
