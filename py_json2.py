import json

# a python object {dict}

x= {
    "name": "Dhiraj",
    "age":22,
    "hobby":"Coding",
    "address":"Bhiwadi"
}

# convert into json :

y= json.dumps(x)

print(y) # the result is a json string