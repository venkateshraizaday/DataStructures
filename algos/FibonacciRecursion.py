def fibonacciRecursion(n):
    if n == 1 or n == 2:
        return 1
    return fibonacciRecursion(n-1) + fibonacciRecursion(n-2)

print(fibonacciRecursion(5))
print(fibonacciRecursion(30))
#n=500 Too slow O(2^n) hence trying memoization.
#print(fibonacciRecursion(500))