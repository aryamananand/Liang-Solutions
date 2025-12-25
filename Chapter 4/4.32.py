#   Write a program that prompts the user
#   to enter the x- and y-coordinates for
#   the three points p0, p1, and p2 and displays whether
#   p2 is on the line segment from p0 to p1. 



x1,y1, x2,y2, x3,y3 = eval(input("Enter coordinates for the three points p0, p1 and p2: "))


position = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

print(position)

if (((position == 0) and ((x2 - x1) >= 0) and (x3 >= x1) and (x3 <= x2) \
    and ((y2 - y1) >= 0) and (y3 >= y1) and (y3 <= y2)) or ((position == 0) and ((x2 - x1) <= 0) and (x3 >= x2) \
    and (x3 <= x1) and ((y2 - y1) <= 0) and (y3 >= y2) and (y3 <= y1))):

    print("(", x3, ", ", y3, ")", "is on the line segment from (", x1, ", ", y1, ") to (", x2, ", ", y2, ")")

else:
    print("(", x3, ", ", y3, ")", "is not on the line segment from (", x1, ", ", y1, ") to (", x2, ", ", y2, ")")


user = eval(input("Draw the line and the point? Yes (1), No (0)."))


if user == 1:
    
    import turtle as t

    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.dot(5)
    t.goto(x2,y2)
    t.dot(5)
    t.penup()
    t.goto(x3,y3)
    t.dot(7)

    t.done()
    
else:
    print("Program over.")

    
