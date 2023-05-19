"""
下面程序使用 Rectangle 类,并为该类定义了一个 __radd__ 方法,这样即使运算符左边的对象没有提供对应的运算符方法,
但是只要把Rectangle对象放在运算符的右边,程序也一样可以执行运算。
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

    # 定义__radd__方法,该对象可出现在+的右边
    def __radd__(self, other):
        # 要求参与+运算的另一个运算数必须是数值
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('+运算要求目标是数值')
        return Rectangle(self.width + other, self.height + other)

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r1 = Rectangle(4, 5)
# r1有__radd__方法,因此它可以出现在+运算符的右边
r = 3 + r1
print(r)  # Rectangle(width=7, height=8)
"""
上面程序为 Rectangle 提供了 __radd__ 方法,因此 Rectangle 对象可出现在"+"运算符的右边,支持加法运算。
运行上面程序,可以看到如下输出结果。
Rectangle(width=7, height=8)

此外,Python 还支持各种扩展后的赋值运算符,这些扩展后的赋值运算符也是由特殊方法来提供支持的。
(1)object.__iadd__()(self,other):加法运算,为"+"运算符提供支持。
(2)object.__isub__(self,other):减法运算,为"- "运算符提供支持。
(3)object.__imul__(self,other):乘法运算,为"*"运算符提供支持。
(4)object.__imatmul__(self,other): 矩阵乘法,为"@"运算符提供支持。
(5)object.__itruediv__(self,other): 除法运算,为"/"运算符提供支持。
(6)object.__ifloordiv__(self,other): 整除运算,为"//"运算符提供支持。
(7)object.__imod__(self,other):求余运算,为"%"运算符提供支持。
(8)object.__idivmod__(self,other): 求余运算,为 divmod 运算符提供支持。
(9)object.__ipow__(self,other[,modulo]):乘方运算,为"**"运算符提供支持。
(10)object.__ilshift__(self,other):左移运算,为"<<"运算符提供支持。
(11.1 Python的 GUI 库)object.__irshift__(self,other): 右移运算,为">>"运算符提供支持。
(12)object.__iand__(self,other):按位与运算,为"&"运算符提供支持。
(13)object.__ixor__(self,other): 按位异或运算,为"^"运算符提供支持。
(14)object.__ior__(self,other):按位或运算,为"|"运算符提供支持。
"""
