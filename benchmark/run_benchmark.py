#!/usr/bin/env python3
"""poeskill benchmark runner.

Runs the same business-decision case twice — once without any skill
(baseline), once with the poeskill stack simulated (treatment) — and writes
both outputs plus a comparison template to benchmark/results/.

No third-party dependencies: only the stdlib, so it runs anywhere Python 3
does. Tested on Windows and Linux.

Usage:
  python benchmark/run_benchmark.py --case benchmark/case-01-queue-app.md \
      --prompt both --provider anthropic

  # OpenAI-compatible endpoint (e.g. OpenAI, DeepSeek, DashScope):
  python benchmark/run_benchmark.py --provider openai-compatible \
      --model gpt-4o --base-url https://api.openai.com/v1

Auth: reads ANTHROPIC_API_KEY / OPENAI_API_KEY from the environment, or take
--api-key. Never commit keys.
"""

import argparse
import json
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CASE = ROOT / "benchmark" / "case-01-queue-app.md"
PROMPTS = {
    "baseline": ROOT / "benchmark" / "prompts" / "baseline.md",
    "poeskill": ROOT / "benchmark" / "prompts" / "poeskill.md",
}
EVAL_DIMENSIONS = [
    "1. 是否质疑前提（排队真的是痛点吗）",
    "2. 是否追问缺失的关键信息（市场/竞品/付费意愿）",
    "3. 结论是否可证伪（有没有明确判断，而非\"取决于你\"）",
    "4. 是否给出低成本验证路径",
    "5. 风险提示是否具体（点名竞品/成本，而非泛泛而谈）",
]


def parse_prompt(path: Path) -> dict:
    """Extract the ```-fenced System prompt and User message from a prompt file."""
    text = path.read_text(encoding="utf-8")
    fences = re.findall(r"```\n(.*?)\n```", text, flags=re.S)
    if len(fences) < 2:
        sys.exit(f"[ERROR] {path.name}: expected 2 code fences (system + user)")
    return {"system": fences[0], "user": fences[1]}


def call_anthropic(key: str, model: str, system: str, user: str) -> str:
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps({
            "model": model,
            "max_tokens": 2000,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }).encode(),
        headers={
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.load(resp)
    return "".join(b.get("text", "") for b in data.get("content", []))


def call_openai_compat(base_url: str, key: str, model: str, system: str, user: str) -> str:
    req = urllib.request.Request(
        f"{base_url.rstrip('/')}/chat/completions",
        data=json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }).encode(),
        headers={"authorization": f"Bearer {key}", "content-type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.load(resp)
    return data["choices"][0]["message"]["content"]


def main() -> None:
    ap = argparse.ArgumentParser(description="poeskill benchmark runner")
    ap.add_argument("--case", default=str(DEFAULT_CASE), help="case file (markdown)")
    ap.add_argument("--prompt", choices=["baseline", "poeskill", "both"], default="both")
    ap.add_argument("--provider", choices=["anthropic", "openai-compatible"], default="anthropic")
    ap.add_argument("--model", default="claude-sonnet-4-20250514")
    ap.add_argument("--base-url", default="https://api.openai.com/v1", help="openai-compatible only")
    ap.add_argument("--api-key", default="", help="fallback if env var missing")
    ap.add_argument("--output-dir", default=str(ROOT / "benchmark" / "results"))
    args = ap.parse_args()

    key = args.api_key or {
        "anthropic": __import__("os").environ.get("ANTHROPIC_API_KEY", ""),
        "openai-compatible": __import__("os").environ.get("OPENAI_API_KEY", ""),
    }[args.provider]
    if not key:
        sys.exit(f"[ERROR] no API key. Set {args.provider.upper()} key or pass --api-key. "
                 f"(Repo ships example outputs; run this only when you want fresh numbers.)")

    out_dir = Path(args.output_dir) / datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir.mkdir(parents=True, exist_ok=True)

    case_text = Path(args.case).read_text(encoding="utf-8")
    runs = ["baseline", "poeskill"] if args.prompt == "both" else [args.prompt]

    for name in runs:
        print(f"[RUN] {name} via {args.provider}/{args.model} ...")
        p = parse_prompt(PROMPTS[name])
        try:
            if args.provider == "anthropic":
                out = call_anthropic(key, args.model, p["system"], p["user"])
            else:
                out = call_openai_compat(args.base_url, key, args.model, p["system"], p["user"])
        except urllib.error.HTTPError as e:
            sys.exit(f"[ERROR] {name}: HTTP {e.code} {e.read().decode(errors='replace')[:400]}")
        (out_dir / f"{name}.md").write_text(
            f"# {name} output\n\n> run: {datetime.now().isoformat()} | provider: "
            f"{args.provider} | model: {args.model}\n\n{out}\n",
            encoding="utf-8",
        )

    if args.prompt == "both":
        comp = out_dir / "comparison.md"
        lines = ["# Comparison\n", "Score each dimension 0-5 for both runs.\n",
                 f"| Dimension | baseline | poeskill |", "|---|---|---|"]
        for d in EVAL_DIMENSIONS:
            lines.append(f"| {d} | | |")
        lines += ["", "## Verdict", "", "Which answer would you bet money on? Quote the line that decides it.", ""]
        comp.write_text("\n".join(lines), encoding="utf-8")
        print(f"[DONE] results in {out_dir} — baseline.md / poeskill.md / comparison.md")


if __name__ == "__main__":
    main()
