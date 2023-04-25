"""
8.5.4	与类型转换相关的特殊方法
1.  Python提供了 str()、int()、float()、complex()等函数(其实是这些类的构造器)将其他类型的对象转换成
字符串、整数、浮点数和复数,这些转换同样也是由特殊方法在底层提供支持的。下面是这些特殊方法。
(1)object. __str__(self): 对应于调用内置的str()函数将该对象转换成字符串。
(2)object.__bytes__(self):对应于调用内置的bytes()函数将该对象转换成字节内容。该方法应该返回bytes对象
(3)object.__complex__(self): 对应于调用内置的 complex()函数将该对象转换成复数。该方法应该返回 complex 对象
(4)object.__int__(self): 对应于调用内置的 int()函数将对象转换成整数。该方法应该返回 int 对象
(5)object.__float__(self):对应于调用内置的float()函数将对象转换成浮点数。该方法应该返回float对象
2.  提示：对象的 __str__()和 __repr__()方法的功能有些类似,它们都用于将对象转换成字符串,区别在于：
__repr__代表的是"自我描述"的方法,当程序调用print()函数输出对象时,Python 会自动调用该对象的 __repr__()方法,
而 __str__()方法则只有在显式调用str()函数时才会起作用。
3.  下面还是以自定义的 Rectangle为例,程序为该类提供了一个 __int__() 方法,这样程序就可用 int()函数将Rectangle对象转换成整数了。
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义setSize()函数
    def setSize(self, size):
        self.width, self.height = size

    # 定义getSize()函数
    def getSize(self):
        return self.width, self.height

    # 使用property定义属性
    size = property(getSize, setSize)

    # 定义__int__方法,程序可调用int()函数将该对象转成整数
    def __int__(self):
        return int(self.width * self.height)

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r = Rectangle(4, 5)
print(int(r))  # 20
