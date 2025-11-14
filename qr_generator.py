import qrcode

url = input("Enter any URL or text content: ").strip()
file_path = "qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code successfully generated!!")

#https://www.youtube.com/watch?v=dQw4w9WgXcQ