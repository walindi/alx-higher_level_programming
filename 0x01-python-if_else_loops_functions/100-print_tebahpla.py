#!/usr/bin/python3
"""print ASCII alphabte in reverse order,
alternating lowercase and uppercase"""

i = 0
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        i = letter
    else:
        i = letter - 32
    print("{:c}".format(i), end="")
