array1 = [1, 6, 9, 10, 11, 21]
m = len(array1)

array2 = [2, 6, 9, 11, 17, 21]
n = len(array2)


array_loop = []
array_binary = []
array_linear = []  

for i in range(m):
    for j in range(n):
        if array1[i] == array2[j]: #if values are duplicate, append into an array, else go to the next value
            array_loop.append(array1[i])
print(f'Loop: {array_loop}')


for i in range(n):#going through array2
    l = 0
    r = len(array1) - 1
    while l <= r:#binary search array1
        m = l + (r-l)//2
        if array1[m] == array2[i]:
            array_binary.append(array1[m])#if found, appends the value and exit the loop to go the next value of array2
            break
        elif array1[m] > array2[i]:
            r = m-1
        else:
            l = m+1
print(f'Binary: {array_binary}')


c1 = 0
c2 = 0
while c1 <= m and c2 <= n:#set 2 cursors, comparing values from the 2 arrays
    if array1[c1] == array2[c2]:
        array_linear.append(array1[c1])#append the duplicates into an array
        c1 += 1
        c2 += 1
    elif array1[c1] < array2[c2]:
        c1 += 1
    else:
        c2 += 1
print(f'Linear: {array_linear}')

'''
test cases:

if not array1 or array2: #if input is null
    print("Input is Null")
elif m == 1 and n == 1: #if length of array is 1
    if array1[0] == array2[0]:
        print(array1)
    else:
        print('There are no duplicates')
        
isIntegers = all(isinstance(x, int) for x in array1) #if there are not integer values in the arrays
if not isIntegers:
    print('There are not integers in Input')

'''


