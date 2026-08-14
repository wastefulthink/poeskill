# poeskill

> 🌐 [简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

---

**당신의 AI는 당신에게 계속 동의만 합니다.**

"이 아이디어 괜찮은가요?"라고 물으면 "성장 가능성이 크네요"라고 답합니다. "이걸 해야 할까요?"라고 물으면 "실행력에 달렸죠"라고 답합니다.

절대 "아니요"라고 말하지 않습니다. "그거 검증해 봤어요?"라고 묻지도 않습니다.

poeskill은 정확히 그 문제를 해결합니다. 어떤 AI 도구든 반박을 아끼지 않는 파트너로 바꿔주는 32개의 스킬 — 먼저 전제를 의심하고, 데이터를 요구한 다음, 실제로 반증할 수 있는 결론을 내려줍니다. "그럴듯하네요"가 아니라 "맞다 혹은 틀리다 — 이렇게 확인해 보세요"입니다.

---

## 왜 만들었나

저는 오랫동안 AI 도구를 사용하면서 한 가지 패턴을 발견했습니다. **AI가 똑똑해질수록 더 빨리 동의합니다.**

구멍투성이인 사업 계획서를 건네면 그 구멍을 메워줍니다. 막연한 바람을 말하면 단계로 쪼개 줍니다. 하지만 아무도 멈춰서 묻지 않습니다. "잠깐, 그 전제 자체가 사실인가요?"

좋은 결정은 "실행을 도와줘"에서 나오지 않습니다. "의심하게 도와줘"에서 나옵니다. 그래서 저는 흄(Hume)부터 하이에크(Hayek), 파인만(Feynman)부터 카너먼(Kahneman)까지 25명 사상가의 사고법을 취해 출처가 명시된 305개의 지식 단위로 증류하고, 명령어 하나로 설치되는 32개의 스킬로 묶었습니다.

모든 스킬은 하나의 설계 원칙을 따릅니다: **도와주기 전에 반드시 당신과 논쟁해야 한다.**

---

## 30초 설치

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

로컬 클론에서도 설치할 수 있습니다:

```bash
git clone https://github.com/wastefulthink/poeskill.git
cd poeskill
bash install.sh            # auto-detects your AI tool
bash install.sh --all      # install into every detected tool
bash install.sh --target ~/.claude/skills
```

Claude Code, Codex, Cline, WorkBuddy, Kiro, Qwen Code 등 폴더에서 스킬을 읽는 어떤 에이전트와도 작동합니다.

설치 후 **기억해야 할 명령어는 단 하나: `/poe`입니다.** 32개 스킬 이름을 하나도 외울 필요가 없습니다 — 자동으로 라우팅해 줍니다.

---

## 첫 3분

1. AI 도구를 열고 평범한 언어로 입력하세요:

   ```
   /poe I have an idea: a coffee shop AI queue app. Should I do it?
   ```

2. 일반 AI는 "좋은 아이디어네요, 이렇게 만들면 됩니다"라고 답합니다. poeskill이 설치된 AI는 먼저 논쟁합니다:
   - "그 대기열이 정말 그들의 가장 큰 골칫거리인가요? 검증해 보셨나요?"
   - "사장님이 실제로 돈을 낼까요? 증거가 있나요?"
   - 그러고는 "실행력에 달렸죠" 대신: "**하지 마세요 — 단, X가 발생한다면**"이라고 말합니다.

3. **먼저 논쟁하기 때문에 더 나은 결정을 내릴 수 있습니다.** 그것이 전부입니다.

처음이신가요? [3분 퀵스타트](QUICKSTART.en.md)를 읽어보세요 (전문 용어 전혀 없음).

---

## 하는 일

**비즈니스 문제 진단**
- `/poe-diagnosis` — 비즈니스 모델 진단, 컨설팅 + 체크업 모드
- `/poe-decision` — 장기적인 결정을 검토 가능한 로컬 아카이브로 전환
- `/poe-standard-answer` — 당신의 딜레마와 동형인 역사적 메커니즘 탐색
- `/poe-benchmark` — 벤치마크 탐색, 스크리닝 절차로 노이즈 제거

**콘텐츠 제작 전체 파이프라인**
- `/poe-good-question` — 막연한 질문을 추론 가능한 스펙으로 재작성
- `/poe-content` — 주제부터 카피까지 콘텐츠 전면 진단
- `/poe-hook` — 숏폼 오프닝 최적화
- `/poe-script-flow` — 스크립트 흐름과 이탈 지점 점검
- `/poe-resonate` / `/poe-spread` — 공감 탐지 및 커뮤니케이션 심리학
- `/poe-ai-check` — AI 작성 흔적 감지
- `/poe-content-risk-check` — 발행 전 리스크 및 플랫폼 심사 점검
- `/poe-xhs-title` — 샤오홍슈(RED) 제목 공식
- `/poe-wechat-html` — 마크다운을 위챗(WeChat) 공식 계정 HTML로 변환

**사고 / 인지 도구**
- `/poe-deconstruct` — 언어 분석 관점에서 막연한 개념 해체
- `/poe-action` — "무엇을 해야 할지 아는데 움직일 수 없다"를 진단
- `/poe-slowisfast` — 조급함과 필요한 마찰을 구분하고 복리(compounding) 경로 설계
- `/poe-goal` — 막연한 바람을 점검 가능한 목표로 전환

**시스템 도구 (poeskill 자체 유지보수)**
- `/poe` — 메인 진입점이자 다이내믹 라우터
- `/poe-chatroom` / `/poe-chatroom-market` — 다중 역할 토론 (시장질서학파 관점 포함)
- `/poe-save` / `/poe-restore` / `/poe-report` — 진단 상태 아카이빙 및 리포트
- `/poe-knowledge` / `/poe-content-system` — 로컬 지식베이스 및 콘텐츠 자산 엔지니어링
- `/poe-learning` — 인터랙티브 러닝
- `/poe-verify` — 모든 결론에 대한 반증 (증거 추적 / 반례 / 출처 등급 / 이해상충 점검)
- `/poe-update` — 이 저장소에서 자체 업데이트
- `/poe-bridge` / `/poe-agent-migration` — 다른 에이전트로의 브리지 및 워크스페이스 마이그레이션
- `/poe-skill-cleaner` — 스킬에 숨은 상업적 의도 감사

---

## 지식베이스: 305개 단위 · 25명의 사상가

`knowledge/`에는 막연한 "AI 요약"이 들어 있지 않습니다. 25명 사상가의 원전에서 증류한 305개의 파워 유닛이 들어 있습니다 — 흄, 칸트, 포퍼, 비트겐슈타인, 도이치, 러셀, 스미스, 미제스, 하이에크, 노자, 아들러, 쇼펜하우어, 마르쿠스 아우렐리우스, 니체, 카뮈, 아리스토텔레스, 밀, 베버, 케인스, 프리드먼, 슘페터, 소로스, 그로브, 다윈, 파인만, 아인슈타인, 뉴턴, 섀넌, 튜링, 베이컨, 데카르트, 멍거, 카너먼, 탈러, 탤럽, 드러커, 포터, 사이먼, 코스, 핑커, 데넷.

모든 단위에는 원전 출처가 명시되어 있습니다. "믿어달라"가 아니라 "출처는 여기, 직접 판단하세요"입니다.

- `powers/powers_poe.jsonl` — 마스터 데이터셋
- `Skill知识包/` — 스킬별 지식 팩 12개
- `philosophy-glossary.md` — 80개 개념 빠른 참조

---

## 측정 가능합니다

동일한 비즈니스 결정을 같은 모델에서 두 번 실행했습니다 — poeskill 없이 vs. poeskill과 함께. 케이스 01에서 poeskill 없는 모델은 **6/25**, poeskill은 **25/25**를 기록했습니다. 같은 모델, 같은 질문; 유일한 차이는 AI가 당신과 논쟁하도록 지시받았는지 여부입니다.

```bash
python benchmark/run_benchmark.py --prompt both   # needs an API key
```

케이스, 프롬프트, 러너, 채점 기준은 [`benchmark/`](benchmark/)에서 확인하세요. **격차가 곧 제품입니다.**

---

## 왜 "poe"라는 이름인가

세 가지 층위가 있습니다:

1. **에드거 앨런 포(Edgar Allan Poe)에 대한 오마주** — 탐정소설의 창시자. 그의 탐정들은 표면적 서사를 결코 믿지 않습니다. 작은 단서들로부터 진실을 재구성하지요. 이 도구함의 기질도 정확히 그렇습니다: `/poe-diagnosis`는 증상을 근본 원인까지 추적하고, `/poe-verify`는 반증으로 결론을 스트레스 테스트하며, `/poe-deconstruct`는 남용되는 유행어를 해체합니다.
2. **Problem-Oriented Engine (문제 지향 엔진)** — 모든 도구는 정답이 아닌 문제에서 출발합니다.
3. **독립적인 이름** — 짧고 기억하기 쉬우며, 주요 언어 어디에서도 부정적 의미가 없습니다.

---

## 이 저장소에 스타를 눌러야 하는 이유

- **당신과 논쟁합니다.** 핵심은 반박입니다 — 모든 진단 스킬은 결론에 반증 가능한 조건과 출처 강도 등급을 반드시 붙여야 합니다.
- **모든 것이 검증 가능합니다.** 출처가 명시된 305개 단위. 막연한 느낌이나 "믿어달라"는 없습니다.
- **로컬에서 실행됩니다.** 텔레메트리(telemetry)도, SaaS도, 계정도 없습니다. 당신의 질문은 기계 밖으로 나가지 않습니다.
- **MIT + 완전한 오리지널.** 처음부터 직접 작성했습니다. 포크하고, 벤더링하고, 그 위에 구축하세요.

---

## 주의해서 사용하기 (중요)

poeskill은 사고 도구이지, 답안 생성기가 아닙니다:

1. 결론형 스킬은 **반드시** 출처 강도 등급(A/B/C/D)을 붙여야 합니다; C 미만이면 아이디어일 뿐입니다
2. 질적 판단에는 반증 가능한 조건이 따라야 합니다
3. 확신이 없으면 `/poe-verify`로 반증하세요
4. 중대한 결정(투자, 커리어, 건강)은 교차 검증하세요 — 단일 프레임워크를 절대 믿지 마세요
5. `/poe-action` 등 심리 관련 도구는 자기 인식을 돕는 도구이지, 심리치료가 아닙니다

---

## 업데이트

- 메인 진입점은 24시간에 최대 한 번 `UPDATE.json`을 확인합니다
- `/poe-update`는 이 저장소에서 동기화하며, `~/.poe/` 아카이브를 유지합니다
- 변경사항을 검토하려면 업데이트 전에 `git pull`을 실행하세요

## 기여하기

[CONTRIBUTING.md](CONTRIBUTING.md) (i18n 워크플로 포함), [ROADMAP.md](ROADMAP.md), [CHANGELOG.md](CHANGELOG.md)를 참고하세요.

## 라이선스

MIT. [LICENSE](LICENSE) 참조.

## 커피 한 잔 사주기

poeskill이 어떤 결정을 정리하는 데 도움을 주었다면, 커피 한 잔 어떠세요:

[![Buy Me a Coffee](https://img.shields.io/badge/☕-커피_한_잔-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xueyegog)

전적으로 자발적입니다 — 후원하지 않아도 그대로 사용할 수 있고 업데이트도 계속됩니다.

## 감사의 말

- 이 저장소는 처음부터 직접 작성한 오리지널 구현입니다. 모든 스킬, 지식 단위, 스크립트, 문서는 이 프로젝트를 위해 독립적으로 작성되었습니다.
- 프로젝트 자체는 무료 오픈소스이며, 유일한 지원 방법은 자발적 후원(위 참조)입니다. 유료 커뮤니티나 강의 유입은 없습니다.
- 지식베이스 콘텐츠는 공개적으로 접근 가능한 철학·경제 원전에서 정리되었으며, 모든 단위는 원출처를 인용합니다.
