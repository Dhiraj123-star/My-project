# blur the image using Python pillow

from PIL import Image,ImageFilter

original_image = Image.open("sunset.jpg")

# show the original image

original_image.show()

# Applying simple blur function

blur_image = original_image.filter(ImageFilter.BLUR)

# show the blur image

blur_image.show()