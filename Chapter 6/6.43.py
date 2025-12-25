import turtle as t
import math
t.speed(10)

def drawGraph():
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

    t.forward(200)
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
    t.goto(0,100)
    t.left(90)
    t.pendown()
    t.right(135)
    t.forward(12)
    t.left(180)
    t.forward(12)
    t.left(90)
    t.forward(12)
    t.penup()


def drawSine(x1,x2):
    t.penup()
    t.goto(-175,50)
    t.pendown()
    t.color("red")
    for x in range(x1, x2):
        t.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
    

def drawCosine(x1,x2):
    t.penup()
    t.color("blue")
    t.goto(x1, 50 * math.cos((x1 / 100) * 2 * math.pi))
    t.pendown()
    for x in range (x1, x2):
        t.goto(x, 50 * math.cos((x / 100) * 2 * math.pi))

def writeInfo():
    t.color("black")
    t.penup()
    t.goto(102,-10)
    t.pendown()
    t.write("2 \u03c0")

    t.penup()
    t.goto(-99,-10)
    t.pendown()
    t.write("-2 \u03c0")
    t.penup()

    t.color("red")
    t.goto(-100,-150)
    t.left(90)
    t.pendown()
    t.write("f(x) = sin x")

    t.penup()
    t.color("blue")
    t.goto(-100, -160)
    t.pendown()
    t.write("f(x) = cos x")


def main():
    drawGraph()
    drawSine(-175,175)
    drawCosine(-175,175)
    writeInfo()
    t.hideturtle()
main()
