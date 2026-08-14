# Quickstart (3 minutos, sin tecnicismos)

> No se necesita ningún conocimiento técnico. Sigue los pasos — en 3 minutos tu IA te llevará la contraria por primera vez.

🌐 [简体中文](QUICKSTART.md) · [English](QUICKSTART.en.md) · [한국어](QUICKSTART.ko.md) · [Русский](QUICKSTART.ru.md) · [Español](QUICKSTART.es.md) · [日本語](QUICKSTART.ja.md) · [Français](QUICKSTART.fr.md) · [Deutsch](QUICKSTART.de.md) · [Português](QUICKSTART.pt.md)

---

## Lo único que necesitas recordar

**Después de instalar, solo necesitas recordar un comando: `/poe`**

Él descubre qué intentas hacer y te enruta a la herramienta correcta.
**No necesitas aprender ninguno de los 32 nombres de skills.**

---

## Paso 1 — Instalar (≈30 segundos)

En una terminal (en Windows: usa Git Bash o WSL):

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

O, si ya descargaste la carpeta del proyecto, ejecuta esto dentro de ella:

```bash
bash install.sh
```

El instalador detecta automáticamente tus herramientas de IA (Claude Code, Codex, Cline,
WorkBuddy, …), pide confirmación e instala las skills. Verás:

```
[poeskill] done. Run /poe in your Agent to get started.
```

> **¿No tienes bash?** Consulta [Consejos para Windows](#windows-tips).

## Paso 2 — Di tu primera frase (30 segundos)

Abre tu herramienta de IA y simplemente escribe — lenguaje natural, sin formato:

```
/poe I have an idea: a coffee shop AI queue-ordering mini-app. Should I do it?
```

Eso es todo. Él se encarga a partir de ahí.

## Paso 3 — Experimenta la réplica (2 minutos)

Una IA normal responde «buena idea, así se construye». Una IA con poeskill
discute contigo primero:

- Cuestiona tu premisa: «**¿La cola es de verdad su mayor dolor?
  ¿Lo has verificado?**»
- Pide evidencia: «¿El dueño pagará realmente por esto? ¿Tienes pruebas?»
- Da una conclusión falsable: «**No lo hagas — a menos que** ocurra X»
  en lugar de «depende de cómo lo ejecutes».

**Ese es todo el punto: primero discute para que tomes mejores decisiones.**

---

## ¿Cómo sé que la instalación funcionó?

| Método | Cómo |
|---|---|
| Pruébalo | Escribe `/poe` — si recibes onboarding/enrutamiento, está instalado |
| Revisa la carpeta | Existen 32 carpetas `poe-*` en tu directorio de skills (p. ej. `~/.claude/skills/`) |
| Revisa la salida de instalación | `skills installed → <dir> (32 skills)` significa éxito |

## Situaciones habituales, en lenguaje claro

No necesitas esta tabla — `/poe` enruta automáticamente. Solo sirve para que
te hagas un mapa mental:

| Lo que quieres | Solo di | Bajo el capó |
|---|---|---|
| Decidir si una idea merece la pena | «ayúdame a analizar si debería hacer esto» | `/poe-diagnosis` |
| Verificar una afirmación o artículo | «ayúdame a verificar esta afirmación» | `/poe-verify` |
| No sabes articular lo que quieres | «ayúdame a aclarar este objetivo» | `/poe-goal` |
| Sabes lo que hacer pero no empiezas | «¿por qué sigo procrastinando?» | `/poe-action` |
| Una palabra de moda no significa nada concreto | «desmóntame esta palabra» | `/poe-deconstruct` |
| No consigues escribir una buena apertura | «ayúdame a mejorar este gancho» | `/poe-hook` |
| Una decisión que podrías lamentar después | «ayúdame a seguir esta decisión a largo plazo» | `/poe-decision` |

## Consejos para Windows

1. **Usa Git Bash o WSL** para ejecutar el instalador — es un script de bash, y
   ambos traen bash incorporado.
2. **¿No quieres usar bash en absoluto?** Perfecto: pide a alguien (o a tu
   herramienta de IA) que ejecute la instalación por ti. Después, usarlo es
   solo escribir `/poe` — sin necesidad de terminal.
3. **¿Dónde se instaló?** El instalador imprime `skills installed → <path>`.
   Apunta esa ruta.
4. **¿El instalador se bloquea o da error?** Pega el error a `/poe` («tengo un
   problema de instalación»), o abre un issue.

---

## Siguientes pasos

- Qué hace de verdad cada herramienta → [README](README.en.md)
- Prueba de que funciona → [`benchmark/`](benchmark/) (misma pregunta: sin poeskill 6/25 vs
  con poeskill 25/25)
- Cualquier problema → dile a `/poe` «tengo un problema», o abre un
  [issue](https://github.com/wastefulthink/poeskill/issues/new)

> v3.6.0 ｜ MIT ｜ Se ejecuta localmente: sin telemetría, sin registro, sin cuenta
