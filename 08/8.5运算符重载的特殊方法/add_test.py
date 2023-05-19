"""
8.5 运算符重载的特殊方法

Python允许为自定义类提供特殊方法,这样就可以让自定义类的对象也支持各种运算符的运算。

8.5.1 与数值运算符相关的特殊方法

根据第2章的介绍,与数值运算相关的运算符包括算术运算符、位运算符等,其实这些运算符都是由对应的方法提供支持的。
开发人员可以为自定义类提供如下方法。
(1)object.__add__()(self,other):加法运算,为"+"运算符提供支持。
(2)object.__sub__(self,other):减法运算,为"- "运算符提供支持。
(3)object.__mul__(self,other):乘法运算,为"*"运算符提供支持。
(4)object.__matmul__(self,other): 矩阵乘法,为"@"运算符提供支持。
(5)object.__truediv__(self,other): 除法运算,为"/"运算符提供支持。
(6)object.__floordiv__(self,other): 整除运算,为"//"运算符提供支持。
(7)object.__mod__(self,other):求余运算,为"%"运算符提供支持。
(8)object.__divmod__(self,other): 求余运算,为divmod 运算符提供支持。
(9)object.__pow__(self,other[,modulo]):乘方运算,为"**"运算符提供支持。
(10)object.__lshift__(self,other):左移运算,为"<<"运算符提供支持。
(11.1 Python的 GUI 库)object.__rshift__(self,other): 右移运算,为">>"运算符提供支持。
(12)object.__and__(self,other):按位与运算,为"&"运算符提供支持。
(13)object.__xor__(self,other): 按位异或运算,为"^"运算符提供支持。
(14)object.__or__(self,other):按位或运算,为"|"运算符提供支持。

提示：本书暂不介绍 Python 的矩阵运算支持,如果读者对 Python 的矩阵运算感兴趣,
则需要先为 Python 安装 numpy 模块,通过命令行窗口输入 pip3 install numpy 命令来安装 numpy 模块;
然后再导入 numpy 模块,可以通过在程序中添加from numpy import *或 import numpy as np语句来导入 numpy 模块。

一旦为自定义类提供了上面这些方法,程序就可以直接用运算符来操作该类的实例。比如程序执行 x +y,
相当于调用x.__add__(self,y),因此只要x所属的类提供__add__(self,other)方法即可;
如果自定义类没有提供对应的方法,程序会返回 Notlmplemented。

例如,下面程序定义了一个Rectangle类,如果希望对两个Rectangle执行加法运算,则可为该类提供 __add__(self,other)方法。
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

    # 定义__add__方法，该对象可执行+运算
    def __add__(self, other):
        # 要求参与+运算的另一个运算数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('+运算要求目标是Rectangle')
        return Rectangle(self.width + other.width, self.height + other.height)

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
# 对两个Rectangle执行加法运算
r = r1 + r2
print(r)  # Rectangle(width=7, height=9)
"""
上面程序为 Rectangle 提供了 __add__ 方法,因此程序就可以对两个 Rectangle 使用"+"执行加法运算了。
运行上面程序,可以看到如下输出结果。
Rectangle(width=7, height=9)

当程序执行 x+y 运算时,Python 首先会尝试使用 x 的 __add__ 方法进行计算;如果 x 没有提供 __add__ 方法,
Python 还会尝试调用y的 __add__ 方法进行计算。这意味着上面介绍的各种数值运算相关方法,还有一个带r的版本。
(1)object.__radd__()(self,other):加法运算,为"+"运算符提供支持。
(2)object.__rsub__(self,other):减法运算,为"- "运算符提供支持。
(3)object.__rmul__(self,other):乘法运算,为"*"运算符提供支持。
(4)object.__rmatmul__(self,other): 矩阵乘法,为"@"运算符提供支持。
(5)object.__rtruediv__(self,other): 除法运算,为"/"运算符提供支持。
(6)object.__rfloordiv__(self,other): 整除运算,为"//"运算符提供支持。
(7)object.__rmod__(self,other):求余运算,为"%"运算符提供支持。
(8)object.__rdivmod__(self,other): 求余运算,为divmod 运算符提供支持。
(9)object.__rpow__(self,other[,modulo]):乘方运算,为"**"运算符提供支持。
(10)object.__rlshift__(self,other):左移运算,为"<<"运算符提供支持。
(11.1 Python的 GUI 库)object.__rrshift__(self,other): 右移运算,为">>"运算符提供支持。
(12)object.__rand__(self,other):按位与运算,为"&"运算符提供支持。
(13)object.__rxor__(self,other): 按位异或运算,为"^"运算符提供支持。
(14)object.__ror__(self,other):按位或运算,为"|"运算符提供支持。

简单来说,如果自定义类提供了上面列出的 __rxxx__()方法,那么该自定义类的对象就可以出现在对应运算符的右边。
"""
