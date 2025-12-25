import turtle as t
import math 

x1, y1, x2, y2, x3, y3 = eval(input ("Enter three points: "))


a = math.sqrt((x2-x3) * (x2-x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1-x3) * (x1-x3) + (y1 - y3) * (y1 - y3))
d = math.sqrt((x1-x2) * (x1-x2) + (y1 - y2) * (y1 - y2))


A = math.degrees(math.acos((a * a - b * b - d * d) / (-2 * b * d)))
B = math.degrees(math.acos((b * b - a * a - d * d) / (-2 * a * d)))
C = math.degrees(math.acos((d * d - b * b - a * a) / (-2 * a * b)))

#print("The three angles are ", round((A * 100) / 100.0), round((B * 100) / 100.0), round((C * 100) / 100.0))

#Integer Values
'''a1 = round((A * 100) / 100)
a2 = round((B * 100) / 100)
a3 = round((C * 100) / 100)'''

#2 digits after decimal
a_1 = format(A, ".2f")
a_2 = format(B, ".2f")
a_3 = format(C, ".2f")

t.penup()
t.goto(x1,y1)
t.color("black")
t.pendown()
t.goto(x2,y2)
t.goto(x3,y3)
t.goto(x1,y1)
t.penup()
t.goto(x1,y1)
t.pendown()
t.color("blue")
t.write("p1 ( " + str(a_1) + ")", font = ("Times", 15, "bold"))
t.penup()
t.goto(x2,y2)
t.pendown()
t.write("p2 (" + str(a_2) + ")", font = ("Times", 15, "bold"))
t.penup()
t.goto(x3,y3)
t.pendown()
t.write("p3 ( " + str(a_3) + ")", font = ("Times", 15, "bold"))

t.done()
