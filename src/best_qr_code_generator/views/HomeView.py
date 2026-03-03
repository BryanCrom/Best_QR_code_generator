from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from best_qr_code_generator.views.components.Button import Button
from best_qr_code_generator.views.components.InputField import InputField
from best_qr_code_generator.views.components.RoundedRect import RoundedRect
from best_qr_code_generator.views.components.Title import Title


class HomeView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100,100, 400, 500)
        self.setStyleSheet("background-color: #2B2D42;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.layout.addStretch()

        self.layout.addWidget(Title("QR Code Generator"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(InputField(), alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(Button("ENTER"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(RoundedRect(200, 200), alignment=Qt.AlignmentFlag.AlignCenter)

        self.layout.addStretch()

