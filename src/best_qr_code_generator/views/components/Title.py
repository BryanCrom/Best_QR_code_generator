# Purpose: GUI component class for the title on the home view
# Author: Bryan Crombach

from PyQt6.QtWidgets import QLabel


class Title(QLabel):
    """
    Title is a QLabel that displays the title of the application on the home view.
    Inherits from QLabel to support the PyQt GUI.
    """

    def __init__(self, text: str) -> None:
        """
        Initialises the Title by setting up the properties for displaying the title text.

        :param text: The text to be displayed as the title of the application on the home view.
        :return: None.
        """
        super().__init__(text)

        self.setStyleSheet("""
        QLabel {
            color: rgb(217, 4, 41); 
            font-size: 24px; 
            font-weight: bold; 
            font-family: Georgia;
        }
        """)
