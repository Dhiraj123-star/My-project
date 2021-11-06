# example example of rotation

from PIL import Image

# open the image

img = Image.open("sunset.jpg")

# perform the flip

horizon_flip_img = img.transpose(Image.ROTATE_270)

# show the original image

img.show()

# show the flipped image

horizon_flip_img.show()