import pandas as pd

df1 = pd.DataFrame({"Int_Rate":[2,1,2,4],"Int_GDP":[50,70,80,90]},index=[2001,2002,2003,2004])

df2 = pd.DataFrame({"Lower_Tier_HPI":[50,70,80,9],"Unemployement":[1,3,5,6]},index=[2001,2003,2003,2004])

joined = df1.join(df2) # join df1 with df2

print(joined)
