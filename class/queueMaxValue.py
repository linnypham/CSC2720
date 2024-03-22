def maxQueue(array):
    max_q = deque()
    for num in array:
        while max_q and max_q[-1] < num:
            max_q.pop()
        max_q.append(num)
    return max_q[0]

q = [1,4,2,3]
output = maxQueue(q)
print(output)