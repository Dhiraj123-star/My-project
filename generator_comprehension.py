# generator comprehension using Python

sequence_list = ["Python","Java","C",1200,130.5,True]

# create generator

generator = (x for x in sequence_list)

for s in generator:
    print(s,end=" ")


print("\nThanks for using Python!!")