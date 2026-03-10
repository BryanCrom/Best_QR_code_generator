from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout

from best_qr_code_generator.views.components.QrImage import QrImage


class RoundedRect(QFrame):
    def __init__(self, width: int, height: int):
        super().__init__()

        self.setStyleSheet("background-color: rgb(141, 153, 174);")
        self.setFixedSize(width, height)

        self.image = QrImage()

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.image, alignment=Qt.AlignmentFlag.AlignCenter)

    def get_image_widget(self) -> QrImage:
        return self.image