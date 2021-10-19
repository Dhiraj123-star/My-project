
# collection module using Python

from collections import namedtuple

stud_details = namedtuple('stud_details',["Name","Language","hobby"])
p = stud_details('Dhiraj','Python','Programming')

print(p)

print(p.Name)
print(p.hobby)
print(p.Language)
