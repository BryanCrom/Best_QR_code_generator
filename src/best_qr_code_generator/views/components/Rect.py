# Purpose: GUI component class for the rectangle container that contains the QrImage on the home view
# Author: Bryan Crombach

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout

from best_qr_code_generator.views.components.QrImage import QrImage


class Rect(QFrame):
    """
    Rect is a container widget that holds the QrImage widget, which displays the generated QR code.
    Inherits from QFrame to support the PyQt GUI.

    attributes:
    - image (QrImage): The QrImage widget that displays the generated QR code.
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes the Rect by setting up the properties for the container.

        :param width: the width of the rectangle container that holds the QrImage widget.
        :param height: the height of the rectangle container that holds the QrImage widget.
        :return: None.
        """
        super().__init__()

        self.setStyleSheet("background-color: rgb(141, 153, 174);")
        self.setFixedSize(width, height)

        self.image = QrImage()

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.image, alignment=Qt.AlignmentFlag.AlignCenter)

    def get_image_widget(self) -> QrImage:
        """
        Retrieves the QrImage widget contained within the Rect.

        :return: image (QrImage): The QrImage widget that displays the generated QR code within the Rect container.
        """
        return self.image
