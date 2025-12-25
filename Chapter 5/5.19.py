#   (Display a pyramid) Write a program that prompts the user to enter
#    an integer and displays a pyramid


inputLINES = eval(input("Enter the number of lines: "))

if inputLINES >= 9:
    k = inputLINES * 4 - 9
if inputLINES < 9:
    k = inputLINES * 3
    


for firDig in range(1,inputLINES + 1):

    #print intial space before each line
    if firDig < 10:
        k -= 3
    elif firDig <= inputLINES:
        k -= 4
    
    space = " " * k
    print(space, end = '')
    
    count = firDig #Descending numbers before 1
    
    for count in range (firDig, 1, -1): 
        
        print(count, " ", end = '')
        

    #Ascending numbers after 1
    for count in range(1,firDig+1, 1):
        print(count, " ", end = '')

    print()
