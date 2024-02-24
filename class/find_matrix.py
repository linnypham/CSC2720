def findMatrix(array, target):
    top = 0
    bottom = len(matrix) - 1
    m = 0  # Define m outside the loop

    while top <= bottom:
        m = top + (bottom - top) // 2
        if target > matrix[m][-1]:
            top = m + 1
        elif target < matrix[m][0]:
            bottom = m - 1
        else:
            break

    left = 0
    right = len(matrix[0]) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if target == matrix[m][mid]:
            print(True)
            break
        elif target < matrix[m][mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        print(False)

matrix = [[3, 5, 10, 12],
          [13, 15, 20, 21],
          [22, 24, 26, 29],
          [30, 31, 35, 40]]
target = 26
findMatrix(matrix, target)
