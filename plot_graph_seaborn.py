import matplotlib.pyplot as plt

import seaborn as sns

# x axis values

x= ['sun','mon','tues','wed','thurs','fri','sat']

# y axis values

y=[5,6,8,9,1,10,11]

ax=sns.stripplot(x=x,y=y)

# giving labels to x and y axis

ax.set(xlabel="Days",ylabel="Attendance")

plt.title("Attendance Graph")

plt.show()