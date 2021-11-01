# web scraping using Python(requests)

import requests

url = "https://realpython.github.io/fake-jobs/"

page = requests.get(url)

print(page.text)