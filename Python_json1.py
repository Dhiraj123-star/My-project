import json

# key:value mapping

student ={
    "Name":"Dhiraj",
    "Rollno":"918106",
    "Grade":"A",
    "Age":"23",
    "Subject":["Computer Graphics","Data structures","Mathematics"]


}

with open("data.json","w") as write_file:
    json.dump(student,write_file)


print("File dumped successfully!!")