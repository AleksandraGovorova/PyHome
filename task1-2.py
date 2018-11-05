def simplenum(n):
    numbers = range(2, n)
    for numb in numbers:
        numbers = list(filter(lambda x: (x == numb) or not (x % numb == 0), numbers))
    print(numbers)

simplenum(10)