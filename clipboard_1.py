import pyperclip

text = "Python is very easy programming language"

# copy text to clipboard

pyperclip.copy(text)

# paste text from clipboard

text = pyperclip.paste()

print(text)
