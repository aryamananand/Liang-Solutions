# Find the greatest value in a 2D list of integers. 

import sys
import random
class GetLargestValueIn2DList:
    def __init__(self):
        mtr = self.getMatrix()  #Generate the list
        print(self.getLargestValue(mtr))    #Find largest vaue

    # Input the list 
    def getMatrix(self):
        matrix = []
        numRows = random.randint(1,5)
        # if numRows != int:
        #     print("Invalid row count.")
        #     sys.exit
        for row in range(numRows):
            matrix.append([])
            lst = input("Enter a row: ").split(' ')
            for x in lst:
                matrix[row].append(int(x))  # Convert input to integers
        return matrix
    
    # Find the largest value
    def getLargestValue(self,lst):
        largest = max(lst[0])  
        for i in range(len(lst)):
            if largest <= max(lst[i]):  
                largest = max(lst[i]) 
            print("max in ", i, " is ", max(lst[i])) 

        return largest  

c1 = GetLargestValueIn2DList()

