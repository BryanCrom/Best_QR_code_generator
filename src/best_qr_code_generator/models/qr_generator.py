# Purpose: Holds all the functions related to the QR code generation process.
# Author: Bryan Crombach

import io

import qrcode
from PyQt6.QtGui import QImage


def create_qr_code(url: str) -> QImage:
    """
    generates a QR code image from the provided URL and converts it to a QImage for display in the PyQt GUI.

    :param url: The URL for which the QR code will be generated.
    :return: Image (QImage): The generated QR code image as a QImage object that can be displayed in the PyQt GUI.
    """
    qr_code = qrcode.make(url)
    buffer = io.BytesIO()
    qr_code.save(buffer, format="PNG")
    return QImage.fromData(buffer.getvalue())
