# Purpose: GUI component class for the save button on the home view
# Author: Bryan Crombach

from PyQt6.QtWidgets import QPushButton, QFileDialog


class SaveButton(QPushButton):
    """
    SaveButton is a button that allows the user to save the generated QR code as an image file.
    Inherits from QPushButton to support the PyQt GUI.

    attributes:
    - rect (Rect): The Rect widget that contains the QrImage widget, which displays the generated QR code.
    """

    def __init__(self, text: str, rect) -> None:
        """
        Initialises the SaveButton by setting up the button properties and connecting the click event to the on_save function.

        :param text: The text to be displayed on the button.
        :param rect: The Rect widget that contains the QrImage widget, which displays the generated QR code.
        :return: None.
        """
        super().__init__(text)

        self.rect = rect
        self.setStyleSheet("""
            background-color: rgb(125, 4, 41);
            border-radius: 20px;
            padding: 10px;
            color: rgb(0, 0, 0);
            font-size: 16px;
            font-family: Georgia;
        """)

        self.setFixedWidth(75)
        self.clicked.connect(lambda: self.on_save())
        self.setEnabled(False)

    def on_save(self) -> None:
        """
        Retrieves the generated QR code from the QrImage widget within the Rect container and opens a file dialog to
        allow the user to save the QR code as an image file (PNG or JPEG).

        :return: None.
        """
        qr_code = self.rect.get_image_widget().get_pixmap()
        if qr_code.isNull():
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save QR Code",
            "",
            "PNG Files (*.png);;JPEG Files (*.jpg)",
        )

        if file_path:
            qr_code.save(file_path)
