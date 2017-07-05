import sys
import inspect
from types import FunctionType


def magic():
    s = ''
    f_locals = sys._getframe(1).f_locals
    for var, value in inspect.getmembers(f_locals['self']):
        if not (var.startswith('__') and var.endswith('__')) \
           and var not in f_locals:
            s += var + ' = self.' + var + '\n'
    return s


def outdent_lines(lines):
    outer_ws_count = 0
    for ch in lines[0]:
        if not ch.isspace():
            break
        outer_ws_count += 1
    return [line[outer_ws_count:] for line in lines]


def insert_self_in_header(header):
    return header[0:header.find('(') + 1] + 'self, ' + \
        header[header.find('(') + 1:]


def get_indent_string(srcline):
    indent = ''
    for ch in srcline:
        if not ch.isspace():
            break
        indent += ch
    return indent


def rework(func):
    srclines, line_num = inspect.getsourcelines(func)
    srclines = outdent_lines(srclines)
    dst = insert_self_in_header(srclines[0])
    if len(srclines) > 1:
        dst += get_indent_string(srclines[1]) + 'exec(magic())\n'
        for line in srclines[1:]:
            dst += line
    dst += 'new_func = eval(func.__name__)\n'
    exec(dst)
    return new_func


class WithoutSelf(type):
    def __init__(self, name, bases, attrs):
        super(WithoutSelf, self).__init__(name, bases, attrs)
        try:
            for attr, value in attrs.items():
                if isinstance(value, FunctionType):
                    setattr(self, attr, rework(value))
        except IOError:
            print "Couldn't read source code - it wont work."
            sys.exit()


class Person(object):
    __metaclass__ = WithoutSelf
    def __init__(name):
        self.name = name

    def sayHi(name=None):
        print 'Hi {}!'.format(name or self.name)


p = Person('World')
p.sayHi()
p.sayHi('Python')
