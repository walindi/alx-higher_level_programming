#!/usr/bin/python3

def print_last_digit(number):
    """returns last digit of a number
    Args:
        number (int): the number whose last digit is to be printed
    """
    last_digit = 0

    if number < 0:
        last_digit = -number % 10
    else:
        last_digit = number % 10

    print("{}".format(last_digit), end="")

    return last_digit
