"""
1.  	__dict__ 属性用于查看对象内部存储的所有属性名和属性值组成的字典,通常程序直接使用该属性即可。
程序使用 __dict__ 属性既可查看对象的所有内部状态,也可通过字典语法来访问或修改指定属性的值。例如如下程序。
2.  上面程序中①号代码直接输出对象的 __dict__ 属性,这样将会直接输出该对象内部存储的所有属性名和属性值组成的 dict 对象：
接下来的两行粗体字代码通过 __dict__ 属性访问对象的 name、price两个属性；
最后两行粗体字代码通过 __dict__ 属性对name、price 两个属性赋值。
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


im = Item('鼠标', 28.9)
print(im.__dict__)  # ①
# 通过__dict__访问name属性
print(im.__dict__['name'])
# 通过__dict__访问price属性
print(im.__dict__['price'])
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 32.8
print(im.name)  # 键盘
print(im.price)  # 32.8
