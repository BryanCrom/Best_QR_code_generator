from best_qr_code_generator.models.qr_generator import create_qr_code

def on_enter(url: str, image_widget, save_button) -> None:
    qr_code = create_qr_code(url)
    image_widget.set_pixmap(qr_code)
    save_button.setEnabled(True)
    save_button.setStyleSheet("""
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
