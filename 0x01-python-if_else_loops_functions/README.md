## 0x01. Python - if/else, loops, functions

- [1-last_digit.py](1-last_digit.py) assigns a random number to the variable `number` and prints the last digit of the number stored in the variable `number`
- [2-print_alphabet.py](2-print_alphabet.py) prints the aSCII alphabet in loercase, not followed by a new line.
- [3-print_alphabt.py](3-print_alphabt.py) prints the ASCII alphabet in lowercase not followed by a new line. `q` and `e` are not printed.
- [4-print_hexa.py](4-print_hexa.py) prints all numbers from `0` to `98` in decimal and hexadecimal.
- [5-print_comb2.py](5-print_comb2.py) prints numbers from `0` to `99` separated by `,`, followed by a space. Numbers are printed in ascending order with two digits. The last number is followed by a new line.
- [6-print_comb3.py](6-print_comb3.py) prints all possible different combinations of two digits.
- [7-islower.py](7-islower.py)
- []()
- []()
- []()
- []()
- [102-magic_calculation.py](102-magic_calculation.py) does exactly the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
