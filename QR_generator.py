import pyqrcode
from PIL import Image
url = input("Enter anything you want a QR code for : ")
qr_code = pyqrcode.create(url)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png")
print('QR code has been Generated and saved on the local folder')
