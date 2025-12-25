import math

a, b, c = eval(input("Enter a, b anc c values (separated by commas) for a quadratic equation in the form of ax^2 + bx + c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    r1 = (- b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    r2 = (- b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("The roots are", r1, "and", r2)
elif discriminant == 0:
    r1 = (- b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("The root is: ", r1)
else:
    print("This quadratic equation has no real roots. ")

