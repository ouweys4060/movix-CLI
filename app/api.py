import json
import urllib.error
import urllib.parse
import urllib.request


API_URL = "https://api.movix.dog/api"


class MovixAPIError(Exception):
    """Erreur de communication avec l'API Movix."""


def _get_json(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "MovixCLI/1.0",
            "Accept": "application/json",
            "Referer": "https://movix.dog/",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        raise MovixAPIError(
            f"Movix a répondu avec HTTP {error.code}."
        ) from error
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        raise MovixAPIError(
            f"Connexion à Movix impossible : {error}"
        ) from error
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise MovixAPIError(
            "L'API Movix a renvoyé une réponse invalide."
        ) from error

    if not isinstance(data, dict):
        raise MovixAPIError("Format de réponse Movix inattendu.")

    return data


def search_title(title):
    """Recherche tous les titres ayant un identifiant TMDB valide."""
    query = urllib.parse.urlencode({"title": title})
    data = _get_json(f"{API_URL}/search?{query}")
    results = data.get("results", [])

    if not isinstance(results, list):
        return []

    valid_results = []
    seen = set()

    for item in results:
        if not isinstance(item, dict):
            continue

        name = item.get("name")
        tmdb_id = str(item.get("tmdb_id", "")).strip()
        media_type = str(item.get("type", "")).lower().strip()

        if not isinstance(name, str) or not name.strip():
            continue

        if not tmdb_id.isdigit() or int(tmdb_id) <= 0:
            continue

        # L'API Movix peut renvoyer des films sous des types inattendus,
        # par exemple "animes". Ne pas filtrer sur le champ "type".
        # is_series, lorsqu'il est fourni par l'API, permet de distinguer
        # une série d'un film sans dépendre de la catégorie du catalogue.
        is_series = item.get("is_series")
        if isinstance(is_series, bool):
            playback_type = "tv" if is_series else "movie"
        elif media_type in ("tv", "series", "show"):
            playback_type = "tv"
        else:
            playback_type = "movie"

        key = (playback_type, tmdb_id)
        if key in seen:
            continue

        seen.add(key)
        result = dict(item)
        result["tmdb_id"] = tmdb_id
        result["_playback_type"] = playback_type
        valid_results.append(result)

    return valid_results


def get_players(media_type, tmdb_id):
    """Récupère les lecteurs tiers disponibles pour un film ou une série."""
    media_type = str(media_type).lower().strip()

    if media_type in ("series", "show"):
        media_type = "tv"

    if media_type not in ("movie", "tv"):
        raise MovixAPIError("Type de média non reconnu.")

    tmdb_id = str(tmdb_id).strip()
    if not tmdb_id.isdigit() or int(tmdb_id) <= 0:
        raise MovixAPIError("Identifiant TMDB invalide.")

    data = _get_json(f"{API_URL}/tmdb/{media_type}/{tmdb_id}")
    players = data.get("player_links", [])

    if not isinstance(players, list):
        return []

    valid_players = []

    for player in players:
        if not isinstance(player, dict):
            continue

        url = player.get("decoded_url")
        if not isinstance(url, str):
            continue

        parsed = urllib.parse.urlparse(url)

        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            continue

        valid_players.append({
            "url": url,
            "host": parsed.hostname.removeprefix("www."),
            "quality": str(player.get("quality") or "Lecteur vidéo"),
            "language": str(player.get("language") or "Langue inconnue"),
        })

    # Certaines réponses fournissent aussi un lecteur principal séparé.
    main_url = data.get("iframe_src")
    if isinstance(main_url, str):
        parsed = urllib.parse.urlparse(main_url)
        if (
            parsed.scheme in ("http", "https")
            and parsed.hostname
            and not any(player["url"] == main_url for player in valid_players)
        ):
            valid_players.insert(0, {
                "url": main_url,
                "host": parsed.hostname.removeprefix("www."),
                "quality": "Lecteur principal",
                "language": "Langue inconnue",
            })

    return valid_players
