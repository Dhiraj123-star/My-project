''' the circle module has functions that performs
calculations related to circles-circle.py'''
import math
#area function accepts a circle's radius as an argument and returns the area of the circle
def area(radius):
    return math.pi*radius**2
#the circumference functions accepts a circle's radius and returns the circle's circumference
def circumference(radius):
    return 2*math.pi*radius
