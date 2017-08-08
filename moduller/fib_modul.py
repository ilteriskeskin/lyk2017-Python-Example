def fib(n):

    results = []

    a,b = 1,1

    while a < n:
        results.append(a)
        a, b = b, a+b
    return results



