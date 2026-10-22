#!/usr/bin/env python3

from app.api import MovixAPIError, search_title, get_players
from app.selection import choisir_titre, choisir_lecteur
from app.player import ouvrir_lecteur


def afficher_banniere():
    print(r"""
███╗   ███╗ ██████╗ ██╗   ██╗██╗██╗  ██╗     ██████╗██╗     ██╗
████╗ ████║██╔═══██╗██║   ██║██║╚██╗██╔╝    ██╔════╝██║     ██║
██╔████╔██║██║   ██║██║   ██║██║ ╚███╔╝     ██║     ██║     ██║
██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██║ ██╔██╗     ██║     ██║     ██║
██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║██╔╝ ██╗    ╚██████╗███████╗██║
╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝
""")


def est_serie(film):
    type_media = str(film.get("type", "")).lower()
    return any(mot in type_media for mot in ("tv", "series", "show"))


def main():
    afficher_banniere()
    print("Recherche de films et séries avec lecture dans une fenêtre dédiée.")
    print("Tapez q pour quitter.\n")

    while True:
        try:
            titre = input("Rechercher un film ou une série : ").strip()

            if titre.lower() == "q":
                break
            if not titre:
                continue

            print("Recherche en cours...")
            films = search_title(titre)

            if not films:
                print("Aucun résultat avec un identifiant TMDB valide.\n")
                continue

            choix = choisir_titre(films)
            if choix == "QUIT":
                break
            if choix is None:
                print("Sélection annulée.\n")
                continue

            # Le type de catégorie Movix peut être trompeur (ex. "animes"\n            # pour un film). Préférer le type de lecture normalisé par l’API.\n            media_type = choix.get("_playback_type")\n            if media_type not in ("movie", "tv"):\n                media_type = "tv" if choix.get("is_series") is True or est_serie(choix) else "movie"
            nom = choix["name"]
            tmdb_id = choix["tmdb_id"]

            print(f"\nRécupération des lecteurs pour {nom}...")
            lecteurs = get_players(media_type, tmdb_id)

            if not lecteurs:
                print("Aucun lecteur disponible pour ce titre.\n")
                continue

            lecteur = choisir_lecteur(lecteurs)
            if lecteur == "QUIT":
                break
            if lecteur is None:
                print("Choix du lecteur annulé.\n")
                continue

            print(f"\nOuverture : {nom}")
            print(f"Lecteur : {lecteur['quality']}")
            print("Fermez la fenêtre vidéo pour revenir au terminal.")

            ouvrir_lecteur(lecteur["url"], f"Movix — {nom}")

        except MovixAPIError as error:
            print(f"\nErreur Movix : {error}\n")
        except KeyboardInterrupt:
            print("\nArrêt de Movix CLI.")
            break
        except EOFError:
            print("\nArrêt de Movix CLI.")
            break


if __name__ == "__main__":
    main()
