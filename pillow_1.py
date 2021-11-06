# image processing with pillow

from PIL import Image

# open image using image module

im=Image.open("Python.jpg")

# show the actual image

im.show()

# show rotated image

im = im.rotate(45)

im.show()