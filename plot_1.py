# plotting using Python

import numpy as np

import matplotlib.pyplot as plt

# setting the axes projection as polar

plt.axes(projection='polar')

# setting the radius

r=2

# creating an array containing the radian values

rads= np.arange(0,(2*np.pi),0.01) 

# plotting  the circle

for rad in rads:
    plt.plot(rad,r,'r.')

# display the polar plot
plt.show()