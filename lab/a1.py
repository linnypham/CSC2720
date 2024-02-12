def loop(array1,array2):
    if not array1 or not array2: #check if inputs are null
        return ('Null input case, so no output')
    m = len(array1)
    n = len(array2)
    array_loop = []
    for i in range(m):
        for j in range(n):
            if array1[i] == array2[j]: #if values are duplicate, append into an array, else go to the next value
                array_loop.append(array1[i])
    if not array_loop: #check if output is empty
        return 'There are no duplicates'
    else:
        return array_loop

def binary(array1,array2):
    if not array1 or not array2:
        return ('Null input case, so no output')
    m = len(array1)
    n = len(array2)
    array_binary = []
    for i in range(n):#going through array2
        l = 0
        r = len(array1) - 1
        while l <= r:#binary search array1
            m = l + (r-l)//2
            if array1[m] == array2[i]:
                array_binary.append(array1[m])#if found, appends the value and exit the loop to go the next value of array2
                break
            elif array1[m] > array2[i]:#move cursors in array1 depend on the value of array2
                r = m-1
            else:
                l = m+1
    if not array_binary:
        return 'There are no duplicates'
    else:
        return array_binary

def linear(array1,array2):
    if not array1 or not array2:
        return ('Null input case, so no output')
    m = len(array1)
    n = len(array2)
    array_linear = []
    c1 = 0
    c2 = 0
    while c1 < m and c2 < n:#set 2 cursors, comparing values from the 2 arrays
        if array1[c1] == array2[c2]:
            array_linear.append(array1[c1])#append the duplicates into an array
            c1 += 1
            c2 += 1
        elif array1[c1] < array2[c2]: #if a value of an array is lower, move its cursor up
            c1 += 1
        else:
            c2 += 1
    if not array_linear:
        return 'There are no duplicates'
    else:
        return array_linear

array1 = [1, 6, 9, 10, 11, 21]
array2 = [2, 6, 9, 11, 17, 21]
print(f'Loop: {loop(array1,array2)}')
print(f'Binary: {binary(array1,array2)}')
print(f'Linear: {linear(array1,array2)}')

'''print('Test1: Null input') #expected: print 'Null input case, so no output'
array1 = []
array2 = []
print(f'Loop: {loop(array1,array2)}')
print(f'Binary: {binary(array1,array2)}')
print(f'Linear: {linear(array1,array2)}')

print('Test2: length of 1') #expected: either a null output, or output with 1 integer
array1 = [11]               #solution: check if the output is null and print 'There are no duplicates'
array2 = [12]
print(f'Loop: {loop(array1,array2)}')
print(f'Binary: {binary(array1,array2)}')
print(f'Linear: {linear(array1,array2)}')

print('Test3: Not integers') #expexted: output  a string array instead of integer
array1 = ['a','b','d','f','g']
array2 = ['d','f','g','h','j']
print(f'Loop: {loop(array1,array2)}')
print(f'Binary: {binary(array1,array2)}')
print(f'Linear: {linear(array1,array2)}')

print('Test4: Unsorted inputs') #exptedted: wrong outputs
array1 = [4,3,5,2,1]            #solution: sort input arrays
array2 = [7,4,6,5,9]
print(f'Loop: {loop(array1,array2)}')
print(f'Binary: {binary(array1,array2)}')
print(f'Linear: {linear(array1,array2)}')
'''
