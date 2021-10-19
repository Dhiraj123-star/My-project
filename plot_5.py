# importing the required libraries

import matplotlib.pyplot as plt

# dateset-1

x1= [89,43,36,36,95,10,66,34,38,20]

y1= [21,46,3,35,67,95,53,72,58,10]

# dataset-2

x2=[26,29,48,64,6,5,36,66,72,40]

y2=[26,34,90,33,38,20,56,2,47,15]

# plot the chart

plt.scatter(x1,y1,c='pink',linewidths=2,
marker="s",edgecolors='green',s=40)

plt.scatter(x2,y2,c='yellow',linewidths=2,
marker="^",edgecolors='red',s=60)

# adding title and label of axis

plt.title('Scatter Plot by Dhiraj')
plt.xlabel('Grades Range')
plt.ylabel('Grades Scored')

# to show the plot

plt.show()

