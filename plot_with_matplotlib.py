# plot with matplotlib using Python

import matplotlib.pyplot as plt

labels = 'Windows','Mac Os','Unknown','Linux','Chrome OS'
 
percantage = [75.4,10.60,2,0.4,1.6]

patches, texts= plt.pie(percantage,labels=labels)

percantage_label = ["{}%".format(i) for i in percantage]

plt.legend(patches,percantage_label,loc='center left')

plt.show()