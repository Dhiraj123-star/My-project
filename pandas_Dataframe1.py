# convert Pandas Dataframe to json

import pandas as pd

# create Dataframe of players

df = pd.DataFrame({
    'Name':['Ankit','Anjali','Ansh'],
    'Hobby':['Programmig','Coding','Web Development'],
    'Class':["B.Tech","BCA","BSC(Computer Science)"]

})
# save dataframe to json file

df.to_json('myinfo.json')

print("Dataframe to json conversion successfully!!")