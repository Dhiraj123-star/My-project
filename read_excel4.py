# read excel data into dictionary, csv and json
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df=pd.read_excel("my.xlsx",sheet_name="Sheet1")

# print into the form of dictionary

print("Excel to dictionary :",df.to_dict(orient="records"))

print() # for new line
# print into the form of json

print("Excel to Json :",df.to_json(orient="records"))

print() # for new line


# print into the form of csv

print("Excel to csv :",df.to_csv(index=False))