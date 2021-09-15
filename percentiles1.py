# find percentiles in python
import numpy
marks=[76,56,59,87,90,34,49,48,75,62]

# calculate the percentiles of 55 in the marks
x=numpy.percentile(marks,55)
print(x) #returns 61.85 means 61.85 marks did better by
# 55 percentile among others