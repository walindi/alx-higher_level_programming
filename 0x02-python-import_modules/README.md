## 0x02. Python - import & modules

- [0-add.py](0-add.py) imports the function `def add(a, b):` from the file [add_0.py](add_0.py) and prints the result of the addition `1 + 2 = 3`.
- [1-calculation.py](1-calculation.py) imports functions from the file [calculator_1.py](calculator_1.py), does some Maths and prints the result.
- [2-args.py](2-args.py) prints the number of and the list of its arguments.
- [3-infinite_add.py](3-infinite_add.py) prints the result of the addition of all arguments.
- [4-hidden_discovery.py](4-hidden_discovery.py) prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc).
- [5-variable_load.py](5-variable_load.py) imports the variable `a` from the file [variable_load_5.py](variable_load_5.py) and prints its value.
- [100-my_calculator.py](100-my_calculator.py) imports all functions from `calculator_1.py` and handles basic operations.
  - Usage: `./100-my_calculator.py a operator b`
    - Number of arguments must be 3, otherwise the program exits with the value `1`
    - `operator` can be:
      - `+` for addition
      - `-` for subtraction
      - `*` for multiplication
      - `/` for division
    - If the operator is not one of the above, the program exits with the value `1`
    - `a` and `b` are cast into integers. (Assumed that all arguments will be castable into integers)
    - The result is printed this way: `<a> <operator> <b> = <result>`
- [101-easy_print.py](101-easy_print.py) prints to stdout without using `print` or `eval` or `open` or `import sys`
- [102-magic_calculation.py](102-magic_calculation.py) is a python function that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```

    - Useful tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)
- [103-fast_alphabet.py](103-fast_alphabet.py) prints the alphabet in uppercase.
