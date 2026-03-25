# Purpose: Entry point for the Best QR Code Generator PyQt application.
# Author: Bryan Crombach

import sys

from PyQt6.QtWidgets import QApplication

from .views.HomeView import HomeView

def main() -> None:
    """
    Entry point for the application.
    Initializes the QApplication, creates the HomeView, and starts the event loop.
    """
    app = QApplication(sys.argv)
    window = HomeView()
    window.show()
    sys.exit(app.exec())