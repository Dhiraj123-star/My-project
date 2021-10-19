# pdf to audio file convertor

import PyPDF2
from PyPDF2 import pdf
from pyttsx3 import engine
pdfreader = PyPDF2.PdfFileReader(open("myfile.pdf","rb"))

import pyttsx3

speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text=pdfreader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()


engine.save_to_file(text,'audio.mp3')
engine.runAndWait()
