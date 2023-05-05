"""
此外,Python 为所有类都提供了一个 __bases__ 属性,通过该属性可以查看该类的所有直接父类,该属性返回所有直接父类组成的元组。
例如如下代码。
"""


class A:
    pass


class B:
    pass


class C(A, B):
    pass


print('类A的所有父类:', A.__bases__)
print('类B的所有父类:', B.__bases__)
print('类C的所有父类:', C.__bases__)
"""
运行上面程序,可以看到如下运行结果。

类A的所有父类: (<class 'object'>,)
类B的所有父类: (<class 'object'>,)
类C的所有父类: (<class '__main__.A'>, <class '__main__.B'>)

从上面的运行结果可以看出,如果在定义类时没有显式指定它的父类,则这些类默认的父类是 object类。

Python 还为所有类都提供了一个 __subclasses__(方法,通过该方法可以查看该类的所有直接子类,该方法返回该类的所有子类组成的列表。
例如,在上面程序中增加如下两行。
"""
print('类A的所有子类:', A.__subclasses__())
print('类B的所有子类:', B.__subclasses__())

