# Guide de démarrage (3 minutes, zéro jargon)

> Aucune compétence technique requise. Suivez le guide — 3 minutes pour obtenir votre première « contestation » de l'IA.

🌐 [简体中文](QUICKSTART.md) · [English](QUICKSTART.en.md) · [한국어](QUICKSTART.ko.md) · [Русский](QUICKSTART.ru.md) · [Español](QUICKSTART.es.md) · [日本語](QUICKSTART.ja.md) · [Français](QUICKSTART.fr.md) · [Deutsch](QUICKSTART.de.md) · [Português](QUICKSTART.pt.md)

---

## La seule chose à retenir

**Après l'installation, vous n'avez qu'une seule commande à retenir : `/poe`**

Elle identifie ce que vous essayez de faire et vous oriente vers le bon outil.
**Vous n'avez pas besoin d'apprendre les noms des 32 skills.**

---

## Étape 1 — Installer (≈ 30 secondes)

Dans un terminal (Windows : utilisez Git Bash ou WSL) :

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

Ou, si vous avez déjà téléchargé le dossier du projet, lancez ceci à l'intérieur :

```bash
bash install.sh
```

L'installateur détecte automatiquement vos outils d'IA (Claude Code, Codex, Cline,
WorkBuddy, …), demande confirmation, et installe les skills. Vous verrez :

```
[poeskill] done. Run /poe in your Agent to get started.
```

> **Pas de bash ?** Voir les [astuces Windows](#astuces-windows).

## Étape 2 — Tapez votre première phrase (30 secondes)

Ouvrez votre outil d'IA et tapez simplement — en langage naturel, sans format particulier :

```
/poe I have an idea: a coffee shop AI queue-ordering mini-app. Should I do it?
```

C'est tout. Il prend le relais à partir de là.

## Étape 3 — Vivez la contestation (2 minutes)

Une IA normale répond « excellente idée, voici comment la construire ». Une IA
équipée de poeskill commence par vous contester :

- Elle remet votre prémisse en question : « **La file d'attente est-elle
  vraiment leur principal point de douleur ? L'avez-vous vérifié ?** »
- Elle exige des preuves : « Le patron paiera-t-il vraiment pour ça ?
  Avez-vous une preuve ? »
- Elle livre une conclusion falsifiable : « **Ne le faites pas — sauf si**
  X se produit » au lieu de « cela dépend de votre exécution ».

**C'est tout l'enjeu : elle conteste d'abord pour que vous preniez de meilleures décisions.**

---

## Comment savoir si l'installation a fonctionné ?

| Méthode | Comment |
|---|---|
| Essayez simplement | Tapez `/poe` — si vous obtenez l'onboarding ou le routage, c'est installé |
| Vérifiez le dossier | 32 dossiers `poe-*` existent dans votre répertoire de skills (ex. `~/.claude/skills/`) |
| Vérifiez la sortie d'installation | `skills installed → <dir> (32 skills)` signifie succès |

## Situations courantes, en langage naturel

Vous n'avez pas besoin de ce tableau — `/poe` route automatiquement. Il est là
pour vous donner une carte mentale :

| Ce que vous voulez | Dites simplement | En coulisses |
|---|---|---|
| Décider si une idée vaut la peine d'être réalisée | « aide-moi à analyser si je devrais le faire » | `/poe-diagnosis` |
| Vérifier une affirmation ou un article | « aide-moi à vérifier cette affirmation » | `/poe-verify` |
| Incapable d'exprimer ce que vous voulez | « aide-moi à clarifier cet objectif » | `/poe-goal` |
| Vous savez quoi faire mais n'arrivez pas à démarrer | « pourquoi est-ce que je procrastine sans cesse » | `/poe-action` |
| Un buzzword ne veut rien dire de concret | « démonte ce mot pour moi » | `/poe-deconstruct` |
| Vous n'arrivez pas à écrire une bonne accroche | « aide-moi à améliorer ce hook » | `/poe-hook` |
| Une décision que vous pourriez regretter plus tard | « aide-moi à suivre cette décision sur le long terme » | `/poe-decision` |

## Astuces Windows

1. **Utilisez Git Bash ou WSL** pour lancer l'installateur — c'est un script
   bash, et les deux embarquent bash.
2. **Vous ne voulez pas de bash du tout ?** Très bien : demandez à quelqu'un
   (ou à votre outil d'IA) de lancer l'installation pour vous. Ensuite,
   l'utilisation se résume à taper `/poe` — aucun terminal requis.
3. **Où s'est-il installé ?** L'installateur affiche
   `skills installed → <path>`. Notez ce chemin.
4. **L'installateur bloqué ou en erreur ?** Collez l'erreur dans `/poe`
   (« j'ai un problème d'installation »), ou ouvrez un ticket.

---

## Et ensuite ?

- Ce que fait réellement chaque outil → [README](README.fr.md)
- La preuve que ça fonctionne → [`benchmark/`](benchmark/) (même question :
  à nu 6/25 vs avec poeskill 25/25)
- Un problème quelconque → dites à `/poe` « j'ai un problème », ou ouvrez un
  [ticket](https://github.com/wastefulthink/poeskill/issues/new)

> v3.5.1 ｜ MIT ｜ Fonctionne en local : pas de télémétrie, pas d'inscription, pas de compte
