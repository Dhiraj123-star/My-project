# flipped image using Pillow 
from PIL import Image

# open the image

img = Image.open("sunset.jpg")

# perform the a flip left and right

hori_flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# display the original image

img.show()

# display the horizontal flipped image

hori_flipped_img.show()
