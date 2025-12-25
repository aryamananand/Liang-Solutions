import turtle as t
import random

t.speed(0)

def drawCircle(x,y,radius):
    t.penup()
    t.goto(x,y-radius)
    t.pendown()
    t.circle(radius)

def drawRectangle(x, y, width, height):
    t.penup()
    t.goto(x + width/2, y + height/2)
    t.pendown()
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)

def randomRectanglePoints(n):
    
    for i in range (n):
        t.penup()
        x_ = -125
        y_ = -50
        x = random.random()
        y = random.random()

        x *= 100
        y *= 100

        x = x + x_
        y = y + y_

        t.goto(x,y)
        t.pendown()
        t.dot(3, "red")
        t.penup()
def randomCirclePoints(n, radius):

    count = 0
    while count < n:
        t.penup()
        a = random.randint(-1,1)
        if a == 0:
            continue
        x = random.random() 
        y = random.random()
        x *= 100 
        y *= 100 * a
        
        if (x - radius)** 2 + y ** 2 < radius ** 2:
            t.goto(x, y)
            t.pendown()
            t.dot(3, "red")
            count += 1
 
def main():
    drawRectangle(-75, 0, 100, 100)
    randomRectanglePoints(10)
    drawCircle (50,0, 50)
    randomCirclePoints(1000, 50)

main()




        
