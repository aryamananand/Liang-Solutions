import turtle as t

t.right(90)
t.begin_fill()
t.color("red")
t.circle(100, steps = 6)
t.end_fill()
t.penup()
t.goto(40,-30)
t.left(90)
t.color("white")
t.write("STOP",
        font = ("Times", 50, "bold"))
t.hideturtle()

t.done()

