# Purpose: GUI class for main view of the application, where the user can enter text and generate a QR code.
# Author: Bryan Crombach

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from best_qr_code_generator.views.components.EnterButton import EnterButton
from best_qr_code_generator.views.components.InputField import InputField
from best_qr_code_generator.views.components.Rect import Rect
from best_qr_code_generator.views.components.SaveButton import SaveButton
from best_qr_code_generator.views.components.Title import Title

from importlib import resources


class HomeView(QMainWindow):
    """
    HomeView is the main view of the application.
    It inherits from QMainWindow to support the PyQt GUI.

    Components:
    - Title: Displays the title of the application.
    - InputField: A text input field where the user can enter the text to be converted into a QR code.
    - Rect: A widget that displays the generated QR code in a rectangle.
    - SaveButton: A button that allows the user to save the generated QR code as an image file.
    - EnterButton: A button that triggers the generation of the QR code based on the text entered in the InputField.
    """

    def __init__(self):
        """
        Initializes the HomeView by setting up the window properties and adding the components to the layout.
        """
        super().__init__()

        self.setWindowTitle("QR Code Generator")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #2B2D42;")
        with resources.as_file(resources.files("best_qr_code_generator.assets").joinpath("logo.svg")) as logo_path:
             self.setWindowIcon(QIcon(str(logo_path)))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.title = Title("QR Code Generator")
        self.input_field = InputField()
        self.rect = Rect(200, 200)
        self.save_button = SaveButton("SAVE", self.rect)
        self.enter_button = EnterButton(
            "ENTER", self.rect, self.input_field, self.save_button
        )

        self.layout = QVBoxLayout(self.central_widget)

        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.layout.addStretch()
        self.layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.input_field, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.enter_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.rect, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.save_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addStretch()
