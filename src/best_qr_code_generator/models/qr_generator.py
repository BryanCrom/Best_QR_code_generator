import io

import qrcode
from PyQt6.QtGui import QImage


def create_qr_code(url: str) -> QImage:
    qr_code = qrcode.make(url)
    buffer = io.BytesIO()
    qr_code.save(buffer, format="PNG")
    return QImage.fromData(buffer.getvalue())