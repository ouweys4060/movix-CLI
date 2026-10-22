
import curses


def ecrire(stdscr, y, x, texte, attribut=0):
    try:
        hauteur, largeur = stdscr.getmaxyx()
        if 0 <= y < hauteur and 0 <= x < largeur:
            stdscr.addnstr(
                y, x, str(texte), max(0, largeur - x - 1), attribut
            )
    except curses.error:
        pass


def initialiser_couleurs():
    if not curses.has_colors():
        return

    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, -1)
    curses.init_pair(3, curses.COLOR_CYAN, -1)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(5, curses.COLOR_YELLOW, -1)


def choisir(stdscr, elements, titre, afficher):
    if not elements:
        return None

    curses.curs_set(0)
    stdscr.keypad(True)
    initialiser_couleurs()

    selection = 0
    debut = 0

    while True:
        stdscr.erase()
        hauteur, largeur = stdscr.getmaxyx()

        ecrire(stdscr, 0, 2, "◆ MOVIX CLI", curses.color_pair(3) | curses.A_BOLD)
        ecrire(stdscr, 1, 2, titre, curses.color_pair(2) | curses.A_BOLD)
        ecrire(stdscr, 2, 2, "─" * max(0, largeur - 4), curses.color_pair(3))
        ecrire(
            stdscr, 3, 2,
            "↑ ↓ Naviguer   Entrée / → Valider   ← Retour   Q Quitter",
            curses.color_pair(5),
        )

        zone_debut = 5
        capacite = max(1, hauteur - zone_debut - 2)

        if selection < debut:
            debut = selection
        elif selection >= debut + capacite:
            debut = selection - capacite + 1

        for i in range(debut, min(debut + capacite, len(elements))):
            texte = afficher(elements[i])
            y = zone_debut + i - debut

            if i == selection:
                ecrire(
                    stdscr, y, 2,
                    "  ❯ " + texte,
                    curses.color_pair(1) | curses.A_BOLD,
                )
            else:
                ecrire(
                    stdscr, y, 2,
                    "    " + texte,
                    curses.color_pair(2),
                )

        ecrire(
            stdscr, hauteur - 1, 2,
            f"{selection + 1}/{len(elements)} éléments",
            curses.color_pair(3),
        )

        stdscr.refresh()
        touche = stdscr.getch()

        if touche in (curses.KEY_UP, ord("k")):
            selection = (selection - 1) % len(elements)
        elif touche in (curses.KEY_DOWN, ord("j")):
            selection = (selection + 1) % len(elements)
        elif touche in (curses.KEY_ENTER, 10, 13, curses.KEY_RIGHT):
            return elements[selection]
        elif touche in (curses.KEY_LEFT, 27):
            return None
        elif touche in (ord("q"), ord("Q")):
            return "QUIT"


def choisir_titre(films):
    return curses.wrapper(
        choisir,
        films,
        "CHOISIR UN FILM OU UNE SÉRIE",
        lambda film: (
            f"{film.get('name', 'Titre inconnu')} "
            f"({film.get('year') or '?'}) · {film.get('type') or '?'}"
        ),
    )


def choisir_lecteur(lecteurs):
    return curses.wrapper(
        choisir,
        lecteurs,
        "CHOISIR UN LECTEUR VIDÉO",
        lambda lecteur: (
            f"{lecteur.get('host', 'lecteur inconnu')} · "
            f"{lecteur.get('quality', 'Lecteur vidéo')} "
            f"· {lecteur.get('language', 'Langue inconnue')}"
        ),
    )
