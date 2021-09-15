
import pandas as pd

mydataset= {
    "cars":["BMW","volvo","ford"],
    "passings":[10,45,67]
}

# convert into the dataframe

myvar = pd.DataFrame(mydataset)

print(myvar)