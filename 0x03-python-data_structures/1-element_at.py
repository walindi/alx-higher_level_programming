#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        for i in range(0, len(my_list)):
            if i == idx:
                return int(my_list[i])
