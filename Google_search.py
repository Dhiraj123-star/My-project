# google search using python

from googlesearch import search

query = 'best course for Python'  # write your query

for i in search(query,tld="co.in",num=10,stop=18,pause=2):
    print(i)


