#!/usr/bin/env bash
# =============================================================================
# poeskill — one-line installer for Claude Code / Codex / Cline / Kiro /
# Qwen Code / WorkBuddy and any other Agent that reads skills from a folder.
#
#   curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
#   # or from a local clone:
#   bash install.sh [--target DIR] [--all] [--dry-run]
#
# Options:
#   --target DIR   install into DIR instead of auto-detecting
#   --all          install into every detected Agent skill directory
#   --dry-run      print what would be done, change nothing
#   -h, --help     show this help
# =============================================================================
set -euo pipefail

POESKILL_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VERSION="$(cat "$POESKILL_HOME/VERSION" 2>/dev/null || echo 'unknown')"
DRY_RUN=0
INSTALL_ALL=0
TARGET_DIR=""

usage() {
  sed -n '2,17p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) TARGET_DIR="${2:-}"; shift 2 ;;
    --all)    INSTALL_ALL=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) usage ;;
    *) echo "unknown option: $1" >&2; usage ;;
  esac
done

# ---------------------------------------------------------------- detection
detect_targets() {
  local targets=()
  [[ -n "$TARGET_DIR" ]] && { echo "$TARGET_DIR"; return; }
  # WorkBuddy
  [[ -d "$HOME/.workbuddy/skills" ]] && targets+=("$HOME/.workbuddy/skills")
  # Claude Code
  [[ -d "$HOME/.claude/skills" ]] && targets+=("$HOME/.claude/skills")
  # Codex
  [[ -d "$HOME/.codex/skills" ]] && targets+=("$HOME/.codex/skills")
  # Qwen Code
  [[ -d "$HOME/.qwen/skills" ]] && targets+=("$HOME/.qwen/skills")
  # Kiro
  [[ -d "$HOME/.kiro/skills" ]] && targets+=("$HOME/.kiro/skills")
  # Cline (VSCode extension data)
  for base in "$HOME/.config/Code/User/globalStorage/saoudrizwan.claude-dev/skills" \
              "$HOME/Library/Application Support/Code/User/globalStorage/saoudrizwan.claude-dev/skills" \
              "$HOME/AppData/Roaming/Code/User/globalStorage/saoudrizwan.claude-dev/skills"; do
    [[ -d "$base" ]] && targets+=("$base")
  done
  # fallback: create a suggested default if nothing was found
  if [[ ${#targets[@]} -eq 0 ]]; then
    echo "$HOME/.claude/skills"
  fi
  # dedupe
  echo "${targets[@]}" | tr ' ' '\n' | awk '!seen[$0]++'
}

say() { printf '\033[1;32m[poeskill]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[poeskill]\033[0m %s\n' "$*" >&2; }

# ---------------------------------------------------------------- install
install_into() {
  local dest="$1"
  if [[ "$INSTALL_ALL" -eq 0 && "$TARGET_DIR" == "" ]]; then
    read -r -p "安装到 ${dest}? ｜ Install into ${dest}? [y/N] " ans
    [[ "${ans,,}" == "y" || "${ans,,}" == "yes" ]] || { warn "跳过 ${dest} ｜ skipped"; return 0; }
  fi
  if [[ "$DRY_RUN" -eq 1 ]]; then
    say "模拟运行 ｜ dry-run: 将安装到 ${dest}"
    return 0
  fi
  mkdir -p "$dest"
  cp -r "$POESKILL_HOME/skills/." "$dest/"
  say "技能已安装 → ${dest}（32 个技能 ｜ 32 skills）"
  if [[ -d "$POESKILL_HOME/knowledge" ]]; then
    mkdir -p "$dest/../poeskill-knowledge" 2>/dev/null || true
    local kb_dest="$dest/../poeskill-knowledge"
    cp -r "$POESKILL_HOME/knowledge/." "$kb_dest/" 2>/dev/null && say "知识库已安装 → ${kb_dest}（305 条 ｜ 305 units）"
  fi
}

main() {
  say "poeskill 安装器 v${VERSION} ｜ installer"
  local targets
  targets=$(detect_targets)
  if [[ -z "$targets" ]]; then
    warn "未检测到 AI 工具目录，请用 --target <目录> 指定 ｜ no Agent detected, use --target <dir>"
    exit 1
  fi
  for t in $targets; do
    install_into "$t"
  done
  say "完成。在 AI 工具里输入 /poe 即可开始 ｜ done. Run /poe in your Agent."
}

main "$@"
