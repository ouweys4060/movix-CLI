import sys
from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)
view = QWebEngineView()
view.setWindowTitle("Movix — Lecteur")
view.resize(1000, 700)
view.setUrl(QUrl("https://luluvdo.com/e/tgse2g1118v6"))
view.show()
sys.exit(app.exec())
