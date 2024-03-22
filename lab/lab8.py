from collections import deque

main_q = deque() #initialize main queue
max_q = deque() #initialize max queue

def enqueue(num):
    main_q.append(num) #append number to main queue
    while max_q and max_q[-1]<num: #check if new number is larger than current number in max queue
        max_q.pop()
    max_q.append(num) #append new number into max queue
def dequeue():
    num = main_q.popleft()
    if num == max_q[0]: #check if current number is equal to the front of Max Queue,
        max_q.popleft()
    return num

q = [1,4,2,3]

for num in q:
    enqueue(num)
    print(max_q[0])
print()
for num in q:
    dequeue()
    if max_q:
        print(max_q[0])
    else:
        print('Null')
'''
test 1: input is null
q = []
for num in q:
    enqueue(num)
    print(max_q[0])
print()
for num in q:
    dequeue()
    if max_q:
        print(max_q[0])
    else:
        print('Null')
        
test 2: input has length of 1
q = [1]
for num in q:
    enqueue(num)
    print(max_q[0])
print()
for num in q:
    dequeue()
    if max_q:
        print(max_q[0])
    else:
        print('Null')
        
test 3: inputs have same values
q = [1,1,1,1]
for num in q:
    enqueue(num)
    print(max_q[0])
print()
for num in q:
    dequeue()
    if max_q:
        print(max_q[0])
    else:
        print('Null')
        
test 4: input is string
q = ['1','4','2','3']
for num in q:
    enqueue(num)
    print(max_q[0])
print()
for num in q:
    dequeue()
    if max_q:
        print(max_q[0])
    else:
        print('Null')
'''