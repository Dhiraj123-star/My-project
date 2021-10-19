# changing pdf documents to speech using python

# importing the modules

import PyPDF2
import pyttsx3

# path of the pdf file

path= open("myfile.pdf",'rb')

# creating a PdfFileReader object

pdfreader = PyPDF2.PdfFileReader(path)

# the page with which you want to start 
# this will read the page of 10th page

from_page = pdfreader.getPage(10)

# extracting the text from the PDF

text = from_page.extractText()

# reading the text

speak= pyttsx3.init()
speak.say(text)
speak.runAndWait()