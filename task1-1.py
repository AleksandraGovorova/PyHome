def fibonacci(n):
    numbers = range(0, n)
    fib = lambda x: x if x <= 2 else fib(x-1) + fib(x-2)
    res = list(map(fib, numbers))
    it = list(filter(lambda y: y % 2 == 0, res))
    print(it)
fibonacci(10)