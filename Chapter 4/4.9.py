weight1, price1 = eval(input("Enter weight and price of package 1: "))
weight2, price2 = eval(input("Enter weight and price of package 2: "))

ratio1 = weight1 / price1
ratio2 = weight2 / price2

if ratio1 > ratio2:
    print("Package 1 has the better price.")
elif ratio1 == ratio2:
    print("Package 1 and Package 2 have the same price. ")
else:
    print("Package 2 has the better price. ")
