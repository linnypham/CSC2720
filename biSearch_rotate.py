array = [4,5,6,7,10,0,1,2,3]
target = 2

left = 0
right = len(array)-1

while left <= right:
    mid = left+(right-left) // 2
    if target == array[mid]:
        print (mid)
        break
    if array[left]<= array[mid]: #left
        if target >array[mid] or target <array[left]:
            left = mid+1
        else:
            right = mid-1
    else:
        if target<array[mid] or target>array[right]:
            right = mid -1
        else:
            left = mid + 1

else:
    print(False)








