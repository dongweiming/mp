class _Missing(object):
	def __repr__(self):
	    return 'no value'

	def __reduce__(self):
	    return '_missing'


_missing = _Missing()


class cached_property(property):
    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func

    def __set__(self, obj, value):
        obj.__dict__[self.__name__] = value

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, _missing)
        if value is _missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


class Foo(object):
    @cached_property
    def bar(self):
        print 'Call me!'
        return 42


foo = Foo()
print foo.bar
print foo.bar
