# import the following modules
from captcha.image import ImageCaptcha

# create an image instance of the given size

image = ImageCaptcha(width=300,height=100)

# image captcha text

captcha_text  = "Dhiraj loves Python"

# generate the image of the given text

data= image.generate(captcha_text)

# write the image on the given file and save it

image.write(captcha_text,"captcha.png")