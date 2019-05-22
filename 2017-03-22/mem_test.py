from __future__ import print_function
import resource


class A(object):
    def __init__(self):
        self.a = 'string'
        self.b = 10
        self.c = True


class B(object):
    __slots__ = ['a', 'b', 'c']
    def __init__(self):
        self.a = 'string'
        self.b = 10
        self.c = True

    def d(self):
        return 20


def test(cls):
    mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    l = []
    for i in range(500):
        l.append(cls())
    mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    del l
    print('Class: {}:\n'.format(getattr(cls, '__name__')))
    print('Initial RAM usage: {:14,}'.format(mem_init))
    print('  Final RAM usage: {:14,}'.format(mem_final))
    print('-' * 20)


if __name__ == '__main__':
    import sys
    test(globals()[sys.argv[1].upper()])


