import os.path
import random 

filename = input("Enter a file name: ")
if os.path.isfile(filename):
    print("The file already exists.")
else:
    main_file = open(filename, "w")
    for r in range(100):
        integer = random.randint(0,1000)
        main_file.write(str(integer))
        main_file.write(" ")

    main_file.close()

    file = open(filename, "r")
    numString = file.read()
    numList = numString.split()

    for x in numList:
        x = int(x)
    numList.sort()
    print(numList)
