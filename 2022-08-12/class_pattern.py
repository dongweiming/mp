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


def class_pattern(obj):
    match obj:
        case Point(x, y):
            print(f'Point({x=},{y=})')
        case Point2(x, y):
            print(f'Point2({x=},{y=})')
