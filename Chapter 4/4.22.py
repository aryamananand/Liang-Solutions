x,y = eval(input("Enter the coordinates of a point: "))

distance = (x ** 2 + y ** 2) ** 0.5

if distance <= 10:
    print("The point (", x, ",", y, ") is inside the circle of radius 10.")
else:
    print("The point (", x, ",", y, ") is outside the circle of radius 10.")
    
