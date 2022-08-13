from dataclasses import dataclass


class Point:
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


@dataclass
class Point2:
    x: int
    y: int


def or_pattern(obj):
    match obj:
        case 0 | 1 | 2:
            print('small number')
        case list() | set():
            print('list or set')
        case str() | bytes():
            print('str or bytes')
        case Point(x, y) | Point2(x, y):
            print(f'{x=},{y=}')
        case [x] | x:
            print(f'{x=}')
