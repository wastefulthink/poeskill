# poeskill

> 🌐 [简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

---

**Deine KI stimmt dir ständig zu.**

Du fragst „Ist diese Idee überhaupt gut?" — sie sagt „großes Potenzial." Du fragst „Soll ich das machen?" — sie sagt „das hängt von deiner Umsetzung ab."

Sie sagt nie Nein. Sie fragt nie „hast du das überprüft?"

Genau das behebt poeskill. 32 Skills, die jedes KI-Werkzeug in einen Partner verwandeln, der Widerspruch leistet — es hinterfragt zuerst deine Prämisse, fordert deine Daten ein und liefert dir dann eine Schlussfolgerung, die du tatsächlich falsifizieren kannst. Nicht „klingt plausibel", sondern „richtig oder falsch — so überprüfst du es."

---

## Warum wir das gebaut haben

Ich habe lange KI-Werkzeuge genutzt und ein Muster bemerkt: **Je kluger sie wird, desto schneller stimmt sie dir zu.**

Du gibst ihr einen Businessplan voller Löcher — sie stopft sie. Du gibst ihr einen vagen Wunsch — sie zerlegt ihn in Schritte. Aber niemand hält inne und fragt: „Moment, stimmt die Prämisse überhaupt?"

Gute Entscheidungen entstehen nicht aus „hilf mir bei der Umsetzung", sondern aus „hilf mir beim Hinterfragen". Deshalb habe ich die Denkmethoden von 25 Denkern — von Hume bis Hayek, von Feynman bis Kahneman — destilliert, in 305 belegte Wissenseinheiten (knowledge units) gegossen und in 32 Skills verpackt, die sich mit einem einzigen Befehl installieren lassen.

Jeder Skill folgt einem einzigen Designprinzip: **Er muss mit dir streiten, bevor er dir hilft.**

---

## Installation in 30 Sekunden

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

Oder aus einem lokalen Clone:

```bash
git clone https://github.com/wastefulthink/poeskill.git
cd poeskill
bash install.sh            # erkennt dein KI-Werkzeug automatisch
bash install.sh --all      # Installation in jedes erkannte Werkzeug
bash install.sh --target ~/.claude/skills
```

Funktioniert mit Claude Code, Codex, Cline, WorkBuddy, Kiro, Qwen Code — mit jedem Agent, der Skills aus einem Ordner liest.

Nach der Installation **musst du dir nur einen einzigen Befehl merken: `/poe`.** Lerne keines der 32 Skill-Namen — das Routing passiert automatisch.

---

## Deine ersten 3 Minuten

1. Öffne dein KI-Werkzeug und tippe in normaler Sprache:

   ```
   /poe I have an idea: a coffee shop AI queue app. Should I do it?
   ```

2. Eine normale KI sagt „tolle Idee, so baust du sie." Eine KI mit poeskill streitet zuerst:
   - „Ist die Warteschlange wirklich deren größtes Problem? Hast du das überprüft?"
   - „Wird der Besitzer dafür tatsächlich bezahlen? Hast du Belege?"
   - Und dann: „**Lass es bleiben — es sei denn**, X tritt ein" statt „das hängt von deiner Umsetzung ab."

3. **Sie streitet zuerst, damit du bessere Entscheidungen triffst.** Genau darum geht es.

Neu hier? Lies den [3-Minuten-Quickstart](QUICKSTART.en.md) (ganz ohne Fachjargon).

---

## Was es tut

**Diagnose von Geschäftsproblemen**
- `/poe-diagnosis` — Geschäftsmodell-Diagnose, Modi „Beratung" (consultation) und „Check-up" (checkup)
- `/poe-decision` — langfristige Entscheidungen in überprüfbare lokale Archive verwandeln
- `/poe-standard-answer` — historische Mechanismen finden, die zu deinem Dilemma isomorph sind
- `/poe-benchmark` — Benchmarks finden, mit einem Screening-Prozess Rauschen herausfiltern

**Vollständige Content-Pipeline**
- `/poe-good-question` — vage Fragen in spezifikationsreife, reasoning-fähige Aufgaben umschreiben
- `/poe-content` — vollständige Content-Diagnose von Topic bis Copy
- `/poe-hook` — Optimierung von Kurzvideo-Einstiegen
- `/poe-script-flow` — Skript-Kohärenz und Abbruchpunkt-Checks
- `/poe-resonate` / `/poe-spread` — Resonanz-Erkennung und Kommunikationspsychologie
- `/poe-ai-check` — KI-Schreibspuren erkennen
- `/poe-content-risk-check` — Risiko- und Plattform-Review-Checks vor der Veröffentlichung
- `/poe-xhs-title` — Titel-Formeln für Xiaohongshu (RED)
- `/poe-wechat-html` — Markdown zu HTML für WeChat Official Accounts

**Denk- und Kognitions-Werkzeuge**
- `/poe-deconstruct` — vage Konzepte aus sprachanalytischer Perspektive zerlegen
- `/poe-action` — „Ich weiß, was zu tun ist, aber ich komme nicht in Gang" diagnostizieren
- `/poe-slowisfast` — Ungeduld vs. notwendige Reibung unterscheiden, Zinseszins-Pfade gestalten
- `/poe-goal` — vage Wünsche in überprüfbare Ziele verwandeln

**System-Werkzeuge (Wartung von poeskill selbst)**
- `/poe` — Haupteinstieg und dynamischer Router
- `/poe-chatroom` / `/poe-chatroom-market` — Mehr-Rollen-Diskussionen (inkl. Perspektive der Marktordnungsschule)
- `/poe-save` / `/poe-restore` / `/poe-report` — Archivierung & Reporting von Diagnose-Zuständen
- `/poe-knowledge` / `/poe-content-system` — lokale Wissensbasis & Content-Asset-Engineering
- `/poe-learning` — interaktives Lernen
- `/poe-verify` — Gegenprüfung jeder Schlussfolgerung (Beleg-Rückverfolgung / Gegenbeispiele / Quellen-Grading / Interessenkonflikt-Checks)
- `/poe-update` — Selbst-Update aus diesem Repository
- `/poe-bridge` / `/poe-agent-migration` — Anbindung an andere Agents & Workspace-Migration
- `/poe-skill-cleaner` — Skills auf versteckte kommerzielle Absichten prüfen

---

## Wissensbasis: 305 Einheiten · 25 Denker

`知识库/` enthält keine vagen „KI-Zusammenfassungen". Sie umfasst 305 Power-Einheiten, destilliert aus den Originalwerken von 25 Denkern — Hume, Kant, Popper, Wittgenstein, Deutsch, Russell, Smith, Mises, Hayek, Laozi, Adler, Schopenhauer, Marcus Aurelius, Nietzsche, Camus, Aristoteles, Mill, Weber, Keynes, Friedman, Schumpeter, Soros, Grove, Darwin, Feynman, Einstein, Newton, Shannon, Turing, Bacon, Descartes, Munger, Kahneman, Thaler, Taleb, Drucker, Porter, Simon, Coase, Pinker, Dennett.

Jede Einheit trägt ihre Originalquelle. Kein „glaub mir" — nur „hier ist die Quellenangabe, urteile selbst."

- `能量库/powers_poe.jsonl` — der Master-Datensatz
- `Skill知识包/` — 12 wissensbasierte Pakete pro Skill
- `哲学概念词典.md` — Schnellreferenz mit 80 Konzepten

---

## Es ist messbar

Dieselbe Geschäftsentscheidung, zweimal mit demselben Modell ausgeführt — nackt vs. mit poeskill. Bei Fall 01 erzielt das nackte Modell **6/25**; poeskill **25/25*. Gleiches Modell, gleiche Frage; der einzige Unterschied ist, ob der KI gesagt wurde, mit dir zu streiten.

```bash
python benchmark/run_benchmark.py --prompt both   # benötigt einen API-Schlüssel
```

Details zu Fall, Prompts, Runner und Bewertungsrubrik findest du in [`benchmark/`](benchmark/). **Die Lücke ist das Produkt.**

---

## Warum der Name „poe"

Drei Ebenen:

1. **Eine Hommage an Edgar Allan Poe** — die Gründungsfigur der Detektivliteratur. Seine Detektive vertrauen nie Oberflächenerzählungen; sie rekonstruieren die Wahrheit aus kleinen Hinweisen. Genau das ist das Temperament dieses Werkzeugkastens: `/poe-diagnosis` verfolgt Symptome bis zu ihren Ursachen, `/poe-verify` stellt Schlussfolgerungen mit Gegenevidenz auf die Probe, `/poe-deconstruct` zerlegt missbrauchte Buzzwords.
2. **Problem-Oriented Engine** — jedes Werkzeug startet bei einem Problem, nicht bei einer Antwort.
3. **Ein eigenständiger Name** — kurz, einprägsam, ohne negative Konnotationen in einer großen Sprache.

---

## Warum du dieses Repo mit einem Star versehen solltest

- **Es streitet mit dir.** Der ganze Sinn ist Widerspruch — jeder diagnostische Skill muss seiner Schlussfolgerung eine falsifizierbare Bedingung und eine Quellen-Stärke-Einstufung anfügen.
- **Alles ist überprüfbar.** 305 Einheiten, jede mit Quellenangabe. Keine Bauchgefühl-Aussagen, kein „glaub mir".
- **Es läuft lokal.** Keine Telemetrie, kein SaaS, kein Account. Deine Fragen verlassen dein Gerät nie.
- **MIT + vollständig original.** Von Grund auf neu geschrieben. Forke es, binde es ein, baue darauf auf.

---

## Kritische Nutzung (wichtig)

poeskill ist ein Denkwerkzeug, keine Antwortmaschine:

1. Jeder Skill mit Schlussfolgerungen **muss** eine Quellen-Stärke-Einstufung (A/B/C/D) anfügen; unter C ist es nur eine Idee
2. Qualitative Zuschreibungen müssen mit falsifizierbaren Bedingungen einhergehen
3. Im Zweifel `/poe-verify` für eine Gegenprüfung ausführen
4. Bei riskanten Entscheidungen (Investment, Karriere, Gesundheit) immer kreuzvalidieren — niemals einem einzelnen Framework vertrauen
5. `/poe-action` und andere psychologische Werkzeuge sind Hilfen zur Selbsterkenntnis, keine Psychotherapie

---

## Updates

- Der Haupteinstieg prüft `UPDATE.json` höchstens einmal pro 24 Stunden
- `/poe-update` synchronisiert mit diesem Repository und behält dein `~/.poe/`-Archiv
- Vor dem Update `git pull` ausführen, um die Änderungen zu prüfen

## Mitwirken

Siehe [CONTRIBUTING.md](CONTRIBUTING.md) (inkl. i18n-Workflow), [ROADMAP.md](ROADMAP.md) und [CHANGELOG.md](CHANGELOG.md).

## Lizenz

MIT. Siehe [LICENSE](LICENSE).

## Mir einen Kaffee spendieren

Wenn poeskill dir bei einer Entscheidung geholfen hat, spendier mir gerne einen Kaffee:

[![Buy Me a Coffee](https://img.shields.io/badge/☕-Kaffee_spendieren-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xueyegog)

Vollkommen freiwillig — ohne Sponsoring nutzt du es weiter und bekommst weiterhin Updates.

## Danksagung

- Dieses Repository ist eine originale, von Grund auf neue Implementierung. Alle Skills, Wissenseinheiten, Skripte und die Dokumentation wurden unabhängig für dieses Projekt geschrieben.
- Das Projekt ist frei und Open Source; die einzige Unterstützung ist freiwillige Spenden (siehe oben). Keine bezahlte Community, kein Kurs-Funnel.
- Die Inhalte der Wissensbasis sind aus öffentlich zugänglichen philosophischen und ökonomischen Werken zusammengestellt; jede Einheit zitiert ihre Originalquelle.
