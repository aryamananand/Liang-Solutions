#   Write a program that displays
#   a table (note that 1 kilogram is 2.2 pounds)


print("Kilogram       Pounds")
print()

kilogram = 1

for kilogram in range (1,200):
    pound = format(kilogram * 2.2, ".3f")
    print(kilogram, "            ", pound, "\n")
    kilogram += 1

          
