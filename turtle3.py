import turtle

# creating turtle

t=turtle.Turtle()

c=t.clone()

t.color("orange")

c.color("red")

t.circle(20)

t.circle(30)

for i in range(40,100,10):
    c.circle(i)

turtle.mainloop()