fib = {0:0, 1:1}
def fibonacci(n):
    if n in fib:
        return fib[n]
    else:
        fib[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib[n]
while True:
    a = int(input('The fibonacci number at location: '))
    print(f'Fibonacci number: {fibonacci(a)}')
    print(fib)

