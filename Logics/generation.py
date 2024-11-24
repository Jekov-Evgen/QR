import qrcode
import os

def get_desk():
    path = os.path.join(os.path.expanduser('~'), r"OneDrive/Desktop")
    return path

def generate(url):
    image = qrcode.make(url)
    user_path = get_desk()
    
    image.save(os.path.join(user_path, "QR_CODE.png"))
    