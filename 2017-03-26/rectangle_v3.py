import abc


class Quantity(object):
    __counter = 0
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError('value must be > 0')


class Rectangle(object):
    height = Quantity()
    width = Quantity()

    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.height * self.width


r = Rectangle(10, 20)
print r.area
r = Rectangle(-1, 20)
print r.area
