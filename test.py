def partition(array,left,right):
    i = left - 1
    pivot = array[right]


    for j in range(left,right):
        if array[j]<pivot:
            i +=1
            array[i],array[j]= array[j],array[i]
    array[i+1],array[right] = array[right],array[i+1]
    return i+1

def quickSort(array,left,right):
    if left<right:
        pivot = partition(array,left,right)
        quickSort(array,left,pivot-1)
        quickSort(array,pivot+1,right)

array = [10,9,7,5,3,2,1]
quickSort(array,0,len(array)-1)
print(array)
