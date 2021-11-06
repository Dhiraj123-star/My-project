import matplotlib.pyplot as plt

import numpy as np

x=int(input("Enter your value of x: "))

plt.plot(x,np.sin(x),label='sin')
plt.plot(x,np.cos(x),label='cos')

plt.legend()
plt.show()