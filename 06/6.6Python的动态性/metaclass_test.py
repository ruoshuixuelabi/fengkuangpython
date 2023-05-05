"""
6.6.3 使用metaclass

如果希望创建某一批类全部具有某种特征,则可通过 metaclass 来实现。使用 metaclass 可以在创建类时动态修改类定义。

为了使用 metaclass 动态修改类定义,程序需要先定义 metaclass,metaclass 应该继承 type 类, 并重写 __new__() 方法。
下面程序定义了一个metaclass类。
"""


# 定义ItemMetaClass,继承type
class ItemMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attrs 代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 动态为该类添加一个cal_price方法
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, bases, attrs)


"""
上面程序定义了一个 ItemMetaClass 类,该类继承了 type 类,并重写了 __new__ 方法,
在重写该方法时为目标类动态添加了一个 cal_price 方法。
metaclass 类的 __new__ 方法的作用是：当程序使用 class 定义新类时,如果指定了 metaclass,
那么metaclass的 __new__ 方法就会被自动执行。

例如,如下程序使用metaclass定义了两个类(程序清单同上)。

"""


# 定义Book类
class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


# 定义Book类
class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '_discount')

    def __init__(self, price):
        self.price = price

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount


"""
上面程序定义了 Book 和 CellPhone 两个类,在定义这两个类时都指定了 metaclass信息,
因此当 Python 解释器在创建这两个类时,ItemMetaClass 的 __new__ 方法就会被调用,用于修改这两个类

ItemMetaClass 类的 __new__ 方法会为目标类动态添加 cal_price 方法,因此,虽然在定义Book、CellPhone类时没有定义 cal_price()方法,
但这两个类依然有 cal_price()方法。如下程序测试了Book、CellPhone两个类的 cal_price()方法(程序清单同上)。
"""

b = Book("疯狂Python讲义", 89)
b.discount = 0.76
# 创建Book对象的cal_price()方法
print(b.cal_price())
cp = CellPhone(2399)
cp.discount = 0.85
# 创建CellPhone对象的cal_price()方法
print(cp.cal_price())
"""
从上面的运行结果来看,通过使用 metaclass 可以动态修改程序中的一批类,对它们集中进行某种修改。
这个功能在开发一些基础性框架时非常有用,程序可以通过使用 metaclass 为某一批需要具有通用功能的类添加方法。
"""
