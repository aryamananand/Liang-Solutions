#Implements Cramers rule for solving two linear equations


a,b,c,d,e,f = eval(input("Enter a, b, c, d, e and f\n"
                         "for two linear equations in the form of\n"
                         "ax + by = e, and, cx + dy = f: "))

if (a * d - b * c) != 0:
    x = format((e * d - b * f) / (a * d - b * c), ".2f")
    y = format((a * f - e * c) / (a * d - b * c), ".2f")
    print("x is " +  str(x) + " and y is " + str(y))
    print("Note: Values may be approximations.")

else:
    print("The system has no solution")
    
