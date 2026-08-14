# Quickstart (3 Minuten, kein Fachjargon)

> Keine technischen Vorkenntnisse nötig. Einfach mitmachen — in 3 Minuten zum ersten „Widerspruch" deiner KI.

🌐 [简体中文](QUICKSTART.md) · [English](QUICKSTART.en.md) · [한국어](QUICKSTART.ko.md) · [Русский](QUICKSTART.ru.md) · [Español](QUICKSTART.es.md) · [日本語](QUICKSTART.ja.md) · [Français](QUICKSTART.fr.md) · [Deutsch](QUICKSTART.de.md) · [Português](QUICKSTART.pt.md)

---

## Das Einzige, was du dir merken musst

**Nach der Installation musst du dir nur einen einzigen Befehl merken: `/poe`**

Er erkennt, was du vorhast, und leitet dich an das richtige Werkzeug weiter.
**Du musst keines der 32 Skill-Namen lernen.**

---

## Schritt 1 — Installieren (≈30 Sekunden)

In einem Terminal (Windows: Git Bash oder WSL verwenden):

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

Oder, wenn du den Projektordner bereits heruntergeladen hast, führe das innerhalb des Ordners aus:

```bash
bash install.sh
```

Der Installer erkennt deine KI-Werkzeuge automatisch (Claude Code, Codex, Cline,
WorkBuddy, …), fragt nach Bestätigung und installiert die Skills. Du siehst dann:

```
[poeskill] done. Run /poe in your Agent to get started.
```

> **Kein bash?** Siehe [Windows-Tipps](#windows-tips).

## Schritt 2 — Dein erster Satz (30 Sekunden)

Öffne dein KI-Werkzeug und tippe einfach — in normaler Sprache, ohne Format:

```
/poe I have an idea: a coffee shop AI queue-ordering mini-app. Should I do it?
```

Das war's. Von da an übernimmt es.

## Schritt 3 — Den Widerspruch erleben (2 Minuten)

Eine normale KI sagt „tolle Idee, so baust du sie." Eine KI mit poeskill
streitet zuerst mit dir:

- Sie stellt deine Prämisse infrage: „**Ist die Warteschlange wirklich deren größtes Problem? Hast du das überprüft?**"
- Sie fordert Belege: „Wird der Besitzer dafür tatsächlich bezahlen? Hast du Beweise?"
- Sie liefert eine falsifizierbare Schlussfolgerung: „**Lass es bleiben — es sei denn**, X tritt ein" statt „das hängt von deiner Umsetzung ab."

**Genau darum geht es: Sie streitet zuerst, damit du bessere Entscheidungen triffst.**

---

## Woran erkenne ich, dass die Installation geklappt hat?

| Methode | Vorgehen |
|---|---|
| Einfach ausprobieren | Tippe `/poe` — wenn du Onboarding/Routing bekommst, ist es installiert |
| Ordner prüfen | In deinem Skills-Verzeichnis (z. B. `~/.claude/skills/`) existieren 32 `poe-*`-Ordner |
| Installer-Ausgabe prüfen | `skills installed → <dir> (32 skills)` bedeutet Erfolg |

## Häufige Situationen, in normaler Sprache

Diese Tabelle brauchst du nicht — `/poe` leitet automatisch weiter. Sie dient
nur als Überblickskarte:

| Was du willst | Sag einfach | Im Hintergrund |
|---|---|---|
| Entscheiden, ob eine Idee es wert ist | „hilf mir zu analysieren, ob ich das tun sollte" | `/poe-diagnosis` |
| Eine Behauptung oder einen Artikel faktenprüfen | „hilf mir, diese Behauptung zu prüfen" | `/poe-verify` |
| Nicht formulieren können, was du willst | „hilf mir, dieses Ziel zu klären" | `/poe-goal` |
| Wissen, was zu tun ist, aber nicht anfangen können | „warum prokrastiniere ich ständig" | `/poe-action` |
| Ein Buzzword ohne konkrete Bedeutung | „zerlege mir dieses Wort" | `/poe-deconstruct` |
| Keinen guten Einstieg schreiben können | „hilf mir, diesen Hook zu verbessern" | `/poe-hook` |
| Eine Entscheidung, die du später bereuen könntest | „hilf mir, diese Entscheidung langfristig zu verfolgen" | `/poe-decision` |

## Windows-Tipps

1. **Git Bash oder WSL verwenden**, um den Installer auszuführen — es ist ein
   bash-Skript, und beide bringen bash mit.
2. **Gar kein bash wollen?** Kein Problem: Lass jemanden (oder dein KI-Werkzeug)
   die Installation für dich ausführen. Danach ist die Nutzung nur noch Tippen von `/poe` — kein Terminal nötig.
3. **Wo wurde installiert?** Der Installer gibt `skills installed → <pfad>` aus.
   Merke dir diesen Pfad.
4. **Installer hängt oder meldet Fehler?** Füge den Fehler bei `/poe` ein
   („I hit an install problem"), oder öffne ein Issue.

---

## Nächste Schritte

- Was jedes Werkzeug tatsächlich tut → [README](README.en.md)
- Beweis, dass es funktioniert → [`benchmark/`](benchmark/) (gleiche Frage: nackt 6/25 vs. mit poeskill 25/25)
- Problem → sag `/poe` „I have a problem", oder öffne ein [Issue](https://github.com/wastefulthink/poeskill/issues/new)

> v3.6.0 ｜ MIT ｜ Läuft lokal: keine Telemetrie, keine Anmeldung, kein Account
