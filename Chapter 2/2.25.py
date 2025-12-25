import turtle as t 

xc, yc = eval(input("Enter coordinates of the centre point:"))
length = eval(input("Enter length of rectangle:"))
width = eval(input("Enter width of rectangle:"))

halfLength = length / 2
halfWidth = width / 2

t.penup()
t.goto(xc,yc)
t.forward(halfLength)
t.pendown()
t.left(90)
t.forward(halfWidth)
t.left(90)
t.forward(length)
t.left(90)
t.forward(width)
t.left(90)
t.forward(length)
t.left(90)
t.forward(halfWidth)

t.done()

