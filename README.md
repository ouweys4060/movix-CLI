# Movix CLI

**Un lecteur de films en ligne de commande, écrit en Python et basé sur l’API Movix.**

Movix CLI permet de rechercher des films, de sélectionner une source vidéo et d’ouvrir le lecteur dans une fenêtre dédiée. Le projet est développé sous Linux et utilise une interface interactive dans le terminal.

> [!WARNING]
> **Version 0.1 Beta**
>
> Le projet est encore en développement et a été réalisé avec beaucoup d’aide de l’intelligence artificielle, en expérimentant au fur et à mesure. Le code et les fonctionnalités pourront évoluer : des bugs sont possibles.
>
> **Les séries ne fonctionnent pas encore.** Pour le moment, seule la lecture des films est prise en charge.

## Fonctionnalités

- Recherche de films via l’API Movix.
- Interface interactive dans le terminal.
- Sélection parmi les lecteurs vidéo disponibles.
- Lecture dans une fenêtre dédiée grâce à Qt WebEngine.
- Navigation au clavier.

## Prérequis

- Linux
- Python 3
- Git
- Une connexion Internet

## Installation

### 1. Télécharger le projet

Remplace `VOTRE_PSEUDO` par ton nom d’utilisateur GitHub.

```bash
git clone https://github.com/VOTRE_PSEUDO/movix-cli.git
cd movix-cli
```

### 2. Installer les dépendances

Créer un environnement virtuel :

```bash
python -m venv .venv
source .venv/bin/activate
```

Installer PySide6 et ses composants :

```bash
pip install PySide6 PySide6-Addons PySide6-Essentials shiboken6
```

### 3. Lancer Movix CLI

Depuis le dossier du projet :

```bash
python movix.py
```

## Créer la commande `movix`

Pour lancer l’application depuis n’importe quel dossier avec simplement `movix`, tu peux créer un lanceur dans `~/.local/bin`.

Depuis le dossier `movix-cli`, exécute :

```bash
mkdir -p ~/.local/bin
printf '#!/bin/sh\ncd "$HOME/Projets/movix-cli" && exec "$HOME/Projets/movix-cli/.venv/bin/python" "$HOME/Projets/movix-cli/movix.py" "$@"\n' > ~/.local/bin/movix
chmod +x ~/.local/bin/movix
```

Cette commande suppose que le projet se trouve dans `~/Projets/movix-cli`. Si tu l’as installé ailleurs, adapte le chemin dans le lanceur.

Si `~/.local/bin` n’est pas déjà dans ton `PATH`, ajoute-le à ton fichier de configuration Fish :

```fish
fish_add_path ~/.local/bin
```

Tu peux maintenant lancer l’application avec :

```bash
movix
```

## Utilisation

1. Saisir le titre à rechercher.
2. Choisir un résultat dans le menu.
3. Sélectionner un lecteur vidéo.
4. Le lecteur s’ouvre dans une fenêtre séparée.
5. Fermer cette fenêtre pour revenir au terminal.

### Commandes clavier

| Touche | Action |
|---|---|
| `↑` / `↓` | Naviguer |
| `Entrée` / `→` | Confirmer |
| `←` / `Échap` | Revenir en arrière ou annuler |
| `Q` | Quitter |

## Limitations actuelles

- **Les séries ne fonctionnent pas encore.** La sélection des saisons et des épisodes reste à développer.
- Le projet n’a pas encore été testé de manière approfondie sur différentes distributions Linux.
- Certains lecteurs tiers peuvent ne pas fonctionner ou afficher des publicités.
- La gestion des erreurs et l’installation pourront être améliorées.

## Développement et contributions

Movix CLI est actuellement en **version 0.1 Beta**. C’est un projet expérimental qui évoluera en fonction des tests, des retours et des contributions.

**Toute aide est la bienvenue !**

Tu peux contribuer en :

- Ajoutant la prise en charge des séries.
- Corrigeant des bugs.
- Améliorant l’interface et l’expérience utilisateur.
- Simplifiant l’installation.
- Améliorant le code et la documentation.
- Testant l’application sur d’autres distributions Linux.

Les suggestions, issues et pull requests sont les bienvenues, quel que soit ton niveau en programmation.

## Crédits

Un grand merci à l’équipe de **Movix** pour le projet original, son API et le travail de mise à disposition du code source.

- Projet original : [Movix Open Source sur GitHub](https://github.com/movixcorp/MovixOpenSource)
- Site et services Movix : [movix.online](https://movix.online)

Movix CLI est un projet indépendant, développé à partir de l’API Movix. Il n’est pas le projet officiel de l’équipe Movix et n’est pas nécessairement affilié à celle-ci.

## Avertissement

Movix CLI n’héberge aucune vidéo. L’application récupère des informations et des liens vers des lecteurs tiers via l’API Movix. L’utilisation de ces services doit respecter les lois applicables et leurs conditions d’utilisation.

## Licence

La licence de Movix CLI reste à définir. Le projet original Movix possède sa propre licence : consulte son [dépôt GitHub](https://github.com/movixcorp/MovixOpenSource) pour connaître les conditions applicables à son code. Cette licence ne s’applique pas automatiquement à Movix CLI.
