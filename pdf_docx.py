# pdf to docx convertor using Python

from pdf2docx import Converter

# pdf file

pdf_file = 'file_1.pdf'

# docx file to be created

docx_file = 'gitword.docx'

# convert pdf to docx

cv= Converter(pdf_file)
cv.convert(docx_file,start=0,end=None)

print("File converted successfully!!!")

cv.close()
