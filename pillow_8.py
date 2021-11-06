# blur image using BoxBlur () function

from PIL import Image,ImageFilter

# open the original image

original_image = Image.open("sunset.jpg")

# show the original image

original_image.show()

# blur image 

blur_image = original_image.filter(ImageFilter.BoxBlur(4))

# show the blur image

blur_image.show()