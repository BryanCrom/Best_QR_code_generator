from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


class QrImage(QLabel):
    def __init__(self):
        super().__init__()

        self.setScaledContents(True)
        self.setFixedSize(150, 150)
        self.setPixmap(QPixmap())

    def set_pixmap(self, image) -> None:
        pixmap = QPixmap.fromImage(image)
        self.setPixmap(pixmap)

    def get_pixmap(self) -> QPixmap:
        return self.pixmap()