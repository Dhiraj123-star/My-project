import numpy
import matplotlib.pyplot as plt

# the first array will have the mean set to 5.0 with a standard deviation of 2.0
x=numpy.random.normal(5.0,2.0,1000)

# the second array will have the mean set to 10.0 with standard devaition of 2.0
y=numpy.random.normal(10.0,2.0,1000)

plt.scatter(x,y)
plt.show()

