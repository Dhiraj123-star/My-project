# linear regression 
from scipy import stats
import matplotlib.pyplot as plt

# create the arrays that represents the value of x and y
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]

# execute the method that returns some important key values of linear regression

slope,intercept,r,p,std_err=stats.linregress(x,y)

"""create a function that uses the slope and intercept values to return 
 a new value represents where on the y-axis the corresponding  x values will
 be placed
"""
def myfun(x):
    return slope*x+intercept

""" run each value of the x array through the function. this will return in
a new array with new values for the y-axis """

mymodel=list(map(myfun,x))

# draw the original scatter plot
plt.scatter(x,y)

# draw the line of linear regression

plt.plot(x,mymodel)

# display the diagram
plt.show()


