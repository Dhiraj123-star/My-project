# image processing with pillow
from PIL import Image

img = Image.open("sunset.jpg")

r,g,b = img.split()

img.show()

img = Image.merge('RGB',(b,g,r))

img.show()
