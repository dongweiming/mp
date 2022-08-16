from collections.abc import Callable
from typing import Any, TypeVar


R = TypeVar('R')


def log(func: Callable[..., R]) -> Callable[..., R]:
    def inner(*args: Any, **kwargs: Any) -> R:
        print('In')
        return func(*args, **kwargs)
    return inner


@log
def join(items: list[str]):
    return ','.join(items)


print(join(['1', '2']))
print(join([1, 2]))
