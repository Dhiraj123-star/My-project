import pandas as pd

df1= pd.DataFrame({"HPI":[100,200,300,400],"Int_rate":[2,1,2,4], "Ind_GDP":[50,100,300,400]},index=[2001,2002,2003,2004])
df2= pd.DataFrame({"HPI":[100,200,300,400],"Int_rate":[2,1,2,4], "Ind_GDP":[50,100,300,400]},index=[2005,2006,2007,2008])

merged = pd.merge(df1,df2)

print(merged) # merged two  different data frames