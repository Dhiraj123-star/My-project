# csv to excel file convertor using python

import pandas as pd

import numpy as np

# reading the csv file
df_new = pd.read_csv("file.csv")

# saving xlsx file

myfile = pd.ExcelWriter("Myfile.xlsx")

df_new.to_excel(myfile,index=False)

myfile.save()

print("File is converted successfully !!")