#(Geography: estimate areas) Find the GPS locations for Atlanta, Georgia; Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina
#from www.gps-data-team.com/map/ and compute the estimated area enclosed by these four cities.
#(Hint: Use the formula in Programming Exercise 3.2 to compute the distance between two cities.
#Divide the polygon into two triangles and use the for- mula in Programming
#Exercise 2.14 to compute the area of a triangle.)


import math as m


xD1 = 28.6100   #DELHI (N)
yD1 = 77.2300

xM1 = 19.0761   #MUMBAI (W)
yM1 = 72.8775

xB1 = 12.9789   #BANGALORE (S)
yB1 = 77.5917

xK1 = 22.5675   #KOLKATA (E)
yK1 = 88.3700 

xD = m.radians(xD1)
yD = m.radians(yD1)

xM = m.radians(xM1)
yM = m.radians(yM1)

xB = m.radians(xB1)
yB = m.radians(yB1)

xK = m.radians(xK1)
yK = m.radians(yK1)


#Implement formula
#for Delhi -> Mumbai

d1 = 6371.01 * m.acos(m.sin(xD) * m.sin(xM) + m.cos(xD) * m.cos(xM) * m.cos(yD - yM))

print("The distance between Delhi and Mumbai is", d1, "km")

#Mumbai -> Bangalore
d2 = 6371.01 * m.acos(m.sin(xM) * m.sin(xB) + m.cos(xM) * m.cos(xB) * m.cos(yM - yB))

print("The distance between Mumbai and Bangalore is", d2, "km")

#Bangalore -> Kolkata

d3 = 6371.01 * m.acos(m.sin(xB) * m.sin(xK) + m.cos(xB) * m.cos(xK) * m.cos(yB - yK))

print("The distance between Bangalore and Kolkata is", d3, "km")

#Kolkata -> Delhi

d4 = 6371.01 * m.acos(m.sin(xK) * m.sin(xD) + m.cos(xK) * m.cos(xD) * m.cos(yK - yD))

print("The distance between Kolkata and Delhi is", d4, "km")

#Delhi -> Bangalore

d5 = 6371.01 * m.acos(m.sin(xD) * m.sin(xB) + m.cos(xD) * m.cos(xB) * m.cos(yB - yB))

print("The distance between Delhi and Bangalore is", d5, "km")


#TRIANGLE 1: M --> D --> B

s = (d1 + d2 + d5) / 2

area = (s * (s - d1) * (s - d2) * (s - d5)) ** 0.5

print("The area of the triangle 1 is:", area, "sq.km")


#TRIANGLE 2: D --> K --> B

s_ = (d3 + d4 + d5) / 2
area_ = (s_ * (s_ - d3) * (s_ - d4) * (s_ - d5)) ** 0.5

print("The area of the triangle 2 is:",  area_, "sq.km")


AREA = area + area_
print("The area enclosed by Delhi, Mumbai, Bangalore and Kolkata is", format(AREA, ".2f"), "sq.km")








