import pywhatkit

text = "Python is an awesome programming language to learn!!"

pywhatkit.text_to_handwriting(text,rgb=(0,0,255),save_to="handwriting.png")

print("converted ")
