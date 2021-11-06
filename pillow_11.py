# vertically flipped image

from PIL import Image

# open the original image

img = Image.open("sunset.jpg")

# perform the flip of top and bottom

ver_flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)

# show the original image

img.show()

# show the vertically flipped image

ver_flipped_img.show()