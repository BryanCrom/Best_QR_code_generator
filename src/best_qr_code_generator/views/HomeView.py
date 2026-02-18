import sys

from PyQt6 import QtGui, QtCore, QtWidgets
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class HomeView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)

        self.window = QMainWindow()
        self.window.setWindowTitle("QR Code Generator")
        self.window.setGeometry(100, 100, 400, 200)
        self.window.setStyleSheet("background-color: #2B2D42;")

        label = QLabel("Hello World!", self.window)
        label.setStyleSheet("color: #EDF2F4; font-weight: bold; font-size: 18px;")
        label.setGeometry(100, 100, 200, 100)
        label.move(150, 80)

        self.window.show()

    def paint_event(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setPen(QtCore.Qt.GlobalColor.white)
        painter.drawRoundedRect(50,50,300,200, 10, 10)