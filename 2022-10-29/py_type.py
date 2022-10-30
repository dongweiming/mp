# Case 1
def f():
    return "PyCon"


def g():
    return f() + 2019


# Case 2
from typing import List
def get_list() -> List[str]:
    lst = ["PyCon"]
    lst.append(2019)
    return [str(x) for x in lst]
