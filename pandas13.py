import pandas as pd

a=[100,300,400,500,560]


# with the index argument, we can give own name with own labels

myvar = pd.Series(a,index=["Python",'Java','JavaScript',"Scala","TypeScript"])

print(myvar)

