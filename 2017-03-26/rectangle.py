class Quantity(object):
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError('value must be > 0')


class Rectangle(object):
    height = Quantity('height')
    width = Quantity('width')

    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.height * self.width


#r = Rectangle(10, 20)
#print r.area
#r = Rectangle(-1, 20)
#print r.area
