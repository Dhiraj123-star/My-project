# imported the required libraries

import matplotlib.pyplot as plt

import numpy as np

# define data values

x1=np.array([1,2,5,8]) # x-axis
y1= np.array([10,8,17,13]) # y-axis

x2= np.array([3,4,7,9]) # x-axis
y2= np.array([12,8,18,14]) # y-axis

# plot the chart

plt.bar(x1,y1,label='bar1')
plt.bar(x2,y2,label='bar2')

# adding title and label of axis

plt.title('Bar Graph by Dhiraj')
plt.xlabel('Profit')
plt.ylabel('Sales')
plt.legend()

# display

plt.show()