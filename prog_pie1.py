import matplotlib.pyplot as plt
#plot area
stream=('medical','non-medical','comm with maths','comm with ip','humanities')
no_students=[32,41,55,60,50]
colors=['red','gold','yellowgreen','blue','lightcoral']
#explode 1st slices
explode=(0.1,0,0,0,0)
#plot
plt.pie(no_students,explode=explode,labels=stream,colors=colors)
plt.title("grouping of students on the basis of allocated streams")
plt.show()
