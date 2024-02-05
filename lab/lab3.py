def withAllocating(matrix):
    n = len(matrix)
    matrix1 = [[0]*3 for i in range(3)]

    #OLD ROW TO NEW COLUMN
    for i in range(n):
        for j in range(n):
            matrix1[j][n - 1 - i] = matrix[i][j]

    #OLD TO NEW
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix1[i][j]

def withoutAllocating(matrix):
    n = len(matrix)

    #TOP TO BOTTOM
    for i in range(n // 2):
        matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

    #SWAP SYMMETRY
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


matrix1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
withAllocating(matrix1)
print('1:')
for row in matrix1:
    print (row)
print('')

matrix2 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
withoutAllocating(matrix2)
print('2:')
for row in matrix2:
    print (row)