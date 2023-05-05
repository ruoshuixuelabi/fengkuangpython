"""
6.5.2   关于多继承

大部分面向对象的编程语言(除了C++)都只支持单继承,而不支持多继承,
这是由于多继承不仅增加了编程的复杂度,而且很容易导致一些莫名的错误。

Python 虽然在语法上明确支持多继承,但通常推荐：如果不是很有必要,则尽量不要使用多继承,而是使用单继承,
这样可以保证编程思路更清晰,而且可以避免很多麻烦。

当一个子类有多个直接父类时,该子类会继承得到所有父类的方法,这一点在前面示例中已经做了示范。现在的问题是：
如果多个父类中包含了同名的方法,此时会发生什么呢?此时排在前面的父类中的方法会"遮蔽"排在后面的父类中的同名方法。

下面①号粗体字代码让Mouse 继承了Item 类和Product类,由于Item 排在前面,因此Item 中定义的方法优先级更好,
Python 会优先到Item 父类中搜寻方法, 一旦在Item 父类中搜寻到目标方法,Python 就不会继续向下搜寻了。

下面程序中Item 和 Product两个父类中都包含了info()方法,当Mouse 子类对象调用info()方法时——
子类中没有定义info()方法,因此Python 会从父类中寻找info()方法,此时优先使用第一个父类 Item 中的info()方法。
"""


class Item:
    def info(self):
        print("Item中方法:", '这是一个商品')


class Product:
    def info(self):
        print("Product中方法:", '这是一个工业产品')


# class Mouse(Item, Product): # ①
class Mouse(Product, Item):  # ①
    pass


m = Mouse()
m.info()
"""
上面①号粗体字代码让Mouse 继承了 Item 类和 Product 类,由于 Item 排在前面,因此 Item 中定义的方法优先级更好,
Python 会优先到Item 父类中搜寻方法,一旦在 Item 父类中搜寻到目标方法,Python 就不会继续向下搜寻了。

上面程序中 Item 和 Product两个父类中都包含了info()方法,当 Mouse 子类对象调用info()方法时——
子类中没有定义 info() 方法,因此 Python 会从父类中寻找info()方法,此时优先使用第一个父类 Item 中的info()方法。

运行上面程序,将看到如下输出结果。
Item 中方法：这是一个商品

如果将上面粗体字代码改为如下形式。
class Mouse(Product, Item):  # ①

此时 Product 父类的优先级高于 Item 父类,因此 Product 中的 info() 方法将会起作用。运行上面程序,将会看到如下输出结果。
Product 中方法：这是一个工业产品
"""