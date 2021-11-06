# extracting image details 

from PIL import Image

im = Image.open("Python.jpg")

print(im.format) # returning the format
 
print(im.filename)  # returning the filename

print(im.mode) # returning the mode of the image

print(im.size) # returning the size of the image

print(im.height) # returning the height of the image

print(im.width) # returning the width of the image

print(im.info) # returning the info of the image

print("Thanks for using Python!!")