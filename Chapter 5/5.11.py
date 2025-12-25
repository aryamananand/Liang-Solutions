NUMBER_OF_STUDENTS = eval(input("Enter number of students: "))
#minimum = eval(input("Enter minimum possible score on the test: "))
largest = 0    #minimum
second = 0

number = 1
while number <= NUMBER_OF_STUDENTS:
    
    score = eval(input("Enter score of student: "))
      
    if largest < score:
        largest = score
    if second < score < largest:
        second = score
        
    number += 1 


print("The highest score is: ", largest)
print("The second highest score is: ", second)
