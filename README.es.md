# poeskill

> 🌐 [简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

---

**Tu IA siempre acaba dándote la razón.**

Le preguntas «¿tiene futuro esta idea?» — te responde «tiene mucho potencial». Le preguntas «¿debería hacer esto?» — te responde «depende de cómo lo ejecutes».

Nunca te dice que no. Nunca te pregunta «¿lo has verificado?»

poeskill arregla exactamente eso. 32 skills que convierten cualquier herramienta de IA en un socio que te planta cara: primero cuestiona tu premisa, luego exige tus datos y, por último, te da una conclusión que de verdad puedes falsar. No «suena bien», sino «bien o mal: así lo compruebas».

---

## Por qué lo construimos

Durante mucho tiempo usé herramientas de IA y noté un patrón: **cuanto más inteligente se vuelve, antes te da la razón.**

Le das un plan de negocio lleno de agujeros y te los rellena. Le pides un deseo vago y lo descompone en pasos — pero nadie se detiene a preguntar: «un momento, ¿es siquiera cierta la premisa?»

Las buenas decisiones no salen de «ayúdame a ejecutar». Salen de «ayúdame a cuestionar». Así que tomé los métodos de pensamiento de 25 pensadores — de Hume a Hayek, de Feynman a Kahneman — los destilé en 305 unidades de conocimiento citadas y los empaqueté en 32 skills que se instalan con un solo comando.

Toda skill sigue un principio de diseño: **debe discutir contigo antes de ayudarte.**

---

## Instalación en 30 segundos

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

O desde un clon local:

```bash
git clone https://github.com/wastefulthink/poeskill.git
cd poeskill
bash install.sh            # auto-detects your AI tool
bash install.sh --all      # install into every detected tool
bash install.sh --target ~/.claude/skills
```

Funciona con Claude Code, Codex, Cline, WorkBuddy, Kiro, Qwen Code — con cualquier agente que lea skills de una carpeta.

Después de instalar, **solo necesitas recordar un comando: `/poe`.** No aprendas ninguno de los 32 nombres de skills — enruta automáticamente.

---

## Tus primeros 3 minutos

1. Abre tu herramienta de IA y escribe en lenguaje natural:

   ```
   /poe I have an idea: a coffee shop AI queue app. Should I do it?
   ```

2. Una IA normal responde «buena idea, así se construye». Una IA con poeskill discute primero:
   - «¿La cola es de verdad su mayor dolor? ¿Lo has verificado?»
   - «¿El dueño pagará realmente por esto? ¿Tienes pruebas?»
   - Después: «**No lo hagas — a menos que** ocurra X» en lugar de «depende de cómo lo ejecutes».

3. **Primero discute para que tomes mejores decisiones.** Ese es todo el punto.

¿Eres nuevo? Lee el [quickstart de 3 minutos](QUICKSTART.en.md) (sin tecnicismos).

---

## Qué hace

**Diagnóstico de problemas de negocio**
- `/poe-diagnosis` — diagnóstico de modelo de negocio, modos consulta + chequeo
- `/poe-decision` — convierte decisiones de largo plazo en archivos locales revisables
- `/poe-standard-answer` — encuentra mecanismos históricos isomorfos a tu dilema
- `/poe-benchmark` — encuentra referencias (benchmarks) y filtra el ruido con un proceso de cribado

**Pipeline completo de creación de contenido**
- `/poe-good-question` — reescribe preguntas vagas en especificaciones listas para razonar
- `/poe-content` — diagnóstico completo de contenido, del tema al copy
- `/poe-hook` — optimización de la apertura para vídeo corto
- `/poe-script-flow` — comprobación de continuidad y fugas de espectadores en el guion
- `/poe-resonate` / `/poe-spread` — detección de resonancia y psicología de la comunicación
- `/poe-ai-check` — detecta rastros de escritura con IA
- `/poe-content-risk-check` — comprobaciones de riesgo pre-publicación y revisión de plataformas
- `/poe-xhs-title` — fórmulas de títulos para Xiaohongshu (RED)
- `/poe-wechat-html` — de Markdown a HTML para cuentas oficiales de WeChat

**Herramientas de pensamiento / cognición**
- `/poe-deconstruct` — desmonta conceptos vagos desde el análisis del lenguaje
- `/poe-action` — diagnostica el «sé lo que debo hacer pero no me muevo»
- `/poe-slowisfast` — distingue impaciencia de fricción necesaria y diseña caminos de interés compuesto
- `/poe-goal` — convierte deseos vagos en objetivos comprobables

**Herramientas de sistema (mantenimiento de poeskill)**
- `/poe` — entrada principal y enrutador dinámico
- `/poe-chatroom` / `/poe-chatroom-market` — discusiones multirol (incluye la escuela del orden de mercado)
- `/poe-save` / `/poe-restore` / `/poe-report` — archivado e informes del estado de diagnóstico
- `/poe-knowledge` / `/poe-content-system` — base de conocimiento local e ingeniería de activos de contenido
- `/poe-learning` — aprendizaje interactivo
- `/poe-verify` — contraverificación de cualquier conclusión (rastreo de evidencia / contraejemplos / graduación de fuentes / comprobaciones de conflicto de intereses)
- `/poe-update` — autoactualización desde este repositorio
- `/poe-bridge` / `/poe-agent-migration` — puente hacia otros agentes y migración de espacios de trabajo
- `/poe-skill-cleaner` — audita skills en busca de intención comercial oculta

---

## Base de conocimiento: 305 unidades · 25 pensadores

`知识库/` no contiene vagos «resúmenes de IA». Contiene 305 unidades de poder destiladas de las obras originales de 25 pensadores: Hume, Kant, Popper, Wittgenstein, Deutsch, Russell, Smith, Mises, Hayek, Laozi, Adler, Schopenhauer, Marco Aurelio, Nietzsche, Camus, Aristóteles, Mill, Weber, Keynes, Friedman, Schumpeter, Soros, Grove, Darwin, Feynman, Einstein, Newton, Shannon, Turing, Bacon, Descartes, Munger, Kahneman, Thaler, Taleb, Drucker, Porter, Simon, Coase, Pinker, Dennett.

Cada unidad lleva su fuente original. Nada de «confía en mí» — solo «aquí está la cita, juzga por ti mismo».

- `能量库/powers_poe.jsonl` — el dataset maestro
- `Skill知识包/` — 12 paquetes de conocimiento por skill
- `哲学概念词典.md` — referencia rápida de 80 conceptos

---

## Es medible

La misma decisión de negocio, ejecutada dos veces sobre el mismo modelo — sin poeskill y con poeskill. En el caso 01, el modelo desnudo puntúa **6/25**; poeskill **25/25**. Mismo modelo, misma pregunta; la única diferencia es si se le pide a la IA que discuta contigo.

```bash
python benchmark/run_benchmark.py --prompt both   # needs an API key
```

Consulta [`benchmark/`](benchmark/) para ver el caso, los prompts, el runner y la rúbrica de puntuación. **La diferencia es el producto.**

---

## Por qué el nombre «poe»

Tres capas:

1. **Un homenaje a Edgar Allan Poe** — la figura fundacional de la ficción policiaca. Sus detectives nunca se fían de la narración superficial; reconstruyen la verdad a partir de pequeños indicios. Ese es exactamente el temperamento de esta caja de herramientas: `/poe-diagnosis` sigue los síntomas hasta las causas raíz, `/poe-verify` somete las conclusiones a prueba con contraevidencia, `/poe-deconstruct` desmonta las palabras de moda mal usadas.
2. **Problem-Oriented Engine** — toda herramienta parte de un problema, no de una respuesta.
3. **Un nombre independiente** — corto, memorable, sin connotaciones negativas en ningún idioma importante.

---

## Por qué deberías darle estrella a este repo

- **Discute contigo.** Todo el sentido es discrepar — toda skill de diagnóstico debe adjuntar a su conclusión una condición falsable y una calificación de la fortaleza de la fuente.
- **Todo es verificable.** 305 unidades, cada una con su cita. Nada de «vibraciones», nada de «confía en mí».
- **Se ejecuta localmente.** Sin telemetría, sin SaaS, sin cuentas. Tus preguntas nunca salen de tu máquina.
- **MIT + completamente original.** Escrito desde cero. Hazle fork, intégralo en tu stack, constrúyelo encima.

---

## Uso crítico (importante)

poeskill es una herramienta de pensamiento, no una máquina de respuestas:

1. Toda skill de tipo conclusión **debe** adjuntar una calificación de la fortaleza de la fuente (A/B/C/D); por debajo de C solo es una idea
2. Las atribuciones cualitativas deben venir con condiciones falsables
3. Ante la duda, ejecuta `/poe-verify` para una contraverificación
4. En decisiones de alto riesgo (inversión, carrera, salud), valida de forma cruzada — nunca confíes en un único marco
5. `/poe-action` y otras herramientas psicológicas son ayudas de autoconocimiento, no psicoterapia

---

## Actualización

- La entrada principal comprueba `UPDATE.json` como máximo una vez cada 24 h
- `/poe-update` se sincroniza desde este repositorio, conservando tu archivo `~/.poe/`
- Haz `git pull` antes de actualizar para revisar los cambios

## Contribuir

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) (incluye el flujo de trabajo i18n), [ROADMAP.md](ROADMAP.md) y [CHANGELOG.md](CHANGELOG.md).

## Licencia

MIT. Ver [LICENSE](LICENSE).

## Invítame a un café

Si poeskill te ayudó a clarificar alguna decisión, invítame a un café:

[![Buy Me a Coffee](https://img.shields.io/badge/☕-Invítame_un_café-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xueyegog)

Totalmente voluntario — sin patrocinio, igual puedes usarlo y recibir actualizaciones.

## Agradecimientos

- Este repositorio es una implementación original, hecha desde cero. Todas las skills, unidades de conocimiento, scripts y documentación fueron escritos de forma independiente para este proyecto.
- El proyecto es gratuito y de código abierto; la única forma de apoyarlo es mediante donaciones voluntarias (ver arriba). Sin comunidad de pago ni embudo de cursos.
- El contenido de la base de conocimiento está organizado a partir de obras filosóficas y económicas de dominio público; cada unidad cita su fuente original.
