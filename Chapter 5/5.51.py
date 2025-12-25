import turtle as t
t.speed(0)
scale = 2



for i in range (19):
    t.goto((i * scale * 5), 0)
    t.left(90)
    t.forward(90 * scale)
    t.right(180)
    t.forward(90 * scale)
    t.left(90)



for j in range (19):
    t.goto(0, (j * scale * 5))
    t.forward(90 * scale)
    t.left(180)
    t.forward(90 * scale)
    t.right(180)

t.hideturtle()
