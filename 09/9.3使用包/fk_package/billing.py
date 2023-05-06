"""
上面模块文件中定义了一个打印乘法口诀表的函数。

billing.py模块文件的内容如下。
"""
class Item:
    """定义代表商品的Item类"""

    def __init__(self, price):
        self.price = price

    def __repr__(self):
        return 'Item[price=%g]' % self.price
