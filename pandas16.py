import pandas as pd

# multi dimensional array

data= {

 "name":["Dhiraj","Yasweer","Ashish","Gajendra","Akash"],
 "marks":[430,345,234,400,346],
 "age":[22,24,34,21,20]
}

myvar = pd.DataFrame(data)

print(myvar)