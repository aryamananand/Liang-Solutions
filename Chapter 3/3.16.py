import turtle as t

t.speed(8)
t.penup()
t.goto(-110,120)
t.color("black")
t.pendown()
t.write("Cool Colourful Shapes", font = ("Times", 30, "bold"))




#TRIANGLE - VIOLET
t.penup()
t.goto(-300,0)
t.right(60)
t.pendown()
t.color("violet")
t.begin_fill()
t.circle(50, steps = 3)
t.end_fill()

t.penup()

#SQUARE - INDIGO
t.goto(-150,0)
t.left(15)
t.pendown()
t.color("indigo")
t.begin_fill()
t.circle(50, steps = 4)
t.end_fill()

#PENTAGON - BLUE
t.penup()
t.goto(0,0)
t.pendown()
t.left(9)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(50, steps = 5)
t.end_fill()

#HEXAGON - GREEN

t.penup()
t.goto(150,0)
t.pendown()
t.left(6)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(50, steps = 6)
t.end_fill()

#OCTAGON - RED

t.penup()
t.goto(300,0)
t.pendown()
t.left(9.5)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(50, steps = 8)
t.end_fill()
t.hideturtle()
