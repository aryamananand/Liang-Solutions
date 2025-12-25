import math as m

radius = eval(input("Enter radius of the cylinder (in m):"))
length = eval(input("Enter length of the cylinder (in m):"))

area = radius * radius * (m.pi)
volume = area * length

print("The area of the base of the cylinder is:", area, "m^2")
print("The volume of the cylinder is:", volume, "m^2")

