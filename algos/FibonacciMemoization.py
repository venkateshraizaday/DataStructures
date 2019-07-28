def fibonacciMemoization(n, dictionary):
    if n in dictionary:
        return dictionary[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacciMemoization(n-1, dictionary) + fibonacciMemoization(n-2, dictionary)
        dictionary[n] = result
    return result

dictionary = {}
print(fibonacciMemoization(5, dictionary))
print(fibonacciMemoization(30, dictionary))
print(fibonacciMemoization(500, dictionary))
print(fibonacciMemoization(1000, dictionary))
# Call stack filling up larger values. Moving to a an iterative solution next.
#print(fibonacciMemoization(10000, dictionary))