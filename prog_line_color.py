#multiple lines with multiple colors given explicitly

import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'y')
plt.plot(y+1,'m')
plt.plot(y+2,'c')
plt.show()
