# Quickstart (3 minutos, sem jargão)

> Nenhum conhecimento técnico necessário. Acompanhe — 3 minutos para o seu primeiro "pushback" (questionamento) da sua IA.

🌐 [简体中文](QUICKSTART.md) · [English](QUICKSTART.en.md) · [한국어](QUICKSTART.ko.md) · [Русский](QUICKSTART.ru.md) · [Español](QUICKSTART.es.md) · [日本語](QUICKSTART.ja.md) · [Français](QUICKSTART.fr.md) · [Deutsch](QUICKSTART.de.md) · [Português](QUICKSTART.pt.md)

---

## A única coisa que você precisa lembrar

**Após a instalação, você só precisa lembrar de um comando: `/poe`**

Ele descobre o que você está tentando fazer e encaminha você para a ferramenta certa.
**Você não precisa aprender nenhum dos 32 nomes de skill.**

---

## Passo 1 — Instalação (≈30 segundos)

Em um terminal (no Windows: use Git Bash ou WSL):

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

Ou, se você já baixou a pasta do projeto, execute isto dentro dela:

```bash
bash install.sh
```

O instalador detecta automaticamente suas ferramentas de IA (Claude Code, Codex, Cline,
WorkBuddy, …), pede confirmação e instala as skills. Você verá:

```
[poeskill] done. Run /poe in your Agent to get started.
```

> **Não tem bash?** Veja as [dicas para Windows](#windows-tips).

## Passo 2 — Digite sua primeira frase (30 segundos)

Abra sua ferramenta de IA e apenas digite — linguagem natural, sem formato necessário:

```
/poe I have an idea: a coffee shop AI queue-ordering mini-app. Should I do it?
```

É isso. Ele assume a partir daí.

## Passo 3 — Experimente o pushback (2 minutos)

Uma IA normal diz "ótima ideia, aqui está como construir". Uma IA com poeskill
argumenta com você primeiro:

- Ela desafia sua premissa: "**A fila é realmente o maior ponto de dor deles?
  Você verificou isso?**"
- Ela pede evidências: "O dono realmente vai pagar por isso? Você tem provas?"
- Ela dá uma conclusão falseável: "**Não faça — a menos que** X aconteça"
  em vez de "depende da sua execução".

**Esse é o ponto principal: ela argumenta primeiro para que você tome decisões melhores.**

---

## Como sei que a instalação funcionou?

| Método | Como |
|---|---|
| Apenas experimente | Digite `/poe` — se aparecer onboarding/roteamento, está instalado |
| Verifique a pasta | Existem 32 pastas `poe-*` no seu diretório de skills (ex.: `~/.claude/skills/`) |
| Verifique a saída da instalação | `skills installed → <dir> (32 skills)` significa sucesso |

## Situações comuns, em linguagem simples

Você não precisa desta tabela — `/poe` roteia automaticamente. Ela serve apenas
para você ter um mapa mental:

| O que você quer | Basta dizer | Por baixo dos panos |
|---|---|---|
| Decidir se uma ideia vale a pena | "me ajude a analisar se eu devo fazer isso" | `/poe-diagnosis` |
| Checar os fatos de uma afirmação ou artigo | "me ajude a verificar essa afirmação" | `/poe-verify` |
| Não consegue articular o que quer | "me ajude a esclarecer essa meta" | `/poe-goal` |
| Sabe o que fazer, mas não consegue começar | "por que eu continuo procrastinando" | `/poe-action` |
| Um jargão que não significa nada concreto | "desmonte essa palavra para mim" | `/poe-deconstruct` |
| Não consegue escrever uma boa abertura | "me ajude a melhorar esse hook" | `/poe-hook` |
| Uma decisão que você pode se arrepender depois | "me ajude a acompanhar essa decisão a longo prazo" | `/poe-decision` |

## Dicas para Windows

1. **Use Git Bash ou WSL** para executar o instalador — é um script bash, e
   ambos vêm com bash.
2. **Não quer usar bash de jeito nenhum?** Tudo bem: peça para alguém (ou para
   sua ferramenta de IA) executar a instalação por você. Depois disso, usar é
   só digitar `/poe` — sem necessidade de terminal.
3. **Onde foi instalado?** O instalador imprime `skills installed → <path>`.
   Guarde esse caminho.
4. **Instalador travou ou dando erro?** Cole o erro no `/poe` ("tive um
   problema na instalação"), ou abra uma issue.

---

## Próximos passos

- O que cada ferramenta realmente faz → [README](README.en.md)
- Prova de que funciona → [`benchmark/`](benchmark/) (mesma pergunta: puro 6/25 vs.
  com poeskill 25/25)
- Qualquer problema → diga ao `/poe` "tenho um problema", ou abra uma
  [issue](https://github.com/wastefulthink/poeskill/issues/new)

> v3.5.1 ｜ MIT ｜ Roda localmente: sem telemetria, sem cadastro, sem conta
