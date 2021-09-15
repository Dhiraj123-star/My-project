# histogram  example

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0,50.0,250)
plt.hist(x,50)
plt.show()
