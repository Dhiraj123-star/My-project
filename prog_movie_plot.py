#program to plot a bar chart showing the choice showing the choice of
#favorite movie among the people


import numpy as np
import matplotlib.pyplot as plt
objects=('comedy','action','romance','drama','scifi')
y_pos=np.arange(len(objects))
types=(4,5,6,1,4)
plt.bar(y_pos,types,align='center',color='blue')
plt.xticks(y_pos,objects)
plt.ylabel('people')
plt.title('favorite type of movie')
plt.show()
