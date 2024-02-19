
def withArray(a,x):
    lower = []
    equal =[]
    higher = []
    for num in range(len(a)):
        if a[num] < a[x]:
            lower.append(a[num])
        elif a[num] > a[x]:
            higher.append(a[num])
        else:
            equal.append(a[num])

    return lower + equal + higher

'''def withoutArray(a, x):
    low = 0
    mid = 0
    high = len(a) - 1

    while mid <= high:
        if a[mid] < a[x]:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == a[x]:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1

    return a'''

def withoutArray(a,x):
    low = 0
    mid = a[x]
    high = len(a)-1
    while low<=high:
        if a[low]<mid:
            low+=1
        elif a[low]==mid:
            low+=1
            x+=1
        elif a[low]>mid:
            a[low],a[high]=a[high],a[low]
            low+=1
            high-=1


a = [3,5,2,6,8,4,4,6,4,4,3]
x = 5
print(withArray(a,x))
withoutArray(a,x)
print(a)