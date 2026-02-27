from PyQt6.QtWidgets import QFrame

class RoundedRect(QFrame):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: rgb(141, 153, 174); border-radius: 20px;")
        self.setFixedSize(200, 200)