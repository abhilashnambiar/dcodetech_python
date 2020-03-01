import qrcode
from qrcode import QRCode

qr = qrcode.QRCode()
qr.add_data("Hello World!")
qr.make()
img = qr.make_image(fill_color="white",back_color="black")
img.save('DCodetech/test.png')