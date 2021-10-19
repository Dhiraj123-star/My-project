# collection modules 

from collections import ChainMap

d1={'a':1}
d2= {'b':2}
d3 = {'c':3}
d4 = {'d':4}
d5 ={'e':5}

c=ChainMap(d1,d2,d3,d4,d5)

print(c)