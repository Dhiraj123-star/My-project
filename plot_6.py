# plotting with Python

# importing the required libraries

import matplotlib.pyplot as plt

import numpy as np

# generates array containing 60 integer b/w 0 to 100

x=np.random.randint(low=0,high=100,size=(60,))

# plot the chart

bins =[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(x,bins,ec='orange')


# adding title and label of axis

plt.title('Students Exam Results')
plt.xlabel('Marks Obtained')
plt.ylabel('No. of Students')

# display

plt.xticks(bins)
plt.show()


