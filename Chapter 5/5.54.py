import turtle as t

t.speed(10)

t.penup()
#x - axis
t.goto(-200,0)
t.pendown()
t.goto(200,0)
#right arrow
t.left(135)
t.forward(12)
t.right(180)
t.forward(12)
t.right(90)
t.forward(12)
t.left(135)
t.penup()
t.goto(0,0)
t.penup()
#y -axis
t.goto(0,-100)
t.right(90)


#bottom arrow
t.pendown()
t.left(135)
t.forward(12)
t.right(180)
t.forward(12)
t.right(90)
t.forward(12)
t.right(45)
t.goto(0,-100)

#y - axis line

t.forward(300)
t.right(90)
t.penup()
t.goto(-200,0)
t.left(180)
t.pendown()
#left arrow
t.right(135)
t.forward(12)
t.left(180)
t.forward(12)
t.left(90)
t.forward(12)

#top arrow
t.left(45)
t.penup()
t.goto(0,200)
t.left(90)
t.pendown()
t.right(135)
t.forward(12)
t.left(180)
t.forward(12)
t.left(90)
t.forward(12)
t.penup()
t.goto(-60,180)

t.pendown()

for x in range (-60,60):
    t.goto(x, (1/20) * (x ** 2))
       



