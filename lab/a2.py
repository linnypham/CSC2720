def calculator(input):
    def calculate(operators, operand):
        operator = operators.pop()
        a = operand.pop()
        b = operand.pop()
        if operator == '+':
            operand.append(b+a)
        elif operator == '-':
            operand.append(b-a)
        elif operator == '*':
            operand.append(b*a)
        elif operator == '/':
            operand.append(b/a)
    def priority(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        else:
            return 0
    def evaluate(input):
        equation = input.split()
        operand = []
        operators = []
        i=0
        while i < len(equation):
            if equation[i] == ' ':
                i+=1
            if equation[i].isdigit():
                operand.append((int(equation[i])))
            else:
                operators.append(equation[i])
            while operators[-1]:
                if operand[-1]>=operators[-1]:
                    pass

input = "10 * 2 - 15"
equation = input.split()
print(equation)