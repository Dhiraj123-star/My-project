# web scraping using Python library (requests)

import requests

from bs4 import BeautifulSoup # this is library for web scraping which is much easier than requests

url ="https://quotes.toscrape.com/"

page = requests.get(url)

print(page.status_code) # 200 

# print HTML contents of page

print(page.content)

soup = BeautifulSoup(page.content,'html.parser')

# print the HTML content of the page in nicely formatted way using the prettify method

print(soup.prettify())


