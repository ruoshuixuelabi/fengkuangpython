"""
1.  Python 提供的>、<、>=、<=、=和!=等运算符同样是由特殊方法提供支持的。
因此,如果程 序为自定义类提供了这些特殊方法,那么程序就可使用这些比较运算符来比较大小了。
2.  下面是与比较运算符相关的特殊方法。
(1)object.__lt__()(self,other):为"<"运算符提供支持。
(2)object.__le__(self,other):为"<="运算符提供支持。
(3)object.__eq__(self,other):为"=="运算符提供支持。
(4)object.__ne__(self,other):为"!="运算符提供支持。
(5)object.__gt__(self,other):为">"运算符提供支持。
(6)object.__ge__(self,other):为">="运算符提供支持。
3.  虽然Python 为每个比较运算符都提供了特殊方法,但实际上往往并不需要实现这么多的特殊方法,
对于同一个类的实例比较大小而言,通常只要实现其中三个方法即可。因为在实现 __gt__ 方法之后,程序即可使用">"和"<"两个运算符；
在实现 __eq__() 方法之后,程序即可使用"==" 和"!="两个运算符；在实现 __ge__ 方法之后,程序即可使用">="和"<="两个运算符。
下面程序还是为Rectangle类提供了这些特殊方法,从而使得两个Rectangle可以比较大小(基于面积比较大小)。
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

    # 定义__gt__方法,该对象可支持>和<比较
    def __gt__(self, other):
        # 要求参与>运算的另一个运算数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('>运算要求目标是Rectangle')
        return True if self.width * self.height > other.width * other.height else False

    # 定义__eq__方法,该对象可支持==和!=比较
    def __eq__(self, other):
        # 要求参与==运算的另一个运算数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('==运算要求目标是Rectangle')
        return True if self.width * self.height == other.width * other.height else False

    # 定义__ge__方法,该对象可支持>=和<=比较
    def __ge__(self, other):
        # 要求参与>=运算的另一个运算数必须是Rectangle
        if not isinstance(other, Rectangle):
            raise TypeError('>=运算要求目标是Rectangle')
        return True if self.width * self.height >= other.width * other.height else False

    def __repr__(self):
        return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)


r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
print(r1 > r2)  # True
print(r1 >= r2)  # True
print(r1 < r2)  # False
print(r1 <= r2)  # False
print(r1 == r2)  # False
print(r1 != r2)  # True
print('------------------')
r3 = Rectangle(2, 6)
print(r2 >= r3)  # True
print(r2 > r3)  # False
print(r2 <= r3)  # True
print(r2 < r3)  # False
print(r2 == r3)  # True
print(r2 != r3)  # False
