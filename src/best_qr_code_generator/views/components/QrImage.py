# Purpose: GUI component class for the image of the QR code on the home view
# Author: Bryan Crombach

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

class QrImage(QLabel):
    """
    This class is responsible for displaying the generated QR code as an image.
    Inherits from QLabel to support the PyQt GUI.
    """
    def __init__(self) -> None:
        """
        Initializes the QrImage by setting up the properties for displaying the QR code image.

        :return: None.
        """
        super().__init__()

        self.setScaledContents(True)
        self.setFixedSize(150, 150)
        self.setPixmap(QPixmap())

    def set_pixmap(self, image) -> None:
        """
        sets the pixmap of the QLabel to the generated QR code image.

        :param image: The generated QR code image that will be displayed in the QLabel.
        :return: None.
        """
        pixmap = QPixmap.fromImage(image)
        self.setPixmap(pixmap)

    def get_pixmap(self) -> QPixmap:
        """
        Retrieves the current pixmap of the QLabel

        :return: pixmap (QPixmap): The current pixmap of the QLabel, which is the generated QR code image.
        """
        return self.pixmap()