from  turtle import *

bgcolor("black")

speed(11)

hideturtle()

for i in range(120):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    right(3)
    forward(3)

done()