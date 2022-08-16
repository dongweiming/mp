from collections.abc import Callable
from typing import TypeVar, ParamSpec


R = TypeVar('R')
P = ParamSpec('P')


def log(func: Callable[P, R]) -> Callable[P, R]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        print('In')
        return func(*args, **kwargs)
    return inner


@log
def join(items: list[str]):
    return ','.join(items)


print(join(['1', '2']))
print(join([1, 2]))
