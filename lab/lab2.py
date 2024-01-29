
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

def withoutArray(a, x):
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

    return a


a = [3,5,2,6,8,4,4,6,4,4,3]
x = 5
print(withArray(a,x))
print(withoutArray(a,x))