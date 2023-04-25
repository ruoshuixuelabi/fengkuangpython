"""
6.6.2	使用type()函数定义类

1.  前面已经提到使用 type()函数可以查看变量的类型，但如果想使用type()直接查看某个类的类型呢?看如下程序。
2.  从上面的输出结果可以看到， Role 类本身的类型是type。 这句话有点拗口，怎样理解Role 类的类型是type?
3.  从 Python 解释器的角度来看，当程序使用class定 义 Role 类时，也可理解为定义了一个特殊的对象 (type 类的对象),
并将该对象赋值给Role 变量。因此，程序使用class定义的所有类都是 type类的实例。
"""


class Role:
    pass


r = Role()
# 查看变量r的类型 
print(type(r))  # <class '__main__.Role'>
# 查看Role类本身的类型
print(type(Role))  # <class 'type'>
