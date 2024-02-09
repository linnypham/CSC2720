def partition(array,left,right):
    pivot = array[right] #choosing the last number as a pivot
    i = left - 1

    for j in range(left,right):
        if array[j]<pivot:
            i = i+1 #moving the cursor i to the right
            array[i], array[j] = array[j], array[i] #if the value is smaller than the pivot, switch the places of cursors i and j

    array[i+1], array[right] = array[right],array[i+1] #put the pivot into its intended place.
    return i + 1
def quickSort(array,left,right):
    if left < right:
        pivot = partition(array, left, right)#partition the array to find the pivot index, also putting the pivot to its rightful place
        quickSort(array,left,pivot-1) #partition the left side of the pivot
        quickSort(array,pivot+1,right) #partition the right side of the pivot

def removeDuplicate(array):
    if not array:
        return ('Null input case, so no output')
    unique = []
    for i in array: #run through the array, add unique values into another array
        if i not in unique:
            unique.append(i)
    return unique

array = [50, 11, 33, 21, 40, 50, 40, 40, 21]
quickSort(array,0,len(array)-1)
output = removeDuplicate(array)
print(output)

'''
#test 1: Null
array = []
quickSort(array,0,len(array)-1)
output = removeDuplicate(array)
print(output)

#test2: 1 value
array = [1]
quickSort(array,0,len(array)-1)
output = removeDuplicate(array)
print(output)

#test3: no duplicates
array = [50, 11, 33, 21, 40]
quickSort(array,0,len(array)-1)
output = removeDuplicate(array)
print(output)

#test4: all duplicates
array = [50,50,50,50,50,50,50,50]
quickSort(array,0,len(array)-1)
output = removeDuplicate(array)
print(output)
'''