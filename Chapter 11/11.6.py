matrix_input = input('Enter matrix 1:').split(' ')
#print(matrix_input)
matrix1 = []
for i in range(3):
    matrix1.append([])
    r = i*3
    for j in range(3):
        matrix1[i].append(matrix_input[j+r])
        
#print(matrix1)

matrix_input2 = input('Enter matrix 2:').split(' ')
#print(matrix_input2)
matrix2 = []
for i in range(3):
    matrix2.append([])
    r = i*3
    for j in range(3):
        matrix2[i].append(matrix_input2[j+r])
        
#print(matrix2)

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(float(matrix1[i][0])*float(matrix2[0][j]) + float(matrix1[i][1])*float(matrix2[1][j]) + float(matrix1[i][2])*float(matrix2[2][j]))

print()
print('product matrix is:')
print(matrix)

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end = '  ')
    print()
    
