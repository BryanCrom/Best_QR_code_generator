import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class HomeView:
    def __init__(self):
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setWindowTitle("QR Code Generator")
        window.setGeometry(100, 100, 400, 200)

        label = QLabel("Hello World!", window)
        label.move(150, 80)

        window.show()

        sys.exit(app.exec())