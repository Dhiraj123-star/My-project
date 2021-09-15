import pandas as pd

data = {
    "calories":[200,450,600,400],
    "duration":[20,45,60,40]
}

# we can specify own index names

df= pd.DataFrame(data, index=["day1","day2","day3","day4"])


print(df)

print() # for new line

# refer to the named index

print(df.loc["day2"])