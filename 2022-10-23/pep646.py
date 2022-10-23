'''U = int | str


def max_1(a: U, b: U) -> U:
    return max(a, b)


max_1("foo", 1)
max_1(1, "foo")
max_1("foo", "bar")
max_1(1, 2)
'''

from typing import TypeVar

T = TypeVar("T", int, str)


def max_2(a: T, b: T) -> T:
    return max(a, b)


max_2("foo", 1)
max_2(1, "foo")
max_2("foo", "bar")
max_2(1, 2)


def max_3(items: list[T]) -> T:
    return max(*items)


max_3([1, 2, 3])
max_3([1, 2, '3'])


from typing import Generic


K = TypeVar("K", int, str)
V = TypeVar("V")


class Item(Generic[K, V]):
    key: K
    value: V
    def __init__(self, k: K, v: V):
        self.key = k
        self.value = v


i = Item(1, 'a')
i2 = Item[int, str](1, 'a')
i3 = Item[int, int](1, 2)
i4 = Item[int, int](1, 'a')

from typing import TypeVarTuple


K2 = TypeVar("K2", int, str)
V2 = TypeVarTuple("V2")


class Item2(Generic[K2, *V2]):
    def __init__(self, k: K2, *v: *V2):
        self.key = k
        self.values = v


d = Item2(1, 2, '3', {'d': 4})
d = Item2(1, 2, 3, 4)
d = Item2(1, {}, set(), [])
d = Item2('1', {}, set(), [])
d = Item2('1', {})
