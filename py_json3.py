# convert python objects into json strings and print the values

import json

# the python dictionary

print(json.dumps({"name":"Python","rank":1}))

# python tuple

print(json.dumps(("Python","Java","Dart")))

# python list

print(json.dumps(["JavaScript","TypeScript","C#"]))

# python string 

print(json.dumps(("Python is popular programming language")))

# python int

print(json.dumps(2321))

# python float

print(json.dumps(89.56))

#python boolean

print(json.dumps(True))

#python boolean

print(json.dumps(False))

# python special operator None

print(json.dumps(None))