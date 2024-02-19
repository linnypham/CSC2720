def smallest(array):
    left = 0
    right = len(array)-1
    curr_min = array[0]
    while left<=right:
       if array[left]<=array[right]:
           curr_min = min(curr_min, array[left])
           left+=1
       else:
           mid = left+(right-left)//2
           curr_min = curr_min = min(curr_min, array[mid])
           if array[left]<= array[mid]:
               left = mid +1
           else:
               right = mid - 1
    return curr_min
array = [6,7,8,9,1,2,3,4,5]
print(smallest(array))
