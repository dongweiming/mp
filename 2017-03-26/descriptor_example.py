# coding=utf-8
class MyDescriptor(object):
     _value = ''
     def __get__(self, instance, klass):
         return self._value

     def __set__(self, instance, value):
         self._value = value.swapcase()


class Swap(object):
     swap = MyDescriptor()


#instance = Swap()
#print instance.swap  # 没有报AttributeError错误，因为对swap的属性访问被描述符类重载了
#instance.swap = 'make it swap' # 使用__set__重新设置_value
#print instance.swap
#print instance.__dict__ # 没有用到__dict__:被劫持了
