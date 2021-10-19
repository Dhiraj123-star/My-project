import fitz

# read pdf file

pdf= fitz.open('test_file.pdf')

# load pdf page using index

page = pdf.loadPage(0)

# take image of page

img= page.getPixmap()

#save the image

img.writeImage(f'image.png')
