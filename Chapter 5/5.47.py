import turtle as t
import random

ballCount = 10

t.speed(0)
t.goto(120,0)
t.goto(120,100)
t.goto(0,100)
t.goto(0,0)
t.penup()


for i in range (ballCount):
        
    x_ = random.random()
    y_ = random.random()

    x = x_ * 120
    y = y_ * 100

    
    t.goto(x,y)
    t.pendown()
    t.dot(3,"red") 
    t.penup()

t.hideturtle()
t.done()
