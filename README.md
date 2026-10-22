# Movix CLI

**Un lecteur de films en ligne de commande pour Linux, écrit en Python et basé sur l’API Movix.**

Movix CLI permet de rechercher des films, de choisir un lecteur vidéo disponible et de l’ouvrir dans une fenêtre dédiée. L’interface de sélection fonctionne directement dans le terminal.

> [!WARNING]
> **Version 0.1 Beta**
>
> Le projet a été réalisé avec beaucoup d’expérimentation et l’aide de l’intelligence artificielle (*vibe coding*). Il est encore en développement : des bugs sont possibles et le code peut évoluer.
>
> **Les séries ne fonctionnent pas encore.** Pour le moment, la prise en charge concerne uniquement les films.

## Fonctionnalités

- Recherche de titres via l’API Movix.
- Interface interactive dans le terminal.
- Sélection parmi les lecteurs vidéo disponibles.
- Ouverture du lecteur dans une fenêtre dédiée avec Qt WebEngine.
- Navigation au clavier.

## Prérequis

- Linux
- Python 3
- Git
- Une connexion Internet

## Installation

### 1. Télécharger le projet

```bash
git clone https://github.com/ouweys4060/movix-CLI.git
cd movix-CLI
```

### 2. Créer un environnement Python

Créer un environnement virtuel :

```bash
python -m venv .venv
```

L’activer avec Bash ou Zsh :

```bash
source .venv/bin/activate
```

Ou avec Fish :

```fish
source .venv/bin/activate.fish
```

Installer la dépendance de l’interface et du lecteur :

```bash
python -m pip install PySide6
```

### 3. Lancer l’application

Depuis le dossier du projet :

```bash
python movix.py
```

## Créer la commande `movix`

Tu peux créer un lanceur local pour démarrer l’application depuis n’importe quel dossier. Après l’installation des dépendances, exécute ces commandes **depuis le dossier du projet** :

```bash
mkdir -p ~/.local/bin
printf '#!/bin/sh\nexec "%s/.venv/bin/python" "%s/movix.py" "$@"\n' "$PWD" "$PWD" > ~/.local/bin/movix
chmod +x ~/.local/bin/movix
```

Le lanceur mémorise le chemin du dossier dans lequel tu l’as créé. Si `~/.local/bin` n’est pas dans ton `PATH`, ajoute-le à Fish :

```fish
fish_add_path ~/.local/bin
```

Tu peux ensuite lancer l’application avec :

```bash
movix
```

Si tu déplaces le dossier du projet, recrée le lanceur depuis son nouvel emplacement.

## Utilisation

1. Saisir le titre à rechercher.
2. Sélectionner un résultat dans le menu.
3. Choisir un lecteur vidéo disponible.
4. Le lecteur s’ouvre dans une fenêtre séparée.
5. Fermer cette fenêtre pour revenir au terminal.

### Commandes clavier

| Touche | Action |
|---|---|
| `↑` / `↓` | Naviguer dans le menu |
| `Entrée` / `→` | Confirmer la sélection |
| `←` / `Échap` | Revenir en arrière ou annuler |
| `Q` | Quitter |

## Limitations actuelles

- **Les séries ne fonctionnent pas encore.** La sélection des saisons et des épisodes reste à implémenter.
- Certains lecteurs tiers peuvent ne pas fonctionner ou afficher des publicités.
- La gestion des erreurs et la compatibilité doivent encore être améliorées.
- Le projet n’a pas encore été testé de manière approfondie sur différentes distributions Linux.

## Contributions

Movix CLI est un projet expérimental en version **0.1 Beta**. **Toute aide est la bienvenue !**

Tu peux contribuer en ajoutant la prise en charge des séries, en corrigeant des bugs, en améliorant l’interface ou l’installation, en révisant le code et la documentation, ou en testant l’application sur d’autres distributions Linux.

Les suggestions, issues et pull requests sont les bienvenues, quel que soit ton niveau en programmation.

## Crédits

Merci aux créateurs et contributeurs de **Movix** pour le projet original, son API et le travail partagé avec la communauté.

- Projet original : [Movix Open Source sur GitHub](https://github.com/movixstream/MovixOpenSource)
- Site de Movix : [movix.dog](https://movix.dog)

Movix CLI est un projet indépendant et non officiel. Il n’est pas présenté comme étant le projet officiel de l’équipe Movix.

## Avertissement

Movix CLI n’héberge aucune vidéo. L’application récupère des informations et des liens vers des lecteurs tiers via l’API Movix. Les utilisateurs sont responsables du respect des lois applicables et des conditions d’utilisation des services auxquels ils accèdent.

## Licence

Movix CLI est distribué sous la **licence MIT**. Tu peux utiliser, modifier et redistribuer le code couvert par cette licence, y compris dans des projets commerciaux, à condition de conserver les mentions de copyright et le texte de la licence dans les copies ou portions substantielles du code.

Cette licence concerne le code de Movix CLI dont les droits peuvent être accordés par son auteur. Le code provenant du projet original Movix reste soumis à sa propre licence. Consulte le fichier [`LICENSE`](LICENSE) et la licence du projet original pour plus de détails.
