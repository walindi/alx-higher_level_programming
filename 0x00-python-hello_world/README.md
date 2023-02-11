## 0x00. Python - Hello, World

- [0-run](0-run) is a Shell script that runs a Python script whose file name is saved in the environment variable `$PYFILE`.
-[1-run_inline](1-run_inline) is a Shell script that runs Python code that is saved in the environment variable `$PYCODE`.
- [2-print.py](2-print.py) is a Python script that prints a string followed by a new line.
- [3-print_number.py](3-print_number.py) prints the integer stored in the variable `number`, followed by `Battery street`.
- [4-print_float.py](4-print_float.py) prints a float with a precisionof 2 digits.
- [5-print_string.py](5-print_string.py) prints 3 times a string stored in the variable `str`, followed by its first 9 charaters.
- [6-concat.py](6-concat.py) concatenates two strings.
- [7-edges.py](7-edges.py) sets three string variables based on the string contained in the variable `word` as follows:
  - `word_first_3`: contains the first 3 letters of the variable `word`
  - `word_first_2`: contains the last 2 letters
  - `middle_word`: contains the value of the variale `word` without the first and last letters
- [8-concat_edges.py](8-concat_edges.py) prints `object-oriented programming with Python`, followed by a new line without creating new variables or string literals. It is a completion of [this source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py).
- [9-easter_egg.py](9-easter_egg.py) prints "The Zen of Python", by Tim Peters.
- [100-write.py](100-write.py) prints `and that piece of art is useful - Dora Korpar, 2015-10-19`followed by a new line to `stderr` using the function `write` from the `sys` module. The script exits with the status code `1`.
- [101-compile](101-compile) is a script that compiles a Python script file. The Python file name will be stored in the environment variable `$PYFILE`. The output filename has to be `$PYFILEc`
- [102-magic_calculation.py](102-magic_calculation.py) is a python function that does exactly the same as the following bytecode:

```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
