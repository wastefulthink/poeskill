# poeskill

> 🌐 [简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

---

**Sua IA continua concordando com você.**

Você pergunta "essa ideia é boa?" — ela responde "grande potencial". Você pergunta "devo fazer isso?" — ela responde "depende da sua execução".

Ela nunca diz não. Ela nunca pergunta "você verificou isso?"

poeskill resolve exatamente isso. 32 skills que transformam qualquer ferramenta de IA em uma parceira que rebate — ela questiona sua premissa primeiro, exige seus dados e só então dá uma conclusão que você consegue de fato falsear. Não "parece certo", mas "certo ou errado — aqui está como verificar".

---

## Por que criamos isso

Usei ferramentas de IA por muito tempo e notei um padrão: **quanto mais inteligente ela fica, mais rápido ela concorda com você.**

Você entrega um plano de negócios cheio de furos, e ela os preenche. Você dá um desejo vago, e ela o transforma em etapas — mas ninguém para para perguntar: "espera, será que a premissa é mesmo verdadeira?"

Boas decisões não vêm de "me ajude a executar". Elas vêm de "me ajude a questionar". Então peguei os métodos de pensamento de 25 pensadores — de Hume a Hayek, de Feynman a Kahneman — destilei-os em 305 unidades de conhecimento citadas e os empacotei em 32 skills instaláveis com um único comando.

Toda skill segue um princípio de design: **ela deve argumentar com você antes de ajudar.**

---

## Instalação em 30 segundos

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

Ou a partir de um clone local:

```bash
git clone https://github.com/wastefulthink/poeskill.git
cd poeskill
bash install.sh            # auto-detects your AI tool
bash install.sh --all      # install into every detected tool
bash install.sh --target ~/.claude/skills
```

Funciona com Claude Code, Codex, Cline, WorkBuddy, Kiro, Qwen Code — qualquer agente que leia skills a partir de uma pasta.

Após a instalação, **você só precisa lembrar de um comando: `/poe`.** Não precisa aprender nenhum dos 32 nomes de skill — ele roteia automaticamente.

---

## Seus primeiros 3 minutos

1. Abra sua ferramenta de IA e digite, em linguagem natural:

   ```
   /poe I have an idea: a coffee shop AI queue app. Should I do it?
   ```

2. Uma IA normal diz "ótima ideia, aqui está como construir". Uma IA com poeskill argumenta primeiro:
   - "A fila é realmente o maior ponto de dor deles? Você verificou isso?"
   - "O dono vai mesmo pagar por isso? Você tem provas?"
   - E então: "**Não faça — a menos que** X aconteça" em vez de "depende da sua execução".

3. **Ela argumenta primeiro para que você tome decisões melhores.** Esse é o ponto principal.

É novo por aqui? Leia o [quickstart de 3 minutos](QUICKSTART.en.md) (zero jargão).

---

## O que ela faz

**Diagnóstico de problemas de negócio**
- `/poe-diagnosis` — diagnóstico de modelo de negócio, modos consulta + checkup
- `/poe-decision` — transforme decisões de longo prazo em arquivos locais revisáveis
- `/poe-standard-answer` — encontre mecanismos históricos isomórficos ao seu dilema
- `/poe-benchmark` — encontre benchmarks e filtre o ruído com um processo de triagem

**Pipeline completo de criação de conteúdo**
- `/poe-good-question` — reescreva perguntas vagas em especificações prontas para raciocínio
- `/poe-content` — diagnóstico completo de conteúdo, do tema ao texto final
- `/poe-hook` — otimização da abertura de vídeos curtos
- `/poe-script-flow` — verificação de continuidade e evasão do roteiro
- `/poe-resonate` / `/poe-spread` — detecção de ressonância e psicologia da comunicação
- `/poe-ai-check` — detecção de vestígios de escrita por IA
- `/poe-content-risk-check` — verificação de risco pré-publicação e revisão de plataforma
- `/poe-xhs-title` — fórmulas de título para Xiaohongshu (RED)
- `/poe-wechat-html` — de Markdown para HTML do WeChat Official Account

**Ferramentas de pensamento / cognição**
- `/poe-deconstruct` — desmonte conceitos vagos a partir de uma análise da linguagem
- `/poe-action` — diagnóstico de "sei o que fazer, mas não consigo agir"
- `/poe-slowisfast` — identifique impaciência vs. atrito necessário, desenhe caminhos de acumulação (compounding)
- `/poe-goal` — transforme desejos vagos em metas verificáveis

**Ferramentas de sistema (manutenção do próprio poeskill)**
- `/poe` — entrada principal e roteador dinâmico
- `/poe-chatroom` / `/poe-chatroom-market` — discussões com múltiplos papéis (incluindo a visão da escola da ordem de mercado)
- `/poe-save` / `/poe-restore` / `/poe-report` — arquivamento e relatórios de estado do diagnóstico
- `/poe-knowledge` / `/poe-content-system` — base de conhecimento local e engenharia de ativos de conteúdo
- `/poe-learning` — aprendizado interativo
- `/poe-verify` — contra-verificação de qualquer conclusão (rastreamento de evidências / contraexemplos / gradação de fontes / verificação de conflitos de interesse)
- `/poe-update` — auto-atualização a partir deste repositório
- `/poe-bridge` / `/poe-agent-migration` — ponte para outros agentes e migração de workspace
- `/poe-skill-cleaner` — audite skills em busca de intenção comercial oculta

---

## Base de conhecimento: 305 unidades · 25 pensadores

`knowledge/` não contém "resumos de IA" vagos. Ela guarda 305 unidades de conhecimento destiladas das obras originais de 25 pensadores — Hume, Kant, Popper, Wittgenstein, Deutsch, Russell, Smith, Mises, Hayek, Laozi, Adler, Schopenhauer, Marco Aurélio, Nietzsche, Camus, Aristóteles, Mill, Weber, Keynes, Friedman, Schumpeter, Soros, Grove, Darwin, Feynman, Einstein, Newton, Shannon, Turing, Bacon, Descartes, Munger, Kahneman, Thaler, Taleb, Drucker, Porter, Simon, Coase, Pinker, Dennett.

Cada unidade traz sua fonte original. Nada de "confie em mim" — apenas "aqui está a citação, julgue você mesmo".

- `powers/powers_poe.jsonl` — o conjunto de dados principal
- `Skill知识包/` — 12 pacotes de conhecimento por skill
- `philosophy-glossary.md` — referência rápida de 80 conceitos

---

## É mensurável

A mesma decisão de negócio, executada duas vezes no mesmo modelo — puro vs. com poeskill. No caso 01, o modelo puro marca **6/25**; com poeskill, **25/25**. Mesmo modelo, mesma pergunta; a única diferença é se a IA foi instruída a argumentar com você.

```bash
python benchmark/run_benchmark.py --prompt both   # needs an API key
```

Veja em [`benchmark/`](benchmark/) o caso, os prompts, o executor e a rubrica de pontuação. **A diferença é o produto.**

---

## Por que o nome "poe"

Três camadas:

1. **Uma homenagem a Edgar Allan Poe** — o fundador da ficção policial. Seus detetives nunca confiam em narrativas superficiais; eles reconstroem a verdade a partir de pequenas pistas. É exatamente o temperamento deste toolbox: `/poe-diagnosis` rastreia sintomas até as causas raiz, `/poe-verify` estressa conclusões com contraevidências, `/poe-deconstruct` desmonta jargões desgastados.
2. **Problem-Oriented Engine** — toda ferramenta parte de um problema, não de uma resposta.
3. **Um nome independente** — curto, memorável, sem conotações negativas em nenhum idioma importante.

---

## Por que você deve dar estrela neste repositório

- **Ela argumenta com você.** O ponto central é discordar — toda skill de diagnóstico deve anexar uma condição falseável e uma nota de força da fonte à sua conclusão.
- **Tudo é verificável.** 305 unidades, cada uma com citação. Sem achismos, sem "confie em mim".
- **Roda localmente.** Sem telemetria, sem SaaS, sem conta. Suas perguntas nunca saem da sua máquina.
- **MIT + totalmente original.** Escrito do zero. Faça fork, incorpore, construa em cima.

---

## Uso crítico (importante)

poeskill é uma ferramenta de pensamento, não uma máquina de respostas:

1. Toda skill do tipo conclusão **deve** anexar uma nota de força da fonte (A/B/C/D); abaixo de C, é apenas uma ideia
2. Atribuições qualitativas devem vir acompanhadas de condições falseáveis
3. Em caso de dúvida, execute `/poe-verify` para contra-verificação
4. Para decisões de alto risco (investimento, carreira, saúde), faça validação cruzada — nunca confie em um único framework
5. `/poe-action` e outras ferramentas psicológicas são auxílios de autoconhecimento, não psicoterapia

---

## Atualização

- A entrada principal verifica `UPDATE.json` no máximo uma vez a cada 24h
- `/poe-update` sincroniza a partir deste repositório, preservando seu arquivo `~/.poe/`
- Execute `git pull` antes de atualizar para revisar as mudanças

## Como contribuir

Veja [CONTRIBUTING.md](CONTRIBUTING.md) (incluindo o fluxo de trabalho de i18n), [ROADMAP.md](ROADMAP.md) e [CHANGELOG.md](CHANGELOG.md).

## Licença

MIT. Veja [LICENSE](LICENSE).

## Me pague um café

Se o poeskill te ajudou a clarear alguma decisão, me pague um café:

[![Buy Me a Coffee](https://img.shields.io/badge/☕-Me_pague_um_café-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xueyegog)

Totalmente voluntário — sem patrocínio você continua usando e recebendo atualizações normalmente.

## Agradecimentos

- Este repositório é uma implementação original, escrita do zero. Todas as skills, unidades de conhecimento, scripts e documentações foram escritos de forma independente para este projeto.
- O projeto é gratuito e de código aberto; a única forma de apoiá-lo é por doações voluntárias (ver acima). Sem comunidade paga nem funil de curso.
- O conteúdo da base de conhecimento é organizado a partir de obras filosóficas e econômicas disponíveis publicamente; cada unidade cita sua fonte original.
