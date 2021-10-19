import matplotlib.pyplot as plt

#data to plot
labels='python','c++','ruby','java'
sizes=[215,130,245,210]
colors=['gold','yellowgreen','lightcoral','lightskyblue']
explode=[0.1,0,0,0]

#plot
plt.pie(sizes,explode=explode,labels=labels,colors=colors,shadow='True',startangle=140)
plt.axis('equal')
plt.show()
