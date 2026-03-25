# Purpose: GUI component class for the input field on the home view
# Author: Bryan Crombach

from PyQt6.QtWidgets import QLineEdit


class InputField(QLineEdit):
    """
    InputField is a text input field where the user can enter the text to be converted into a QR code.
    Inherits from QLineEdit to support the PyQt GUI.
    """

    def __init__(self) -> None:
        """
        Initializes the InputField by setting up the placeholder text, styling, and fixed width.

        :return: None.
        """
        super().__init__()

        self.setPlaceholderText("Enter your URL")
        self.setStyleSheet("""
        QLineEdit {
            background-color: rgb(141, 153, 174);
            border-radius: 40px;
            padding: 10px;
            color: rgb(0, 0, 0);
            font-size: 16px;
            font-family: Georgia;
        }
        """)
        self.setFixedWidth(300)

    def get_text(self) -> str:
        """
        Retrieves the text entered in the input field.

        :return: text (string): The text entered in the input field.
        """
        return self.text()
