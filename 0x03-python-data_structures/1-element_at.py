#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    elif idx >= 0:
        print("Element at index {:d} is {}".format(idx, element_at()))
