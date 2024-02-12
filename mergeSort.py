#O(nlogn)(avg + worse + best case) ~tight-bound time complexity
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)

        i,j,k = 0,0,0 #left,right, array's cursors

        while i<len(left) and j<len(right): #merge
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left): #last left element
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right): #last right element
            array[k] = right[j]
            j += 1
            k += 1
    return array

array = [9,1,17,7,6,2,15,1]

print(mergeSort(array))

