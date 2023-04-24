"""
1.  需要说明的是, Python 允许通过对象访问类变量,但如果程序通过对象尝试对类变量赋值,
此时性质就变了——Python 是动态语言,赋值语句往往意味着定义新变量。
2.  因此,如果程序通过对象对类变量赋值,其实不是对"类变量赋值",而是定义新的实例变量。 例如如下程序。
3.  上面程序中的两行粗体字代码通过实例对item、quantity变量赋值,看上去很像是对类变量赋值,
但实际上不是,而是重新定义了两个实例变量(如果第一次调用该方法)。
4.  上面程序在调用Inventory对象的 change()方法之后,访问Inventory对象的item、quantity变量——
由于该对象本身已有这两个实例变量,因此程序将会输出该对象的实例变量的值；
接下来程 序通过Inventory访问它的item、quantity两个类变量,此时才是真的访问类变量。
"""


class Inventory:
    # 定义两个类变量
    item = '鼠标'
    quantity = 2000

    # 定义实例方法
    def change(self, item, quantity):
        # 下面赋值语句不是对类变量赋值,而是定义新的实例变量
        self.item = item
        self.quantity = quantity


# 创建Inventory对象
iv = Inventory()
iv.change('显示器', 500)
# 访问iv的item和quantity实例变量
print(iv.item)  # 显示器
print(iv.quantity)  # 500
# 访问Inventory的item和quantity类变量
print(Inventory.item)  # 鼠标
print(Inventory.quantity)  # 2000
# 如果程序通过类修改了两个类变量的值,程序中Inventory的实例变量的值也不会受到任何影响
Inventory.item = '类变量item'
Inventory.quantity = '类变量quantity'
# 访问iv的item和quantity实例变量
print(iv.item)
print(iv.quantity)
# 同样,如果程序对一个对象的实例变量进行了修改,这种修改也不会影响类变量和其他对象的实例变量
iv.item = '实例变量item'
iv.quantity = '实例变量quantity'
print(Inventory.item)
print(Inventory.quantity)
