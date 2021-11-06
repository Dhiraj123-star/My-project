# blur the image by gaussian blur function

from PIL import Image,ImageFilter

# open the image

im_1 = Image.open("sunset.jpg")

# show the original image

im_1.show()

# applying gaussian blur function

blur_image = im_1.filter(ImageFilter.GaussianBlur(6))

# show the blur image
blur_image.show()