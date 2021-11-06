# create thumbnail of the image

from PIL import Image

def thumbs():
    try:
        img = Image.open("Python.jpg")
        img.thumbnail((80,80)) # give the size of the thumbnail
        img.save('thumbnail.jpg')
        image1= Image.open('thumbnail.jpg')
        image1.show()
    except IOError:
        pass


thumbs()

