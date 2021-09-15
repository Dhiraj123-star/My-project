import json

a=(10,20,30,40,50,60,70,80)

print(type(a))

b=json.dumps(a)

print(type(json.loads(b)))