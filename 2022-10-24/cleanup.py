from contextlib import ContextDecorator

class mycontext(ContextDecorator):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        raise RuntimeError('hah')
        return False


try:
    with mycontext() as c:
        raise TypeError()
except TypeError:
    print('catch!')
