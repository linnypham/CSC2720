def fibonacci(n):
    if n in {0,1}:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

a = int(input('The fibonacci number at location: '))
print(f'Fibonacci number: {fibonacci(a-1)}')

