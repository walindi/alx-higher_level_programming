#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element by another in a new list

    my_list - initial list
    search - the element to replace
    replace - new element
    """

    newList = my_list[:]

    for i in range(len(newList)):
        if newList[i] == search:
            newList[i] = replace
    return newList
