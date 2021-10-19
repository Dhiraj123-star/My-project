#program for plotting sine wave using line chart

import matplotlib.pyplot as plt
import numpy as np
xvals=np.arange(-2,1,0.01) #grid of 0.01 spacing from -2 to 1
yvals=np.sin(xvals) #evaluate function on xvals
plt.plot(xvals,yvals) #create line plot with yvals against xvals
plt.show() #show the figure
