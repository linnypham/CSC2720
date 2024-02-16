def mergeSort(array):
    if len(array) > 1: #splitting the array in half
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left) #keep splitting recursively
        mergeSort(right)

        i,j,k = 0,0,0 #left,right, array's cursors

        while i<len(left) and j<len(right): #merge smaller array into the bigger array
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left): #merge last left element
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right): #merge last right element
            array[k] = right[j]
            j += 1
            k += 1
    return array
def removeDuplicate(array):
    if not array:
        return ('Null input case, so no output')
    unique = []
    for i in array: #run through the array, add unique values into another array
        if i not in unique:
            unique.append(i)
    return unique

array = [50, 11, 33, 21, 40, 50, 40, 21, 40]
output = removeDuplicate(mergeSort(array))
print(output)
'''
#test1: Input is null
array = []
output = removeDuplicate(mergeSort(array))
print(output)

#test2: Only 1 value
array = [50]
output = removeDuplicate(mergeSort(array))
print(output)

#test3: No duplicates
array = [50, 11, 33, 21, 40]
output = removeDuplicate(mergeSort(array))
print(output)

#test4: All duplicates
array = [50,50,50,50,50]
output = removeDuplicate(mergeSort(array))
print(output)
'''