#!/usr/bin/python3
num = 00
for num in range(0, 100):
    if num != 99:
        print("{:02d}".format(num), end=", ")
    else:
        print("{:d}".format(num))
