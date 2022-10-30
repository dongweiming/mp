from typing import Literal, Union


def accepts_only_four(x: Literal[4]) -> None:
    pass

accepts_only_four(4)   # OK
accepts_only_four(19)  # Rejected
accepts_only_four(2 + 2)  # Rejected


def open(path: Union[str, bytes, int],
         mode: Literal["r", "w", "a", "x", "r+", "w+", "a+", "x+"],
         ):
    ...


open('1.py', 'r')
open('2.py', 'xx')
open('2.py', 'b')


union_var: Literal[Literal[Literal[1, 2, 3], "foo"], 5, None]

union_var = 5
union_var = 'foo'
union_var = 1
union_var = [1, 2]
