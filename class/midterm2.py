def biSearch(array,target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = left+(right-left)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left = mid+1
        else:
            right = mid-1
array = [7, 11, 21, 33, 49, 50, 99, 105]
target = 11
print(biSearch(array,target))