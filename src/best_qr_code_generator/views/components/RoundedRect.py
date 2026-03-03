from PyQt6.QtWidgets import QFrame

class RoundedRect(QFrame):
    def __init__(self, height: int, width: int):
        super().__init__()

        self.setStyleSheet("background-color: rgb(141, 153, 174); border-radius: 20px;")
        self.setFixedSize(width, height)