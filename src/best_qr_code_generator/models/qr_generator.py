import qrcode

def create_qr_code(url: str) -> None:
    img = qrcode.make(url)
    img.save("qrcode.png")
    print("success")