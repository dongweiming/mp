from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class NewColor:
    YELLOW = 4


def constant_value(color):
    match color:
        case Color.RED:
            print('Red')
        case NewColor.YELLOW:
            print('Yellow')
        case new_color:
            print(new_color)


constant_value(Color.RED)
constant_value(NewColor.YELLOW)
constant_value(Color.GREEN)
constant_value(4)
constant_value(10)
