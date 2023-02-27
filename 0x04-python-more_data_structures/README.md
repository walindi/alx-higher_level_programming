## 0x04. Python - More Data Structures: Set, Dictionary

- [0-square_matrix_simple.py](0-square_matrix_simple.py) computes the square value of all integers of a matrix which is a 2 dimensional array.
- [1-search_replace.py](1-search_replace.py) replaces all occurrences of an element by another in a new list.
- [2-uniq_add.py](2-uniq_add.py) adds all unique integers in a list (only once for each integer).
- [3-common_elements.py](3-common_elements.py) returns a set of common elements in two sets.
- [4-only_diff_elements.py](4-only_diff_elements.py) returns a set of all elements present in only one set.
- [5-number_keys.py](5-number_keys.py) returns the number of keys in a dict.
- [6-print_sorted_dictionary.py](6-print_sorted_dictionary.py) prints a dictionary by ordered keys. The keys are ordered alphabetically.
- [7-update_dictionary.py](7-update_dictionary.py) replaces or adds key/value pairs in a dictionary. If key exists in the dict, the value will be replaced. If not, it will be created.
- [8-simple_delete.py](8-simple_delete.py) deletes a key in a dictionary. If a key doesn't exist, the dictionary won't change.
- [9-multiply_by_2.py](9-multiply_by_2.py) returns a new dictionary with all values multiplied by 2.
- [10-best_score.py](10-best_score.py) returns a key with the biggest integer value, assuming that all values are only integers.
- [11-multiply_list_map.py](11-multiply_list_map.py) returns a list with all values multiplied by a number using `map`.
- [12-roman_to_int.py](12-roman_to_int.py) converts a [Roman numeral](https://en.wikipedia.org/wiki/Roman_numerals) to an integer.
- [100-weight_average.py](100-weight_average.py) returns the weighted average of all integers tuple `(<score>, <weight>)`
```
walindi:~/0x04$ cat 100-main.py
weight_average = __import__('100-weight_average').weight_average

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

walindi:~/0x04$ ./100-main.py
Average: 2.80
walindi:~/0x04$
```
- [103-python.c](103-python.c) contains two C functions that print some basic info about Python lists and Python bytes objects.

Python lists:
  - Prototype: `void print_python_list(PyObject *p);`

Python bytes:
  - Prototype: `void print_python_bytes(PyObject *p);`
  - Lin “first X bytes”: print a maximum of 10 bytes
  - If `p` is not a valid `PyBytesObject`, print an error message
About:
  - Python version: 3.4
  - Shared library compiled with: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
