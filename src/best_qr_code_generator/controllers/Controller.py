# Purpose: contains the controller functions for the best QR code generator application.
# Authors: Bryan Crombach

from best_qr_code_generator.models.qr_generator import create_qr_code

def on_enter(url: str, image_widget, save_button) -> None:
    """
    Controller function to handle the event when the user presses the "Enter" key after inputting a URL.
    It generates a QR code from the input URL, displays it in the specified image widget,
    and enables the save button for the user to save the generated QR code.

    :param url: input URL to generate the QR code from.
    :param image_widget: widget container to display the generated QR code.
    :param save_button: save button widget to enable after generating the QR code.
    :return: None.
    """
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
