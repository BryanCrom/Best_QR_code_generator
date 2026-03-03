from PyQt6.QtWidgets import QLabel


class Title(QLabel):
    def __init__(self, text: str):
        super().__init__(text)

        self.setStyleSheet("""
        QLabel {
            color: rgb(217, 4, 41); 
            font-size: 24px; 
            font-weight: bold; 
            font-family: Georgia;
        }
        """)