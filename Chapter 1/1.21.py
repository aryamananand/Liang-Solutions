import turtle as t

#displaying the clock

t.penup()
t.goto(0,-100)
t.pendown()
t.circle(100)
t.penup()
t.goto(-95,-4)
t.pendown()
t.write("9")
t.penup()
t.goto(-3,85)
t.pendown()
t.write("12")
t.penup()
t.goto(90,-4)
t.pendown()
t.write("3")
t.penup()
t.goto(-3,-95)
t.pendown()
t.write("6")
t.penup()
t.goto(-17,-120)
t.pendown()
t.write("09:15:00")

#displaying the hands

t.penup()
t.goto(0,0)
t.left(172.5)
t.pendown()
t.forward(70)
t.penup()
t.goto(0,0)
t.pendown()
t.right(82.5)
t.forward(90)
t.penup()
t.goto(0,0)
t.right(90)
t.pendown()
t.forward(85)



t.done()



