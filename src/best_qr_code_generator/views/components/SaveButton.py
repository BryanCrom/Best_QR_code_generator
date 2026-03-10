from PyQt6.QtWidgets import QPushButton, QFileDialog


class SaveButton(QPushButton):
    def __init__(self, text: str, rounded_rect) -> None:
        super().__init__(text)

        self.rounded_rect = rounded_rect
        self.setStyleSheet("""
            background-color: rgb(125, 4, 41);
            border-radius: 20px;
            padding: 10px;
            color: rgb(0, 0, 0);
            font-size: 16px;
            font-family: Georgia;
        """)

        self.setFixedWidth(75)
        self.clicked.connect(lambda: self.on_save())
        self.setEnabled(False)

    def on_save(self) -> None:
        qr_code = self.rounded_rect.get_image_widget().get_pixmap()
        if qr_code.isNull():
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save QR Code",
            "",
            "PNG Files (*.png);;JPEG Files (*.jpg)",
        )

        if file_path:
            qr_code.save(file_path)