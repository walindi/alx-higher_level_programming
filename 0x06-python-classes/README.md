## 0x06. Python - Classes and Objects

- [0-square.py](0-square.py) is an empty class `Square` that defines a square.
- [1-square.py](1-square.py) is a class `Square` that defines a square by:
  - Private instance attribute: `size`
  - Instantiation with `size`
  - based on [0-square.py](0-square.py)
- [2-square.py](2-square.py) is a class `Square` that defines a square by:
  - Private instance attribute: `size`
  - Instantiation with optional `size`:`def _init__(self, size=0):`
    - `size` being an int, otherwise it raises a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, it raises a `ValueError` exception with the message `size must be >= 0`
  - based on [1-square.py](1-square.py)
- [3-square.py](3-square.py)
