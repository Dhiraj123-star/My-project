from urllib.request import urlopen

open_url=urlopen('https://www.djangoproject.com/')

webcontent = open_url.read()

print(webcontent)