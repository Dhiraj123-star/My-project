from scipy.optimize import root

from math import cos

def eqn(x):
    return x+cos(x)


myroot= root(eqn,0)

# find the root of the equation x+cos(x)

print(myroot.x)

# print all the information about the solution 

print(myroot)