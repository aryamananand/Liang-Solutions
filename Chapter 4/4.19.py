#   (Compute the perimeter of a triangle) Write a program that reads three edges
#   for a triangle and computes the perimeter if the input is valid.
#   Otherwise, display that the input is invalid.
#   The input is valid if the sum of every pair
#   of two edges is greater than the remaining edge.



side1, side2, side3 = eval(input("Enter the length of the three sides: "))

if (((side1 + side2) > side3) and ((side2 + side3) > side1) and ((side1 + side3) > side2)):
    perimeter = side1 + side2 + side3
    print("The perimeter of the triangle is: ", perimeter)
elif (((side1 + side2) == side3) or ((side2 + side3) == side1) or ((side1 + side3) == side2)):
    print("The triangle is flat.")
else:
    print("The input is invalid")

