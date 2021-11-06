# Merging Two images

from PIL import Image

img1 = Image.open("sunset.jpg")

#img1.show()

img2 = Image.open("Python.jpg")

#img2.show()

# resize the first image before merging

img1.paste(img2)

img1.show()