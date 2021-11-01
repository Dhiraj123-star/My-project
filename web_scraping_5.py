# web scraping using one and only Python :)

from bs4 import BeautifulSoup

import requests

url = "https://www.javatpoint.com/"

# make a GET request to fetch the raw HTML content

html_content = requests.get(url).text

# parse the html content

soup = BeautifulSoup(html_content,'html5lib')

print(soup.prettify()) # print the parsed data of html

print("Title :",soup.title.text)

for link in soup.find_all('a'):
    print("Inner Text is: {}".format(link.text))
    print("Title is:{}".format(link.get('title')))
    print("href is: {}".format(link.get('href')))
    