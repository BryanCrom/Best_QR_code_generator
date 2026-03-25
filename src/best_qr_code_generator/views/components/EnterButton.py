# Purpose: GUI component class for the enter button on the home view
# Author: Bryan Crombach

from PyQt6.QtWidgets import QPushButton

from best_qr_code_generator.controllers.Controller import on_enter
from best_qr_code_generator.views.components.SaveButton import SaveButton


class EnterButton(QPushButton):
    """
    Enter button component that triggers the generation of the QR code based on the text entered in the InputField.
    Inherits from QPushButton to support the PyQt GUI.
    """

    def __init__(
        self, text: str, rect_widget, input_field, save_button: SaveButton
    ) -> None:
        """
        Initializes the EnterButton by setting up the button properties and connecting the click event to the on_enter function.

        params:
        - text (string): The text to be displayed on the button.
        - rect_widget (Rect): The Rect widget that displays the generated QR code.
        - input_field (InputField): The InputField widget where the user enters the text to be converted into a QR code.
        - save_button (SaveButton): The SaveButton widget that allows the user to save the generated QR code as an image file only after a qr code has been generated.

        :return: None
        """
        super().__init__(text)

        self.setStyleSheet("""
            QPushButton{ 
                background-color: rgb(217, 4, 41);
                border-radius: 20px;
                padding: 10px;
                color: rgb(0, 0, 0);
                font-size: 16px;
                font-family: Georgia;
            }
            QPushButton:hover { 
                background-color: rgb(239, 35, 60); 
            }
            """)
        self.setFixedWidth(150)
        self.clicked.connect(
            lambda: on_enter(
                input_field.get_text(), rect_widget.get_image_widget(), save_button
            )
        )
