def print_spiral(n):
    # Initialize variables
    matrix = [[0] * n for _ in range(n)]
    num = 1

    # Starting position
    row, col = n // 2, n // 2

    # Spiral filling loop
    for i in range(1, n + 1, 2):
        for _ in range(i):
            matrix[row][col] = num
            num += 1
            col += 1
        for _ in range(i):
            matrix[row][col] = num
            num += 1
            row -= 1
        for _ in range(i + 1):
            matrix[row][col] = num
            num += 1
            col -= 1
        for _ in range(i + 1):
            matrix[row][col] = num
            num += 1
            row += 1

    # Print the spiral matrix
    for r in range(n):
        for c in range(n):
            print(f'{matrix[r][c]:2}', end=' ')
        print()

# Set the size of the matrix (assuming it's an odd number)
matrix_size = 5
print_spiral(matrix_size)
