from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from best_qr_code_generator.views.components.RoundedRect import RoundedRect

class HomeView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100,100, 400, 500)
        self.setStyleSheet("background-color: #2B2D42;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(RoundedRect())