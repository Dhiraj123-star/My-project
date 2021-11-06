import json

x={
    "name":"John",
    "age":55,
    "married":True,
    "divorced":False,
    "Children":("Ann","Billy"),
    "Pets":None,
    "cars":[{"model":"BMW 322","mpg":33.8},
    {"model":"Ford Edge","mpg":13.8}
           
    ]
}

print(json.dumps(x))