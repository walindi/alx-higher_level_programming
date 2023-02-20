#!/usr/bin/python3

def fizzbuzz():
    """Prints numbers 1 t0 100
    subtituting multiples of 3 with `Fizz`,
    and multiples of 5 with `Buzz`
    Multiples of both are substituted with`FizzBuzz`"""

    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            num = "FizzBuzz"
        elif num % 3 == 0:
            num = "Fizz"
        elif num % 5 == 0:
            num = "Buzz"
        print("{}".format(num), end=" ")
