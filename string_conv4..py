# python program for converting list into the string using join()

s=['we','are','using', 4, 'laptops','and',3,'keyboards']

#using map() method

list_to_str = ' '.join(map(str,s))

print(list_to_str)
