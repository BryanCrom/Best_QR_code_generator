import sys

from PyQt6.QtWidgets import QApplication

from .views.HomeView import HomeView

def main() -> None:
    app = QApplication(sys.argv)
    window = HomeView()
    window.show()
    sys.exit(app.exec())