from best_qr_code_generator.models.qr_generator import create_qr_code

def on_enter(url: str) -> None:
    create_qr_code(url)

def on_save() -> None:
    pass