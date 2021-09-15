# normal data distribution
import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0,2.0,1000000) # deviate by 2.0 from mean 5.0 among the random numbers

plt.hist(x,100) # represent by 100 bars

plt.show()