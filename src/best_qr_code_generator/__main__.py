import qrcode

def main() -> None:
    url = ""
    img = qrcode.make(url)
    img.save("qrcode.png")
    print("success")