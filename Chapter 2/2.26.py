import turtle as t
import math as m

xc, yc = eval(input("Enter coordinates of the centre point:"))
radius = eval(input("Enter radius of the circle:"))

area = radius * radius * m.pi

'''#draw the x axis and y axis
t.forward(300)
t.left(180)
t.forward(600)
t.goto(0,0)
t.left(90)
t.forward(300)
t.right(180)
t.forward(600)
t.left(180)
t.forward(300)
t.left(90)'''

#draw the circle
t.penup()
t.goto(xc,yc)
t.right(90)
t.forward(radius)
t.left(90)
t.pendown()
t.circle(radius)
t.penup()
t.goto(xc,yc)
t.pendown()
t.write(round(area,2))

t.done()
