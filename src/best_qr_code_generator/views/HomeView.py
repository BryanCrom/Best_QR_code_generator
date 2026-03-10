from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from best_qr_code_generator.views.components.EnterButton import EnterButton
from best_qr_code_generator.views.components.InputField import InputField
from best_qr_code_generator.views.components.RoundedRect import RoundedRect
from best_qr_code_generator.views.components.Title import Title


class HomeView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Code Generator")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #2B2D42;")
        self.setWindowIcon(QIcon("src/assets/logo.svg"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.rounded_rect = RoundedRect(200, 200)
        self.input_field = InputField()
        self.layout.addStretch()

        self.layout.addWidget(Title("QR Code Generator"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.input_field, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(EnterButton("ENTER", self.rounded_rect, self.input_field), alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.rounded_rect, alignment=Qt.AlignmentFlag.AlignCenter)

        self.layout.addStretch()

