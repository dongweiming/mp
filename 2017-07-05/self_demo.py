class Person(object):
    def sayHi(self):
        print 'Hi!'


p = Person()
p.sayHi()

p = Person()
Person.sayHi(p)


class Person(object):
    def sayHi():
        print 'Hi!'


p = Person()
p.sayHi()

