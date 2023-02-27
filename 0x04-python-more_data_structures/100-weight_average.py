#!/usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple
    (<score>, <weight>)
    """
    if len(my_list) == 0:
        return 0

    total = 0
    weight_sum = 0
    for tup in my_list:
        total += (tup[0] * tup[1])
        weight_sum += tup[1]

    return total / weight_sum
