# poeskill

> 🌐 [简体中文](README.md) · [English](README.en.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md) · [日本語](README.ja.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

---

**Votre IA ne cesse d'être d'accord avec vous.**

Vous demandez « cette idée vaut-elle quelque chose ? » — elle répond « un fort potentiel ». Vous demandez « dois-je le faire ? » — elle répond « cela dépend de votre exécution ».

Elle ne dit jamais non. Elle ne demande jamais « l'avez-vous vérifié ? »

poeskill corrige précisément cela. 32 skills qui transforment n'importe quel outil d'IA en un partenaire qui vous tête — il remet d'abord vos prémisses en question, exige vos données, puis vous livre une conclusion que vous pouvez réellement falsifier. Pas « ça semble cohérent », mais « vrai ou faux — voici comment vérifier ».

---

## Pourquoi nous avons créé cela

J'ai longtemps utilisé des outils d'IA et j'ai remarqué un schéma récurrent : **plus l'IA devient intelligente, plus elle vous donne raison vite.**

Vous lui confiez un business plan plein de trous, elle les comble. Vous lui soumettez un souhait vague, elle le découpe en étapes — mais personne ne s'arrête pour demander : « attendez, la prémisse est-elle seulement vraie ? »

Les bonnes décisions ne naissent pas de « aide-moi à exécuter ». Elles naissent de « aide-moi à remettre en question ». J'ai donc repris les méthodes de pensée de 25 penseurs — de Hume à Hayek, de Feynman à Kahneman — distillées en 305 unités de connaissance sourcées, et les ai regroupées dans 32 skills installables en une seule commande.

Chaque skill suit un principe de conception unique : **il doit contester vos idées avant de vous aider.**

---

## Installation en 30 secondes

```bash
curl -fsSL https://raw.githubusercontent.com/wastefulthink/poeskill/main/install.sh | bash
```

Ou depuis un clone local :

```bash
git clone https://github.com/wastefulthink/poeskill.git
cd poeskill
bash install.sh            # auto-detects your AI tool
bash install.sh --all      # install into every detected tool
bash install.sh --target ~/.claude/skills
```

Fonctionne avec Claude Code, Codex, Cline, WorkBuddy, Kiro, Qwen Code — tout agent qui lit ses skills depuis un dossier.

Après l'installation, **vous n'avez qu'une seule commande à retenir : `/poe`.** Inutile d'apprendre les noms des 32 skills — le routage est automatique.

---

## Vos 3 premières minutes

1. Ouvrez votre outil d'IA et tapez, en langage naturel :

   ```
   /poe I have an idea: a coffee shop AI queue app. Should I do it?
   ```

2. Une IA normale répond « excellente idée, voici comment la construire ». Une IA équipée de poeskill commence par contester :
   - « La file d'attente est-elle vraiment leur principal point de douleur ? L'avez-vous vérifié ? »
   - « Le patron paiera-t-il vraiment pour ça ? Avez-vous une preuve ? »
   - Puis : « **Ne le faites pas — sauf si** X se produit » au lieu de « cela dépend de votre exécution ».

3. **Il conteste d'abord pour que vous preniez de meilleures décisions.** C'est tout l'objet de la démarche.

Nouveau ici ? Lisez le [guide de démarrage en 3 minutes](QUICKSTART.fr.md) (zéro jargon).

---

## Ce que cela fait

**Diagnostic de problèmes business**
- `/poe-diagnosis` — diagnostic de modèle économique, modes consultation + bilan
- `/poe-decision` — transformer les décisions à long terme en archives locales révisables
- `/poe-standard-answer` — trouver des mécanismes historiques isomorphes à votre dilemme
- `/poe-benchmark` — trouver des références (benchmarks), filtrer le bruit par un processus de sélection

**Chaîne complète de création de contenu**
- `/poe-good-question` — réécrire des questions vagues en spécifications prêtes pour le raisonnement
- `/poe-content` — diagnostic complet du contenu, du sujet au texte
- `/poe-hook` — optimisation des accroches de vidéos courtes
- `/poe-script-flow` — continuité du script et détection des points d'abandon
- `/poe-resonate` / `/poe-spread` — détection de résonance et psychologie de la communication
- `/poe-ai-check` — détecter les traces d'écriture IA
- `/poe-content-risk-check` — vérifications de risques avant publication et de conformité aux modérations de plateforme
- `/poe-xhs-title` — formules de titres pour Xiaohongshu (RED)
- `/poe-wechat-html` — Markdown vers HTML pour Compte Officiel WeChat

**Outils de pensée / cognition**
- `/poe-deconstruct` — démonter les concepts vagues par l'analyse du langage
- `/poe-action` — diagnostiquer « je sais quoi faire mais je n'arrive pas à passer à l'action »
- `/poe-slowisfast` — distinguer impatience et friction nécessaire, concevoir des trajectoires à intérêts composés
- `/poe-goal` — transformer des souhaits vagues en objectifs vérifiables

**Outils système (maintenance de poeskill lui-même)**
- `/poe` — entrée principale et routeur dynamique
- `/poe-chatroom` / `/poe-chatroom-market` — discussions multi-rôles (incl. la perspective de l'école de l'ordre de marché)
- `/poe-save` / `/poe-restore` / `/poe-report` — archivage et reporting de l'état des diagnostics
- `/poe-knowledge` / `/poe-content-system` — base de connaissances locale et ingénierie des actifs de contenu
- `/poe-learning` — apprentissage interactif
- `/poe-verify` — contre-vérification de toute conclusion (traçabilité des preuves / contre-exemples / grading des sources / vérification des conflits d'intérêts)
- `/poe-update` — mise à jour automatique depuis ce dépôt
- `/poe-bridge` / `/poe-agent-migration` — passerelle vers d'autres agents et migration d'espaces de travail
- `/poe-skill-cleaner` — auditer les skills pour y déceler des intentions commerciales dissimulées

---

## Base de connaissances : 305 unités · 25 penseurs

`知识库/` ne contient pas de vagues « résumés d'IA ». Elle rassemble 305 unités de puissance distillées des œuvres originales de 25 penseurs — Hume, Kant, Popper, Wittgenstein, Deutsch, Russell, Smith, Mises, Hayek, Laozi, Adler, Schopenhauer, Marc Aurèle, Nietzsche, Camus, Aristote, Mill, Weber, Keynes, Friedman, Schumpeter, Soros, Grove, Darwin, Feynman, Einstein, Newton, Shannon, Turing, Bacon, Descartes, Munger, Kahneman, Thaler, Taleb, Drucker, Porter, Simon, Coase, Pinker, Dennett.

Chaque unité indique sa source originale. Pas de « croyez-moi sur parole » — seulement « voici la citation, jugez par vous-même ».

- `能量库/powers_poe.jsonl` — le jeu de données maître
- `Skill知识包/` — 12 packs de connaissances dédiés aux skills
- `哲学概念词典.md` — référence rapide de 80 concepts

---

## C'est mesurable

La même décision business, exécutée deux fois sur le même modèle — à nu vs. avec poeskill. Sur le cas 01, le modèle à nu obtient **6/25** ; avec poeskill, **25/25**. Même modèle, même question ; la seule différence est qu'on a demandé ou non à l'IA de contester vos idées.

```bash
python benchmark/run_benchmark.py --prompt both   # needs an API key
```

Voir [`benchmark/`](benchmark/) pour le cas, les prompts, le runner et la grille de notation. **Cet écart, c'est le produit.**

---

## Pourquoi le nom « poe »

Trois niveaux de lecture :

1. **Un hommage à Edgar Allan Poe** — figure fondatrice du roman policier. Ses détectives ne se fient jamais aux récits de surface ; ils reconstruisent la vérité à partir d'indices infimes. C'est exactement le tempérament de cette boîte à outils : `/poe-diagnosis` remonte des symptômes aux causes racines, `/poe-verify` met les conclusions à l'épreuve par des contre-preuves, `/poe-deconstruct` démonte les buzzwords galvaudés.
2. **Problem-Oriented Engine** — chaque outil part d'un problème, jamais d'une réponse.
3. **Un nom indépendant** — court, mémorable, sans connotation négative dans les grandes langues.

---

## Pourquoi vous devriez mettre une étoile à ce dépôt

- **Il vous conteste.** Tout l'objectif est de ne pas être d'accord — chaque skill de diagnostic doit adjoindre à sa conclusion une condition falsifiable et un grade de fiabilité de la source.
- **Tout est vérifiable.** 305 unités, chacune avec sa citation. Aucune impression, aucun « croyez-moi ».
- **Tout fonctionne en local.** Pas de télémétrie, pas de SaaS, pas de compte. Vos questions ne quittent jamais votre machine.
- **MIT et entièrement original.** Écrit de zéro. Forkez-le, intégrez-le, construisez dessus.

---

## Usage critique (important)

poeskill est un outil de pensée, pas une machine à réponses :

1. Chaque skill produisant des conclusions **doit** adjoindre un grade de fiabilité de la source (A/B/C/D) ; en dessous de C, ce n'est qu'une piste
2. Les attributions qualitatives doivent s'accompagner de conditions falsifiables
3. En cas de doute, lancez `/poe-verify` pour une contre-vérification
4. Pour les décisions à forts enjeux (investissement, carrière, santé), recoupez plusieurs sources — ne faites jamais confiance à un seul cadre d'analyse
5. `/poe-action` et les autres outils psychologiques sont des aides à la connaissance de soi, pas de la psychothérapie

---

## Mises à jour

- L'entrée principale vérifie `UPDATE.json` au maximum une fois toutes les 24 h
- `/poe-update` se synchronise avec ce dépôt en préservant votre archive `~/.poe/`
- Faites un `git pull` avant la mise à jour pour examiner les changements

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md) (incl. le flux i18n), [ROADMAP.md](ROADMAP.md) et [CHANGELOG.md](CHANGELOG.md).

## Licence

MIT. Voir [LICENSE](LICENSE).

## Offrez-moi un café

Si poeskill vous a aidé à clarifier une décision, offrez-moi un café :

[![Buy Me a Coffee](https://img.shields.io/badge/☕-Offrir_un_café-FFDD00?logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/xueyegog)

Entièrement volontaire — sans mécénat, vous profitez quand même de l'outil et des mises à jour.

## Remerciements

- Ce dépôt est une implémentation originale, écrite de zéro. Tous les skills, unités de connaissance, scripts et documentations ont été rédigés indépendamment pour ce projet.
- Le projet est gratuit et open source ; le seul moyen de le soutenir est le don volontaire (voir ci-dessus). Aucune communauté payante ni tunnel de vente de cours.
- Le contenu de la base de connaissances est organisé à partir d'œuvres philosophiques et économiques publiquement disponibles ; chaque unité cite sa source originale.
