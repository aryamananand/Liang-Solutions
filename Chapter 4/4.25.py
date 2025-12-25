x1,y1, x2,y2, x3,y3, x4,y4 = eval(input("Enter x1,y1, x2,y2, x3,y3, x4,y4: "))

# (y1 - y2) * x - (x1 - x2) * y = (y1 - y2) * x1 - (x1 - x2) * y1
# (y3 -y4) * x - (x3 -x4) * y = (y3 -y4) * x3 - (x3 -x4) * y3

a = y1 - y2
b = - (x1 - x2)
e = (y1 - y2) * x1 - (x1 - x2) * y1
c = y3 - y4
d = - (x3 - x4)
f = (y3 -y4) * x3 - (x3 - x4) * y3

if (a * d - b * c) != 0:
    
    x = format((e * d - b * f) / (a * d - b * c), ".2f")
    y = format((a * f - e * c) / (a * d - b * c), ".2f")
    print("The intersecting point is: (", x, ",", y, ")")

else:
    print("The two lines are parallel.")
