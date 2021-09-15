import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,3*np.pi,0.1)

y=np.tan(x)   # finds the tan value


plt.plot(x,y)

plt.show()