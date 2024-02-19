#O(n^2)(worst case)
#O(nlogn)(avg case)
def partition(array,left,right):
    i = left - 1

    for j in range(left,right):
        if array[j]<array[right]:
            i = i+1 #moving the cursor i to the right
            array[i], array[j] = array[j], array[i] #if the value is smaller than the pivot, switch the places of cursors i and j

    array[i+1], array[right] = array[right],array[i+1] #put the pivot into its intended place.
    return i + 1 #return index of the pivot
def quickSort(array,left,right):
    if left < right:
        pivot = partition(array, left, right)#partition the array to find the pivot index, also putting the pivot to its rightful place
        quickSort(array,left,pivot-1) #partition the left side of the pivot
        quickSort(array,pivot+1,right) #partition the right side of the pivot

array = [10,9,7,5,3,2,1]
quickSort(array,0,len(array)-1)
print(array)

