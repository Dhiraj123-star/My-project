# word to pdf convertor using Python

from docx2pdf  import convert

# converting docx present in the same folder as the python file

convert("Intro.docx")

print("Converted Successfully")