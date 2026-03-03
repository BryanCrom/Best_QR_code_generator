from PyQt6.QtWidgets import QLineEdit


class InputField(QLineEdit):
    def __init__(self):
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

