"""
8.5.3 与单目运算符相关的特殊方法

Python 还提供了+(单目求正)、- (单目求负)、~(单目取反)等运算符,这些运算符也有对应的特殊方法。
(1)object.__neg__(self)：为单目求负(-)运算符提供支持。
(2)object.__pos__(self)：为单目求正(+)运算符提供支持。
(3)object.__invert__(self)：为单目取反(~)运算符提供支持。

下面程序为 Rectangle 类实现了一个 __neg__()方法,该方法用于控制将矩形的宽、高交换。下面是该类的代码。

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

    # 定义__neg__方法,该对象可执行求负（-）运算
    def __neg__(self):
        self.width, self.height = self.height, self.width

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r = Rectangle(4, 5)
# 对Rectangle执行求负运算
-r
print(r)  # Rectangle(width=5, height=4)
"""
上面程序中粗体字代码定义了 __neg__方法,这样即可对 Rectangle 对象执行求负运算,在  __neg__ 方法内部就是交换矩形的宽和高,
因此程序对Rectangle执行求负运算其实就是交换矩形的宽和高。

运行上面程序,可以看到如下输出结果。
Rectangle(width=5, height=4)
"""
