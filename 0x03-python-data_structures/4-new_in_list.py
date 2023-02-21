#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
    without modifying the original list

    Args:
        my_list: the list
        idx: index whose item is to be replaced
        element: new element
    """

    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        new_list = []
        for item in my_list:
            new_list.append(item)

        new_list[idx] = element

        return new_list
