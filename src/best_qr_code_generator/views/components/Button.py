from PyQt6.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self, text: str):
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