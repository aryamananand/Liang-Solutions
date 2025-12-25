#   (Display a pyramid) Write a program that prompts the user to enter
#    an integer from 1 to 15 and displays a pyramid


inputLINES = eval(input("Enter the number of lines: "))

    

k = inputLINES * 4

for firDig in range(1,inputLINES + 1, 1):

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

'''
#FINAL CODE ----->

k = inputLINES * 4  
firDig = 1
while firDig <= inputLINES:
    
    
    count = firDig #Descending numbers before 1

    #print intial space before each line
    if firDig < 10:
        k -= 3
    else:
        k -=4
    
    space = " " * k
    print(space, end = '')
    
    while count > 1:
        
        print(count, " ", end = '')
        count -= 1

    count = 1 #Ascending numbers after 1
    while count <= firDig:
        print(count, " ", end = '')
        count += 1
    print()
        
    firDig += 1
    
#AFTER 10
'''
'''
secDig = 10
while secDig <= inputLINES:
    
    
    count = secDig #Descending numbers before 1

    #print intial space before each line
    k = k - 4

    space = " " * k
    print(space, end = '')
    
    while count > 1:
        
        print(count, " ", end = '')
        count -= 1

    count = 1 #Ascending numbers after 1
    while count <= secDig:
        print(count, " ", end = '')
        count += 1
    print()
        
    secDig += 1
'''
    
