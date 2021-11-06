import json

# some Json:

x='{"name": "Dhiraj","age":30, "City":"Bhiwadi"}'

# parse x:

y=json.loads(x)

# the result is a python dictionary

print(y["age"])

print(y["name"])

print(y["City"])

print(y)