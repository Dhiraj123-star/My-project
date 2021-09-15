import numpy as np

x=np.array([(12,34,45),(90,100,120),(123,789,456)])

y=np.array([(100,300,500),(1000,890,900),(1200,780,899)])

print(np.vstack((x,y))) # vertical stacking

print() # for new line


print(np.hstack((x,y))) # horizontal stacking

