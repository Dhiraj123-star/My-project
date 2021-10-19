# save all the links using python code

import requests as rq
from bs4 import BeautifulSoup

url= input("Enter link: ")
if ('https' or "http") in url:
    data= rq.get(url)
else:
    data= rq.get("https://"+url)
soup= BeautifulSoup(data.text,"html.parser")

links=[]

for link in soup.find_all("a"):
    links.append(link.get("href"))

# writing the output to a file (mylinks.txt)
# you can change 'a' to 'w' to overwrite the file each time

with open("mylinks.txt",'a') as saved:
    print(links[:10],file=saved)

