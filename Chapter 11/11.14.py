# A program that prompts the user to enter the length of a square
# matrix, randomly fills in 0s and 1s into the matrix, prints the matrix, and
# finds the rows, columns, and major diagonal with all 0s or all 1s.

import sys
import random


class ExploreMatrix:

    # Generate the matrix
    def generateSquareMatrix(n):
        squareMatrix = []
        for i in range(n):
            squareMatrix.append([])
            for j in range(n):
                squareMatrix[i].append(random.randint(0,1))

        # Display the matrix

        for i in range(n):
            for j in range(n):
                print(squareMatrix[i][j], end = '')
            print()
        return squareMatrix  # Return the generated matrix

    # Analyse the Matrix
    def analyse(matrix):
        n = len(matrix)

        # Analyse for rows
        var1 = False
        for i in range(n):
            total = 0  # Initialize total for each row
            for j in range(n):
                total += matrix[i][j]
            if total == 0:
                print(f"All 0s on row {i}.")
                var1 = True
            elif total == n:
                print(f"All 1s on row {i}.")
                var1 = True
        if var1 == False:
                print("No same numbers in a row.")

        # Analyse columns
        var2 = False
        for i in range(n): 
            total = 0  # Initialize total for each column
            for j in range(n):
                total += matrix[j][i]
            if total == 0:
                print(f"All 0s on column {i}.")
                var2 = True
            elif total == n:
                print(f"All 1s on column {i}.")
                var2 = True
        if var2 == False:
            print("No same numbers in a column.")

        # Analyse the major diagonal
        total = 0  # Initialize total for the major diagonal
        for i in range(n):
            total += matrix[i][i]
        if total == 0:
            print(f"All 0s in the major diagonal.")
        elif total == n:
            print(f"All 1s in the major diagonal.")
        else:
            print("No same numbers in the major diagonal.")

ExploreMatrix()

# Run and Test
def main():
    matrixSize = eval(input("Enter the size for the matrix: "))
    matrix = ExploreMatrix.generateSquareMatrix(matrixSize)
    ExploreMatrix.analyse(matrix)

main()
