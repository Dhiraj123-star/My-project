import fitz

# read pdf file

pdf = fitz.open("test_file.pdf")

# iterate through pdf pages

for page in range(0,len(pdf)):

    # load pages with index
    pages= pdf.loadPage(page)
    #takes image of page
    img= pages.getPixmap()
    #save image
    img.writeImage(f'image1{page+1}.png')

print("Converted successfully!!")