
import os
import sys
from urllib.parse import urlparse

# Réduire les journaux Qt et Chromium avant leur initialisation.
os.environ["QT_LOGGING_RULES"] = "*.debug=false;qt.qpa.*=false;qt.webenginecontext=false"
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--log-level=3 --disable-logging"

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView


def ouvrir_lecteur(url, titre="Movix — Lecteur"):
    """Ouvre un lecteur vidéo dans une fenêtre dédiée."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("URL du lecteur invalide.")

    # Masquer les sorties natives de Qt/Chromium pendant la lecture.
    devnull = os.open(os.devnull, os.O_WRONLY)
    ancien_stdout = os.dup(1)
    ancien_stderr = os.dup(2)

    try:
        os.dup2(devnull, 1)
        os.dup2(devnull, 2)

        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)

        app.setApplicationName("Movix CLI")

        view = QWebEngineView()
        view.setWindowTitle(titre)
        view.resize(1000, 700)
        view.setUrl(QUrl(url))
        view.show()

        return app.exec()
    finally:
        os.dup2(ancien_stdout, 1)
        os.dup2(ancien_stderr, 2)
        os.close(ancien_stdout)
        os.close(ancien_stderr)
        os.close(devnull)


if __name__ == "__main__":
    ouvrir_lecteur("https://luluvdo.com/e/tgse2g1118v6")
