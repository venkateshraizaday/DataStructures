def fibonacciIterative(n):
    if n == 1 or n == 2:
        return 1
    first = 1
    second = 1
    for i in range(2, n):
        next = first + second

        first = second
        second = next
    return next
    
print(fibonacciIterative(5))
print(fibonacciIterative(30))
print(fibonacciIterative(500))
print(fibonacciIterative(1000))
print(fibonacciIterative(10000))