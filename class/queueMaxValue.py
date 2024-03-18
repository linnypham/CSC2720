from collections import deque

def maxQueue(array):
    max_q = deque([0])
    while array[i] > max_q[-1]:
        max_q.pop()
    max_q.appendleft(q[i])
    return max_q[0]

q = [1,4,2,3]
output = maxQueue(q)
print(output)

