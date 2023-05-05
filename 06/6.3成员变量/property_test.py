"""
6.3.2   使用property函数定义属性

如果为Python类定义了 getter、setter 等访问器方法,则可使用 property() 函数将它们定义成属性(相当于实例变量)。

property()函数的语法格式如下：property(fget=None,fset=None,fdel=None,doc=None)

从上面的语法格式可以看出,在使用 property() 函数时,可传入4个参数,分别代表getter方法、setter方法、del方法和doc,
其中doc 是一个文档字符串,用于说明该属性。
当然,开发者调用 property 也可传入0个(既不能读,也不能写的属性)、1个(只读属性)、2个(读写属性、
3个(读写属性,也可删除)和4个(读写属性,也可删除,包含文档说明)参数。

例如,如下程序定义了一个Rectangle类,该类使用property()函数定义了一个size属性。

"""


class Rectangle:
    # 定义构造方法
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义setsize()函数
    def setsize(self, size):
        self.width, self.height = size

    # 定义getsize()函数
    def getsize(self):
        return self.width, self.height

    # 定义 delsize()函数
    def delsize(self):
        self.width, self.height = 0, 0
        # 使用property定义属性

    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')


# 访问size属性的说明文档
print(Rectangle.size.__doc__)
# 通过内置的help()函数查看Rectangle.size的说明文档
help(Rectangle.size)
rect = Rectangle(4, 3)
# 访问rect的size属性
print(rect.size)  # (4, 3)
# 对rect的size属性赋值
rect.size = 9, 7
# 访问rect的width、height实例变量
print(rect.width)  # 9
print(rect.height)  # 7
# 删除rect的size属性
del rect.size
# 访问rect的width、height实例变量
print(rect.width)  # 0
print(rect.height)  # 0
print(dir(Rectangle))
"""
上面程序中的粗体字代码使用 property() 函数定义了一个 size 属性,在定义该属性时一共传入了4个参数,
这意味着该属性可读、可写、可删除,也有说明文档。

所以,该程序尝试对 Rectangle 对象的 size 属性进行读、写、删除操作,
其实这种读、写、删 除操作分别被委托给getsize()、setsize()和 delsize()方法来实现。

运行上面程序，将会看到如下输出结果。
用于描述矩形大小的属性
Help on property:

    用于描述矩形大小的属性

(4, 3)
9
7
0
0

"""
