# histogram for big data
import numpy
import matplotlib.pyplot as plt

x=numpy.random.uniform(0.0,100.0,100000000) # big data 

plt.hist(x,100)  # display random numbers into 100 bars
plt.show()