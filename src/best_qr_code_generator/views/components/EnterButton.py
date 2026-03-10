from PyQt6.QtWidgets import QPushButton

from best_qr_code_generator.controllers.Controller import on_enter
from best_qr_code_generator.views.components.InputField import InputField


class EnterButton(QPushButton):
    def __init__(self, text: str, rounded_rect_widget, input_field):
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
        self.clicked.connect(lambda: on_enter(input_field.get_text(), rounded_rect_widget.get_image_widget()))