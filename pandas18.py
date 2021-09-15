import pandas as pd

data = {
    "programming_lang":["Python","java","C","C++","javascript"],
    "rank":[1,2,3,4,5]
}

# pandas use loc attribute to return one or more specified row(s)

df = pd.DataFrame(data)

print(df.loc[1])

print() # for new line

# use of list of indexes

print(df.loc[[1,2]])