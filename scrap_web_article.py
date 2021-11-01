# scrapping web article using Python

import newspaper

# assign url

url = "https://copyassignment.com/15-common-coding-mistakes-by-beginners/"

# extract web data

url_i = newspaper.Article(url="%s"%(url),langauge='en')
url_i.download()
url_i.parse()

# display scrapped data

print(url_i.text)