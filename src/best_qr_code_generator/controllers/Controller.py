from best_qr_code_generator.models.qr_generator import create_qr_code
from best_qr_code_generator.views.components.QrImage import QrImage


def on_enter(url: str, image_widget) -> None:
    qr_code = create_qr_code(url)
    image_widget.set_pixmap(qr_code)

def on_save() -> None:
    pass