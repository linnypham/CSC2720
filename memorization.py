def longest(array):

    memo = [1]*len(array)

    for i in range(len(array)-1, -1, -1):
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                memo[i] = max(memo[i], 1 + memo[j])
    return max(memo)