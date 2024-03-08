from collections import deque #import deque
def calculator(input):
    stack = deque() #initialize deque
    f = input.split() # split input
    for char in f:
        if char.isdigit(): #if character is number, append in stack
            stack.append(int(char))
        else: #if character is operand, pop the first 2 numbers in stack, and do calculation
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                result = b + a
            elif char == '-':
                result = b - a
            stack.append(result) #append the result back in stack
    return stack.pop() #return the result in stack

input = "3 5 + 1 -"
output = calculator(input)
print(output)
'''
Time: O(n)
Space: O(n)
'''

'''#test1: Input is null
input = " "
output = calculator(input)
print(output)

#test2: Input is 1 number
input = "10"
output = calculator(input)
print(output)

#test3: Inputs are just operators
input = "+ - * /"
output = calculator(input)
print(output)

#test4: Inputs are letters
input = "example text"
output = calculator(input)
print(output)'''