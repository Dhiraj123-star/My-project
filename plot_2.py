# plotting using Python

import numpy as np

import matplotlib.pyplot as plt

import math

# setting the axes projection as polar

plt.axes(projection='polar')


# setting the length of axes of cardiod

a=4

# creating an array containing the radian values

rads = np.arange(0,(2*np.pi),0.01)

# plotting the cardiod

for rad in rads:
    r=a+(a*np.cos(rad))
    plt.polar(rad,r,'o')

# display the polar plot

plt.show()
