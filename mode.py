# find the mode of the number
from scipy import stats
speed = [12,34,56,12,67,5,12]
x=stats.mode(speed)

print("The mode is :",x)