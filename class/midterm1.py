def partition(array,left,right):
    i = left-1
    for j in range(left,right):
        if array[j]<=array[right]:
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[right]=array[right],array[i+1]
    return i + 1

def quickSort(array,left,right):
    if left<=right:
        pivot = partition(array,left,right)
        quickSort(array,left,pivot-1)
        quickSort(array,pivot+1,right)

array = [50, 11, 33, 21, 40, 50, 40, 21, 40]
quickSort(array,0,len(array)-1)
print(array)