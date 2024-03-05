def calculator(input):
    def calculate(operators, operand): #calculation
        operator = operators.pop() #pop the operator
        b = operand.pop() #pop the last number
        a = operand.pop() #pop the next number
        if operator == '+': #do the calculation base on the operator
            operand.append(a + b)
        elif operator == '-':
            operand.append(a - b)
        elif operator == '*':
            operand.append(a * b)
        elif operator == '/':
            operand.append(a / b)

    def priority(operator): #prioritize doing * and / first
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        else:
            return 0

    def evaluate(input):
        equation = input.split() #split input into strings
        operand = [] #store digit
        operators = [] #store operators
        i = 0 #counters
        while i < len(equation):
            if equation[i] == ' ':
                i += 1
                continue
            if equation[i].isdigit(): #append digit into operand
                operand.append(int(equation[i]))
            elif equation[i] in '+-*/': #check operators
                while (len(operators) > 0 and priority(operators[-1]) >= priority(equation[i])):#calculating base on the priority of the operators
                    calculate(operators, operand)
                operators.append(equation[i]) #append operator into operators
            i += 1

        while len(operators) > 0:
            calculate(operators, operand)

        return operand[0]

    result = evaluate(input)
    return result

# Example usage:
input = "10 * 2 - 15"
output = calculator(input)
print(output)

'''Since deque is similar to a double linked-list, 
you can traverse through the list, appending, and popping  from both sides instead of 1 side.
So deque will be faster in Time complexity'''