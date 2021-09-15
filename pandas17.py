import pandas as pd

data = {
    "programming_lang":["Python","java","C","C++","javascript"],
    "rank":[1,2,3,4,5]
}

df= pd.DataFrame(data)

print(df)