# get wikipedia search results

import wikipedia

wikipedia.set_lang("en")

usrinp = input("Enter your query: ")

print(wikipedia.summary(usrinp)) # give summary about python