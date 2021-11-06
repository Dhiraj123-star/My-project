import qrcode  # qrcode is a module 

img= qrcode.make(
    'https://m.facebook.com/Abharti.5220'
)

img.save('myQrcode.png')
img.show()