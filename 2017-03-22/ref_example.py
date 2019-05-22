from weakref import ref

class A(object):
    __slots__ = ['b']
    def __init__(self):
        self.b = 1


class B(object):
    __slots__ = ['b', '__weakref__']
    def __init__(self):
        self.b = 1
