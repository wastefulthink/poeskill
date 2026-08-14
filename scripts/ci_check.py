#!/usr/bin/env python3
"""poeskill repo CI checks (local or GitHub Actions).

Checks:
  1. Every skills/*/SKILL.md has valid YAML frontmatter with a `lang:` field.
  2. Every line in 知识库/能量库/powers_poe.jsonl is valid JSON and carries the
     required fields with legal values.
  3. install.sh parses (bash -n equivalent via subprocess).
  4. Cross-reference: every id in the jsonl is unique; knowledge packs reference
     only existing ids.

Exit code 0 on success, 1 on any failure.
"""
import json
import os
import shutil
import subprocess
import sys
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILURES = []


def fail(where, msg):
    FAILURES.append(f"[{where}] {msg}")


def check_frontmatter():
    skills_dir = os.path.join(ROOT, "skills")
    if not os.path.isdir(skills_dir):
        fail("frontmatter", "skills/ directory missing")
        return
    for name in sorted(os.listdir(skills_dir)):
        md = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(md):
            fail("frontmatter", f"skills/{name}: SKILL.md missing")
            continue
        text = open(md, encoding="utf-8").read()
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
        if not m:
            fail("frontmatter", f"skills/{name}: no YAML frontmatter")
            continue
        fm = m.group(1)
        if not re.search(r"^lang:\s*\S+", fm, re.M):
            fail("frontmatter", f"skills/{name}: missing `lang:` in frontmatter")
        # frontmatter must not contain stray `---` inside the block
        if fm.count("---") > 0:
            fail("frontmatter", f"skills/{name}: unexpected `---` inside frontmatter")


def check_jsonl():
    path = os.path.join(ROOT, "知识库", "能量库", "powers_poe.jsonl")
    if not os.path.isfile(path):
        fail("jsonl", "powers_poe.jsonl missing")
        return
    required = {"id", "knowledge", "original", "url", "date", "topics", "skills", "type", "confidence"}
    ids = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError as e:
                fail("jsonl", f"line {i}: invalid JSON ({e})")
                continue
            missing = required - set(d)
            if missing:
                fail("jsonl", f"line {i} ({d.get('id','?')}): missing fields {sorted(missing)}")
            if d.get("confidence") not in ("high", "medium", "low"):
                fail("jsonl", f"line {i} ({d.get('id','?')}): bad confidence")
            if d.get("type") not in ("principle", "method", "case", "anti-pattern", "insight", "tool"):
                fail("jsonl", f"line {i} ({d.get('id','?')}): bad type")
            if not isinstance(d.get("skills"), list) or not d["skills"]:
                fail("jsonl", f"line {i} ({d.get('id','?')}): skills must be non-empty list")
            if not isinstance(d.get("topics"), list) or not d["topics"]:
                fail("jsonl", f"line {i} ({d.get('id','?')}): topics must be non-empty list")
            ids.append(d.get("id"))
    dupes = {x for x in ids if ids.count(x) > 1}
    if dupes:
        fail("jsonl", f"duplicate ids: {sorted(dupes)}")


def check_install_sh():
    path = os.path.join(ROOT, "install.sh")
    if not os.path.isfile(path):
        fail("install.sh", "install.sh missing")
        return
    bash = shutil.which("bash")
    if not bash:
        print("  (skip) bash not available on this host")
        return
    r = subprocess.run([bash, "-n", path], capture_output=True, text=True, errors="replace")
    if r.returncode != 0:
        fail("install.sh", r.stderr.strip())


def check_knowledge_packs():
    packs_dir = os.path.join(ROOT, "知识库", "Skill知识包")
    if not os.path.isdir(packs_dir):
        fail("packs", "Skill知识包/ missing")
        return
    jsonl = os.path.join(ROOT, "知识库", "能量库", "powers_poe.jsonl")
    known_ids = set()
    with open(jsonl, encoding="utf-8") as f:
        for line in f:
            try:
                known_ids.add(json.loads(line)["id"])
            except Exception:
                pass
    for fname in os.listdir(packs_dir):
        text = open(os.path.join(packs_dir, fname), encoding="utf-8").read()
        for m in re.finditer(r"^## (\S+)", text, re.M):
            if m.group(1) not in known_ids:
                fail("packs", f"{fname}: references unknown id {m.group(1)}")


def main():
    check_frontmatter()
    check_jsonl()
    check_install_sh()
    check_knowledge_packs()
    if FAILURES:
        for f in FAILURES:
            print(f"FAIL {f}")
        print(f"\n{len(FAILURES)} check(s) failed")
        sys.exit(1)
    print("All poeskill CI checks passed.")


if __name__ == "__main__":
    main()
