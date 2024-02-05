a = [71,72,74,73]

'''
count = 1
longest = 0

for i in range(len(a)-1):
    if a[i]<a[i+1]:
        count +=1
        longest = max(count,longest)
    else:
        count = 1

print(longest)
'''

memo = [1] * len(a)

for i in range(len(a) - 1, -1, -1):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            memo[i] = max(memo[i], 1 + memo[j])

print(max(memo))