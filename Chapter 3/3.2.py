import math as m

xrad1, yrad1 = eval(input("Enter point 1 (lat and long) in deg: "))
xrad2, yrad2 = eval(input("Enter point 2 (lat and long) in deg: "))

x1 = m.radians(xrad1)
y1 = m.radians(yrad1)

x2 = m.radians(xrad2)
y2 = m.radians(yrad2)

#Implement formula

d = 6371.01 * m.acos(m.sin(x1) * m.sin(x2) + m.cos(x1) * m.cos(x2) * m.cos(y1 - y2))

print("The distance between the two points is", d, "km")

