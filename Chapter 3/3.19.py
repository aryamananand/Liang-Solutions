import turtle as t

x1,y1,x2,y2 = eval(input("Enter two points, (x1, y1, x2, y2): "))

t.penup()
t.goto(x1,y1)
t.pendown()
t.goto(x2,y2)
t.penup()
t.goto(x1,y1)
t.pendown()
t.write("(" + str(x1) + ", " + str(y1) + ")", font = ("Times", 15, "bold"))
t.penup()
t.goto(x2,y2)
t.pendown()
t.write("(" + str(x2) + ", " + str(y2) + ")", font = ("Times", 15, "bold"))

t.done()
