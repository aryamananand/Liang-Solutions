'''

(Turtle: two circles) Write a program that prompts
the user to enter the center coordinates and radii of
two circles and determines whether the second circle is
inside the first or overlaps with the first

'''

import math

x1, y1, r1 = eval(input("Enter circle1's centre's coordinates and radius: "))
x2, y2, r2 = eval(input("Enter circle2's centre's coordinates and radius: "))

centreDistance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if centreDistance <= math.fabs(r1 - r2) and r1 > r2:
    print("circle2 is inside circle1.")
elif centreDistance <= math.fabs(r1 - r2) and r1 < r2:
    print("circle 2 engulfs circle1")
elif centreDistance <= (r1 + r2) and r1 > r2:
    print("circle2 overlaps circle1.")
elif centreDistance <= (r1 + r2) and r1 < r2:
    print("circle2 overlaps circle2.")
elif ((x1 == x2) and (y1 == y2) and (r1 == r2)):
    print("The circles are the same.")
else:
    print("circle2 does not overlap circle1")

user = eval(input("Draw the circles? Yes (1), No (0)."))

if user == 1:
    import turtle as t

    t.penup()
    t.goto(x1,y1)
    t.right(90)
    t.forward(r1)
    t.pendown()
    t.left(90)
    t.circle(r1)
    t.write("Circle1", align = "center", font = ("Times", 20, "italic"))

    t.penup()
    t.goto(x2,y2)
    t.right(90)
    t.forward(r2)
    t.left(90)
    t.pendown()
    t.circle(r2)
    t.write("Circle2", align = "center", font = ("Times", 20, "italic"))

    t.goto(x,y)
elif user == 0:
    print("Program over.")
else:
    print("No selection.")
