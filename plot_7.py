# importing the required libraries

import matplotlib.pyplot as plt
import numpy as np

# define data values

x=np.array([1,2,3,4,5]) # x-axis

y= np.array([10,20,30,40,50])  # y-axis

# plot the chart

plt.bar(x,y)

# adding grid lines

plt.grid(color='#999b84',linestyle="-.",
axis='y',alpha=0.5)

# display

plt.show()