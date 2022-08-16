from collections.abc import Callable
from typing import TypeVar, ParamSpec, Concatenate

R = TypeVar('R')
P = ParamSpec('P')


def remove_first(func: Callable[P, R]) -> Callable[Concatenate[int, P], R]:
    def inner(a: int, *args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)
    return inner


@remove_first
def add(a: int, b: int):
    return a + b


print(add(1, 2, 3))
