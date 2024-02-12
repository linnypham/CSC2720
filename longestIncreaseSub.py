def longest(array):
    memo = [1] * len(a)

    for i in range(len(a) - 1, -1, -1):
        for j in range(i + 1, len(a)):
            if a[i] < a[j]:
                memo[i] = max(memo[i], 1 + memo[j])
    return max(memo)

a = [71,72,74,73]
print(longest(a))
