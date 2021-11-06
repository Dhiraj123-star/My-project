# creating Watermark on the image

from PIL import Image, ImageDraw

# creating an Image Object

img = Image.open("sunset.jpg")

d1= ImageDraw.Draw(img)

d1.text((250,100),"Dhiraj Pythonic",fill=(255,255,0))

# show the resultant image

img.show()