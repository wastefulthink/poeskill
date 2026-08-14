# 퀵스타트 (3분, 전문 용어 없음)

> 기술 배경지식이 필요 없습니다. 그대로 따라 하세요 — 3분이면 AI의 첫 "반박"을 경험할 수 있습니다.

🌐 [简体中文](QUICKSTART.md) · [English](QUICKSTART.en.md) · [한국어](QUICKSTART.ko.md) · [Русский](QUICKSTART.ru.md) · [Español](QUICKSTART.es.md) · [日本語](QUICKSTART.ja.md) · [Français](QUICKSTART.fr.md) · [Deutsch](QUICKSTART.de.md) · [Português](QUICKSTART.pt.md)

---

## 꼭 기억해야 할 딱 하나

**설치 후 기억해야 할 명령어는 단 하나: `/poe`입니다**

당신이 하려는 일을 파악해서 알맞은 도구로 라우팅해 줍니다.
**32개 스킬 이름은 하나도 외울 필요가 없습니다.**

---

## 1단계 — 설치 (약 30초)

터미널에서 (Windows: Git Bash 또는 WSL 사용):

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

또는 이미 프로젝트 폴더를 다운로드했다면, 그 안에서 다음을 실행하세요:

```bash
bash install.sh
```

설치 프로그램이 AI 도구를 자동 감지하고(Claude Code, Codex, Cline, WorkBuddy, …), 확인을 요청한 뒤 스킬을 설치합니다. 다음과 같은 메시지가 표시됩니다:

```
[poeskill] done. Run /poe in your Agent to get started.
```

> **bash가 없나요?** [Windows 팁](#windows-tips)을 참고하세요.

## 2단계 — 첫 문장을 입력하세요 (30초)

AI 도구를 열고 그냥 입력하세요 — 평범한 언어, 형식은 필요 없습니다:

```
/poe I have an idea: a coffee shop AI queue-ordering mini-app. Should I do it?
```

그게 전부입니다. 이후는 알아서 진행됩니다.

## 3단계 — 반박을 경험하세요 (2분)

일반 AI는 "좋은 아이디어네요, 이렇게 만들면 됩니다"라고 말합니다. poeskill이 설치된 AI는 먼저 당신과 논쟁합니다:

- 전제에 도전합니다: "**그 대기열이 정말 그들의 가장 큰 골칫거리인가요? 검증해 보셨나요?**"
- 증거를 요구합니다: "사장님이 실제로 돈을 지불할까요? 증거가 있나요?"
- 반증 가능한 결론을 내려줍니다: "실행력에 달렸죠" 대신 "**하지 마세요 — 단, X가 발생한다면**"

**그것이 핵심입니다: 먼저 논쟁하기 때문에 더 나은 결정을 내릴 수 있습니다.**

---

## 설치가 잘 됐는지 어떻게 알까요?

| 방법 | 확인 방법 |
|---|---|
| 그냥 시도해 보기 | `/poe` 입력 — 온보딩/라우팅이 나오면 설치된 것 |
| 폴더 확인 | 스킬 디렉토리(예: `~/.claude/skills/`)에 `poe-*` 폴더 32개가 있는지 |
| 설치 출력 확인 | `skills installed → <dir> (32 skills)` 출력이면 성공 |

## 자주 겪는 상황, 쉬운 말로

이 표를 외울 필요는 없습니다 — `/poe`가 자동으로 라우팅합니다. 머릿속 지도를 그리기 위한 참고일 뿐입니다:

| 원하는 것 | 그냥 이렇게 말하면 | 내부적으로 실행되는 것 |
|---|---|---|
| 아이디어가 실행할 가치가 있는지 판단 | "이걸 해야 할지 분석해 줘" | `/poe-diagnosis` |
| 주장이나 글의 사실 여부 확인 | "이 주장을 검증해 줘" | `/poe-verify` |
| 원하는 게 뭔지 말로 표현하기 어려움 | "이 목표를 명확히 해 줘" | `/poe-goal` |
| 무엇을 해야 할지는 아는데 시작이 안 됨 | "왜 자꾸 미루는 걸까" | `/poe-action` |
| 유행어가 구체적으로 와닿지 않음 | "이 단어를 해체해 줘" | `/poe-deconstruct` |
| 좋은 오프닝을 못 쓰겠음 | "이 훅을 개선해 줘" | `/poe-hook` |
| 나중에 후회할지도 모를 결정 | "이 결정을 장기적으로 추적해 줘" | `/poe-decision` |

## Windows 팁

1. **Git Bash 또는 WSL을 사용**해 설치 프로그램을 실행하세요 — bash 스크립트이며, 둘 다 bash가 내장되어 있습니다.
2. **bash를 전혀 안 쓰고 싶나요?** 괜찮습니다: 다른 사람(또는 당신의 AI 도구)에게 설치를 대신 맡기세요. 이후 사용은 그냥 `/poe`를 입력하는 것뿐입니다 — 터미널이 필요 없습니다.
3. **어디에 설치됐나요?** 설치 프로그램이 `skills installed → <path>`를 출력합니다. 그 경로를 기억해 두세요.
4. **설치 프로그램이 멈추거나 오류가 나나요?** 오류 내용을 `/poe`에 붙여넣거나("설치 문제가 발생했습니다"), 이슈를 열어 주세요.

---

## 다음 단계

- 각 도구가 실제로 무엇을 하는지 → [README](README.en.md)
- 작동하는 증거 → [`benchmark/`](benchmark/) (같은 질문: poeskill 없이 6/25 vs poeskill과 함께 25/25)
- 문제가 생기면 → `/poe`에 "문제가 있습니다"라고 말하거나 [이슈](https://github.com/wastefulthink/poeskill/issues/new)를 열어 주세요

> v3.6.0 ｜ MIT ｜ 로컬 실행: 텔레메트리 없음, 가입 없음, 계정 없음
