'''class Result:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.__class__.__name__}(value={self.value})'

    def add_value(self, value: int) -> 'Result':
        self.value += value
        return self

    @classmethod
    def get(cls, value) -> 'Result':
        return cls(value)


class NewResult(Result):
    ...


r = NewResult(10)
print(r.add_value(5))
print(NewResult.get(20))


class Node:
    def __init__(self, data):
        self.data = data
        self.next: 'Node'|None = None
        self.previous: 'Node'|None = None


node = Node(10)
node.next = Node(20)
node.previous = Node(5)
'''

from typing import Self

class Result:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.__class__.__name__}(value={self.value})'

    def add_value(self, value: int) -> Self:
        self.value += value
        return self

    @classmethod
    def get(cls, value) -> Self:
        return cls(value)


class NewResult(Result):
    ...


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Self|None = None
        self.previous: Self|None = None
