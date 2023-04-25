"""
8.1.3	__dir__方 法
1.  对象的   __dir__()方法用于列出该对象内部的所有属性(包括方法)名,该方法将会返回包含所有属性(方法)名的序列。
2.  当程序对某个对象执行dir(object)函数时,实际上就是将该对象的  __dir__()方法返回值进行排序,然后包装成列表。
3.  例如,如下程序示范了 __dir__()方法的功能。
4.  运行上面程序,可以看到程序不仅会输出我们为对象定义的 name、price、info三个属性和方法,
而且还有大量系统内置的属性和方法,如刚刚所介绍的 __repr__    和 __del__ 方法。
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info():
        pass


# 创建一个Item对象,将之赋给im变量
im = Item('鼠标', 29.8)
print(im.__dir__())  # 返回所有属性(包括方法)组成列表
print(dir(im))  # 返回所有属性(包括方法)排序之后的列表
