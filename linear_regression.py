# linear regression 
from scipy import stats

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
# predict the speed of 10 years old car 
speed=myfun(10)
print(speed) # returns 85.59 