import pandas as pd

df=pd.DataFrame({"Day":[1,2,3,4],"visitors":[200,300,400,500],"Bounce_rate":[20,45,56,33]})

df.set_index("Day",inplace=True)  # changing the index value

print(df)