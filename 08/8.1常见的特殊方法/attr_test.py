"""
 8.1.5	__getattr__、__setattr__等

当程序操作(包括访问、设置、删除)对象的属性时,Python 系统同样会执行该对象特定的方法。这些方法共涉及如下几个。
(1)__getattribute__(self,name):  当程序访问对象的 name 属性时被自动调用。
(2)__getattr__(self,name): 当程序访问对象的 name 属性且该属性不存在时被自动调用。
(3)__setattr__(self,name,value): 当程序对对象的 name 属性赋值时被自动调用。
(4)__delattr__(self,name):当程序删除对象的 name 属性时被自动调用。

通过重写上面的方法,可以为Python 类"合成"属性—— 当属性不存在时,程序会委托给上面的__getattr__、
 __setattr__、__delattr__ 方法来实现,因此程序可通过重写这些方法来"合成"属性,例如如下程序
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        print('----设置%s属性----' % name)
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        print('----读取%s属性----' % name)
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError

    def __delattr__(self, name):
        print('----删除%s属性----' % name)
        if name == 'size':
            self.__dict__['width'] = 0
            self.__dict__['height'] = 0


rect = Rectangle(3, 4)
print(rect.size)
rect.size = 6, 8
print(rect.width)
del rect.size
print(rect.size)
"""
上面程序实现了 __setattr__()和 __getattr__()方法,并在实现这两个方法时对 size 属性进行了判断,
如果程序正在获取size属性,__getattr__()方法将返回 self.width 和 self.height 组成的元组,
如果获取其他属性则直接引发AttributeError异常;如果程序正在设置 size 属性,则转换为对 self.width、self.height 属性的赋值,
如果是对其他属性赋值,则通过对象的 __dict__ 属性进行赋值。

关于上面这两个方法要进行一些说明。
(1)对于 __getattr__()方法：它只处理程序访问指定属性且该属性不存在的情形。
比如程序访问 width 或 height 属性,Rectangle 对象本身包含该属性,因此该方法不会被触发。
所以重写该方法只需处理我们需要"合成"的属性(比如 size), 假如程序试图访问其他不存在的属性,当然直接引发AttributeError异常即可。
(2)对于 __setattr__()方法,只要程序试图对指定属性赋值时总会触发该方法,因此无论程序是对 width、height 属性赋值,
还是对 size 属性赋值,该方法都会被触发。所以重写该方法既要处理对 size 属性赋值的情形,也要处理对width、height属性赋值的情形。
尤其是处理对 width、height属性赋值的时候,千万不要在 __setattr__()方法中再次对 width、height赋,
值因为对这两个属性赋值会再次触发 __setattr__()方法,这样会让程序陷入死循环中。 运行上面程序,可以看到如下输出结果。

----设置width属性----
----设置height属性----
----读取size属性----
(3, 4)
----设置size属性----
----设置width属性----
----设置height属性----
6
----删除size属性----
----读取size属性----
(0, 0)
"""