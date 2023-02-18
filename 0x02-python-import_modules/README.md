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
